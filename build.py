"""Build the visual Frontier Model Matrix pages and atlas figure export from data/*.json.

The JSON files are the record. This script validates and renders them.
Run from the repository root: python build.py
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
HARNESS_DIR = DATA / "harnesses"

HUB = "https://minerclass.github.io/frontier-benchmark-atlas/"

PUBLISHER_LAB = {
    "Google DeepMind": "Google",
    "Anthropic": "Anthropic",
    "OpenAI": "OpenAI",
    "xAI": "xAI",
    "Meta": "Meta",
    "Cursor": "Cursor",
    "DeepSeek": "DeepSeek",
    "Moonshot AI": "Moonshot AI",
}

ORIGIN_LABEL = {
    "measured": "Measured by publisher",
    "quoted": "Quoted external",
    "derived": "Derived arithmetic",
    "unspecified": "Origin unspecified",
}

STANCE_LABEL = {
    "claim": "Own lab claim",
    "rival": "Rival table / quoted",
    "independent": "Independent run",
}

LAB_COLOR_VAR = {
    "Google": "var(--lab-google)",
    "Anthropic": "var(--lab-anthropic)",
    "OpenAI": "var(--lab-openai)",
    "Meta": "var(--lab-meta)",
    "xAI": "var(--lab-xai)",
    "Moonshot AI": "var(--lab-moonshot)",
    "DeepSeek": "var(--lab-deepseek)",
    "Z.AI": "var(--lab-zai)",
    "Cursor": "var(--lab-cursor)",
}


def load() -> tuple[dict, list[dict], list[dict]]:
    models = json.loads((DATA / "models.json").read_text(encoding="utf-8"))
    releases = json.loads((DATA / "releases.json").read_text(encoding="utf-8"))
    harnesses = []
    for path in sorted(HARNESS_DIR.glob("*.json")):
        harnesses.append(json.loads(path.read_text(encoding="utf-8")))
    return models, releases, harnesses


def esc(value) -> str:
    return html.escape("" if value is None else str(value))


def model_name(models: dict, model_id: str) -> str:
    found = models["models"].get(model_id)
    if not found:
        raise SystemExit(f"Unknown model id: {model_id}")
    return found["name"]


def lab_var(lab: str) -> str:
    return LAB_COLOR_VAR.get(lab, "var(--accent)")


def fmt_score_num(benchmark: dict, score: float) -> str:
    unit = benchmark["unit"]
    if unit == "percent":
        return f"{score:.1f}%"
    if unit == "elo":
        return f"{score:,.0f} Elo"
    if unit == "index":
        return f"{score:.0f}" if float(score).is_integer() else f"{score:.1f}"
    if unit == "usd":
        return f"${score:,.0f}" if score >= 100 and float(score).is_integer() else f"${score:,.2f}"
    return str(score)


def fmt_score(benchmark: dict, row: dict) -> str:
    text = fmt_score_num(benchmark, row["score"])
    effort = row.get("effort")
    if effort:
        text = f"{text} · {effort}"
    return text


def bar_width_pct(benchmark: dict, score: float, max_score: float) -> float:
    unit = benchmark["unit"]
    if unit == "percent":
        denom = max(100.0, max_score) if max_score > 0 else 100.0
        if max_score < 35:
            denom = max_score * 1.1
        return max(3.0, min(100.0, (score / denom) * 100.0))
    if unit == "elo":
        lo = 1200.0
        hi = max(1900.0, max_score)
        return max(4.0, min(100.0, ((score - lo) / (hi - lo)) * 100.0))
    denom = max_score if max_score > 0 else 1.0
    return max(4.0, min(100.0, (score / denom) * 100.0))


def score_bar_html(benchmark: dict, row: dict, max_score: float, color: str = "var(--accent)") -> str:
    num_txt = esc(fmt_score_num(benchmark, row["score"]))
    effort = row.get("effort")
    eff_html = f"<span class='score-effort'>{esc(effort)}</span>" if effort else ""
    pct = bar_width_pct(benchmark, row["score"], max_score)
    return (
        f"<div class='score-bar-wrap'>"
        f"<div><span class='score-num'>{num_txt}</span>{eff_html}</div>"
        f"<div class='bar-track'><div class='bar-fill' style='width:{pct:.1f}%;--bar-color:{color}'></div></div>"
        f"</div>"
    )


def origin_badge(origin: str) -> str:
    return f"<span class='badge badge-{esc(origin)}'>{esc(ORIGIN_LABEL[origin])}</span>"


def stance_badge(stance: str) -> str:
    return f"<span class='badge badge-{esc(stance)}'>{esc(STANCE_LABEL.get(stance, stance))}</span>"


def validate(models: dict, harnesses: list[dict]) -> None:
    known = set(models["models"])
    benchmark_ids: dict[str, str] = {}
    for harness in harnesses:
        for bench in harness["benchmarks"]:
            previous = benchmark_ids.get(bench["id"])
            if previous and previous != bench["unit"]:
                raise SystemExit(
                    f"{bench['id']} uses unit {bench['unit']} in {harness['id']} "
                    f"and {previous} elsewhere"
                )
            benchmark_ids[bench["id"]] = bench["unit"]
            for row in bench["rows"]:
                if row["modelId"] not in known:
                    raise SystemExit(f"{harness['id']} cites unknown model {row['modelId']}")
                if row["origin"] not in ORIGIN_LABEL:
                    raise SystemExit(f"Bad origin on {harness['id']} {bench['id']} {row['modelId']}")
                if row["origin"] in {"quoted", "derived"} and not row.get("note"):
                    raise SystemExit(
                        f"{harness['id']} {bench['id']} {row['modelId']} needs a note"
                    )


def page(title: str, body: str, depth: int, current_nav: str = "") -> str:
    prefix = "../" * depth
    nav_items = [
        (HUB, "Atlas hub", "hub"),
        (f"{prefix}index.html", "Visual Atlas", "index"),
        (f"{prefix}harnesses/index.html", "Harnesses", "harnesses"),
        (f"{prefix}models/index.html", "Models", "models"),
        (f"{prefix}NOTES.md", "Notes", "notes"),
    ]
    nav_links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if key == current_nav else ""}>{label}</a>'
        for href, label, key in nav_items
    )
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <script>
    (function() {{
      try {{
        var saved = localStorage.getItem("fmm-theme");
        document.documentElement.setAttribute("data-theme", saved === "light" ? "light" : "dark");
      }} catch (e) {{
        document.documentElement.setAttribute("data-theme", "dark");
      }}
    }})();
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
  <link rel="stylesheet" href="{prefix}assets/site.css?v=5">
  <script src="{prefix}assets/site.js?v=5" defer></script>
</head>
<body>
  <header class="site">
    <a class="brand" href="{prefix}index.html">
      <span class="brand-mark" aria-hidden="true"></span>
      <span>Frontier Model Matrix</span>
    </a>
    <nav aria-label="Primary">
      {nav_links}
      <button type="button" id="theme-toggle" class="theme-btn" aria-label="Dark mode" aria-pressed="true" onclick="window.__fmmToggleTheme&&window.__fmmToggleTheme()">
        <span>Dark mode</span>
      </button>
    </nav>
  </header>
  <main>
    {body}
  </main>
  <footer class="site-footer">
    <span>Published scores only · Never averages company claims with independent runs · Blank cells mean unpublished</span>
    <span>Cursor compilation · Revision 3 (13 Nov 2026) · <a href="{HUB}">Frontier Benchmark Atlas</a></span>
  </footer>
</body>
</html>
"""


