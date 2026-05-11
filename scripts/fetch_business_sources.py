import datetime as dt
import email.utils
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


# ============================================================
# AI Business Insight Briefing Source Collector
# ============================================================
# Purpose:
# Pull a practical source pack for AI business adoption,
# BI/workflow implications, FMCG/sales/distribution relevance,
# SME-facing software/AI services, and market intelligence.
#
# Uses only Python standard library.
# No paid APIs.
# No API keys.
# ============================================================


TODAY = dt.datetime.utcnow().date().isoformat()
NOW_UTC = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)

OUT_DIR = Path("data/source_packs")
OUT_DIR.mkdir(parents=True, exist_ok=True)

MAX_ITEMS_PER_SOURCE = 5
MAX_RSS_AGE_DAYS = 60


RSS_FEEDS = [
    # AI / company primary sources
    {
        "name": "OpenAI News",
        "type": "company_primary_ai",
        "url": "https://openai.com/news/rss.xml",
    },
    {
        "name": "Google DeepMind Blog",
        "type": "company_primary_ai",
        "url": "https://deepmind.google/blog/rss.xml",
    },
    {
        "name": "AWS Machine Learning Blog",
        "type": "ai_data_tooling",
        "url": "https://aws.amazon.com/blogs/machine-learning/feed/",
    },

    # BI / data tooling
    {
        "name": "Microsoft Power BI Blog",
        "type": "bi_tooling",
        "url": "https://powerbi.microsoft.com/en-us/blog/feed/",
    },

    # FMCG / retail / logistics / distribution
    {
        "name": "Supply Chain Dive",
        "type": "fmcg_supply_chain_news",
        "url": "https://www.supplychaindive.com/feeds/news/",
    },
    {
        "name": "Retail Gazette",
        "type": "retail_fmcg_news",
        "url": "https://www.retailgazette.co.uk/blog/feed/",
    },
    {
        "name": "Logistics Manager",
        "type": "logistics_distribution_news",
        "url": "https://www.logisticsmanager.com/feed/",
    },

    # Professional insight
    {
        "name": "MIT Sloan Management Review",
        "type": "professional_insight",
        "url": "https://sloanreview.mit.edu/feed/",
    },
    {
        "name": "McKinsey Insights",
        "type": "professional_insight",
        "url": "https://www.mckinsey.com/insights/rss",
    },

    # Independent news
    {
        "name": "BBC Business",
        "type": "independent_news",
        "url": "http://feeds.bbci.co.uk/news/business/rss.xml",
    },
    {
        "name": "The Guardian Business",
        "type": "independent_news",
        "url": "https://www.theguardian.com/uk/business/rss",
    },
]


GOVUK_SEARCHES = [
    {
        "name": "GOV.UK AI business adoption",
        "type": "official_policy",
        "query": "artificial intelligence business adoption",
    },
    {
        "name": "GOV.UK SMEs digital adoption",
        "type": "official_policy",
        "query": "SME digital adoption artificial intelligence",
    },
    {
        "name": "GOV.UK business productivity technology",
        "type": "official_policy",
        "query": "business productivity technology SME",
    },
]


NEWS_SEARCHES = [
    {
        "name": "Google News - UK SME AI adoption",
        "type": "news_search",
        "query": "UK SME AI adoption",
    },
    {
        "name": "Google News - FMCG AI supply chain UK",
        "type": "news_search",
        "query": "UK FMCG AI supply chain",
    },
    {
        "name": "Google News - business intelligence AI workflow",
        "type": "news_search",
        "query": "business intelligence AI workflow automation",
    },
    {
        "name": "Google News - retail distribution AI UK",
        "type": "news_search",
        "query": "UK retail distribution AI data",
    },
]


MANUAL_WATCHLIST = [
    {
        "source": "ONS",
        "type": "official_watchlist",
        "title": "ONS business, economy and technology statistics",
        "url": "https://www.ons.gov.uk/",
        "summary": "Official UK statistics source for business conditions, productivity, retail, labour market and economic context.",
    },
    {
        "source": "OECD",
        "type": "official_watchlist",
        "title": "OECD AI, SMEs, productivity and digital adoption",
        "url": "https://www.oecd.org/",
        "summary": "Useful for international context on SME digital adoption, productivity, AI diffusion and policy.",
    },
    {
        "source": "The Grocer",
        "type": "fmcg_watchlist",
        "title": "The Grocer - UK FMCG and grocery sector",
        "url": "https://www.thegrocer.co.uk/",
        "summary": "Specialist UK FMCG and grocery source. Useful for suppliers, wholesalers, pricing, retail pressure and distribution signals.",
    },
    {
        "source": "IGD",
        "type": "fmcg_watchlist",
        "title": "IGD grocery, retail and supply-chain insight",
        "url": "https://www.igd.com/",
        "summary": "Useful for grocery, retail, wholesale and supply-chain context.",
    },
    {
        "source": "Kantar",
        "type": "fmcg_watchlist",
        "title": "Kantar retail and FMCG insights",
        "url": "https://www.kantar.com/uki/industries/retail",
        "summary": "Professional insight source for FMCG, retail, consumers and brand performance.",
    },
    {
        "source": "NielsenIQ",
        "type": "fmcg_watchlist",
        "title": "NielsenIQ retail and FMCG insights",
        "url": "https://nielseniq.com/global/en/insights/",
        "summary": "Professional retail and FMCG data source for market trends, consumer behaviour and category performance.",
    },
]


