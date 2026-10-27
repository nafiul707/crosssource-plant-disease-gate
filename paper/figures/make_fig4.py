"""Figure 4: shortcut evidence (D1-D3) for onion and potato, from paper_results/<crop>/kaggle_tables.
Run from the project folder:  .venv/Scripts/python.exe paper/figures/make_fig4.py"""
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
RES, OUT = ROOT / "paper_results", Path(__file__).resolve().parent
COL = {"onion": "#D55E00", "potato": "#0072B2"}          # colour-blind-safe pair
MRK = {"onion": "o", "potato": "s"}
plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
                     "font.size": 8.5, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6})

def tab(crop, name):
    return pd.read_csv(RES / crop / "kaggle_tables" / f"{name}.csv")

# ---- panel (a): balanced accuracy of the probes ---------------------------
rows = ["Source from metadata\n(all images)",
        "Source from metadata\n(within one disease)",
        "Source from DINOv3 features\n(within one disease)",
        "... after source erasure,\nlinear probe",
        "... after source erasure,\nnon-linear probe",
        "Disease from metadata\n(within one source)"]
def probe_vals(crop):
    d1, d2 = tab(crop, "d1_metadata_probes"), tab(crop, "d2_feature_source_probes")
    w1 = d1[(d1.target == "source") & d1.subset.str.startswith("within")]
    w2 = d2[(d2.target == "source") & d2.subset.str.startswith("within")]
    dis = d1[d1.target == "disease"]
    pick = lambda df: (df.balanced_acc.values, df.chance.values)
    a = d1[(d1.target == "source") & (d1.subset == "all images")]
    return [pick(a), pick(w1),
            pick(w2[(w2.features == "raw") & (w2.probe == "linear")]),
            pick(w2[(w2.features == "class-cond. LEACE") & (w2.probe == "linear")]),
            pick(w2[(w2.features == "class-cond. LEACE") & (w2.probe == "MLP")]),
            pick(dis)]

fig, (ax, bx) = plt.subplots(1, 2, figsize=(4.75, 3.4), gridspec_kw=dict(width_ratios=[1.25, 1], wspace=0.95))
ys = np.arange(len(rows))[::-1].astype(float)
for k, crop in enumerate(["onion", "potato"]):
    off = 0.14 if k == 0 else -0.14
    for y, (acc, ch) in zip(ys, probe_vals(crop)):
        lo, hi, mid = acc.min(), acc.max(), acc.mean()
        if len(acc) > 1:
            ax.plot([lo, hi], [y + off] * 2, color=COL[crop], lw=1.2, alpha=0.8)
        ax.plot(mid, y + off, MRK[crop], color=COL[crop], ms=4.5, label=crop.capitalize() if y == ys[0] else None)
        for c in np.unique(ch):                                  # chance level(s) of this probe
            ax.plot([c, c], [y + off - 0.09, y + off + 0.09], color="0.45", lw=1.0)
ax.set_yticks(ys); ax.set_yticklabels(rows, fontsize=8)
ax.set_xlim(0, 1.02); ax.set_xlabel("Balanced accuracy")
ax.axhline(ys[2] + 0.5, color="0.85", lw=0.6); ax.axhline(ys[5] + 0.5, color="0.85", lw=0.6)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.plot([], [], color="0.45", lw=1.0, label="chance")
ax.legend(fontsize=7.5, frameon=False, loc="lower left", bbox_to_anchor=(0.0, 1.0), ncol=3, handlelength=1.2,
          columnspacing=1.0)
ax.set_title("(a) What identifies the source", fontsize=9.5, fontweight="bold", loc="left", pad=16)

# ---- panel (b): label-consistency index raw -> source-centred ------------
nice = {"downy_mildew": "downy mildew", "healthy": "healthy", "purple_blotch": "purple blotch",
        "stemphylium": "Stemphylium", "viral": "viral", "early_blight": "early blight", "late_blight": "late blight"}
items = []
for crop in ["onion", "potato"]:
    t = tab(crop, "d3_label_consistency_summary").sort_values("raw")
    items += [(crop, nice.get(r.cls, r.cls), r.raw, r["source-centred"]) for _, r in t.iterrows()]
yb = np.arange(len(items))[::-1].astype(float)
yb[:5] += 0.6                                                    # gap between the two crops
for y, (crop, lab, raw, cen) in zip(yb, items):
    bx.annotate("", xy=(cen, y), xytext=(raw, y),
                arrowprops=dict(arrowstyle="-|>", color=COL[crop], lw=1.0, mutation_scale=7, shrinkA=2, shrinkB=2))
    bx.plot(raw, y, MRK[crop], mfc="white", mec=COL[crop], ms=4.5, mew=1.0)
    bx.plot(cen, y, MRK[crop], color=COL[crop], ms=4.5)
bx.axvline(0, color="0.45", lw=0.8, ls="--")
bx.set_yticks(yb); bx.set_yticklabels([f"{lab}" for _, lab, _, _ in items], fontsize=8)
bx.text(-0.43, yb[0] + 0.45, "Onion", color=COL["onion"], fontsize=8, fontweight="bold", ha="left", va="bottom")
bx.text(-0.43, yb[5] + 0.45, "Potato", color=COL["potato"], fontsize=8, fontweight="bold", ha="left", va="bottom")
bx.set_ylim(yb[-1] - 0.6, yb[0] + 1.1)
bx.set_xlabel("Label-consistency index")
bx.set_xlim(-0.45, 0.75)
for s in ("top", "right"):
    bx.spines[s].set_visible(False)
bx.plot([], [], "o", mfc="white", mec="0.3", ms=4.5, label="raw")
bx.plot([], [], "o", color="0.3", ms=4.5, label="source style removed")
bx.legend(fontsize=7.5, frameon=False, loc="lower left", bbox_to_anchor=(0.0, 1.0), ncol=2, handlelength=1.0,
          columnspacing=1.0)
bx.set_title("(b) Do labels mean the same?", fontsize=9.5, fontweight="bold", loc="left", pad=16)

fig.savefig(OUT / "fig4_shortcut.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig4_shortcut.png", dpi=170, bbox_inches="tight")
print("saved", OUT / "fig4_shortcut.pdf")