def render_table(headers: list[str], rows: list[list[str]], row_attrs: list[str] | None = None) -> str:
    head = "".join(f"<th scope='col'>{esc(item)}</th>" for item in headers)
    body = []
    for idx, row in enumerate(rows):
        attr = f" {row_attrs[idx]}" if row_attrs and idx < len(row_attrs) and row_attrs[idx] else ""
        cells = "".join(f"<td>{item}</td>" for item in row)
        body.append(f"<tr{attr}>{cells}</tr>")
    return f"<div class='table-wrap'><table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"


def classify(harness: dict, model: dict, row: dict) -> tuple[str, str]:
    if row.get("stance") and row.get("publishedBy"):
        return row["stance"], row["publishedBy"]
    publisher = harness["publisher"]
    kind = harness["kind"]
    if "Independent" in kind or "Third-party" in kind:
        return "independent", publisher
    if row["origin"] in {"quoted", "unspecified"}:
        return "rival", publisher
    if row["origin"] in {"measured", "derived"} and PUBLISHER_LAB.get(publisher) == model["lab"]:
        return "claim", publisher
    return "rival", publisher


def money(value) -> str:
    if value is None:
        return "—"
    return f"${value:,.2f}"


def num(value) -> str:
    if value is None:
        return "—"
    return f"{value:,}"


