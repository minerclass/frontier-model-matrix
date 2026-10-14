"""Build the local harness pages from data/*.json.

The JSON files are the record. This script only renders them.
Run from the repository root: python build.py
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
HARNESS_DIR = DATA / "harnesses"

ORIGIN_LABEL = {
    "measured": "Measured by this publisher",
    "quoted": "Quoted from another lab",
    "derived": "Arithmetic on a published claim",
    "unspecified": "Publisher did not say who ran it",
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


def fmt_score(benchmark: dict, row: dict) -> str:
    score = row["score"]
    unit = benchmark["unit"]
    if unit == "percent":
        text = f"{score:.1f}%"
    elif unit == "elo":
        text = f"{score:.0f} Elo"
    elif unit == "index":
        text = f"{score:.0f}"
    elif unit == "usd":
        text = f"${score:.2f}"
    else:
        text = str(score)
    effort = row.get("effort")
    if effort:
        text = f"{text} · {effort}"
    return text


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


def page(title: str, body: str, depth: int) -> str:
    prefix = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <link rel="stylesheet" href="{prefix}assets/site.css">
</head>
<body>
  <header class="site">
    <a href="{prefix}index.html">Frontier model matrix</a>
    <nav>
      <a href="{prefix}index.html">Comparison</a>
      <a href="{prefix}harnesses/index.html">Harnesses</a>
      <a href="{prefix}models/index.html">Models</a>
    </nav>
  </header>
  <main>
    {body}
  </main>
  <footer>
    <p>Published scores only. This repository does not test models. A blank cell was not published by that harness.</p>
  </footer>
</body>
</html>
"""


def render_table(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f"<th>{esc(item)}</th>" for item in headers)
    body = []
    for row in rows:
        cells = "".join(f"<td>{item}</td>" for item in row)
        body.append(f"<tr>{cells}</tr>")
    return f"<div class='table-wrap'><table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"


def render_harness(models: dict, harness: dict, depth: int = 1) -> str:
    lists = []
    for key, label in (("howItCompiles", "How this harness compiles a score"), ("limits", "What this page does not claim")):
        items = "".join(f"<li>{esc(item)}</li>" for item in harness.get(key, []))
        lists.append(f"<h2>{label}</h2><ul>{items}</ul>")
    panels = []
    for panel in harness.get("panels", []):
        rendered = render_table(panel["headers"], [[esc(cell) for cell in row] for row in panel["rows"]])
        panels.append(f"<h2>{esc(panel['title'])}</h2>{rendered}")
    benches = []
    for bench in harness["benchmarks"]:
        rows = []
        ordered = sorted(
            bench["rows"],
            key=lambda row: (
                -row["score"] if bench["higherIsBetter"] else row["score"],
                model_name(models, row["modelId"]),
            ),
        )
        for row in ordered:
            rows.append([
                f"<a href='../models/{esc(row['modelId'])}.html'>{esc(model_name(models, row['modelId']))}</a>",
                esc(fmt_score(bench, row)),
                esc(ORIGIN_LABEL[row["origin"]]),
                esc(row.get("note") or ""),
            ])
        extra = []
        if any("costUsd" in row for row in bench["rows"]):
            extra = ["Cost / task", "Tokens / task", "Steps / task"]
            rows = []
            for row in ordered:
                rows.append([
                    f"<a href='../models/{esc(row['modelId'])}.html'>{esc(model_name(models, row['modelId']))}</a>",
                    esc(fmt_score(bench, row)),
                    esc(money(row.get("costUsd"))),
                    esc(num(row.get("tokens"))),
                    esc(num(row.get("steps"))),
                    esc(ORIGIN_LABEL[row["origin"]]),
                    esc(row.get("note") or ""),
                ])
        headers = ["Model", "Score", *extra, "Origin", "Note"] if extra else ["Model", "Score", "Origin", "Note"]
        benches.append(
            f"<h2>{esc(bench['name'])}</h2><p>{esc(bench['about'])}</p>"
            f"<p class='meta'>Unit: {esc(bench['unit'])}. Higher is better: {esc(bench['higherIsBetter'])}.</p>"
            + render_table(headers, rows)
        )
    body = f"""
    <p class='kicker'>{esc(harness['kind'])} · read {esc(harness['readOn'])}</p>
    <h1>{esc(harness['title'])}</h1>
    <p>{esc(harness['summary'])}</p>
    <p><a href='{esc(harness['url'])}'>{esc(harness['url'])}</a></p>
    {''.join(lists)}
    {''.join(panels)}
    {''.join(benches)}
    """
    return page(harness["title"], body, depth)


def money(value) -> str:
    if value is None:
        return ""
    return f"${value:.2f}"


def num(value) -> str:
    if value is None:
        return ""
    return f"{value:,}"


def collect_benchmarks(harnesses: list[dict]) -> dict[str, dict]:
    found: dict[str, dict] = {}
    for harness in harnesses:
        for bench in harness["benchmarks"]:
            bucket = found.setdefault(bench["id"], {
                "id": bench["id"],
                "name": bench["name"],
                "unit": bench["unit"],
                "harnesses": {},
            })
            bucket["harnesses"][harness["id"]] = {
                "title": harness["title"],
                "rows": bench["rows"],
            }
    return found


def best_row(rows: list[dict], model_id: str) -> dict | None:
    matching = [row for row in rows if row["modelId"] == model_id]
    if not matching:
        return None
    return max(matching, key=lambda row: row["score"])