def fetch_url(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ai-business-insight-briefing/0.1 public research workflow"
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def clean_text(text):
    if not text:
        return ""
    text = str(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&#39;", "'", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_date_to_utc(date_text):
    if not date_text:
        return None

    date_text = str(date_text).strip()

    try:
        parsed = email.utils.parsedate_to_datetime(date_text)
        if parsed:
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
    except Exception:
        pass

    try:
        iso_text = date_text.replace("Z", "+00:00")
        parsed = dt.datetime.fromisoformat(iso_text)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc)
    except Exception:
        pass

    return None


def should_keep_item(item, max_age_days=MAX_RSS_AGE_DAYS):
    published = item.get("published", "")
    parsed = parse_date_to_utc(published)

    if not parsed:
        return True

    if parsed > NOW_UTC + dt.timedelta(days=1):
        return False

    if parsed < NOW_UTC - dt.timedelta(days=max_age_days):
        return False

    return True


def relevance_score(item):
    text = " ".join(
        [
            str(item.get("title", "")),
            str(item.get("summary", "")),
            str(item.get("source", "")),
            str(item.get("type", "")),
        ]
    ).lower()

    high_value_terms = [
        "ai adoption",
        "artificial intelligence",
        "generative ai",
        "business intelligence",
        "workflow",
        "automation",
        "data quality",
        "dashboard",
        "power bi",
        "analytics",
        "sme",
        "small business",
        "productivity",
        "supply chain",
        "logistics",
        "distribution",
        "fmcg",
        "retail",
        "grocery",
        "sales",
        "forecasting",
        "inventory",
        "customer service",
        "implementation",
        "business value",
    ]

    medium_value_terms = [
        "data",
        "software",
        "platform",
        "operations",
        "governance",
        "risk",
        "market",
        "buyers",
        "vendors",
        "process",
        "efficiency",
        "decision",
        "insight",
    ]

    score = 1

    for term in high_value_terms:
        if term in text:
            score += 2

    for term in medium_value_terms:
        if term in text:
            score += 1

    return min(score, 5)


def add_quality_notes(item):
    source_type = item.get("type", "")

    if source_type.startswith("company") or source_type in {"bi_tooling", "ai_data_tooling"}:
        item["quality_note"] = "Vendor/company source: useful primary signal, but not neutral proof."
    elif source_type in {"official_policy", "official_watchlist"}:
        item["quality_note"] = "Official source: credible context, but may be broad or slow-moving."
    elif source_type in {"independent_news", "news_search"}:
        item["quality_note"] = "News/search source: useful for current signals, but verify important claims."
    elif "professional" in source_type:
        item["quality_note"] = "Professional insight source: useful framing, but may be marketing-led."
    elif "fmcg" in source_type or "retail" in source_type or "logistics" in source_type:
        item["quality_note"] = "Industry source: useful sector context, but check whether evidence is narrow or anecdotal."
    else:
        item["quality_note"] = "Use with normal source-checking caution."

    item["relevance_score"] = relevance_score(item)
    return item


def parse_feed(raw, source_name, source_type):
    root = ET.fromstring(raw)
    items = []

    for item in root.findall(".//item")[: MAX_ITEMS_PER_SOURCE * 2]:
        parsed_item = {
            "source": source_name,
            "type": source_type,
            "title": clean_text(item.findtext("title", default="")),
            "published": item.findtext("pubDate", default=""),
            "url": item.findtext("link", default=""),
            "summary": clean_text(item.findtext("description", default=""))[:1200],
        }

        if should_keep_item(parsed_item):
            items.append(add_quality_notes(parsed_item))

        if len(items) >= MAX_ITEMS_PER_SOURCE:
            break

    # Atom fallback
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    for entry in root.findall("atom:entry", ns)[: MAX_ITEMS_PER_SOURCE * 2]:
        link = ""
        link_el = entry.find("atom:link", ns)
        if link_el is not None:
            link = link_el.attrib.get("href", "")

        parsed_item = {
            "source": source_name,
            "type": source_type,
            "title": clean_text(entry.findtext("atom:title", default="", namespaces=ns)),
            "published": entry.findtext("atom:published", default="", namespaces=ns),
            "url": link,
            "summary": clean_text(entry.findtext("atom:summary", default="", namespaces=ns))[:1200],
        }

        if should_keep_item(parsed_item):
            items.append(add_quality_notes(parsed_item))

        if len(items) >= MAX_ITEMS_PER_SOURCE:
            break

    return items


def govuk_url(query):
    encoded = urllib.parse.quote(query)
    return f"https://www.gov.uk/api/search.json?q={encoded}&count=5&order=updated-newest"


def parse_govuk_search(raw, source_name, source_type):
    data = json.loads(raw.decode("utf-8"))
    items = []

    for result in data.get("results", [])[: MAX_ITEMS_PER_SOURCE * 2]:
        link = result.get("link", "")
        if link.startswith("/"):
            link = "https://www.gov.uk" + link

        parsed_item = {
            "source": source_name,
            "type": source_type,
            "title": clean_text(result.get("title", "")),
            "published": result.get("public_timestamp") or result.get("updated_at") or "",
            "url": link,
            "summary": clean_text(result.get("description", ""))[:1200],
        }

        if should_keep_item(parsed_item, max_age_days=365):
            items.append(add_quality_notes(parsed_item))

        if len(items) >= MAX_ITEMS_PER_SOURCE:
            break

    return items


def google_news_url(query):
    encoded = urllib.parse.quote(query)
    return f"https://news.google.com/rss/search?q={encoded}&hl=en-GB&gl=GB&ceid=GB:en"


def collect_sources():
    results = []

    for feed in RSS_FEEDS:
        try:
            raw = fetch_url(feed["url"])
            results.extend(parse_feed(raw, feed["name"], feed["type"]))
        except Exception as e:
            results.append(
                add_quality_notes(
                    {
                        "source": feed["name"],
                        "type": feed["type"],
                        "url": feed["url"],
                        "error": str(e),
                    }
                )
            )

    for search in GOVUK_SEARCHES:
        try:
            raw = fetch_url(govuk_url(search["query"]))
            results.extend(parse_govuk_search(raw, search["name"], search["type"]))
        except Exception as e:
            results.append(
                add_quality_notes(
                    {
                        "source": search["name"],
                        "type": search["type"],
                        "url": govuk_url(search["query"]),
                        "error": str(e),
                    }
                )
            )

    for search in NEWS_SEARCHES:
        try:
            raw = fetch_url(google_news_url(search["query"]))
            results.extend(parse_feed(raw, search["name"], search["type"]))
        except Exception as e:
            results.append(
                add_quality_notes(
                    {
                        "source": search["name"],
                        "type": search["type"],
                        "url": google_news_url(search["query"]),
                        "error": str(e),
                    }
                )
            )

    for item in MANUAL_WATCHLIST:
        results.append(
            add_quality_notes(
                {
                    "source": item["source"],
                    "type": item["type"],
                    "title": item["title"],
                    "published": TODAY,
                    "url": item["url"],
                    "summary": item["summary"],
                    "manual_check": True,
                }
            )
        )

    results = sorted(
        results,
        key=lambda x: x.get("relevance_score", 0),
        reverse=True,
    )

    return results


def write_json(items):
    output_path = OUT_DIR / f"{TODAY}-business-source-pack.json"
    payload = {
        "date": TODAY,
        "purpose": "AI business adoption, BI/workflow, FMCG/distribution, SME software and market intelligence source pack.",
        "items": items,
    }

    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return output_path


def write_markdown(items):
    output_path = OUT_DIR / f"{TODAY}-business-source-pack.md"

    lines = []
    lines.append(f"# Business Source Pack - {TODAY}")
    lines.append("")
    lines.append("Purpose: source material for practical AI business adoption and market intelligence briefs.")
    lines.append("")
    lines.append("Use this file as input for `prompts/business_insight_prompt.md`.")
    lines.append("")
    lines.append("## Source selection reminder")
    lines.append("")
    lines.append("- Prefer implementation evidence over hype.")
    lines.append("- Treat vendor/company sources as biased primary signals.")
    lines.append("- Separate fact, meaning, risk and application.")
    lines.append("- Look for BI/workflow, FMCG/distribution, SME and market intelligence relevance.")
    lines.append("")
    lines.append("---")
    lines.append("")

    for idx, item in enumerate(items, start=1):
        lines.append(f"## {idx}. {item.get('title', 'Untitled')}")
        lines.append("")
        lines.append(f"**Source:** {item.get('source', '')}")
        lines.append(f"**Type:** {item.get('type', '')}")
        lines.append(f"**Published:** {item.get('published', '')}")
        lines.append(f"**URL:** {item.get('url', '')}")
        lines.append(f"**Relevance score:** {item.get('relevance_score', '')}/5")
        lines.append(f"**Quality note:** {item.get('quality_note', '')}")

        if item.get("manual_check"):
            lines.append("**Manual check:** Yes - this source is included as a watchlist item.")

        if item.get("error"):
            lines.append(f"**Fetch error:** {item.get('error')}")

        lines.append("")
        lines.append("**Summary:**")
        lines.append("")
        lines.append(item.get("summary", ""))
        lines.append("")
        lines.append("---")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main():
    items = collect_sources()
    json_path = write_json(items)
    md_path = write_markdown(items)

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Collected {len(items)} items")


if __name__ == "__main__":
    main()
