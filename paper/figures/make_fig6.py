"""Figure 6: wrong-treatment risk vs acceptance on unseen sources (target 5%), per calibration and model.
Run from the project folder:  .venv/Scripts/python.exe paper/figures/make_fig6.py"""
from pathlib import Path
import pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator

ROOT = Path(__file__).resolve().parents[2]
RES, OUT = ROOT / "paper_results", Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
                     "font.size": 8.5, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6})
EPS, SCORE = 0.05, "Remedy+kNN"
CALS = [("no gate", "No gate", "#9E9E9E"), ("val-CRC", "Standard (val-CRC)", "#D55E00"),
        ("W-CRC", "Weighted CRC", "#CC79A7"), ("LOSO-CRC", "LOSO-CRC (ours)", "#56B4E9"),
        ("LOSO-CRC-worst", "LOSO-CRC, strict (ours)", "#0072B2")]
MODELS = {"onion": [("LP-global@DINOv3-B", "DINOv3-B probe", "o"), ("SERA@DINOv3-B", "DINOv3-B SERA", "s"),
                    ("SERA@DINOv3-S", "DINOv3-S SERA", "^"), ("ViTS-kNN", "ViT-S", "D")],
          "potato": [("LP-global@DINOv3-B", "DINOv3-B probe", "o"), ("SERA@DINOv3-B", "DINOv3-B SERA", "s"),
                     ("SERA@DINOv3-S", "DINOv3-S SERA", "^"), ("ViTS", "ViT-S", "D")]}


def points(crop):
    sw = pd.read_csv(RES / crop / "extra_analysis" / "gate_eps_sweep.csv")
    sw = sw[(sw.eps == EPS) & (sw.score == SCORE)]
    gs = pd.read_csv(RES / crop / "kaggle_tables" / "gate_summary.csv")
    out = {}
    for key, _, _ in MODELS[crop]:
        ng = gs[(gs.model == key) & (gs.calibration == "no gate")].iloc[0]
        out[(key, "no gate")] = (ng.risk, ng.accept)
        for cal, _, _ in CALS[1:]:
            r = sw[(sw.model == key) & (sw.calibration == cal)].iloc[0]
            out[(key, cal)] = (r.risk, r.accept)
    return out


fig, axes = plt.subplots(1, 2, figsize=(5.4, 3.0), sharey=True, gridspec_kw=dict(wspace=0.08))
for ax, crop, title in zip(axes, ["onion", "potato"], ["(a) Onion", "(b) Potato"]):
    P = points(crop)
    ax.axvspan(0.008, EPS, color="#0072B2", alpha=0.07, lw=0)
    ax.axvline(EPS, color="0.35", ls="--", lw=0.8)
    ax.text(EPS * 0.93, 1.035, "target 5%", ha="right", va="bottom", fontsize=7.2, color="0.3")
    for key, _, mk in MODELS[crop]:
        xs = [P[(key, c)][0] for c, _, _ in CALS]; ys = [P[(key, c)][1] for c, _, _ in CALS]
        ax.plot(xs, ys, color="0.85", lw=0.7, zorder=1)
        for (cal, _, col), x, y in zip(CALS, xs, ys):
            ax.plot(x, y, mk, color=col, ms=5, mec="white", mew=0.5, zorder=3)
    ax.set_xscale("log"); ax.set_xlim(0.008, 0.7)
    ax.xaxis.set_major_locator(FixedLocator([0.01, 0.02, 0.05, 0.1, 0.2, 0.5]))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v * 100:g}%"))
    ax.set_ylim(0, 1.08); ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v * 100:.0f}%"))
    ax.set_xlabel("Wrong-treatment rate (log scale)")
    ax.set_title(title, fontsize=9.5, fontweight="bold", loc="left")
    ax.grid(color="0.93", lw=0.6); ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[0].set_ylabel("Images given advice")
h1 = [plt.Line2D([], [], ls="", marker="o", color=col, ms=5) for _, _, col in CALS]
h2 = [plt.Line2D([], [], ls="", marker=mk, color="0.35", ms=5) for _, _, mk in MODELS["onion"]]
fig.legend(h1 + h2, [n for _, n, _ in CALS] + [n for _, n, _ in MODELS["onion"]], fontsize=7.2, frameon=False,
           loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=3, handletextpad=0.3, columnspacing=1.0)
fig.savefig(OUT / "fig6_gate.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig6_gate.png", dpi=170, bbox_inches="tight")
print("saved")
