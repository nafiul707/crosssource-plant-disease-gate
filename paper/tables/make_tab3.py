"""Table 3: wrong-treatment rate per held-out source, standard calibration vs strict LOSO-CRC (target 5%).
Run from the project folder:  .venv/Scripts/python.exe paper/tables/make_tab3.py"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
BS = "\\"
EOL = " " + BS + BS
SRC = {"onion": [("cold", "COLD"), ("tom2024_onion", "TOM2024"), ("roboflow_capstone", "Capstone"),
                 ("roboflow_onionnet", "OnionNet")],
       "potato": [("plantvillage", "PlantVillage"), ("plantdoc", "PlantDoc"), ("pld_pakistan", "PLD"),
                  ("uncontrolled_indonesia", "Indonesia")]}
MODELS = {"onion": [("LP-global@DINOv3-B", "DINOv3-B probe"), ("SERA@DINOv3-B", "DINOv3-B SERA"),
                    ("SERA@DINOv3-S", "DINOv3-S SERA"), ("ViTS-kNN", "ViT-S")],
          "potato": [("LP-global@DINOv3-B", "DINOv3-B probe"), ("SERA@DINOv3-B", "DINOv3-B SERA"),
                     ("SERA@DINOv3-S", "DINOv3-S SERA"), ("ViTS", "ViT-S")]}


def fmt(std, ours, acc):
    o = f"{ours * 100:.1f}"
    if ours > 0.05:
        o = BS + "textbf{" + o + "}"                      # bold = target missed
    return f"{std * 100:.1f} $" + BS + "rightarrow$ " + o + f" ({acc * 100:.0f})"


lines = [BS + "begin{table}[t]", BS + "centering", BS + "scriptsize",
         BS + "caption{Wrong-treatment rate (\\%) on each unseen source with the standard calibration "
         "(val-CRC) $" + BS + "rightarrow$ with the strict leave-one-source-out calibration (LOSO-CRC-worst); "
         "in parentheses, the share of images given advice (\\%) under LOSO-CRC-worst. Target 5\\%; "
         "bold values miss the target. Remedy+kNN score, mean over three seeds.}",
         BS + "label{tab:gate-source}", BS + "setlength{" + BS + "tabcolsep}{3pt}",
         BS + "begin{tabular}{lcccc}", BS + "toprule"]
for crop in ["onion", "potato"]:
    ps = pd.read_csv(ROOT / "paper_results" / crop / "extra_analysis" / "gate_per_source.csv")
    ps = ps[(ps.eps == 0.05) & (ps.score == "Remedy+kNN")]
    lines.append(BS + "multicolumn{5}{l}{" + BS + "textbf{" + crop.capitalize() + "}}" + EOL)
    lines.append("Model & " + " & ".join(n for _, n in SRC[crop]) + EOL + " " + BS + "midrule")
    for key, name in MODELS[crop]:
        cells = []
        for s, _ in SRC[crop]:
            g = ps[(ps.model == key) & (ps.held_out == s)].set_index("calibration")
            cells.append(fmt(g.loc["val-CRC", "risk"], g.loc["LOSO-CRC-worst", "risk"], g.loc["LOSO-CRC-worst", "accept"]))
        lines.append(name + " & " + " & ".join(cells) + EOL)
    lines.append(BS + ("midrule" if crop == "onion" else "bottomrule"))
lines += [BS + "end{tabular}", BS + "end{table}"]
(Path(__file__).parent / "tab3_gate_sources.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("written")
