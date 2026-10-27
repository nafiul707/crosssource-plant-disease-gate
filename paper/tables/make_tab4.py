"""Table 4: robustness of the gate -- all calibrations at risk targets 5% and 10%, both crops.
Means over models, held-out sources (equal weight) and seeds; Remedy+kNN score.
Run from the project folder:  .venv/Scripts/python.exe paper/tables/make_tab4.py"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
BS = "\\"
EOL = " " + BS + BS
HEADS = ["LP-global@DINOv3-B", "SERA@DINOv3-B", "SERA@DINOv3-S"]
ROWS = [("no gate", "No gate"),
        ("val-CRC", "Standard (val-CRC)"),
        ("W-CRC", "Weighted CRC"),
        ("Robust-CRC(rho=0.05)", "Robust CRC, $" + BS + "rho=0.05$"),
        ("Robust-CRC(rho=0.1)", "Robust CRC, $" + BS + "rho=0.10$"),
        ("target-CRC", "100 labelled target images"),
        ("LOSO-CRC (2 src)", "LOSO-CRC, 2 sources (ours)"),
        ("LOSO-CRC", "LOSO-CRC (ours)"),
        ("LOSO-CRC-worst", "LOSO-CRC strict (ours)"),
        ("LOSO+LCO-CRC", "LOSO+LCO-CRC (ours)$^{a}$"),
        ("LOSO+LCO-CRC-worst", "LOSO+LCO-CRC strict (ours)$^{a}$")]


def per_source_mean(df, cols):
    return df.groupby(["held_out"])[cols].mean().mean() if "held_out" in df else df[cols].mean()


def values(crop):
    sw = pd.read_csv(ROOT / "paper_results" / crop / "kaggle_tables" / "gate_eps_sweep.csv")
    sw = sw[sw.score == "Remedy+kNN"]
    tl = pd.read_csv(ROOT / "paper_results" / crop / "extra_analysis" / "gate_target_labelled.csv")
    gs = pd.read_csv(ROOT / "paper_results" / crop / "kaggle_tables" / "gate_summary.csv")
    models = sorted(set(sw.model))
    out = {}
    for key, _ in ROWS:
        for eps in (0.05, 0.10):
            if key == "no gate":
                g = gs[(gs.calibration == "no gate") & gs.model.isin(models)]
                out[(key, eps)] = (g.risk.mean(), 1.0, 1.0)
            elif key == "target-CRC":
                g = tl[(tl.calibration == key) & (tl.eps == eps) & (tl.n == 100)]
                out[(key, eps)] = (g.risk.mean(), g.accept.mean(), g.violation.mean())
            else:
                g = sw[(sw.calibration == key) & (sw.eps == eps)]
                out[(key, eps)] = (g.risk.mean(), g.accept.mean(), g.violation.mean())
    g = sw[(sw.calibration == "LOSO-CRC-worst") & (sw.eps == 0.05) & sw.model.isin(HEADS)]
    out["heads_strict"] = (g.risk.mean(), g.accept.mean())
    return out


V = {c: values(c) for c in ("onion", "potato")}
pct = lambda v: f"{v * 100:.1f}"
lines = [BS + "begin{table}[t]", BS + "centering", BS + "scriptsize",
         BS + "caption{Robustness of the treatment gate. Wrong-treatment rate / share of images given advice (\\%), "
         "and the share of held-out runs whose rate exceeds the target (\\%), at targets of 5\\% and 10\\%. "
         "Means over four models (three frozen-encoder heads and ViT-S), held-out sources and seeds; Remedy+kNN score. "
         "For labelled target images, the exceedance is over 200 random labelled samples. "
         "$^{a}$Frozen-encoder heads only; the strict LOSO-CRC on the same three heads gives "
         + f"{pct(V['onion']['heads_strict'][0])} / {pct(V['onion']['heads_strict'][1])} (onion) and "
         + f"{pct(V['potato']['heads_strict'][0])} / {pct(V['potato']['heads_strict'][1])} (potato) at 5\\%." + "}",
         BS + "label{tab:robust}", BS + "setlength{" + BS + "tabcolsep}{2.5pt}",
         BS + "begin{tabular}{lcccccc}", BS + "toprule",
         " & " + BS + "multicolumn{3}{c}{Onion} & " + BS + "multicolumn{3}{c}{Potato}" + EOL,
         BS + "cmidrule(lr){2-4}" + BS + "cmidrule(lr){5-7}",
         " & " + BS + "multicolumn{2}{c}{Target 5\\%} & Target 10\\% & " + BS + "multicolumn{2}{c}{Target 5\\%} & Target 10\\%" + EOL,
         BS + "cmidrule(lr){2-3}" + BS + "cmidrule(lr){4-4}" + BS + "cmidrule(lr){5-6}" + BS + "cmidrule(lr){7-7}",
         "Calibration & rate / advice & over & rate / advice & rate / advice & over & rate / advice" + EOL,
         BS + "midrule"]
for key, name in ROWS:
    cells = []
    for c in ("onion", "potato"):
        r5, a5, v5 = V[c][(key, 0.05)]
        r10, a10, _ = V[c][(key, 0.10)]
        cells += [f"{pct(r5)} / {a5 * 100:.0f}", f"{v5 * 100:.0f}", f"{pct(r10)} / {a10 * 100:.0f}"]
    if key == "LOSO-CRC (2 src)":
        lines.append(BS + "midrule")
    lines.append(name + " & " + " & ".join(cells) + EOL)
lines += [BS + "bottomrule", BS + "end{tabular}", BS + "end{table}"]
(Path(__file__).parent / "tab4_robust.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines[-16:]))