def render_index(models: dict, releases: list[dict], harnesses: list[dict]) -> str:
    release_rows = [
        [esc(item["date"]), esc(item["title"]), f"<a href='harnesses/{esc(item['harness'])}.html'>{esc(item['harness'])}</a>", esc(item["note"])]
        for item in releases
    ]
    harness_rows = [
        [f"<a href='harnesses/{esc(item['id'])}.html'>{esc(item['title'])}</a>", esc(item["publisher"]), esc(item["kind"]), esc(item["readOn"])]
        for item in harnesses
    ]
    contested = []
    for bench in collect_benchmarks(harnesses).values():
        if len(bench["harnesses"]) < 2:
            continue
        harness_ids = list(bench["harnesses"])
        model_ids = []
        for payload in bench["harnesses"].values():
            for row in payload["rows"]:
                if row["modelId"] not in model_ids:
                    model_ids.append(row["modelId"])
        headers = ["Model", *[bench["harnesses"][item]["title"] for item in harness_ids]]
        rows = []
        for model_id in model_ids:
            cells = [f"<a href='models/{esc(model_id)}.html'>{esc(model_name(models, model_id))}</a>"]
            for harness_id in harness_ids:
                row = best_row(bench["harnesses"][harness_id]["rows"], model_id)
                if row is None:
                    cells.append("")
                else:
                    cells.append(esc(f"{fmt_score({'unit': bench['unit']}, row)} ({row['origin']})"))
            rows.append(cells)
        contested.append(
            f"<h2>{esc(bench['name'])}</h2>"
            f"<p class='meta'>Same benchmark id across harnesses. A cell is that harness's highest published score for the model, with effort and origin. An empty cell means that harness did not publish one.</p>"
            + render_table(headers, rows)
        )
    body = f"""
    <h1>Frontier model matrix</h1>
    <p>Each harness keeps the scores it published. The comparison below lines up those publications. It is not an in-house test, and it does not average a lab's claim with another lab's measurement.</p>
    <h2>Releases recorded here</h2>
    {render_table(["Date", "Release", "Harness page", "Note"], release_rows)}
    <h2>Harnesses</h2>
    {render_table(["Page", "Publisher", "Kind", "Read on"], harness_rows)}
    <h2>Where more than one harness published the same benchmark</h2>
    {''.join(contested)}
    """
    return page("Frontier model matrix", body, 0)


def render_model(models: dict, model_id: str, meta: dict, harnesses: list[dict]) -> str:
    sections = []
    for harness in harnesses:
        blocks = []
        for bench in harness["benchmarks"]:
            rows = [row for row in bench["rows"] if row["modelId"] == model_id]
            if not rows:
                continue
            rendered = render_table(
                ["Score", "Origin", "Note"],
                [[esc(fmt_score(bench, row)), esc(ORIGIN_LABEL[row["origin"]]), esc(row.get("note") or "")] for row in rows],
            )
            blocks.append(f"<h3>{esc(bench['name'])}</h3>{rendered}")
        if blocks:
            sections.append(
                f"<h2><a href='../harnesses/{esc(harness['id'])}.html'>{esc(harness['title'])}</a></h2>"
                f"<p class='meta'>{esc(harness['publisher'])} · read {esc(harness['readOn'])}</p>"
                + "".join(blocks)
            )
    if not sections:
        sections.append("<p>No harness in this repository has published a score for this model yet.</p>")
    body = f"""
    <p class='kicker'>{esc(meta['lab'])} · {esc(meta['family'])}</p>
    <h1>{esc(meta['name'])}</h1>
    <p>{esc(meta['role'])}</p>
    <p>This page repeats every stored cell for this model. Read each block as that harness compiled it. Do not treat two blocks as one experiment.</p>
    {''.join(sections)}
    """
    return page(meta["name"], body, 1)


def render_model_index(models: dict) -> str:
    rows = []
    for model_id, meta in models["models"].items():
        rows.append([
            f"<a href='{esc(model_id)}.html'>{esc(meta['name'])}</a>",
            esc(meta["lab"]),
            esc(meta["family"]),
            esc(meta["role"]),
        ])
    rows.sort(key=lambda row: (row[1], row[0]))
    body = f"""
    <h1>Models</h1>
    <p>Open a model to see how each harness compiled it. The list grows when a harness file names a new model id.</p>
    {render_table(["Model", "Lab", "Family", "Role"], rows)}
    """
    return page("Models", body, 1)


def render_harness_index(harnesses: list[dict]) -> str:
    rows = [
        [f"<a href='{esc(item['id'])}.html'>{esc(item['title'])}</a>", esc(item["publisher"]), esc(item["summary"])]
        for item in harnesses
    ]
    body = f"""
    <h1>Harnesses</h1>
    <p>One page per publisher. Scores stay in the file for the harness that printed them.</p>
    {render_table(["Page", "Publisher", "What it is"], rows)}
    """
    return page("Harnesses", body, 1)


def main() -> None:
    models, releases, harnesses = load()
    validate(models, harnesses)
    (ROOT / "harnesses").mkdir(exist_ok=True)
    (ROOT / "models").mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(render_index(models, releases, harnesses), encoding="utf-8")
    (ROOT / "harnesses" / "index.html").write_text(render_harness_index(harnesses), encoding="utf-8")
    (ROOT / "models" / "index.html").write_text(render_model_index(models), encoding="utf-8")
    for harness in harnesses:
        (ROOT / "harnesses" / f"{harness['id']}.html").write_text(
            render_harness(models, harness), encoding="utf-8"
        )
    for model_id, meta in models["models"].items():
        (ROOT / "models" / f"{model_id}.html").write_text(
            render_model(models, model_id, meta, harnesses), encoding="utf-8"
        )
    print(f"Wrote {len(harnesses)} harness pages and {len(models['models'])} model pages.")


if __name__ == "__main__":
    main()