def render_harness(models: dict, harness: dict, depth: int = 1) -> str:
    lists = []
    for key, label in (("howItCompiles", "How this harness compiles a score"), ("limits", "Scope & boundaries")):
        items = "".join(f"<li>{esc(item)}</li>" for item in harness.get(key, []))
        lists.append(f"<div class='dir-card'><h3>{label}</h3><ul class='clean-list'>{items}</ul></div>")

    panels = []
    for panel in harness.get("panels", []):
        rendered = render_table(panel["headers"], [[esc(cell) for cell in row] for row in panel["rows"]])
        panels.append(f"<section class='sheet'><h2>{esc(panel['title'])}</h2>{rendered}</section>")

    benches = []
    for bench in harness["benchmarks"]:
        ordered = sorted(
            bench["rows"],
            key=lambda row: (
                -row["score"] if bench["higherIsBetter"] else row["score"],
                model_name(models, row["modelId"]),
            ),
        )
        max_s = max((r["score"] for r in ordered), default=100.0)
        has_cost = any("costUsd" in row for row in ordered)
        has_tokens = any("tokens" in row for row in ordered)

        rows = []
        for row in ordered:
            m_meta = models["models"][row["modelId"]]
            stance, _ = classify(harness, m_meta, row)
            b_color = (
                "var(--stance-claim)" if stance == "claim"
                else "var(--stance-indep)" if stance == "independent"
                else "var(--stance-rival)"
            )
            m_cell = (
                f"<span class='lab-dot' style='background:{lab_var(m_meta['lab'])};margin-right:7px'></span>"
                f"<a href='../models/{esc(row['modelId'])}.html'><strong>{esc(m_meta['name'])}</strong></a>"
            )
            s_cell = f"<div class='score-cell'>{score_bar_html(bench, row, max_s, b_color)}</div>"
            if has_tokens:
                rows.append([
                    m_cell,
                    s_cell,
                    f"<span class='num-col'>{esc(money(row.get('costUsd')))}</span>",
                    f"<span class='num-col'>{esc(num(row.get('tokens')))}</span>",
                    f"<span class='num-col'>{esc(num(row.get('steps')))}</span>",
                    origin_badge(row["origin"]),
                    esc(row.get("note") or ""),
                ])
            elif has_cost:
                rows.append([
                    m_cell,
                    s_cell,
                    f"<span class='num-col'>{esc(money(row.get('costUsd')))}</span>",
                    origin_badge(row["origin"]),
                    esc(row.get("note") or ""),
                ])
            else:
                rows.append([
                    m_cell,
                    s_cell,
                    origin_badge(row["origin"]),
                    esc(row.get("note") or ""),
                ])

        if has_tokens:
            headers = ["Model", "Score & effort", "Cost / task", "Tokens / task", "Steps / task", "Origin", "Note"]
        elif has_cost:
            headers = ["Model", "Score & effort", "Cost / task", "Origin", "Note"]
        else:
            headers = ["Model", "Score & effort", "Origin", "Note"]

        direction_txt = "Higher is better" if bench["higherIsBetter"] else "Lower is better"
        benches.append(
            f"<section class='sheet'>"
            f"<div class='section-head'><div>"
            f"<span class='eyebrow'>{esc(bench['id'])} · {esc(bench['unit'])} · {direction_txt}</span>"
            f"<h2>{esc(bench['name'])}</h2>"
            f"<p class='sub'>{esc(bench['about'])}</p>"
            f"</div><span class='badge'>{len(ordered)} rows</span></div>"
            f"{render_table(headers, rows)}"
            f"</section>"
        )

    total_rows = sum(len(b["rows"]) for b in harness["benchmarks"])
    body = f"""
    <section class="sheet hero-sheet">
      <span class="kicker">{esc(harness['kind'])} · {esc(harness['publisher'])} · read {esc(harness['readOn'])}</span>
      <h1>{esc(harness['title'])}</h1>
      <p class="lede">{esc(harness['summary'])}</p>
      <p class="meta">Primary URL: <a href="{esc(harness['url'])}" target="_blank" rel="noopener">{esc(harness['url'])} ↗</a> · {len(harness['benchmarks'])} benchmarks · {total_rows} recorded cells</p>
      <div class="dir-grid">{''.join(lists)}</div>
    </section>
    {''.join(panels)}
    {''.join(benches)}
    """
    return page(f"{harness['title']} · Frontier Model Matrix", body, depth, "harnesses")


