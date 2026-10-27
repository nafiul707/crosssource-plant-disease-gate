"""Run notebook section 12.2 (gate robustness) locally on downloaded Kaggle outputs.
usage: python analysis_local.py <crop: onion|potato> <downloaded results dir> <out dir>"""
import ast, os, sys, json, re, math, hashlib
from pathlib import Path
from collections import Counter
import numpy as np, pandas as pd, torch, torch.nn as nn, torch.nn.functional as F
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from tqdm import tqdm

SCR = Path(__file__).parent
crop, RESD, OUTD = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
OUTD.mkdir(parents=True, exist_ok=True)

def parse(path):
    cells, cur, kind = [], [], None
    for line in Path(path).read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("##CELL "):
            if kind:
                cells.append((kind, "".join(cur)))
            kind, cur = line.split()[1], []
        else:
            cur.append(line)
    if kind:
        cells.append((kind, "".join(cur)))
    return [src for k, src in cells if k == "code"]

def exec_defs(src, ns):
    """Execute only imports and function/class definitions of a notebook cell."""
    tree = ast.parse(src)
    keep = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom))]
    exec(compile(ast.Module(body=keep, type_ignores=[]), "<cell>", "exec"), ns)

ns = dict(np=np, pd=pd, torch=torch, nn=nn, F=F, math=math, json=json, re=re, hashlib=hashlib, plt=plt, tqdm=tqdm,
          Counter=Counter, Path=Path, os=os)
os.environ["ONION_OUT"] = str(OUTD / "_cfg")
cfg = parse(SCR / ("p3_config.txt" if crop == "potato" else "v2_config.txt"))[0]
exec(cfg, ns)
ns.update(SMOKE=False, RUNS=RESD / "runs", HEADS=RESD / "heads", TABLES=OUTD, FIGS=OUTD, LEGACY_OK=True)

idx = pd.read_csv(RESD / "tables" / "manifest_dedup.csv", keep_default_na=False)
mem = pd.read_csv(RESD / "tables" / "split_membership.csv", index_col=0, keep_default_na=False)
CLASSES = sorted(idx.loc[idx.drop_reason == "", "label_name"].unique())
idx["y"] = idx.y.astype(int).copy()
ns.update(idx=idx, CLASSES=CLASSES, Y_ALL=torch.from_numpy(idx.y.values), dss=list(ns["DATASETS"]))
SPLITS = {}
for col in mem.columns[4:]:
    proto, split = col.split("_", 1)
    rows = {p: mem.index[mem[col] == p].values for p in ("train", "val", "test")}
    seen = set(idx.y.values[rows["train"]])
    rows["test_id"] = rows["test"][np.isin(idx.y.values[rows["test"]], list(seen))]
    SPLITS[(proto, split)] = rows
ns["SPLITS"] = SPLITS

REPORT = []
def md_table(df, floatfmt="{:.3f}"):
    df = df.reset_index() if not isinstance(df.index, pd.RangeIndex) else df
    fmt = lambda v: floatfmt.format(v) if isinstance(v, (float, np.floating)) and not pd.isna(v) else str(v)
    rows = ["| " + " | ".join(str(c) for c in df.columns) + " |", "|" + "---|" * len(df.columns)]
    rows += ["| " + " | ".join(fmt(v) for v in r) + " |" for r in df.itertuples(index=False)]
    return "\n".join(rows)
def report(title, text):
    REPORT.append(f"## {title}\n\n{text}\n")
ns.update(md_table=md_table, report=report)

tail = parse(SCR / "v2_tail.txt")
exec(tail[0], ns)                                    # section 6 helpers
for src in tail:
    if "def load_any" in src or "def decision_view" in src or "def head_key" in src:
        exec_defs(src, ns)
ns["head_done"] = lambda key: (ns["HEADS"] / f"{key}.npz").exists()
ns["run_done"] = lambda key: (ns["RUNS"] / f"{key}.npz").exists()
ns["_RUN_CACHE"] = {}
for name in ("y_of", "g_of"):
    exec_defs(next(s for s in tail if f"def {name}" in s), ns)
ns["EXT"] = None
ns.update(ALL_SEEDS=list(range(10)), PROPOSED="SERA@DINOv3-B",
          GATE_FOCUS=["LP-global@DINOv3-B", "SERA@DINOv3-B", "SERA@DINOv3-S", "ViTS", "ViTS-kNN"])

for src in parse(SCR / "v4_gate_robust.txt") + parse(SCR / "v4b_target_labels.txt"):
    exec(src, ns)
(OUTD / "ANALYSIS.md").write_text(f"# {crop}: gate robustness (section 12.2)\n\n" + "\n".join(REPORT), encoding="utf-8")
print("written", OUTD / "ANALYSIS.md")
