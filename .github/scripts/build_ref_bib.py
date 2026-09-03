#!/usr/bin/env python3
"""Build ref.bib from explicit paper entries in the Awesome-AI4AI repository.

Safety rule: never invent metadata. Every emitted entry must be resolved from an
arXiv record, an official scholarly page / API, or a high-confidence Crossref
match. If any explicit paper entry cannot be resolved, the script exits nonzero
and prints the unresolved list instead of silently guessing authors.
"""
from __future__ import annotations

import difflib
import html
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import xml.etree.ElementTree as ET
from collections import OrderedDict
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
SOURCE_FILES = [
    "foundations/papers.md",
    "foundations/preprint-2026082108-additions.md",
    "agent4ai/papers.md",
    "agent4ai/recent.md",
    "agent4ai/surveys.md",
    "agent4ai/benchmarks.md",
    "writing/reading-list.md",
]

ACADEMIC_HOSTS = {
    "arxiv.org", "www.arxiv.org", "doi.org", "dx.doi.org",
    "proceedings.neurips.cc", "jmlr.org", "www.jmlr.org",
    "proceedings.mlr.press", "aclanthology.org", "www.aclanthology.org",
    "openreview.net", "www.openreview.net", "nature.com", "www.nature.com",
    "link.springer.com", "academic.oup.com", "dl.acm.org",
    "ieeexplore.ieee.org", "ojs.aaai.org", "www.mdpi.com", "mdpi.com",
    "www.automl.org", "automl.org", "www.cs.ubc.ca", "cs.ubc.ca",
    "people.idsia.ch", "www.preprints.org", "preprints.org",
    "onlinelibrary.wiley.com", "onlinelibrary.wiley.com",
}

S = requests.Session()
S.headers.update({
    "User-Agent": "Awesome-AI4AI bibliography verifier/1.0 (https://github.com/Meaw0415/Awsome-AI4AI)"
})


def clean(s: str | None) -> str:
    if not s:
        return ""
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def norm_title(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).lower()
    s = s.replace("–", "-").replace("—", "-")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def title_similarity(a: str, b: str) -> float:
    na, nb = norm_title(a), norm_title(b)
    if not na or not nb:
        return 0.0
    if na == nb:
        return 1.0
    return difflib.SequenceMatcher(None, na, nb).ratio()


def extract_year(text: str) -> int | None:
    m = re.search(r"\b(19\d{2}|20\d{2})\b", text)
    return int(m.group(1)) if m else None


def strip_md_title(label: str) -> str:
    label = re.sub(r"[*_`]+", "", label)
    label = re.sub(r"^[★☆\s]+", "", label)
    return clean(label)


def is_academic_url(url: str) -> bool:
    try:
        host = urllib.parse.urlparse(url).hostname or ""
    except Exception:
        return False
    return host.lower() in ACADEMIC_HOSTS


def extract_candidates() -> list[dict]:
    out: list[dict] = []
    seen_raw = set()
    md_link = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
    bare_url = re.compile(r"https?://[^\s)>]+")

    for rel in SOURCE_FILES:
        p = ROOT / rel
        if not p.exists():
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines, 1):
            year_hint = extract_year(line)
            linked_spans = []
            for m in md_link.finditer(line):
                label, url = strip_md_title(m.group(1)), m.group(2).rstrip(".,;:")
                linked_spans.append(m.span(2))
                if not is_academic_url(url):
                    continue
                key = (label, url)
                if key in seen_raw:
                    continue
                seen_raw.add(key)
                out.append({"title_hint": label, "url": url, "year_hint": year_hint,
                            "source": f"{rel}:{idx}"})

            # Bare academic URL on a line whose emphasized text gives the title.
            for um in bare_url.finditer(line):
                url = um.group(0).rstrip(".,;:")
                if any(a <= um.start() < b for a, b in linked_spans):
                    continue
                if not is_academic_url(url):
                    continue
                # Prefer italic title, then bold title, then text between dash and URL.
                titles = re.findall(r"\*([^*]{5,}?)\*", line[:um.start()])
                title_hint = strip_md_title(titles[-1]) if titles else ""
                if not title_hint:
                    bolds = re.findall(r"\*\*([^*]{5,}?)\*\*", line[:um.start()])
                    title_hint = strip_md_title(bolds[-1]) if bolds else ""
                if not title_hint:
                    prefix = re.sub(r"^[-|\s\d.]+", "", line[:um.start()])
                    prefix = re.sub(r"\*+", "", prefix)
                    title_hint = clean(prefix.split(" — ")[-1])
                key = (title_hint, url)
                if key in seen_raw:
                    continue
                seen_raw.add(key)
                out.append({"title_hint": title_hint, "url": url, "year_hint": year_hint,
                            "source": f"{rel}:{idx}"})

        # Explicit formal entries without a URL in the main foundations bibliography.
        if rel == "foundations/papers.md":
            for idx, line in enumerate(lines, 1):
                if not re.match(r"^- \*\*(?:19|20)\d{2}(?:/\d{2})?\*\*\s+—", line):
                    continue
                if "http://" in line or "https://" in line:
                    continue
                m = re.search(r"\*([^*]{8,}?)\*", line)
                if not m:
                    continue
                title_hint = strip_md_title(m.group(1))
                # Exclude generic/non-citation prose.
                if any(x in title_hint.lower() for x in ["literature", "surveys", "background"]):
                    continue
                key = (title_hint, "")
                if key in seen_raw:
                    continue
                seen_raw.add(key)
                out.append({"title_hint": title_hint, "url": "", "year_hint": extract_year(line),
                            "source": f"{rel}:{idx}"})
    return out