def collect_benchmarks(harnesses: list[dict]) -> dict[str, dict]:
    found: dict[str, dict] = {}
    for harness in harnesses:
        for bench in harness["benchmarks"]:
            bucket = found.setdefault(bench["id"], {
                "id": bench["id"],
                "name": bench["name"],
                "unit": bench["unit"],
                "higherIsBetter": bench["higherIsBetter"],
                "harnesses": {},
            })
            bucket["harnesses"][harness["id"]] = {
                "title": harness["title"],
                "publisher": harness["publisher"],
                "kind": harness["kind"],
                "rows": bench["rows"],
            }
    return found


def best_row(rows: list[dict], model_id: str, higher_is_better: bool = True) -> dict | None:
    matching = [row for row in rows if row["modelId"] == model_id]
    if not matching:
        return None
    return max(matching, key=lambda row: row["score"]) if higher_is_better else min(matching, key=lambda row: row["score"])


def build_compact_atlas_payload(models: dict, releases: list[dict], harnesses: list[dict]) -> str:
    compact_figs = []
    for harness in harnesses:
        for bench in harness["benchmarks"]:
            for row in bench["rows"]:
                m_meta = models["models"][row["modelId"]]
                stance, pub = classify(harness, m_meta, row)
                compact_figs.append({
                    "m": row["modelId"],
                    "bId": bench["id"],
                    "b": bench["name"],
                    "v": row["score"],
                    "u": bench["unit"],
                    "pub": pub,
                    "st": stance,
                    "set": row.get("effort") or "",
                    "cost": row.get("costUsd"),
                    "orig": row["origin"],
                    "note": row.get("note") or "",
                    "url": row.get("sourceUrl") or harness["url"],
                    "date": row.get("sourceDate") or harness["readOn"],
                    "hId": harness["id"],
                })
    payload = {
        "models": models["models"],
        "releases": releases,
        "figures": compact_figs,
    }
    return json.dumps(payload, separators=(",", ":")).replace("</", "<\\/")


