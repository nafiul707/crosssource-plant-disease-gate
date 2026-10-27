"""Figure 5: LODO macro-F1 per model and held-out source, onion and potato.
Run from the project folder:  .venv/Scripts/python.exe paper/figures/make_fig5.py"""
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
RES, OUT = ROOT / "paper_results", Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
                     "font.size": 8.5, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6})

# (display name, key in lodo_macro_f1_all.csv, group); group order = vertical blocks
MODELS = [
    ("ViT-S", "ViTS", "Fine-tuned"), ("ConvNeXt-T", "ConvNeXtT", "Fine-tuned"),
    ("EfficientNet-B0", "EfficientNetB0", "Fine-tuned"), ("ResNet-50", "ResNet50", "Fine-tuned"),
    ("MobileNetV3-L", "MobileNetV3L", "Fine-tuned"),
    ("MixStyle", "DG:MixStyle", "Domain generalisation"), ("SWA", "DG:SWA", "Domain generalisation"),
    ("AmpMix + consistency", "DG:AmpMix+Cons", "Domain generalisation"),
    ("SILA-Net (our design, tested)", "SILA-Net", "Domain generalisation"),
    ("DINOv3-B linear probe", "LP-global@DINOv3-B", "Frozen encoder + head"),
    ("DINOv3-B attention (MIL)", "MIL@DINOv3-B", "Frozen encoder + head"),
    ("DINOv3-B SERA (our design, tested)", "SERA@DINOv3-B", "Frozen encoder + head"),
    ("BioCLIP-2 linear probe", "LP-global@BioCLIP-2", "Frozen encoder + head"),
    ("BioCLIP-2 SERA (our design, tested)", "SERA@BioCLIP-2", "Frozen encoder + head"),
]
SOURCES = {"onion": [("cold", "COLD"), ("tom2024_onion", "TOM2024"), ("roboflow_capstone", "Roboflow Capstone"),
                     ("roboflow_onionnet", "Roboflow OnionNet")],
           "potato": [("plantvillage", "PlantVillage"), ("plantdoc", "PlantDoc"), ("pld_pakistan", "PLD"),
                      ("uncontrolled_indonesia", "Indonesia")]}
PAL = ["#E69F00", "#009E73", "#CC79A7", "#56B4E9"]          # Okabe-Ito
MK = ["o", "s", "^", "D"]

def load(crop):
    t = pd.read_csv(RES / crop / "kaggle_tables" / "lodo_macro_f1_all.csv").set_index("model")
    out = {}
    for _, key, _ in MODELS:
        if key in t.index:
            out[key] = {s: float(str(t.loc[key, s]).split("±")[0]) for s, _ in SOURCES[crop]}
    return out

fig, axes = plt.subplots(1, 2, figsize=(5.15, 4.3), sharey=True, gridspec_kw=dict(wspace=0.08))
y = np.arange(len(MODELS))[::-1].astype(float)
for gi in range(1, len(MODELS)):                                # extra space between groups
    if MODELS[gi][2] != MODELS[gi - 1][2]:
        y[gi:] -= 0.6
for ax, crop, title in zip(axes, ["onion", "potato"], ["(a) Onion", "(b) Potato"]):
    data = load(crop)
    for yi, (name, key, grp) in zip(y, MODELS):
        if key not in data:
            ax.text(0.18, yi, "not run on this crop", fontsize=7, color="0.55", va="center", style="italic")
            continue
        v = data[key]
        vals = [v[s] for s, _ in SOURCES[crop]]
        ax.plot([min(vals), max(vals)], [yi, yi], color="0.80", lw=1.0, zorder=1)
        for k, (s, _) in enumerate(SOURCES[crop]):
            ax.plot(v[s], yi, MK[k], color=PAL[k], ms=4.2, mec="white", mew=0.4, zorder=2)
        ax.plot([np.mean(vals)] * 2, [yi - 0.32, yi + 0.32], color="black", lw=1.6, zorder=3)
    ax.set_xlim(0.15, 1.0); ax.set_xticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_xlabel("Macro-F1 on the unseen source")
    ax.set_title(title, fontsize=9.5, fontweight="bold", loc="left")
    ax.grid(axis="x", color="0.92", lw=0.6); ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    hs = [plt.Line2D([], [], ls="", marker=MK[k], color=PAL[k], ms=4.5) for k in range(4)]
    hs.append(plt.Line2D([], [], color="black", lw=1.6))
    ax.legend(hs, [n for _, n in SOURCES[crop]] + ["mean of four"], fontsize=7, frameon=False,
              loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, handletextpad=0.3, columnspacing=0.8)
axes[0].set_yticks(y); axes[0].set_yticklabels([m[0] for m in MODELS], fontsize=7.8)
for gi, (_, _, grp) in enumerate(MODELS):
    if gi == 0 or MODELS[gi - 1][2] != grp:
        axes[0].text(-0.02, y[gi] + 0.62, grp, transform=axes[0].get_yaxis_transform(), ha="right",
                     fontsize=7.8, fontweight="bold", color="0.25")
fig.savefig(OUT / "fig5_accuracy.pdf", bbox_inches="tight")
fig.savefig(OUT / "fig5_accuracy.png", dpi=170, bbox_inches="tight")
print("saved")