def arxiv_id_from_url(url: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", url)
    return m.group(1) if m else None


def fetch_arxiv(ids: list[str]) -> dict[str, dict]:
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    records: dict[str, dict] = {}
    for i in range(0, len(ids), 40):
        batch = ids[i:i+40]
        params = {"id_list": ",".join(batch), "max_results": len(batch)}
        r = S.get("https://export.arxiv.org/api/query", params=params, timeout=45)
        r.raise_for_status()
        root = ET.fromstring(r.text)
        for e in root.findall("a:entry", ns):
            eid = clean(e.findtext("a:id", default="", namespaces=ns)).split("/abs/")[-1]
            eid = re.sub(r"v\d+$", "", eid)
            title = clean(e.findtext("a:title", default="", namespaces=ns))
            authors = [clean(a.findtext("a:name", default="", namespaces=ns))
                       for a in e.findall("a:author", ns)]
            published = clean(e.findtext("a:published", default="", namespaces=ns))
            journal_ref = clean(e.findtext("x:journal_ref", default="", namespaces=ns))
            records[eid] = {
                "title": title,
                "authors": [a for a in authors if a],
                "year": int(published[:4]) if re.match(r"\d{4}", published) else None,
                "venue": journal_ref or "arXiv preprint",
                "arxiv": eid,
                "url": f"https://arxiv.org/abs/{eid}",
                "doi": "",
                "source_kind": "arXiv",
            }
        time.sleep(1.0)
    return records


def meta_values(soup: BeautifulSoup, names: list[str]) -> list[str]:
    vals = []
    lowers = {n.lower() for n in names}
    for tag in soup.find_all("meta"):
        name = (tag.get("name") or tag.get("property") or "").lower()
        if name in lowers and tag.get("content"):
            vals.append(clean(tag.get("content")))
    return [v for v in vals if v]


def generic_page_metadata(url: str) -> dict | None:
    try:
        r = S.get(url, timeout=30, allow_redirects=True)
        if r.status_code >= 400:
            return None
        soup = BeautifulSoup(r.text, "html.parser")
        titles = meta_values(soup, ["citation_title", "dc.title", "dc.title.alternative"])
        authors = meta_values(soup, ["citation_author", "dc.creator", "dc.contributor.author"])
        dates = meta_values(soup, ["citation_publication_date", "citation_date", "dc.date", "article:published_time"])
        venues = meta_values(soup, ["citation_journal_title", "citation_conference_title", "citation_book_title", "prism.publicationname"])
        dois = meta_values(soup, ["citation_doi", "dc.identifier"])
        title = titles[0] if titles else ""
        if not title:
            return None
        doi = ""
        for d in dois:
            dm = re.search(r"10\.\d{4,9}/\S+", d)
            if dm:
                doi = dm.group(0).rstrip(".,;)")
                break
        year = extract_year(dates[0]) if dates else None
        return {"title": title, "authors": authors, "year": year,
                "venue": venues[0] if venues else "", "doi": doi,
                "url": r.url, "arxiv": arxiv_id_from_url(r.url) or "",
                "source_kind": "official page"}
    except Exception:
        return None


def openreview_metadata(url: str) -> dict | None:
    try:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        forum = q.get("id", [""])[0]
        if not forum:
            return None
        r = S.get("https://api2.openreview.net/notes", params={"forum": forum, "limit": 10}, timeout=30)
        if r.status_code >= 400:
            return None
        notes = r.json().get("notes", [])
        if not notes:
            return None
        # Prefer a submission-like note containing title + authors.
        for n in notes:
            c = n.get("content", {})
            def val(k):
                v = c.get(k, "")
                return v.get("value", "") if isinstance(v, dict) else v
            title, authors = val("title"), val("authors")
            if title and authors:
                if isinstance(authors, str):
                    authors = [a.strip() for a in re.split(r"\s*(?:,|;| and )\s*", authors) if a.strip()]
                year = None
                cdate = n.get("cdate") or n.get("pdate")
                if cdate:
                    year = int(time.strftime("%Y", time.gmtime(cdate / 1000)))
                venue = val("venue") or val("venueid") or "OpenReview"
                return {"title": clean(title), "authors": [clean(a) for a in authors],
                        "year": year, "venue": clean(venue), "doi": "", "arxiv": "",
                        "url": url, "source_kind": "OpenReview API"}
    except Exception:
        return None
    return None


def crossref_lookup(title_hint: str, year_hint: int | None = None) -> dict | None:
    if len(norm_title(title_hint)) < 12:
        return None
    try:
        r = S.get("https://api.crossref.org/works", params={
            "query.bibliographic": title_hint, "rows": 8,
            "select": "DOI,title,author,published-print,published-online,issued,container-title,type,URL"
        }, timeout=30)
        if r.status_code >= 400:
            return None
        best = None
        for item in r.json().get("message", {}).get("items", []):
            titles = item.get("title") or []
            if not titles:
                continue
            t = clean(titles[0])
            sim = title_similarity(title_hint, t)
            if sim < 0.90:
                continue
            year = None
            for fld in ("published-print", "published-online", "issued"):
                parts = item.get(fld, {}).get("date-parts", [])
                if parts and parts[0]:
                    year = parts[0][0]
                    break
            # Penalize implausible year mismatch, but tolerate preprint/publication shifts.
            score = sim - (0.04 if year_hint and year and abs(year - year_hint) > 2 else 0)
            if best is None or score > best[0]:
                authors = []
                for a in item.get("author") or []:
                    name = clean(" ".join(x for x in [a.get("given", ""), a.get("family", "")] if x))
                    if name:
                        authors.append(name)
                venue = clean((item.get("container-title") or [""])[0])
                best = (score, {"title": t, "authors": authors, "year": year,
                                "venue": venue, "doi": item.get("DOI", ""), "arxiv": "",
                                "url": item.get("URL", ""), "source_kind": "Crossref"})
        if best and best[0] >= 0.90 and best[1]["authors"]:
            return best[1]
    except Exception:
        return None
    return None


def resolve_non_arxiv(c: dict) -> dict | None:
    url, title_hint, year_hint = c["url"], c["title_hint"], c["year_hint"]
    if url and "openreview.net" in url:
        m = openreview_metadata(url)
        if m and title_similarity(title_hint, m["title"]) >= 0.72:
            return m
    if url:
        m = generic_page_metadata(url)
        if m and (not title_hint or title_similarity(title_hint, m["title"]) >= 0.72):
            if m.get("authors"):
                return m
    return crossref_lookup(title_hint, year_hint)


def bib_escape(s: str) -> str:
    s = s.replace("\\", "\\textbackslash{}")
    s = s.replace("&", "\\&").replace("%", "\\%").replace("#", "\\#")
    s = s.replace("_", "\\_")
    return s


def key_for(rec: dict, used: set[str]) -> str:
    family = "ref"
    if rec["authors"]:
        # Last token is usually family name; keep alnum only.
        family = re.sub(r"[^A-Za-z0-9]", "", rec["authors"][0].split()[-1]).lower() or "ref"
    year = str(rec.get("year") or "nd")
    words = [w for w in re.findall(r"[A-Za-z0-9]+", rec["title"]) if w.lower() not in {"a","an","the","of","for","to","and","with","via","on","in"}]
    slug = (words[0].lower() if words else "paper")
    base = f"{family}{year}{slug}"
    key = base
    n = 2
    while key in used:
        key = f"{base}{n}"
        n += 1
    used.add(key)
    return key


def dedup_records(records: list[dict]) -> list[dict]:
    chosen: OrderedDict[str, dict] = OrderedDict()
    for r in records:
        if r.get("arxiv"):
            ident = "arxiv:" + r["arxiv"].lower()
        elif r.get("doi"):
            ident = "doi:" + r["doi"].lower()
        else:
            ident = "title:" + norm_title(r["title"])
        if ident not in chosen:
            chosen[ident] = r
        else:
            old = chosen[ident]
            # Prefer official/Crossref publication metadata to a generic page; prefer complete authors.
            if len(r.get("authors", [])) > len(old.get("authors", [])):
                chosen[ident] = r
    # Second pass dedup exact normalized titles (handles same paper via arXiv and venue URL).
    by_title: OrderedDict[str, dict] = OrderedDict()
    for r in chosen.values():
        nt = norm_title(r["title"])
        if nt not in by_title:
            by_title[nt] = r
        else:
            old = by_title[nt]
            # Prefer DOI-bearing official record, otherwise arXiv if it has fuller authors.
            if r.get("doi") and not old.get("doi"):
                by_title[nt] = r
            elif len(r.get("authors", [])) > len(old.get("authors", [])):
                by_title[nt] = r
    return list(by_title.values())


def render_bib(records: list[dict]) -> str:
    used = set()
    lines = [
        "% Auto-generated from the explicit paper entries in Awsome-AI4AI.",
        "% Metadata is resolved from arXiv, official scholarly pages/APIs, or high-confidence Crossref matches.",
        "% No unresolved/guessed author lists are emitted.",
        "",
    ]
    for r in sorted(records, key=lambda x: ((x.get("year") or 9999), norm_title(x["title"]))):
        key = key_for(r, used)
        if r.get("arxiv") and not r.get("doi"):
            etype = "misc"
        elif r.get("venue"):
            etype = "article"
        else:
            etype = "misc"
        lines.append(f"@{etype}{{{key},")
        lines.append(f"  title = {{{bib_escape(r['title'])}}},")
        lines.append(f"  author = {{{' and '.join(bib_escape(a) for a in r['authors'])}}},")
        if r.get("year"):
            lines.append(f"  year = {{{r['year']}}},")
        if r.get("venue"):
            field = "journal" if etype == "article" else "note"
            lines.append(f"  {field} = {{{bib_escape(r['venue'])}}},")
        if r.get("doi"):
            lines.append(f"  doi = {{{r['doi']}}},")
        if r.get("arxiv"):
            lines.append(f"  eprint = {{{r['arxiv']}}},")
            lines.append("  archivePrefix = {arXiv},")
        if r.get("url"):
            lines.append(f"  url = {{{r['url']}}},")
        lines.append("}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    candidates = extract_candidates()
    print(f"Extracted {len(candidates)} explicit citation candidates")

    arxiv_ids = sorted({aid for c in candidates if (aid := arxiv_id_from_url(c["url"]))})
    print(f"Resolving {len(arxiv_ids)} unique arXiv IDs")
    arxiv = fetch_arxiv(arxiv_ids)

    resolved: list[dict] = []
    unresolved: list[dict] = []
    for i, c in enumerate(candidates, 1):
        aid = arxiv_id_from_url(c["url"])
        if aid:
            rec = arxiv.get(aid)
            if rec:
                resolved.append(rec)
            else:
                unresolved.append(c)
            continue
        rec = resolve_non_arxiv(c)
        if rec and rec.get("title") and rec.get("authors"):
            resolved.append(rec)
        else:
            unresolved.append(c)
        if i % 20 == 0:
            time.sleep(0.5)

    records = dedup_records(resolved)
    print(f"Resolved {len(records)} unique papers after deduplication")

    # Remove candidates that are duplicate surface forms of already-resolved titles.
    resolved_titles = [r["title"] for r in records]
    still_unresolved = []
    for c in unresolved:
        if c["title_hint"] and any(title_similarity(c["title_hint"], t) >= 0.93 for t in resolved_titles):
            continue
        still_unresolved.append(c)

    if still_unresolved:
        print("\nUNRESOLVED EXPLICIT PAPER ENTRIES (no metadata guessed):", file=sys.stderr)
        for c in still_unresolved:
            print(f"- {c['source']} | {c['title_hint']} | {c['url']}", file=sys.stderr)
        print(f"\nTotal unresolved: {len(still_unresolved)}", file=sys.stderr)
        return 2

    (ROOT / "ref.bib").write_text(render_bib(records), encoding="utf-8")
    print(f"Wrote ref.bib with {len(records)} verified unique entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