def render_index(models: dict, releases: list[dict], harnesses: list[dict], total_figures: int) -> str:
    harness_pub = {h["id"]: h["publisher"] for h in harnesses}
    timeline_cards = []
    for item in releases[:16]:
        pub = harness_pub.get(item["harness"], "Cursor")
        mapped_lab = PUBLISHER_LAB.get(pub, "Google" if "google" in item["harness"] else "Cursor")
        c_var = lab_var(mapped_lab)
        timeline_cards.append(
            f"<article class='tl-card' style='--tl-color:{c_var}'>"
            f"<time>{esc(item['date'])} · {esc(pub)}</time>"
            f"<h3><a href='harnesses/{esc(item['harness'])}.html'>{esc(item['title'])}</a></h3>"
            f"<p>{esc(item['note'])}</p>"
            f"</article>"
        )

    contested = []
    shared_benches = [
        b for b in collect_benchmarks(harnesses).values()
        if len(b["harnesses"]) >= 2
    ]
    shared_benches.sort(key=lambda b: (-len(b["harnesses"]), b["name"]))

    for idx, bench in enumerate(shared_benches):
        harness_ids = list(bench["harnesses"])
        model_ids = []
        all_scores = []
        for payload in bench["harnesses"].values():
            for row in payload["rows"]:
                all_scores.append(row["score"])
                if row["modelId"] not in model_ids:
                    model_ids.append(row["modelId"])
        max_s = max(all_scores, default=100.0)
        headers = ["Model", *[bench["harnesses"][item]["title"] for item in harness_ids]]
        rows = []
        row_attrs = []
        for model_id in model_ids:
            m_meta = models["models"][model_id]
            row_attrs.append(f"data-model-row='{esc(model_id)}'")
            cells = [
                f"<span class='lab-dot' style='background:{lab_var(m_meta['lab'])};margin-right:7px'></span>"
                f"<a href='models/{esc(model_id)}.html'><strong>{esc(m_meta['name'])}</strong></a>"
            ]
            for harness_id in harness_ids:
                h_info = bench["harnesses"][harness_id]
                row = best_row(h_info["rows"], model_id, bench["higherIsBetter"])
                if row is None:
                    cells.append("<span class='meta'>—</span>")
                else:
                    stance, _ = classify({"publisher": h_info["publisher"], "kind": h_info["kind"]}, m_meta, row)
                    b_color = (
                        "var(--stance-claim)" if stance == "claim"
                        else "var(--stance-indep)" if stance == "independent"
                        else "var(--stance-rival)"
                    )
                    cells.append(
                        f"<div class='score-cell'>{score_bar_html(bench, row, max_s, b_color)}"
                        f"<div style='margin-top:3px'>{origin_badge(row['origin'])}</div></div>"
                    )
            rows.append(cells)

        best_word = "highest" if bench["higherIsBetter"] else "lowest"
        open_attr = " open" if idx < 3 else ""
        contested.append(
            f"<details class='contested-details'{open_attr}>"
            f"<summary><span>{esc(bench['name'])}</span>"
            f"<span class='badge'>{len(harness_ids)} publishers · {len(model_ids)} models</span></summary>"
            f"<p class='meta' style='margin-bottom:8px'>Same benchmark ID (<code>{esc(bench['id'])}</code>) across publishers. "
            f"Each cell shows that publisher's {best_word} published score, effort, and provenance. Blank cells were not published.</p>"
            f"{render_table(headers, rows, row_attrs)}"
            f"</details>"
        )

    atlas_json = build_compact_atlas_payload(models, releases, harnesses)

    body = f"""
    <section class="sheet hero-sheet">
      <span class="eyebrow">Frontier Benchmark Atlas · Cursor Visual Compilation · Revision 3</span>
      <h1>September–November 2026 Frontier Model Atlas</h1>
      <p class="lede">Interactive schematics and multi-source charts comparing Google's Gemini 4 Hydrogen, Carbon, and Argon, Anthropic's Claude Fable 5.2, Mythos 5.2, and 5.5 tiers, OpenAI's GPT-6 Astra, Sol, and GPT-6.1 Sol and Terra, Meta's Muse Wonder, Spark Open, and Ember, xAI's Grok 4.7, and leading open-weight models across vendor claims and independent runs.</p>
      <div class="stat-strip">
        <div class="stat-card"><b>{len(models['models'])}</b><span>Models mapped</span></div>
        <div class="stat-card"><b>{len(harnesses)}</b><span>Publisher & evaluator harnesses</span></div>
        <div class="stat-card"><b>{total_figures}</b><span>Sourced benchmark figures</span></div>
        <div class="stat-card"><b>100%</b><span>Read directly from primary pages</span></div>
      </div>
      <div class="jump-bar" aria-label="Jump to section">
        <a class="jump-pill" href="#schematic">1 · Lineage & Routing Schematic</a>
        <a class="jump-pill" href="#dotplot">2 · Claims vs. Independent Dot-Plot</a>
        <a class="jump-pill" href="#pareto">3 · Cost vs. Score Pareto Frontier</a>
        <a class="jump-pill" href="#timeline">4 · Sept–Nov Release Timeline</a>
        <a class="jump-pill" href="#matrix">5 · Cross-Publisher Matrix</a>
      </div>
    </section>

    <section class="control-bar" aria-label="Filter and spotlight controls">
      <div class="chip-group" id="lab-filter-chips" role="group" aria-label="Filter by lab"></div>
      <div class="control-inputs">
        <label for="model-spotlight">Spotlight</label>
        <select id="model-spotlight"></select>
        <button type="button" id="clear-spotlight" class="btn-small">Reset</button>
      </div>
    </section>

    <section class="sheet" id="schematic" aria-labelledby="h-schematic">
      <div class="section-head">
        <div>
          <span class="eyebrow">Station 1 · Architecture, Routing & Lineage</span>
          <h2 id="h-schematic">How the September–November 2026 model families connect</h2>
          <p class="sub">Select any model card to inspect its role, release date, and claim-versus-independent benchmark profile, or to highlight it across the charts below.</p>
        </div>
        <span class="meta">Click a node to inspect &amp; spotlight</span>
      </div>
      <div class="schematic-layout">
        <div class="lanes" id="schematic-lanes"></div>
        <aside class="inspector" id="model-inspector" aria-live="polite"></aside>
      </div>
    </section>

    <section class="sheet" id="dotplot" aria-labelledby="h-dotplot">
      <div class="section-head">
        <div>
          <span class="eyebrow">Station 2 · Vendor Claims Beside Independent Evaluators</span>
          <h2 id="h-dotplot">Side-by-side benchmark comparison (never averaged)</h2>
          <p class="sub" id="dotplot-note"></p>
        </div>
        <div class="control-inputs">
          <label for="dotplot-select">Benchmark</label>
          <select id="dotplot-select"></select>
        </div>
      </div>
      <div class="legend-row" aria-label="Marker legend">
        <span class="legend-item">
          <svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="5.5" fill="var(--stance-claim)"/></svg>
          <span>Circle · Lab's own claim</span>
        </span>
        <span class="legend-item">
          <svg viewBox="0 0 16 16" aria-hidden="true"><polygon points="8,2 14,8 8,14 2,8" fill="var(--stance-rival)"/></svg>
          <span>Diamond · Rival lab table / quoted</span>
        </span>
        <span class="legend-item">
          <svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="3" width="10" height="10" rx="2" fill="var(--stance-indep)"/></svg>
          <span>Square · Independent (Artificial Analysis / CursorBench)</span>
        </span>
        <span class="legend-item">
          <svg viewBox="0 0 16 16" aria-hidden="true"><polygon points="8,2 14,13 2,13" fill="var(--stance-indep)"/></svg>
          <span>Triangle · Independent (Vals AI)</span>
        </span>
      </div>
      <div class="readout-box" id="dotplot-readout" aria-live="polite">Hover or focus any marker to inspect its exact score, effort setting, publisher, and primary source link.</div>
      <div class="chart-scroll">
        <svg id="dotplot-svg" class="chart-svg" role="img" aria-label="Side-by-side dot plot comparing model claims, rival tables, and independent runs"></svg>
      </div>
    </section>

    <section class="sheet" id="pareto" aria-labelledby="h-pareto">
      <div class="section-head">
        <div>
          <span class="eyebrow">Station 3 · Capability Per Dollar</span>
          <h2 id="h-pareto">Cost per task vs. score &amp; effort trajectories</h2>
          <p class="sub">Logarithmic cost per task on the horizontal axis against benchmark score on the vertical axis. Models on the upper-left dashed envelope form the empirical Pareto efficiency frontier: no recorded run scores higher for less money.</p>
        </div>
        <div class="control-inputs">
          <label for="pareto-select">Dataset</label>
          <select id="pareto-select"></select>
        </div>
      </div>
      <div class="toggle-checks">
        <label><input type="checkbox" id="chk-trajectories" checked> Connect reasoning-effort curves per model</label>
        <label><input type="checkbox" id="chk-frontier" checked> Highlight Pareto efficiency frontier</label>
      </div>
      <div class="readout-box" id="pareto-readout" aria-live="polite">Select or hover a point to inspect its score and task cost.</div>
      <div class="chart-scroll">
        <svg id="pareto-svg" class="chart-svg" role="img" aria-label="Log-cost versus benchmark score scatterplot with Pareto efficiency frontier"></svg>
      </div>
    </section>

    <section class="sheet" id="timeline" aria-labelledby="h-timeline">
      <div class="section-head">
        <div>
          <span class="eyebrow">Station 4 · Chronology</span>
          <h2 id="h-timeline">Releases &amp; benchmark updates (September–November 2026)</h2>
          <p class="sub">Each release links to the publisher or evaluator page where its primary figures are stored.</p>
        </div>
        <a href="harnesses/index.html" class="jump-pill">Browse all {len(harnesses)} harness pages →</a>
      </div>
      <div class="timeline-grid">{''.join(timeline_cards)}</div>
    </section>

    <section class="sheet" id="matrix" aria-labelledby="h-matrix">
      <div class="section-head">
        <div>
          <span class="eyebrow">Station 5 · Structured Cross-Check Tables</span>
          <h2 id="h-matrix">Where two or more publishers recorded the same benchmark ID</h2>
          <p class="sub">Expand any benchmark to compare exact numbers, effort settings, and provenance badges side by side.</p>
        </div>
        <span class="meta">{len(shared_benches)} shared benchmark IDs</span>
      </div>
      <div style="display:grid;gap:10px">{''.join(contested)}</div>
    </section>

    <script id="fmm-atlas-data" type="application/json">{atlas_json}</script>
    """
    return page("Frontier Model Matrix · Sept–Nov 2026 Visual Atlas", body, 0, "index")


