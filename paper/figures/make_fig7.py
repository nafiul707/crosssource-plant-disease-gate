"""Figure 7: faithfulness of the attention (deletion test) and example attention maps (SERA, DINOv3-B, seed 0).
Data: paper_results/<crop>/kaggle_tables/xai_bag_deletion.csv and paper_results/xai_examples/<crop>/
(heads/H_SERA_at_DINOv3-B__lodo__<source>__s0.npz with test_att, audit images + key).
Run from the project folder:  .venv/Scripts/python.exe paper/figures/make_fig7.py"""
from pathlib import Path
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
RES, OUT = ROOT / "paper_results", Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "DejaVu Serif"],
                     "font.size": 8.5, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6})
CANVAS, GRIDS = 672, (1, 2, 3)
NICE = {"purple_blotch": "purple blotch", "late_blight": "late blight", "early_blight": "early blight",
        "downy_mildew": "downy mildew", "stemphylium": "Stemphylium", "healthy": "healthy", "viral": "viral",
        "botrytis": "Botrytis", "rust": "rust", "xanthomonas": "Xanthomonas", "burn_tip": "burn tip",
        "fusarium": "Fusarium", "bulb_blight": "bulb blight", "fungi_other": "other fungal", "bacterial": "bacterial",
        "pest": "pest", "nematode": "nematode"}
SRC = {"cold": "COLD", "tom2024_onion": "TOM2024", "roboflow_capstone": "Capstone", "roboflow_onionnet": "OnionNet",
       "plantvillage": "PlantVillage", "plantdoc": "PlantDoc", "pld_pakistan": "PLD",
       "uncontrolled_indonesia": "Indonesia"}


def tile_boxes():
    boxes = []
    for g in GRIDS:
        e = np.linspace(0, CANVAS, g + 1).round().astype(int)
        for r in range(g):
            for c in range(g):
                boxes.append((e[c], e[r], e[c + 1], e[r + 1], g))
    return boxes


BOXES = tile_boxes()


def heat(att):
    """Attention of the tile views spread over the image (each tile's weight split evenly over its pixels,
    per scale); the whole-image view is reported separately."""
    h = np.zeros((CANVAS, CANVAS))
    for a, (x0, y0, x1, y1, g) in zip(att, BOXES):
        if g > 1:
            h[y0:y1, x0:x1] += a
    return h / max(h.max(), 1e-9)


def examples(crop, picks):
    """picks: list of (source, label) -> first correctly predicted, confident audit image of that cell."""
    base = RES / "xai_examples" / crop
    key = pd.read_csv(base / "expert_audit_KEY_do_not_share.csv")
    man = pd.read_csv(RES / crop / "kaggle_tables" / "manifest_dedup.csv", keep_default_na=False)
    row_of = {r: i for i, r in enumerate(man.rel)}
    classes = sorted(man.loc[man.drop_reason == "", "label_name"].unique())
    out = []
    for src, lab in picks:
        z = np.load(base / "heads" / f"H_SERA_at_DINOv3-B__lodo__{src}__s0.npz")
        pos = {int(g): j for j, g in enumerate(z["test_idx"])}
        cls = list(z["classes"])
        best = None
        for _, r in key[(key.dataset == src) & (key.label_name == lab)].iterrows():
            i = row_of.get(r.rel)
            if i is None or i not in pos:
                continue
            j = pos[i]
            lg = z["test_logits"][j].astype(float); p = np.exp(lg - lg.max()); p /= p.sum()
            pred = classes[int(cls[int(p.argmax())])]
            if pred == lab and (best is None or p.max() > best[2]):
                best = (r.audit_id, z["test_att"][j].astype(float), float(p.max()))
        if best:
            out.append((crop, src, lab, *best, base / "images" / f"{best[0]}.jpg"))
    return out


fig = plt.figure(figsize=(6.3, 3.9))
gs = fig.add_gridspec(2, 5, width_ratios=[1.55, 0.18, 1, 1, 1], wspace=0.08, hspace=0.32,
                      left=0.085, right=0.995, top=0.90, bottom=0.12)
# ---- (a) deletion test --------------------------------------------------
ax = fig.add_subplot(gs[:, 0])
COL = {"onion": "#D55E00", "potato": "#0072B2"}
for crop in ("onion", "potato"):
    d = pd.read_csv(RES / crop / "kaggle_tables" / "xai_bag_deletion.csv")
    d = d[d.model == "SERA@DINOv3-B"].groupby(["mode", "k"]).prob_drop.mean()
    k = [1, 2, 3, 4]
    ax.plot(k, [d["top", i] for i in k], "-o", color=COL[crop], ms=3.5, lw=1.2, label=f"{crop.capitalize()}, most-attended")
    ax.plot(k, [d["random", i] for i in k], "--o", color=COL[crop], ms=3.5, lw=1.0, mfc="white",
            label=f"{crop.capitalize()}, random")
ax.set_xticks([1, 2, 3, 4]); ax.set_xlabel("Views removed (of 14)")
ax.set_ylabel("Drop in predicted probability")
ax.set_ylim(0, 0.3); ax.grid(color="0.93", lw=0.6); ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(fontsize=7.6, frameon=False, loc="upper left")
ax.set_title("(a) Deletion test", fontsize=9.5, fontweight="bold", loc="left")

# ---- (b) examples -------------------------------------------------------
ex = examples("onion", [("cold", "purple_blotch"), ("tom2024_onion", "purple_blotch"), ("roboflow_capstone", "downy_mildew")]) + \
     examples("potato", [("plantdoc", "late_blight"), ("pld_pakistan", "early_blight"), ("uncontrolled_indonesia", "late_blight")])
for n, (crop, src, lab, aid, att, conf, path) in enumerate(ex[:6]):
    a = fig.add_subplot(gs[n // 3, 2 + n % 3])
    img = np.asarray(Image.open(path).convert("RGB").resize((CANVAS, CANVAS)))
    a.imshow(img)
    h = heat(att)
    a.imshow(h, cmap="inferno", alpha=0.75 * h, vmin=0, vmax=1)   # transparent where attention is low
    a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values():
        s.set_linewidth(0.4)
    a.set_title(f"{SRC[src]}: {NICE[lab]}", fontsize=8, pad=2)
    a.text(0.03, 0.03, f"whole: {att[0] * 100:.0f}%", transform=a.transAxes, fontsize=7.5, color="white",
           bbox=dict(boxstyle="round,pad=0.15", fc="black", alpha=0.55, lw=0))
    if n == 0:
        a.text(0.0, 1.22, "(b) Where the model looks (unseen sources)", transform=a.transAxes, fontsize=9.5,
               fontweight="bold", va="bottom")
fig.savefig(OUT / "fig7_xai.pdf", dpi=300)
fig.savefig(OUT / "fig7_xai.png", dpi=170)
print("saved", len(ex), "examples:", [(e[1], e[2], e[3], round(e[5], 2)) for e in ex])
