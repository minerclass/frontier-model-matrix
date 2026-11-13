/* Frontier Model Matrix — Interactive Theme Toggle & Visual Observatory */
(function () {
  "use strict";

  const STORAGE_KEY = "fmm-theme";

  const LAB_VAR = {
    "Google": "var(--lab-google)",
    "Anthropic": "var(--lab-anthropic)",
    "OpenAI": "var(--lab-openai)",
    "Meta": "var(--lab-meta)",
    "xAI": "var(--lab-xai)",
    "Moonshot AI": "var(--lab-moonshot)",
    "DeepSeek": "var(--lab-deepseek)",
    "Z.AI": "var(--lab-zai)",
    "Cursor": "var(--lab-cursor)"
  };

  function labColor(lab) {
    return LAB_VAR[lab] || "var(--accent)";
  }

  function labBucket(lab) {
    if (["Google", "Anthropic", "OpenAI", "Meta", "xAI"].includes(lab)) return lab;
    return "Open";
  }

  function esc(str) {
    return String(str == null ? "" : str).replace(/[&<>"]/g, function (ch) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch];
    });
  }

  function fmtVal(val, unit) {
    if (unit === "elo") return Math.round(val).toLocaleString("en-US") + " Elo";
    if (unit === "index") return (Number.isInteger(val) ? String(val) : val.toFixed(1)) + " pts";
    if (unit === "usd") {
      return val >= 100 && Number.isInteger(val)
        ? "$" + val.toLocaleString("en-US")
        : "$" + val.toFixed(2);
    }
    return val.toFixed(1) + "%";
  }

  /* ---------------- Theme Toggle ---------------- */
  function currentTheme() {
    return document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
  }

  function syncThemeButton(btn, theme) {
    if (!btn) return;
    const isDark = theme === "dark";
    btn.setAttribute("aria-pressed", isDark ? "true" : "false");
    btn.setAttribute("aria-label", isDark ? "Dark mode" : "Light mode");
    btn.setAttribute("title", isDark ? "Switch to light mode" : "Switch to dark mode");
    const icon = isDark
      ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>'
      : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>';
    btn.innerHTML = icon + "<span>" + (isDark ? "Dark mode" : "Light mode") + "</span>";
  }

  function applyTheme(theme) {
    const next = theme === "light" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try {
      localStorage.setItem(STORAGE_KEY, next);
    } catch (e) {}
    syncThemeButton(document.getElementById("theme-toggle"), next);
    return next;
  }

  function toggleTheme() {
    return applyTheme(currentTheme() === "dark" ? "light" : "dark");
  }

  // Inline onclick on the header button calls this once per activation.
  window.__fmmToggleTheme = toggleTheme;

  function initTheme() {
    syncThemeButton(document.getElementById("theme-toggle"), currentTheme());
  }

  /* ---------------- Visual Atlas (index.html) ---------------- */
  const LINEAGE_LANES = [
    {
      lab: "Google",
      title: "Google DeepMind · Gemini 4 family",
      note: "Argon → Carbon → Hydrogen",
      chains: [
        [
          { id: "gemini-3-8-flash", date: "2 Sep", tag: "Prior Flash" },
          { id: "gemini-4-argon", date: "13 Oct", tag: "$4/$20 · Frontier" },
          { id: "gemini-4-carbon", date: "10 Nov GA", tag: "$4/$20 ($2/$10 promo) · Deep reasoning" },
          { id: "gemini-4-hydrogen", date: "12 Nov", tag: "$1.50/$7.50 · Fast agentic" }
        ]
      ]
    },
    {
      lab: "Anthropic",
      title: "Anthropic · Claude 5.5 & Fable / Mythos 5.2",
      note: "Daily-driver 5.5 tiers + high-compute Fable/Mythos",
      chains: [
        [
          { id: "claude-haiku-5-5", date: "7 Oct", tag: "$0.10/$0.50 · Subagent" },
          { id: "claude-sonnet-5-5", date: "28 Sep", tag: "$2/$10 · Everyday" },
          { id: "claude-opus-5-5", date: "22 Sep", tag: "$4/$20 · Daily driver" }
        ],
        [
          { id: "claude-fable-5-1", date: "1 Sep", tag: "$10/$50 · Prior Fable" },
          { id: "claude-fable-5-2", date: "9 Nov", tag: "$8/$40 · GA safeguarded" },
          { id: "claude-mythos-5-2", date: "9 Nov", tag: "Verified cyber & bio" }
        ]
      ]
    },
    {
      lab: "OpenAI",
      title: "OpenAI · GPT-6 slider & GPT-6.1 Work / Codex",
      note: "Chat slider (Sol/Astra) vs. API & Codex tiers",
      chains: [
        [
          { id: "gpt-6-luna", date: "22 Sep", tag: "Low-cost API/Codex" },
          { id: "gpt-6-sol", date: "22 Sep", tag: "Chat Instant–Xhigh" },
          { id: "gpt-6-astra", date: "Sep", tag: "Chat Pro · $10/$50" }
        ],
        [
          { id: "gpt-5-6-terra", date: "Prior", tag: "$2/$12 · Prior Terra" },
          { id: "gpt-6-1-sol", date: "29 Sep", tag: "Work & Codex" },
          { id: "gpt-6-1-terra", date: "26 Oct", tag: "$1/$5 · Fast CUA & coding" },
          { id: "gpt-6-cyber", date: "5 Nov", tag: "Vetted cyber" }
        ]
      ]
    },
    {
      lab: "Meta",
      title: "Meta · Muse Spark, Wonder & Ember",
      note: "Wonder Full distilled into low-cost Ember; Spark Open weights",
      chains: [
        [
          { id: "muse-spark-1-3", date: "Aug", tag: "$1.25/$4.25 · Coding" },
          { id: "muse-spark-open", date: "15 Oct", tag: "816B/42B Open weights" }
        ],
        [
          { id: "muse-wonder", date: "12 Oct", tag: "$4/$20 · API & Muse Code" },
          { id: "muse-wonder-full", date: "12 Oct", tag: "Muse Code Power/Max" },
          { id: "muse-ember", date: "9 Nov", tag: "$0.10/$0.50 · Distilled" }
        ]
      ]
    },
    {
      lab: "xAI",
      title: "xAI · Grok coding & reasoning line",
      note: "Served across efforts in Cursor; 4.8 in C/C++ RL",
      chains: [
        [
          { id: "grok-4-6", date: "12 Aug", tag: "$2/$6 · 500K ctx" },
          { id: "grok-4-7", date: "21 Sep", tag: "$2/$6 · Cursor efforts" },
          { id: null, label: "Grok 4.8 (in RL)", date: "10 Nov note", tag: "No published scores yet" }
        ]
      ]
    },
    {
      lab: "Open",
      title: "Open-Weight & Harness Frontier",
      note: "Moonshot AI, DeepSeek, Z.AI & Cursor",
      chains: [
        [
          { id: "deepseek-v4-1-flash-1017", date: "17 Oct", tag: "MIT · CursorBench & AA" },
          { id: "kimi-k3-1-pro", date: "23 Oct", tag: "2.8T/104B · $2/$10" },
          { id: "glm-5-3", date: "Sep", tag: "Z.AI agent tier" },
          { id: "composer-2-5", date: "Sep", tag: "Cursor native agent" }
        ]
      ]
    }
  ];

  const DOTPLOT_VIEWS = [
    {
      key: "tb4",
      label: "Terminal-Bench 4.0 (Claims vs. AA vs. Vals mini-swe-agent)",
      benchIds: ["terminal-bench-4.0", "terminal-bench-4.0-aa", "terminal-bench-4-0-vals"],
      unit: "percent",
      min: 0,
      max: 75,
      note: "Side-by-side comparison across three distinct Terminal-Bench 4.0 setups: lab-reported agent harnesses (circle/diamond), Artificial Analysis (square), and Vals AI's standardized mini-swe-agent (triangle). Never averaged."
    },
    {
      key: "cb4",
      label: "CursorBench 4.0 (Shared Coding Harness — Effort Spread)",
      benchIds: ["cursorbench-4.0"],
      unit: "percent",
      min: 10,
      max: 65,
      note: "Ambiguous multi-file coding tasks in Cursor across reasoning effort levels (12 Nov 2026 90-row board plus three preserved 13 Oct rows)."
    },
    {
      key: "aav5",
      label: "AA Intelligence Index v5.0 (Composite Index)",
      benchIds: ["aa-intelligence-index-v5-0"],
      unit: "index",
      min: 20,
      max: 70,
      note: "Artificial Analysis's 9-benchmark private/held-out v5.0 index (launched 27 Oct 2026; live 12 Nov 2026 leaderboard plus lab citations)."
    },
    {
      key: "vals",
      label: "Vals Index v2.2 (GDP-Weighted Finance, Coding, Legal & Tax)",
      benchIds: ["vals-index-v2-2"],
      unit: "percent",
      min: 45,
      max: 75,
      note: "Vals AI's GDP-weighted aggregate across Finance (8.0), Coding (5.6), Legal (1.2), and Tax (0.5)."
    },
    {
      key: "osw21",
      label: "OSWorld 2.1 Computer Use (Offline & Partial)",
      benchIds: ["osworld-2-1-offline", "osworld-2-1-partial"],
      unit: "percent",
      min: 45,
      max: 92,
      note: "Desktop computer-use partial credit across offline 82-task and full 108-task OSWorld 2.1 setups."
    },
    {
      key: "auto",
      label: "AutomationBench (Zapier Board vs. AA Strict)",
      benchIds: ["automationbench", "automationbench-aa"],
      unit: "percent",
      min: 10,
      max: 80,
      note: "Zapier's public leaderboard alongside Artificial Analysis's AutomationBench-AA runs. Kept as distinct benchmark IDs."
    },
    {
      key: "tbsci",
      label: "Terminal-Bench Science 0.1 (Lab Claims vs. AA)",
      benchIds: ["terminal-bench-science-0.1", "terminal-bench-science-0-1-aa"],
      unit: "percent",
      min: 5,
      max: 80,
      note: "70 agentic scientific research workflows in a terminal environment."
    },
    {
      key: "deepswe",
      label: "DeepSWE v1.1 (Repository Software Engineering)",
      benchIds: ["deepswe-v1.1"],
      unit: "percent",
      min: 55,
      max: 82,
      note: "Long-horizon software engineering tasks in real repositories. GPT-6.1 Sol (75.2%) is derived from OpenAI's +6.4 pt claim over GPT-6 Sol."
    },
    {
      key: "fswe2",
      label: "FrontierSWE v2 (Agentic Software Engineering)",
      benchIds: ["frontierswe-v2"],
      unit: "percent",
      min: 50,
      max: 74,
      note: "Proximal FrontierSWE v2 across Anthropic's Fable 5.2 table and Google's Argon/Carbon cards."
    },
    {
      key: "mka",
      label: "MKA Climb WSR (Multimodal Knowledge Agent)",
      benchIds: ["mka-climb-wsr"],
      unit: "percent",
      min: 40,
      max: 62,
      note: "200 private real-world visual tasks across 10 industries (launched 10 Nov 2026 by Google DeepMind and Artificial Analysis)."
    },
    {
      key: "hle",
      label: "HLE-Diamond & Humanity's Last Exam (with tools)",
      benchIds: ["hle-diamond", "hle-with-tools"],
      unit: "percent",
      min: 15,
      max: 78,
      note: "Closed-book 1,000-question HLE-Diamond alongside tool-augmented Humanity's Last Exam."
    },
    {
      key: "briefcase",
      label: "AA-Briefcase v1.1 (Long-Horizon Knowledge Work Elo)",
      benchIds: ["aa-briefcase-v1-1"],
      unit: "elo",
      min: 1300,
      max: 1860,
      note: "Artificial Analysis Elo ratings for professional knowledge work."
    }
  ];

  const PARETO_VIEWS = [
    {
      key: "cb4",
      label: "CursorBench 4.0 (93 model-effort runs)",
      filter: function (f) { return f.hId === "cursorbench" && f.bId === "cursorbench-4.0" && f.cost > 0; },
      yLabel: "CursorBench 4.0 (%)",
      unit: "percent"
    },
    {
      key: "aav5",
      label: "AA Intelligence Index v5.0 (Leaderboard runs)",
      filter: function (f) { return f.hId === "artificial-analysis" && f.bId === "aa-intelligence-index-v5-0" && f.cost > 0 && !String(f.set).includes("launch"); },
      yLabel: "AA Intelligence Index v5.0 (pts)",
      unit: "index"
    },
    {
      key: "vals",
      label: "Vals Index v2.2 (21 priced models)",
      filter: function (f) { return f.hId === "vals-ai" && f.bId === "vals-index-v2-2" && f.cost > 0; },
      yLabel: "Vals Index v2.2 (%)",
      unit: "percent"
    },
    {
      key: "valstb4",
      label: "Vals Terminal-Bench 4.0 (mini-swe-agent)",
      filter: function (f) { return f.hId === "vals-ai" && f.bId === "terminal-bench-4-0-vals" && f.cost > 0; },
      yLabel: "Terminal-Bench 4.0 · Vals (%)",
      unit: "percent"
    },
    {
      key: "oaitb4",
      label: "OpenAI Terra Curves: Terminal-Bench 4.0",
      filter: function (f) { return f.hId === "openai-gpt-6" && f.bId === "terminal-bench-4.0" && f.cost > 0; },
      yLabel: "Terminal-Bench 4.0 · OpenAI chart (%)",
      unit: "percent"
    },
    {
      key: "oaiosw",
      label: "OpenAI Terra Curves: OSWorld 2.1 Offline",
      filter: function (f) { return f.hId === "openai-gpt-6" && f.bId === "osworld-2-1-offline" && f.cost > 0; },
      yLabel: "OSWorld 2.1 Offline · OpenAI chart (%)",
      unit: "percent"
    }
  ];

  const EFFORT_ORDER = {
    "Minimal": 0,
    "Low": 1,
    "Default": 2,
    "Medium": 3,
    "High": 4,
    "Extra High": 5,
    "Xhigh": 5,
    "Best reported": 6,
    "Max": 7
  };

  function initVisualAtlas() {
    const dataEl = document.getElementById("fmm-atlas-data");
    if (!dataEl) return;
    let payload;
    try {
      payload = JSON.parse(dataEl.textContent);
    } catch (err) {
      return;
    }

    const models = payload.models || {};
    const figures = payload.figures || [];

    const state = {
      lab: "all",
      spotlight: "",
      inspector: "gemini-4-hydrogen",
      dotView: "tb4",
      paretoView: "cb4",
      showTrajectories: true,
      showFrontier: true
    };

    const labChips = document.getElementById("lab-filter-chips");
    const spotlightSel = document.getElementById("model-spotlight");
    const clearSpotlightBtn = document.getElementById("clear-spotlight");
    const dotSelect = document.getElementById("dotplot-select");
    const paretoSelect = document.getElementById("pareto-select");
    const trajCheck = document.getElementById("chk-trajectories");
    const frontCheck = document.getElementById("chk-frontier");

    function modelMatchesLab(modelId) {
      if (state.lab === "all") return true;
      const m = models[modelId];
      if (!m) return false;
      return labBucket(m.lab) === state.lab;
    }

    /* Populate controls */
    const LAB_FILTERS = [
      { id: "all", label: "All labs", dot: null },
      { id: "Google", label: "Google", dot: "var(--lab-google)" },
      { id: "Anthropic", label: "Anthropic", dot: "var(--lab-anthropic)" },
      { id: "OpenAI", label: "OpenAI", dot: "var(--lab-openai)" },
      { id: "Meta", label: "Meta", dot: "var(--lab-meta)" },
      { id: "xAI", label: "xAI", dot: "var(--lab-xai)" },
      { id: "Open", label: "Open-weight & Harness", dot: "var(--lab-moonshot)" }
    ];

    function renderLabChips() {
      if (!labChips) return;
      labChips.innerHTML = LAB_FILTERS.map(function (item) {
        const dot = item.dot ? '<i class="lab-dot" style="background:' + item.dot + '"></i>' : "";
        return '<button type="button" class="chip" data-lab="' + esc(item.id) + '" aria-pressed="' + (state.lab === item.id) + '">' + dot + esc(item.label) + "</button>";
      }).join("");
      labChips.querySelectorAll("button").forEach(function (btn) {
        btn.addEventListener("click", function () {
          state.lab = btn.getAttribute("data-lab");
          renderAll();
        });
      });
    }

    if (spotlightSel) {
      const sortedIds = Object.keys(models).sort(function (a, b) {
        return models[a].lab.localeCompare(models[b].lab) || models[a].name.localeCompare(models[b].name);
      });
      spotlightSel.innerHTML = '<option value="">Highlight a model across charts…</option>' +
        sortedIds.map(function (id) {
          return '<option value="' + esc(id) + '">' + esc(models[id].name + " (" + models[id].lab + ")") + "</option>";
        }).join("");
      spotlightSel.addEventListener("change", function () {
        state.spotlight = spotlightSel.value;
        if (state.spotlight) state.inspector = state.spotlight;
        renderAll();
      });
    }

    if (clearSpotlightBtn) {
      clearSpotlightBtn.addEventListener("click", function () {
        state.spotlight = "";
        state.lab = "all";
        if (spotlightSel) spotlightSel.value = "";
        renderAll();
      });
    }

    if (dotSelect) {
      dotSelect.innerHTML = DOTPLOT_VIEWS.map(function (v) {
        return '<option value="' + esc(v.key) + '">' + esc(v.label) + "</option>";
      }).join("");
      dotSelect.value = state.dotView;
      dotSelect.addEventListener("change", function () {
        state.dotView = dotSelect.value;
        renderDotPlot();
      });
    }

    if (paretoSelect) {
      paretoSelect.innerHTML = PARETO_VIEWS.map(function (v) {
        return '<option value="' + esc(v.key) + '">' + esc(v.label) + "</option>";
      }).join("");
      paretoSelect.value = state.paretoView;
      paretoSelect.addEventListener("change", function () {
        state.paretoView = paretoSelect.value;
        renderPareto();
      });
    }

    if (trajCheck) {
      trajCheck.addEventListener("change", function () {
        state.showTrajectories = trajCheck.checked;
        renderPareto();
      });
    }
    if (frontCheck) {
      frontCheck.addEventListener("change", function () {
        state.showFrontier = frontCheck.checked;
        renderPareto();
      });
    }

    /* Station 1: Schematic & Inspector */
    function renderSchematic() {
      const box = document.getElementById("schematic-lanes");
      if (!box) return;
      box.innerHTML = LINEAGE_LANES.map(function (lane) {
        const laneVisible = state.lab === "all" || state.lab === lane.lab;
        const lColor = lane.lab === "Open" ? "var(--lab-moonshot)" : labColor(lane.lab);
        const rowsHtml = lane.chains.map(function (chain) {
          const items = chain.map(function (node, idx) {
            const arrow = idx > 0 ? '<span class="flow-arrow" aria-hidden="true">→</span>' : "";
            if (!node.id) {
              return arrow + '<div class="node-btn unscored' + (laneVisible ? "" : " dimmed") + '">' +
                '<div class="node-top"><span class="node-name">' + esc(node.label) + '</span><span class="node-date">' + esc(node.date) + "</span></div>" +
                '<span class="node-meta">' + esc(node.tag) + "</span></div>";
            }
            const m = models[node.id] || { name: node.id };
            const active = state.inspector === node.id || state.spotlight === node.id;
            const dim = !laneVisible || (state.spotlight && state.spotlight !== node.id);
            return arrow + '<button type="button" class="node-btn' + (dim ? " dimmed" : "") + '" data-mid="' + esc(node.id) + '" aria-pressed="' + active + '">' +
              '<div class="node-top"><span class="node-name">' + esc(m.name) + '</span><span class="node-date">' + esc(node.date) + "</span></div>" +
              '<span class="node-meta">' + esc(node.tag) + "</span></button>";
          }).join("");
          return '<div class="lane-flow">' + items + "</div>";
        }).join("");
        return '<div class="lane" style="--lane-color:' + lColor + '">' +
          '<div class="lane-head"><span class="lane-title">' + esc(lane.title) + '</span><span class="lane-note">' + esc(lane.note) + "</span></div>" +
          rowsHtml + "</div>";
      }).join("");

      box.querySelectorAll("button[data-mid]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          const mid = btn.getAttribute("data-mid");
          state.inspector = mid;
          state.spotlight = state.spotlight === mid ? "" : mid;
          if (spotlightSel) spotlightSel.value = state.spotlight;
          renderAll();
        });
      });
    }

    function renderInspector() {
      const panel = document.getElementById("model-inspector");
      if (!panel) return;
      const mid = state.inspector || "gemini-4-hydrogen";
      const m = models[mid];
      if (!m) return;
      const mFigs = figures.filter(function (f) { return f.m === mid; });
      const claims = mFigs.filter(function (f) { return f.st === "claim"; }).length;
      const rivals = mFigs.filter(function (f) { return f.st === "rival"; }).length;
      const indeps = mFigs.filter(function (f) { return f.st === "independent"; }).length;

      const KEY_BENCHES = [
        { ids: ["cursorbench-4.0"], label: "CursorBench 4.0", max: 100 },
        { ids: ["aa-intelligence-index-v5-0"], label: "AA Index v5.0", max: 100 },
        { ids: ["vals-index-v2-2"], label: "Vals Index v2.2", max: 100 },
        { ids: ["terminal-bench-4.0", "terminal-bench-4.0-aa", "terminal-bench-4-0-vals"], label: "Terminal-Bench 4.0", max: 100 },
        { ids: ["terminal-bench-4-1"], label: "Terminal-Bench 4.1", max: 100 },
        { ids: ["osworld-2-1-offline", "osworld-2-1-partial"], label: "OSWorld 2.1", max: 100 },
        { ids: ["deepswe-v1.1"], label: "DeepSWE v1.1", max: 100 },
        { ids: ["frontierswe-v2"], label: "FrontierSWE v2", max: 100 },
        { ids: ["mka-climb-wsr"], label: "MKA Climb WSR", max: 100 },
        { ids: ["swe-sweep"], label: "SWE-sweep", max: 25 }
      ];

      const bars = [];
      KEY_BENCHES.forEach(function (kb) {
        const hits = mFigs.filter(function (f) { return kb.ids.includes(f.bId); });
        if (!hits.length || bars.length >= 7) return;
        const best = hits.reduce(function (a, b) { return b.v > a.v ? b : a; });
        const pct = Math.min(100, Math.max(4, (best.v / kb.max) * 100));
        const stColor = best.st === "claim" ? "var(--stance-claim)" : best.st === "independent" ? "var(--stance-indep)" : "var(--stance-rival)";
        bars.push(
          '<div class="mini-row">' +
            '<div class="mini-top"><span>' + esc(kb.label) + ' <small class="meta">(' + esc(best.pub) + ')</small></span><b>' + esc(fmtVal(best.v, best.u)) + "</b></div>" +
            '<div class="mini-track"><div class="mini-fill" style="width:' + pct.toFixed(1) + "%;background:" + stColor + '"></div></div>' +
          "</div>"
        );
      });

      panel.innerHTML =
        '<div class="node-top">' +
          '<span class="eyebrow" style="color:' + labColor(m.lab) + '">' + esc(m.lab + " · " + m.family) + "</span>" +
          '<span class="badge">' + mFigs.length + " figures</span>" +
        "</div>" +
        "<h3>" + esc(m.name) + "</h3>" +
        '<p class="sub" style="font-size:0.86rem">' + esc(m.role) + "</p>" +
        '<div style="display:flex;flex-wrap:wrap;gap:6px">' +
          '<span class="badge badge-claim">' + claims + " own claims</span>" +
          '<span class="badge badge-independent">' + indeps + " independent</span>" +
          '<span class="badge badge-rival">' + rivals + " rival tables</span>" +
        "</div>" +
        '<div class="inspector-bars">' + (bars.length ? bars.join("") : '<p class="meta">Open model page for non-percent metrics.</p>') + "</div>" +
        '<div style="display:flex;justify-content:space-between;align-items:center;padding-top:4px">' +
          '<a href="models/' + esc(mid) + '.html" style="font-family:var(--f-display);font-weight:700;font-size:0.88rem">Open full ' + esc(m.name) + " record →</a>" +
        "</div>";
    }

    /* Station 2: Claims vs Independent Dot-Plot */
    function renderDotPlot() {
      const svg = document.getElementById("dotplot-svg");
      const noteEl = document.getElementById("dotplot-note");
      const readout = document.getElementById("dotplot-readout");
      if (!svg) return;

      const view = DOTPLOT_VIEWS.find(function (v) { return v.key === state.dotView; }) || DOTPLOT_VIEWS[0];
      if (noteEl) noteEl.textContent = view.note;

      const rowsMap = new Map();
      figures.forEach(function (f) {
        if (!view.benchIds.includes(f.bId)) return;
        if (!modelMatchesLab(f.m)) return;
        if (!rowsMap.has(f.m)) rowsMap.set(f.m, []);
        rowsMap.get(f.m).push(f);
      });

      const modelRows = Array.from(rowsMap.entries()).map(function (entry) {
        const mid = entry[0];
        const pts = entry[1];
        const maxV = Math.max.apply(null, pts.map(function (p) { return p.v; }));
        const minV = Math.min.apply(null, pts.map(function (p) { return p.v; }));
        return { mid: mid, model: models[mid] || { name: mid, lab: "" }, pts: pts, maxV: maxV, minV: minV };
      }).sort(function (a, b) { return b.maxV - a.maxV; });

      if (!modelRows.length) {
        svg.setAttribute("viewBox", "0 0 860 90");
        svg.innerHTML = '<text x="24" y="48" fill="var(--muted)" font-family="var(--f-mono)" font-size="13">No recorded scores match this lab filter on the selected benchmark.</text>';
        return;
      }

      const W = 900;
      const leftPad = 212;
      const rightPad = 78;
      const topPad = 34;
      const rowH = 30;
      const H = topPad + modelRows.length * rowH + 26;
      const plotW = W - leftPad - rightPad;

      function xPos(val) {
        const clamped = Math.max(view.min, Math.min(view.max, val));
        return leftPad + ((clamped - view.min) / (view.max - view.min)) * plotW;
      }

      const ticks = 6;
      let gridHtml = "";
      for (let i = 0; i <= ticks; i++) {
        const tv = view.min + ((view.max - view.min) * i) / ticks;
        const tx = xPos(tv);
        const label = view.unit === "elo" ? Math.round(tv) : view.unit === "index" ? Math.round(tv) : Math.round(tv) + "%";
        gridHtml +=
          '<line x1="' + tx.toFixed(1) + '" y1="' + (topPad - 8) + '" x2="' + tx.toFixed(1) + '" y2="' + (H - 18) + '" stroke="var(--rule)" stroke-dasharray="2,3"/>' +
          '<text x="' + tx.toFixed(1) + '" y="20" text-anchor="middle" fill="var(--muted)" font-family="var(--f-mono)" font-size="11">' + esc(label) + "</text>";
      }

      const markerDefs = [];
      let rowsSvg = "";
      modelRows.forEach(function (row, idx) {
        const cy = topPad + idx * rowH + 12;
        const isSpot = state.spotlight === row.mid;
        const dim = state.spotlight && !isSpot;
        const rowOpacity = dim ? "0.32" : "1";
        const bgRect = isSpot
          ? '<rect x="4" y="' + (cy - 13) + '" width="' + (W - 8) + '" height="' + (rowH - 2) + '" rx="4" fill="var(--accent-soft)"/>'
          : idx % 2 === 1
            ? '<rect x="4" y="' + (cy - 13) + '" width="' + (W - 8) + '" height="' + (rowH - 2) + '" rx="3" fill="var(--sheet)" opacity="0.45"/>'
            : "";

        const x1 = xPos(row.minV);
        const x2 = xPos(row.maxV);
        const multiSetup = new Set(row.pts.map(function (p) { return p.bId + "|" + p.st; })).size > 1;
        const spanLine = row.pts.length > 1
          ? '<line x1="' + x1.toFixed(1) + '" y1="' + cy + '" x2="' + x2.toFixed(1) + '" y2="' + cy + '" stroke="var(--rule-strong)" stroke-width="2"' + (multiSetup ? ' stroke-dasharray="3,2"' : "") + "/>"
          : "";

        /* Draw markers ordered so claims & independent sit on top of rival quotes */
        const orderRank = { rival: 0, independent: 1, claim: 2 };
        const sortedPts = row.pts.slice().sort(function (a, b) { return (orderRank[a.st] || 0) - (orderRank[b.st] || 0); });
        const ptsSvg = sortedPts.map(function (pt) {
          const px = xPos(pt.v);
          const mIdx = markerDefs.length;
          markerDefs.push({ pt: pt, modelName: row.model.name });
          let shape = "";
          const labelDesc = row.model.name + ": " + fmtVal(pt.v, pt.u) + (pt.set ? " (" + pt.set + ")" : "") + " · " + pt.pub + " [" + pt.st + "]";
          if (pt.st === "claim") {
            shape = '<circle cx="' + px.toFixed(1) + '" cy="' + cy + '" r="5.5" fill="var(--stance-claim)" stroke="var(--sheet)" stroke-width="1.4"/>';
          } else if (pt.st === "rival") {
            shape = '<polygon points="' + px.toFixed(1) + "," + (cy - 6) + " " + (px + 6).toFixed(1) + "," + cy + " " + px.toFixed(1) + "," + (cy + 6) + " " + (px - 6).toFixed(1) + "," + cy + '" fill="var(--stance-rival)" stroke="var(--sheet)" stroke-width="1.2"/>';
          } else if (pt.pub === "Vals AI") {
            shape = '<polygon points="' + px.toFixed(1) + "," + (cy - 6) + " " + (px + 5.8).toFixed(1) + "," + (cy + 5) + " " + (px - 5.8).toFixed(1) + "," + (cy + 5) + '" fill="var(--stance-indep)" stroke="var(--sheet)" stroke-width="1.2"/>';
          } else {
            shape = '<rect x="' + (px - 5).toFixed(1) + '" y="' + (cy - 5) + '" width="10" height="10" rx="2" fill="var(--stance-indep)" stroke="var(--sheet)" stroke-width="1.2"/>';
          }
          return '<g class="pt-mark" tabindex="0" role="button" data-idx="' + mIdx + '" aria-label="' + esc(labelDesc) + '" style="cursor:pointer">' + shape + "</g>";
        }).join("");

        rowsSvg +=
          '<g opacity="' + rowOpacity + '">' +
            bgRect +
            '<circle cx="14" cy="' + (cy - 1) + '" r="4" fill="' + labColor(row.model.lab) + '"/>' +
            '<text x="25" y="' + (cy + 4) + '" fill="var(--ink)" font-family="var(--f-display)" font-weight="' + (isSpot ? "750" : "600") + '" font-size="12.5">' + esc(row.model.name) + "</text>" +
            spanLine +
            ptsSvg +
            '<text x="' + (W - 10) + '" y="' + (cy + 4) + '" text-anchor="end" fill="var(--ink-2)" font-family="var(--f-mono)" font-size="11.5">' + esc(fmtVal(row.maxV, view.unit)) + "</text>" +
          "</g>";
      });

      svg.setAttribute("viewBox", "0 0 " + W + " " + H);
      svg.innerHTML = gridHtml + rowsSvg;

      function showReadout(idx) {
        const item = markerDefs[idx];
        if (!item || !readout) return;
        const p = item.pt;
        const costTxt = p.cost != null ? " · $" + p.cost.toFixed(2) + "/task" : "";
        const setTxt = p.set ? " · effort: " + p.set : "";
        const noteTxt = p.note ? " — " + p.note : "";
        readout.innerHTML =
          "<div><strong>" + esc(item.modelName) + "</strong> · <code>" + esc(fmtVal(p.v, p.u)) + "</code>" +
          esc(setTxt + costTxt) + " · published by <strong>" + esc(p.pub) + "</strong> (" + esc(p.st) + ", " + esc(p.orig) + ")" + esc(noteTxt) + "</div>" +
          '<a href="' + esc(p.url) + '" target="_blank" rel="noopener">Source (' + esc(p.date) + ") ↗</a>";
      }

      if (markerDefs.length && readout) {
        const preferredIdx = markerDefs.findIndex(function (m) { return m.pt.st === "claim"; });
        showReadout(preferredIdx >= 0 ? preferredIdx : 0);
      }

      svg.querySelectorAll(".pt-mark").forEach(function (el) {
        const idx = Number(el.getAttribute("data-idx"));
        el.addEventListener("mouseenter", function () { showReadout(idx); });
        el.addEventListener("focus", function () { showReadout(idx); });
        el.addEventListener("click", function () {
          const item = markerDefs[idx];
          if (item) {
            state.inspector = item.pt.m;
            renderInspector();
          }
          showReadout(idx);
        });
      });
    }

    /* Station 3: Cost vs Score Pareto Scatterplot */
    function renderPareto() {
      const svg = document.getElementById("pareto-svg");
      const readout = document.getElementById("pareto-readout");
      if (!svg) return;

      const view = PARETO_VIEWS.find(function (v) { return v.key === state.paretoView; }) || PARETO_VIEWS[0];
      const pts = figures.filter(function (f) {
        return view.filter(f) && modelMatchesLab(f.m);
      });

      if (!pts.length) {
        svg.setAttribute("viewBox", "0 0 880 120");
        svg.innerHTML = '<text x="24" y="60" fill="var(--muted)" font-family="var(--f-mono)" font-size="13">No priced task runs match this filter.</text>';
        return;
      }

      const W = 900;
      const H = 430;
      const padL = 64;
      const padR = 36;
      const padT = 26;
      const padB = 48;
      const plotW = W - padL - padR;
      const plotH = H - padT - padB;

      const minCost = Math.min.apply(null, pts.map(function (p) { return p.cost; }));
      const maxCost = Math.max.apply(null, pts.map(function (p) { return p.cost; }));
      const logMin = Math.floor(Math.log10(minCost * 0.82) * 2) / 2;
      const logMax = Math.ceil(Math.log10(maxCost * 1.22) * 2) / 2;

      const minV = Math.floor(Math.min.apply(null, pts.map(function (p) { return p.v; })) / 5) * 5 - 2;
      const maxV = Math.ceil(Math.max.apply(null, pts.map(function (p) { return p.v; })) / 5) * 5 + 3;

      function xPos(c) {
        return padL + ((Math.log10(c) - logMin) / (logMax - logMin)) * plotW;
      }
      function yPos(v) {
        return padT + plotH - ((v - minV) / (maxV - minV)) * plotH;
      }

      /* Axes & Grid */
      const tickCosts = [0.02, 0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 40].filter(function (c) {
        const lc = Math.log10(c);
        return lc >= logMin && lc <= logMax;
      });

      let grid = "";
      tickCosts.forEach(function (tc) {
        const tx = xPos(tc);
        const lbl = tc < 1 ? "$" + tc.toFixed(2) : "$" + tc;
        grid +=
          '<line x1="' + tx.toFixed(1) + '" y1="' + padT + '" x2="' + tx.toFixed(1) + '" y2="' + (padT + plotH) + '" stroke="var(--rule)" stroke-dasharray="2,3"/>' +
          '<text x="' + tx.toFixed(1) + '" y="' + (H - 22) + '" text-anchor="middle" fill="var(--muted)" font-family="var(--f-mono)" font-size="11">' + lbl + "</text>";
      });
      grid += '<text x="' + (padL + plotW / 2).toFixed(1) + '" y="' + (H - 4) + '" text-anchor="middle" fill="var(--ink-2)" font-family="var(--f-mono)" font-size="11.5">Estimated Cost per Task (USD, log scale · left is cheaper)</text>';

      const ySteps = 5;
      for (let i = 0; i <= ySteps; i++) {
        const yv = minV + ((maxV - minV) * i) / ySteps;
        const yy = yPos(yv);
        grid +=
          '<line x1="' + padL + '" y1="' + yy.toFixed(1) + '" x2="' + (padL + plotW) + '" y2="' + yy.toFixed(1) + '" stroke="var(--rule)" stroke-dasharray="2,3"/>' +
          '<text x="' + (padL - 8) + '" y="' + (yy + 4).toFixed(1) + '" text-anchor="end" fill="var(--muted)" font-family="var(--f-mono)" font-size="11">' + Math.round(yv) + "</text>";
      }
      grid += '<text transform="translate(16,' + (padT + plotH / 2).toFixed(1) + ') rotate(-90)" text-anchor="middle" fill="var(--ink-2)" font-family="var(--f-mono)" font-size="11.5">' + esc(view.yLabel) + "</text>";

      /* Compute Pareto Frontier */
      const byCost = pts.slice().sort(function (a, b) { return a.cost - b.cost || b.v - a.v; });
      const frontier = [];
      let bestSoFar = -Infinity;
      byCost.forEach(function (p) {
        if (p.v > bestSoFar + 0.01) {
          frontier.push(p);
          bestSoFar = p.v;
        }
      });
      const frontierSet = new Set(frontier);

      let frontierSvg = "";
      if (state.showFrontier && frontier.length > 1) {
        const polyPts = frontier.map(function (p) { return xPos(p.cost).toFixed(1) + "," + yPos(p.v).toFixed(1); }).join(" ");
        frontierSvg = '<polyline points="' + polyPts + '" fill="none" stroke="var(--pareto)" stroke-width="2.2" stroke-dasharray="5,4" opacity="0.9"/>';
      }

      /* Effort Trajectories per model */
      let trajSvg = "";
      if (state.showTrajectories) {
        const byModel = new Map();
        pts.forEach(function (p) {
          if (!byModel.has(p.m)) byModel.set(p.m, []);
          byModel.get(p.m).push(p);
        });
        byModel.forEach(function (arr, mid) {
          if (arr.length < 2) return;
          const sorted = arr.slice().sort(function (a, b) {
            const ea = EFFORT_ORDER[a.set] != null ? EFFORT_ORDER[a.set] : a.cost;
            const eb = EFFORT_ORDER[b.set] != null ? EFFORT_ORDER[b.set] : b.cost;
            return ea - eb || a.cost - b.cost;
          });
          const m = models[mid] || { lab: "" };
          const dim = state.spotlight && state.spotlight !== mid;
          const d = sorted.map(function (p) { return xPos(p.cost).toFixed(1) + "," + yPos(p.v).toFixed(1); }).join(" ");
          trajSvg += '<polyline points="' + d + '" fill="none" stroke="' + labColor(m.lab) + '" stroke-width="' + (state.spotlight === mid ? "2.6" : "1.5") + '" opacity="' + (dim ? "0.18" : "0.55") + '"/>';
        });
      }

      /* Points & collision-aware labels */
      const placedBoxes = [];
      let pointsSvg = "";
      let labelsSvg = "";
      pts.forEach(function (p, idx) {
        const m = models[p.m] || { name: p.m, lab: "" };
        const px = xPos(p.cost);
        const py = yPos(p.v);
        const isFront = frontierSet.has(p);
        const isSpot = state.spotlight === p.m;
        const dim = state.spotlight && !isSpot;
        const r = isSpot ? 6.8 : isFront ? 5.8 : 4.6;
        const ring = isFront && state.showFrontier
          ? '<circle cx="' + px.toFixed(1) + '" cy="' + py.toFixed(1) + '" r="' + (r + 3).toFixed(1) + '" fill="none" stroke="var(--pareto)" stroke-width="1.3" opacity="' + (dim ? "0.25" : "0.85") + '"/>'
          : "";
        const aria = m.name + (p.set ? " (" + p.set + ")" : "") + ": " + fmtVal(p.v, view.unit) + " at $" + p.cost.toFixed(2) + " per task";
        pointsSvg +=
          '<g class="pareto-pt" tabindex="0" role="button" data-idx="' + idx + '" aria-label="' + esc(aria) + '" style="cursor:pointer" opacity="' + (dim ? "0.24" : "1") + '">' +
            ring +
            '<circle cx="' + px.toFixed(1) + '" cy="' + py.toFixed(1) + '" r="' + r.toFixed(1) + '" fill="' + labColor(m.lab) + '" stroke="var(--sheet)" stroke-width="1.3"/>' +
          "</g>";

        if (isSpot || isFront) {
          const shortSet = p.set && p.set !== "Best reported" ? " · " + p.set.replace("Extra High", "Xhigh") : "";
          const txt = m.name.replace("Claude ", "").replace("Muse ", "Muse ") + shortSet;
          const approxW = txt.length * 6.2;
          let lx = px + 8;
          let anchor = "start";
          if (lx + approxW > W - padR) {
            lx = px - 8;
            anchor = "end";
          }
          const ly = py - 7;
          const xLeft = anchor === "start" ? lx : lx - approxW;
          const overlaps = placedBoxes.some(function (b) {
            return Math.abs(b.y - ly) < 13 && xLeft < b.x2 && xLeft + approxW > b.x1;
          });
          if (!overlaps || isSpot) {
            placedBoxes.push({ x1: xLeft, x2: xLeft + approxW, y: ly });
            labelsSvg += '<text x="' + lx.toFixed(1) + '" y="' + ly.toFixed(1) + '" text-anchor="' + anchor + '" fill="var(--ink)" font-family="var(--f-display)" font-weight="650" font-size="11" opacity="' + (dim ? "0.3" : "0.95") + '">' + esc(txt) + "</text>";
          }
        }
      });

      svg.setAttribute("viewBox", "0 0 " + W + " " + H);
      svg.innerHTML = grid + frontierSvg + trajSvg + pointsSvg + labelsSvg;

      function showParetoReadout(idx) {
        const p = pts[idx];
        if (!p || !readout) return;
        const m = models[p.m] || { name: p.m };
        const frontBadge = frontierSet.has(p) ? ' <span class="badge badge-independent">Pareto optimal</span>' : "";
        readout.innerHTML =
          "<div><strong>" + esc(m.name) + "</strong>" + (p.set ? " (" + esc(p.set) + ")" : "") +
          " · Score: <code>" + esc(fmtVal(p.v, view.unit)) + "</code> · Cost/task: <code>$" + p.cost.toFixed(2) + "</code> · " +
          esc(p.pub) + frontBadge + "</div>" +
          '<a href="' + esc(p.url) + '" target="_blank" rel="noopener">Source (' + esc(p.date) + ") ↗</a>";
      }

      if (pts.length && readout) {
        const topIdx = pts.indexOf(frontier[frontier.length - 1]);
        showParetoReadout(topIdx >= 0 ? topIdx : 0);
      }

      svg.querySelectorAll(".pareto-pt").forEach(function (el) {
        const idx = Number(el.getAttribute("data-idx"));
        el.addEventListener("mouseenter", function () { showParetoReadout(idx); });
        el.addEventListener("focus", function () { showParetoReadout(idx); });
        el.addEventListener("click", function () {
          const p = pts[idx];
          if (p) {
            state.inspector = p.m;
            renderInspector();
          }
          showParetoReadout(idx);
        });
      });
    }

    /* Highlight rows in static comparison tables when spotlight changes */
    function syncTableSpotlight() {
      document.querySelectorAll("tr[data-model-row]").forEach(function (tr) {
        const mid = tr.getAttribute("data-model-row");
        tr.classList.toggle("spotlit", Boolean(state.spotlight && state.spotlight === mid));
        tr.style.display = modelMatchesLab(mid) ? "" : "none";
      });
    }

    function renderAll() {
      renderLabChips();
      renderSchematic();
      renderInspector();
      renderDotPlot();
      renderPareto();
      syncTableSpotlight();
    }

    renderAll();
  }

  document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initVisualAtlas();
  });
})();