def render_model(models: dict, model_id: str, meta: dict, harnesses: list[dict]) -> str:
    sections = []
    total_cells = 0
    stance_counts = {"claim": 0, "independent": 0, "rival": 0}
    for harness in harnesses:
        blocks = []
        for bench in harness["benchmarks"]:
            rows = [row for row in bench["rows"] if row["modelId"] == model_id]
            if not rows:
                continue
            max_s = max((r["score"] for r in bench["rows"]), default=100.0)
            table_rows = []
            for row in rows:
                total_cells += 1
                st, _ = classify(harness, meta, row)
                stance_counts[st] = stance_counts.get(st, 0) + 1
                b_color = (
                    "var(--stance-claim)" if st == "claim"
                    else "var(--stance-indep)" if st == "independent"
                    else "var(--stance-rival)"
                )
                table_rows.append([
                    f"<div class='score-cell'>{score_bar_html(bench, row, max_s, b_color)}</div>",
                    f"{stance_badge(st)} {origin_badge(row['origin'])}",
                    esc(row.get("note") or ""),
                ])
            rendered = render_table(["Score & effort", "Provenance", "Note"], table_rows)
            blocks.append(f"<div style='display:grid;gap:6px'><h3>{esc(bench['name'])}</h3>{rendered}</div>")
        if blocks:
            sections.append(
                f"<section class='sheet'>"
                f"<div class='section-head'><div>"
                f"<span class='eyebrow'>{esc(harness['publisher'])} · read {esc(harness['readOn'])}</span>"
                f"<h2><a href='../harnesses/{esc(harness['id'])}.html'>{esc(harness['title'])}</a></h2>"
                f"</div><span class='badge'>{esc(harness['kind'])}</span></div>"
                + "".join(blocks)
                + "</section>"
            )
    if not sections:
        sections.append("<section class='sheet'><p>No harness in this repository has published a score for this model yet.</p></section>")

    body = f"""
    <section class="sheet hero-sheet">
      <span class="kicker" style="color:{lab_var(meta['lab'])}">{esc(meta['lab'])} · {esc(meta['family'])}</span>
      <h1>{esc(meta['name'])}</h1>
      <p class="lede">{esc(meta['role'])}</p>
      <div style="display:flex;flex-wrap:wrap;gap:8px">
        <span class="badge">{total_cells} total figures</span>
        <span class="badge badge-claim">{stance_counts['claim']} own claims</span>
        <span class="badge badge-independent">{stance_counts['independent']} independent runs</span>
        <span class="badge badge-rival">{stance_counts['rival']} rival tables</span>
      </div>
      <p class="meta">Read each publisher block as that source compiled it; do not average across blocks.</p>
    </section>
    {''.join(sections)}
    """
    return page(f"{meta['name']} · Frontier Model Matrix", body, 1, "models")


