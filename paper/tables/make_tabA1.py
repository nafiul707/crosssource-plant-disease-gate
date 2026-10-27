"""Appendix Table A.1: LODO macro-F1 (mean +- sd over seeds) for every model and held-out source.
Run from the project folder:  .venv/Scripts/python.exe paper/tables/make_tabA1.py"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
NAMES = {"ViTS": "ViT-S", "ViTS-kNN": "ViT-S (gate runs)", "ConvNeXtT": "ConvNeXt-T", "EfficientNetB0": "EfficientNet-B0",
         "ResNet50": "ResNet-50", "MobileNetV3L": "MobileNetV3-L", "DG:MixStyle": "MixStyle", "DG:SWA": "SWA",
         "DG:AmpMix+Cons": "AmpMix + consistency", "SILA-Net": "SILA-Net",
         "FM:DINOv3-B": "DINOv3-B probe$^{a}$", "FM:DINOv2-B": "DINOv2-B probe$^{a}$", "FM:BioCLIP-2": "BioCLIP-2 probe$^{a}$"}
HEAD = {"LP-global": "linear probe", "LP-global+FMM": "linear probe + moment matching", "LP-mean": "mean of views",
        "MIL": "attention (MIL)", "LP-global+CCE": "linear probe + erasure", "MIL+GE": "MIL + global erasure",
        "SERA": "SERA", "SERA-5": "SERA, 5 views"}
SRC = {"onion": [("cold", "COLD"), ("tom2024_onion", "TOM2024"), ("roboflow_capstone", "Capstone"),
                 ("roboflow_onionnet", "OnionNet")],
       "potato": [("plantvillage", "PlantVillage"), ("plantdoc", "PlantDoc"), ("pld_pakistan", "PLD"),
                  ("uncontrolled_indonesia", "Indonesia")]}
BS = "\\"                      # one backslash, kept out of string literals to avoid escaping mistakes
EOL = " " + BS + BS            # LaTeX row end


def nice(m):
    if "@" in m:
        v, fm = m.split("@")
        return f"{fm} {HEAD.get(v, v)}"
    return NAMES.get(m, m)


def cell(text):
    mean, sd = (float(x) for x in str(text).split("±"))
    return f"{mean:.3f} $" + BS + f"pm$ {sd:.3f}"


lines = [BS + "begin{table}[p]", BS + "centering" + BS + "scriptsize",
         BS + "caption{LODO macro-F1 (mean $" + BS + "pm$ s.d. over seeds) on each held-out source for all models. "
         "Frozen-encoder heads use ten seeds and most fine-tuned models three. "
         "$^{a}$Linear probe trained with the fine-tuning pipeline (one seed).}",
         BS + "label{tab:lodo-all}", BS + "setlength{" + BS + "tabcolsep}{3pt}", BS + "resizebox{" + BS + "textwidth}{!}{%", BS + "begin{tabular}{lccccc}", BS + "toprule"]
for crop in ["onion", "potato"]:
    t = pd.read_csv(ROOT / "paper_results" / crop / "kaggle_tables" / "lodo_macro_f1_all.csv")
    t = t.sort_values("mean", ascending=False)
    lines.append(BS + "multicolumn{6}{l}{" + BS + "textbf{" + crop.capitalize() + "}}" + EOL)
    lines.append("Model & " + " & ".join(n for _, n in SRC[crop]) + " & Mean" + EOL + " " + BS + "midrule")
    for _, r in t.iterrows():
        lines.append(nice(r.model) + " & " + " & ".join(cell(r[s]) for s, _ in SRC[crop])
                     + f" & {r['mean']:.3f}" + EOL)
    lines.append(BS + ("midrule" if crop == "onion" else "bottomrule"))
lines += [BS + "end{tabular}}", BS + "end{table}"]
(Path(__file__).parent / "tabA1_lodo.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("written", len(lines), "lines")
