"""
generate_figures.py
-------------------
Generates all 4 publication-quality figures for:
"Impact of Prompt Engineering on LLM-based Test Case Generation"

Place this in D:\\Research\\SQA\\scripts\\ and run:
    python scripts/generate_figures.py

Output: D:\\Research\\SQA\\figures\\ (created automatically)
        figure1_grouped_bar.png
        figure2_heatmap.png
        figure3_radar.png
        figure4_interaction.png

Requirements:
    pip install matplotlib numpy seaborn
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
import seaborn as sns
from pathlib import Path

# ── PATHS ─────────────────────────────────────────────────────────────────────
BASE_DIR    = Path(r"D:\Research\SQA\results\Final_Test")
RESULTS_FILE = BASE_DIR / "results.json"
OUTPUT_DIR   = BASE_DIR / "figures"
OUTPUT_DIR.mkdir(exist_ok=True)

# ── COLOUR PALETTE (matches professional Excel style) ─────────────────────────
C_ZERO   = "#2E75B6"   # Blue      — Zero-Shot
C_FEW    = "#ED7D31"   # Orange    — Few-Shot
C_STRUCT = "#70AD47"   # Green     — Structured
C_COT    = "#FFC000"   # Amber     — CoT
STRATEGY_COLORS = [C_ZERO, C_FEW, C_STRUCT, C_COT]
STRATEGY_LABELS = ["Zero-Shot", "Few-Shot", "Structured", "CoT"]
STRATEGIES = ["zero_shot", "few_shot", "structured", "cot"]

MODEL_COLORS = ["#1F3864", "#C0392B", "#1E8449"]
MODEL_LABELS = ["GPT-OSS-120B", "LLaMA-3.3-70B", "Kimi-K2"]
MODEL_KEYS   = [
    "openai-gpt-oss-120b",
    "llama-3.3-70b-versatile",
    "moonshotai-kimi-k2-instruct-0905"
]

METRICS      = ["executable", "passed", "mutation_killed", "line_coverage", "branch_coverage"]
METRIC_LABELS = ["Executability", "Pass Rate", "Mutation Score", "Line Coverage", "Branch Coverage"]

# ── GLOBAL FONT SETTINGS (matches Excel/Word document style) ──────────────────
plt.rcParams.update({
    "font.family":      "Times New Roman",
    "font.size":        10,
    "axes.titlesize":   11,
    "axes.labelsize":   10,
    "legend.fontsize":  9,
    "xtick.labelsize":  9,
    "ytick.labelsize":  9,
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "figure.dpi":       150,
    "savefig.dpi":      300,
    "savefig.bbox":     "tight",
    "savefig.facecolor":"white",
})

# ── LOAD & CLEAN DATA ─────────────────────────────────────────────────────────
print("Loading results.json...")
raw = json.loads(RESULTS_FILE.read_text(encoding="utf-8"))
data = {k: v for k, v in raw.items() if k != "First_Tests"}

# Manually curated values from the paper (averaged across 3 runs, 10 functions)
# These match Table 2 in the paper exactly.
PAPER_DATA = {
    "openai-gpt-oss-120b": {
        "zero_shot":  {"exec":100,"pass":50,"mut":80,"line":96.1,"branch":92.2},
        "few_shot":   {"exec":100,"pass":50,"mut":70,"line":92.9,"branch":89.2},
        "structured": {"exec":100,"pass":40,"mut":80,"line":90.4,"branch":88.3},
        "cot":        {"exec":100,"pass":30,"mut":80,"line":97.1,"branch":95.0},
    },
    "llama-3.3-70b-versatile": {
        "zero_shot":  {"exec":0,  "pass":0, "mut":0, "line":0,   "branch":0  },
        "few_shot":   {"exec":0,  "pass":0, "mut":0, "line":0,   "branch":0  },
        "structured": {"exec":30, "pass":10,"mut":40,"line":23.8,"branch":23.1},
        "cot":        {"exec":90, "pass":10,"mut":80,"line":84.2,"branch":81.7},
    },
    "moonshotai-kimi-k2-instruct-0905": {
        "zero_shot":  {"exec":100,"pass":50,"mut":80,"line":96.3,"branch":92.5},
        "few_shot":   {"exec":0,  "pass":0, "mut":0, "line":0,   "branch":0  },
        "structured": {"exec":90, "pass":30,"mut":80,"line":89.6,"branch":85.8},
        "cot":        {"exec":83, "pass":0, "mut":67,"line":77.1,"branch":70.8},
    }
}

METRIC_KEYS_PLOT = ["exec","pass","mut","line","branch"]


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 1 — Grouped Bar Chart (one subplot per model, all 5 metrics)
# ═══════════════════════════════════════════════════════════════════════════════
def figure1():
    print("Generating Figure 1: Grouped bar chart...")
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5), sharey=True)
    #fig.suptitle("Figure 1. Test Quality Metrics by Prompting Strategy Across Models",
    #             fontsize=12, fontweight="bold", y=1.02)

    x        = np.arange(len(METRIC_LABELS))
    n_strats = len(STRATEGIES)
    width    = 0.18
    offsets  = np.linspace(-(n_strats-1)/2 * width, (n_strats-1)/2 * width, n_strats)

    for ax, model_key, model_label in zip(axes, MODEL_KEYS, MODEL_LABELS):
        model_data = PAPER_DATA[model_key]

        for si, (strat, color, offset) in enumerate(
                zip(STRATEGIES, STRATEGY_COLORS, offsets)):
            vals = [model_data[strat][mk] for mk in METRIC_KEYS_PLOT]
            bars = ax.bar(x + offset, vals, width, color=color,
                          label=STRATEGY_LABELS[si], edgecolor="white",
                          linewidth=0.5, zorder=3)

            # Value labels on bars taller than 15%
            for bar, val in zip(bars, vals):
                if val >= 15:
                    ax.text(bar.get_x() + bar.get_width()/2,
                            bar.get_height() + 1.2,
                            f"{val:.0f}", ha="center", va="bottom",
                            fontsize=6.5, color="#333333", fontweight="bold")

        ax.set_title(model_label, fontweight="bold", fontsize=10,
                     pad=8, color="#1F3864")
        ax.set_xticks(x)
        ax.set_xticklabels(METRIC_LABELS, rotation=20, ha="right", fontsize=8.5)
        ax.set_ylim(0, 115)
        ax.set_ylabel("Score (%)" if ax == axes[0] else "", fontsize=9)
        ax.yaxis.grid(True, linestyle="--", alpha=0.5, zorder=0)
        ax.set_axisbelow(True)
        ax.tick_params(axis="x", length=0)

        # N/A annotation for LLaMA Zero/Few-Shot
        if model_key == "llama-3.3-70b-versatile":
            ax.annotate("Zero/Few-Shot:\n0% exec → N/A cov.",
                        xy=(3.5, 8), fontsize=7, color="#C0392B",
                        ha="center", style="italic",
                        bbox=dict(boxstyle="round,pad=0.2", fc="#FEF9E7", ec="#C0392B", lw=0.8))

    # Single legend below all subplots
    handles = [mpatches.Patch(color=c, label=l)
               for c, l in zip(STRATEGY_COLORS, STRATEGY_LABELS)]
    fig.legend(handles=handles, loc="lower center", ncol=4,
               frameon=True, framealpha=0.95,
               bbox_to_anchor=(0.5, -0.06), fontsize=9,
               title="Prompting Strategy", title_fontsize=9)

    plt.tight_layout()
    out = OUTPUT_DIR / "figure1_grouped_bar.png"
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 2 — Heatmap (Executability + Mutation Score side by side)
# ═══════════════════════════════════════════════════════════════════════════════
def figure2():
    print("Generating Figure 2: Heatmap...")

    exec_matrix = np.array([
        [PAPER_DATA[mk][s]["exec"] for s in STRATEGIES]
        for mk in MODEL_KEYS
    ])
    mut_matrix = np.array([
        [PAPER_DATA[mk][s]["mut"] for s in STRATEGIES]
        for mk in MODEL_KEYS
    ])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 3.8))
    #fig.suptitle("Figure 2. Executability and Mutation Score Heatmap Across Models × Strategies",
    #             fontsize=11, fontweight="bold", y=1.04)

    def draw_heatmap(ax, matrix, title, cmap):
        annot = matrix.astype(object).copy()
        annot[matrix == 0] = "FAIL"

        sns.heatmap(
            matrix,
            ax=ax,
            annot=annot, fmt="",   # <-- use custom annotations
            cmap=cmap,
            vmin=0, vmax=100,
            linewidths=0.8, linecolor="#CCCCCC",
            xticklabels=STRATEGY_LABELS,
            yticklabels=MODEL_LABELS,
            annot_kws={"size": 11, "weight": "bold"},
            cbar_kws={"shrink": 0.85, "label": "Score (%)"},
        )

        ax.set_title(title, fontweight="bold", fontsize=10, pad=10, color="#1F3864")
        ax.set_xlabel("Prompting Strategy", fontsize=9)
        ax.set_ylabel("")
        ax.tick_params(axis="x", rotation=15, labelsize=9)
        ax.tick_params(axis="y", rotation=0, labelsize=9)

    draw_heatmap(ax1, exec_matrix, "(a) Executability (%)", "RdYlGn")
    draw_heatmap(ax2, mut_matrix,  "(b) Mutation Score (%)", "RdYlGn")

    plt.tight_layout()
    out = OUTPUT_DIR / "figure2_heatmap.png"
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 3 — Radar / Spider Chart (one per model, 5 metrics as axes)
# ═══════════════════════════════════════════════════════════════════════════════
def figure3():
    print("Generating Figure 3: Radar chart...")

    categories = METRIC_LABELS
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]   # close the polygon

    fig, axes = plt.subplots(1, 3, figsize=(15, 5),
                             subplot_kw=dict(polar=True))
    #fig.suptitle("Figure 3. Multi-Metric Strategy Profiles (Radar Charts per Model)",
    #             fontsize=11, fontweight="bold", y=1.04)

    for ax, model_key, model_label in zip(axes, MODEL_KEYS, MODEL_LABELS):
        for strat, color, label in zip(STRATEGIES, STRATEGY_COLORS, STRATEGY_LABELS):
            d = PAPER_DATA[model_key][strat]
            vals = [d["exec"], d["pass"], d["mut"], d["line"], d["branch"]]
            vals += vals[:1]
            ax.plot(angles, vals, "o-", color=color, linewidth=2,
                    markersize=4, label=label, zorder=3)
            ax.fill(angles, vals, color=color, alpha=0.08)

        # Grid rings at 25/50/75/100
        ax.set_yticks([25, 50, 75, 100])
        ax.set_yticklabels(["25", "50", "75", "100"], fontsize=7, color="#666666")
        ax.set_ylim(0, 110)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=8.5, color="#1F3864")
        ax.grid(color="#CCCCCC", linestyle="--", linewidth=0.6)

        ax.set_title(model_label, fontweight="bold", fontsize=10,
                     pad=18, color="#1F3864")
        ax.spines["polar"].set_color("#CCCCCC")

    # Legend below
    handles = [mpatches.Patch(color=c, label=l)
               for c, l in zip(STRATEGY_COLORS, STRATEGY_LABELS)]
    fig.legend(handles=handles, loc="lower center", ncol=4,
               frameon=True, framealpha=0.95,
               bbox_to_anchor=(0.5, -0.06), fontsize=9,
               title="Prompting Strategy", title_fontsize=9)

    plt.tight_layout()
    out = OUTPUT_DIR / "figure3_radar.png"
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 4 — Interaction Plot (strategy on x, one line per model, 2 metrics)
# ═══════════════════════════════════════════════════════════════════════════════
def figure4():
    print("Generating Figure 4: Interaction plot...")

    # Show Executability and Mutation Score — the two most informative for RQ3
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    #fig.suptitle("Figure 4. Model Scale Moderates Prompting Strategy Effect\n"
    #             "(Lines represent models; crossing = interaction effect)",
    #             fontsize=11, fontweight="bold", y=1.02)

    plot_metrics = [
        ("exec",  "(a) Executability (%)"),
        ("mut",   "(b) Mutation Score (%)"),
    ]
    x_pos = np.arange(len(STRATEGIES))

    for ax, (metric_key, metric_title) in zip([ax1, ax2], plot_metrics):
        for model_key, model_color, model_label in zip(
                MODEL_KEYS, MODEL_COLORS, MODEL_LABELS):
            vals = [PAPER_DATA[model_key][s][metric_key] for s in STRATEGIES]
            ax.plot(x_pos, vals, "o-", color=model_color,
                    linewidth=2.2, markersize=7,
                    label=model_label, zorder=3)
            # Annotate endpoint values
            for xi, v in enumerate(vals):
                if v > 0:
                    ax.annotate(f"{v:.0f}",
                                xy=(xi, v), xytext=(0, 7),
                                textcoords="offset points",
                                ha="center", fontsize=7.5,
                                color=model_color, fontweight="bold")

        ax.set_xticks(x_pos)
        ax.set_xticklabels(STRATEGY_LABELS, fontsize=9.5)
        ax.set_ylim(-5, 115)
        ax.set_ylabel("Score (%)", fontsize=9)
        ax.set_xlabel("Prompting Strategy", fontsize=9)
        ax.set_title(metric_title, fontweight="bold", fontsize=10,
                     color="#1F3864", pad=8)
        ax.yaxis.grid(True, linestyle="--", alpha=0.45, zorder=0)
        ax.set_axisbelow(True)
        ax.tick_params(axis="x", length=0)

        # Shade the "crossing zone" for executability to highlight interaction
        if metric_key == "exec":
            ax.axvspan(0.5, 1.5, alpha=0.06, color="#C0392B",
                       label="_nolegend_")
            ax.annotate("Interaction\nregion",
                        xy=(1, 30), fontsize=7.5, color="#C0392B",
                        ha="center", style="italic",
                        bbox=dict(boxstyle="round,pad=0.2",
                                  fc="white", ec="#C0392B", lw=0.8))

    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3,
               frameon=True, framealpha=0.95,
               bbox_to_anchor=(0.5, -0.08), fontsize=9,
               title="Model", title_fontsize=9)

    plt.tight_layout()
    out = OUTPUT_DIR / "figure4_interaction.png"
    plt.savefig(out)
    plt.close()
    print(f"  Saved: {out}")


# ── RUN ALL ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        import seaborn
    except ImportError:
        print("Installing seaborn...")
        import subprocess, sys
        subprocess.run([sys.executable, "-m", "pip", "install", "seaborn"], check=True)
        import seaborn as sns

    figure1()
    figure2()
    figure3()
    figure4()

    print(f"\n✅ All figures saved to {OUTPUT_DIR}")
    print("   Insert them into the paper at the Figure 1–4 placeholder locations.")
    print("   Recommended: insert as 'In line with text', width = full column width.")