def render_model_index(models: dict, harnesses: list[dict]) -> str:
    counts: dict[str, int] = {mid: 0 for mid in models["models"]}
    for h in harnesses:
        for b in h["benchmarks"]:
            for r in b["rows"]:
                counts[r["modelId"]] = counts.get(r["modelId"], 0) + 1

    cards = []
    for model_id, meta in sorted(models["models"].items(), key=lambda kv: (kv[1]["lab"], kv[1]["name"])):
        cards.append(
            f"<article class='dir-card' style='border-top:3px solid {lab_var(meta['lab'])}'>"
            f"<div class='node-top'><span class='eyebrow'>{esc(meta['lab'])} · {esc(meta['family'])}</span>"
            f"<span class='badge'>{counts.get(model_id, 0)} figures</span></div>"
            f"<h3><a href='{esc(model_id)}.html'>{esc(meta['name'])}</a></h3>"
            f"<p class='sub' style='font-size:0.85rem'>{esc(meta['role'])}</p>"
            f"</article>"
        )
    body = f"""
    <section class="sheet hero-sheet">
      <span class="eyebrow">Model Directory</span>
      <h1>{len(models['models'])} Frontier &amp; Reference Models</h1>
      <p class="lede">Open any model to inspect every claim, rival-table citation, and independent evaluation stored across the 13 harnesses.</p>
    </section>
    <section class="sheet">
      <div class="dir-grid">{''.join(cards)}</div>
    </section>
    """
    return page("Models · Frontier Model Matrix", body, 1, "models")


def render_harness_index(harnesses: list[dict]) -> str:
    cards = []
    for item in harnesses:
        n_benches = len(item["benchmarks"])
        n_rows = sum(len(b["rows"]) for b in item["benchmarks"])
        mapped_lab = PUBLISHER_LAB.get(item["publisher"], "Cursor")
        cards.append(
            f"<article class='dir-card' style='border-top:3px solid {lab_var(mapped_lab)}'>"
            f"<div class='node-top'><span class='eyebrow'>{esc(item['publisher'])} · {esc(item['kind'])}</span>"
            f"<span class='badge'>{n_rows} cells</span></div>"
            f"<h3><a href='{esc(item['id'])}.html'>{esc(item['title'])}</a></h3>"
            f"<p class='sub' style='font-size:0.85rem'>{esc(item['summary'])}</p>"
            f"<span class='meta'>{n_benches} benchmarks · read {esc(item['readOn'])}</span>"
            f"</article>"
        )
    body = f"""
    <section class="sheet hero-sheet">
      <span class="eyebrow">Publisher &amp; Evaluator Harnesses</span>
      <h1>{len(harnesses)} Primary Score Sources</h1>
      <p class="lede">One page per publisher or independent evaluator. Every figure stays in the file of the organization that printed it.</p>
    </section>
    <section class="sheet">
      <div class="dir-grid">{''.join(cards)}</div>
    </section>
    """
    return page("Harnesses · Frontier Model Matrix", body, 1, "harnesses")


def write_figures(models: dict, harnesses: list[dict]) -> int:
    figures = []
    for harness in harnesses:
        for bench in harness["benchmarks"]:
            for row in bench["rows"]:
                model = models["models"][row["modelId"]]
                stance, published_by = classify(harness, model, row)
                figures.append({
                    "model": row["modelId"],
                    "benchmark": bench["name"],
                    "benchmarkId": bench["id"],
                    "value": row["score"],
                    "unit": bench["unit"],
                    "publishedBy": published_by,
                    "stance": stance,
                    "setting": row.get("effort") or "",
                    "sourceUrl": row.get("sourceUrl") or harness["url"],
                    "sourceDate": row.get("sourceDate") or harness["readOn"],
                    "readDirectly": row.get("readDirectly", True),
                    "origin": row["origin"],
                    "note": row.get("note") or "",
                    "storedIn": f"data/harnesses/{harness['id']}.json",
                })
    payload = {
        "compiler": "cursor",
        "computer": "surface-arm",
        "revision": 3,
        "compiledOn": "2026-11-13",
        "brief": "Frontier Benchmark Atlas brief, surface-arm/claude-code, 2026-10-13",
        "hub": HUB,
        "figures": figures,
    }
    (DATA / "figures.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return len(figures)


def main() -> None:
    models, releases, harnesses = load()
    validate(models, harnesses)
    (ROOT / "harnesses").mkdir(exist_ok=True)
    (ROOT / "models").mkdir(exist_ok=True)
    count = write_figures(models, harnesses)
    (ROOT / "index.html").write_text(render_index(models, releases, harnesses, count), encoding="utf-8")
    (ROOT / "harnesses" / "index.html").write_text(render_harness_index(harnesses), encoding="utf-8")
    (ROOT / "models" / "index.html").write_text(render_model_index(models, harnesses), encoding="utf-8")
    for harness in harnesses:
        (ROOT / "harnesses" / f"{harness['id']}.html").write_text(
            render_harness(models, harness), encoding="utf-8"
        )
    for model_id, meta in models["models"].items():
        (ROOT / "models" / f"{model_id}.html").write_text(
            render_model(models, model_id, meta, harnesses), encoding="utf-8"
        )
    print(f"Wrote {len(harnesses)} harness pages, {len(models['models'])} model pages, and {count} figures.")


if __name__ == "__main__":
    main()
