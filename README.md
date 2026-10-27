# Plant-disease models learn the dataset, not the disease

Code, fixed splits and results for the paper

> **Plant-disease models learn the dataset, not the disease: diagnosing cross-source failure and
> controlling treatment risk on unseen sources.**
> Nafiul Islam, Fatima Alifa, Tanni, Abdullah Alif. Submitted to *Computers and Electronics in Agriculture*.

We study onion and potato leaf-disease recognition across **eight public datasets** (four per crop),
always testing on a source the model has never seen (leave-one-dataset-out). We find that:

- **Models pick up the source.** Acquisition metadata alone identifies the source of a photo with a
  balanced accuracy of 0.91 (onion) and 0.99 (potato), even within one disease. Disease labels agree
  across sources once each source's style is removed.
- **No architecture closes the gap.** Fine-tuned CNNs and ViTs, frozen DINOv3 / BioCLIP-2 encoders,
  domain-generalisation methods and two architectures of our own all lose 23–41 macro-F1 points on
  unseen sources.
- **Treatment risk can be controlled without target labels.** The proposed method is a gate that gives
  treatment advice only when a risk score is below a threshold. The threshold is set by conformal
  risk control on predictions for training sources that were left out in turn (LOSO-CRC). At a 5%
  target, standard calibration gives 16–33% wrong treatments on unseen sources. The strict LOSO-CRC
  gate gives 1.7–4.5% in seven of eight model–crop settings and advises on 11–24% of the images.

## Repository contents

```
notebooks/
  onion/
    onion_full_pipeline_SILA-Net.ipynb   v1: data download, deduplication, splits, fine-tuned models, SILA-Net
    onion_v2_SERA.ipynb                  v2.1: frozen-encoder features, MIL/SERA heads, diagnosis, gate, XAI
    onion_v4_robustness.ipynb            v4: gate robustness, unseen-disease calibration, extra seeds, Holm
  potato/
    potato_v3_crosssource.ipynb          the same pipeline on the four potato sources
    potato_v4_robustness.ipynb           v4 additions for potato
analysis/
  analysis_local.py                      offline gate analyses (paper Sections 4.3-4.4) from the Kaggle outputs
  *.txt                                  notebook cells that analysis_local.py executes
paper_results/
  onion/  potato/
    REPORT.md                            summary report written by the notebook
    kaggle_tables/                       all result tables from the notebooks (see below)
    extra_analysis/                      outputs of analysis/analysis_local.py
paper/
  figures/make_fig4.py ... make_fig7.py  paper figures 4-7
  tables/make_tab3.py, make_tab4.py, make_tabA1.py   paper tables 3, 4 and A.1
```

### Key result tables (`paper_results/<crop>/kaggle_tables/`)

| File | Content |
|---|---|
| `manifest_dedup.csv` | one row per image: source, original class, harmonised label, photo group, MD5, and why it was dropped (empty = kept) |
| `split_membership.csv` | the fixed splits: train / val / test role of every image in each leave-one-dataset-out (`lodo_*`) and inner leave-one-source-out (`inner_*`) split |
| `splits_summary.csv` | size of every split and its unseen-class test images |
| `lodo_macro_f1_all.csv` | macro-F1 on each held-out source, for every model |
| `stats_proposed_vs_all.csv` | hierarchical-bootstrap comparisons with Holm-corrected p-values |
| `d1_*.csv`, `d2_*.csv`, `d3_*.csv` | shortcut diagnosis: metadata probes, feature probes before and after concept erasure, label-consistency index |
| `gate_summary.csv`, `gate_per_source.csv`, `gate_eps_sweep.csv`, `gate_all_runs.csv` | treatment-gate risk and acceptance for every model, score and calibration |
| `xai_*.csv` | attention deletion test and correct-versus-wrong attention statistics |
| `efficiency.csv` | parameters, GFLOPs and CPU time of the DINOv3 encoders |

## Datasets

The images are **not** redistributed here. Download them from their original sources:

| Crop | Source | Where to get it |
|---|---|---|
| Onion | COLD (India) | Hugging Face `Project-AgML/COLD_onion_leaf_disease_classification` (raw images only); Aishwarya & Reddy, *Data in Brief* 54 (2024) 110524 |
| Onion | TOM2024, onion subset (Burkina Faso) | Mendeley Data, linked from Appiah et al., *Data in Brief* 59 (2025) 111357 |
| Onion | Onion Disease Capstone Final | Roboflow Universe `school-0xa1n/onion-disease-capstone-final`, version 2 |
| Onion | OnionNet_disease_model 2 | Roboflow Universe `onionnet/onionnet_disease_model-2-hdkxc`, version 10 |
| Potato | PlantVillage (USA, laboratory) | Kaggle `abdallahalidev/plantvillage-dataset` (folder `color`) |
| Potato | PlantDoc (web) | Kaggle `nirmalsankalana/plantdoc-dataset` |
| Potato | PLD (Pakistan) | Kaggle `rizwan123456789/potato-disease-leaf-datasetpld` |
| Potato | Uncontrolled environment (Indonesia) | Kaggle `warcoder/potato-leaf-disease-dataset`; Shabrina et al., *Data in Brief* 52 (2024) 109955 |

## Reproducing the results

### 1. Kaggle notebooks (GPU)

All experiments ran in Kaggle notebooks on NVIDIA T4 GPUs with Internet enabled. Each notebook
begins with a "How to run" cell. Each later version attaches the output of the earlier one and
reuses everything already computed. Long runs are time-guarded: if a session ends, attach the
notebook's own output and run it again to resume.

**Onion**
1. `onion_full_pipeline_SILA-Net.ipynb`: attach the TOM2024 onion images as a Kaggle dataset named
   `tom2024-onion`, and add your own Roboflow key as the Kaggle secret `ROBOFLOW_API_KEY`. COLD and
   both Roboflow sets are downloaded automatically. The full plan takes about 22–26 T4 GPU-hours,
   spread over several sessions.
2. `onion_v2_SERA.ipynb`: attach the output of step 1.
3. `onion_v4_robustness.ipynb`: attach the outputs of steps 1 and 2.

**Potato**
1. `potato_v3_crosssource.ipynb`: attach the four Kaggle datasets listed above (about 8–9 GPU-hours).
2. `potato_v4_robustness.ipynb`: attach the output of step 1 and the same four datasets.

Public versions of the onion v2.1 and v4 notebooks and the potato notebook, with their outputs:
[v2-sera-full-run](https://www.kaggle.com/code/nafiul707/v2-sera-full-run),
[onion-v4-robustness](https://www.kaggle.com/code/nafiul707/onion-v4-robustness),
[potato-crosssource](https://www.kaggle.com/code/nafiul707/potato-crosssource).

### 2. Offline gate analyses (CPU)

Download a notebook's output folder (it contains `runs/`, `heads/` and `tables/`), then run

```bash
pip install -r requirements.txt
python analysis/analysis_local.py onion  <downloaded output folder> paper_results/onion/extra_analysis
python analysis/analysis_local.py potato <downloaded output folder> paper_results/potato/extra_analysis
```

### 3. Paper figures and tables (CPU, seconds)

Run these from the repository root. They read only `paper_results/`:

```bash
python paper/figures/make_fig4.py     # shortcut evidence
python paper/figures/make_fig5.py     # accuracy on unseen sources
python paper/figures/make_fig6.py     # risk versus acceptance
python paper/tables/make_tab3.py      # gate per held-out source
python paper/tables/make_tab4.py      # gate robustness
python paper/tables/make_tabA1.py     # all LODO results
```

`make_fig7.py` (explanation examples) also needs the SERA head outputs and the example images. These
come from the notebook outputs and the original datasets, and are not included here.

Tested with Python 3.12, numpy 2.3, pandas 3.0, matplotlib 3.11, Pillow 12.3, torch 2.14 and tqdm 4.70.

## Licence

- **Code** (notebooks and scripts): MIT licence, see `LICENSE`.
- **Result tables** in `paper_results/`: CC BY 4.0.
- **Datasets**: each keeps its original licence; see the sources above.

## Citation

If you use this code or the splits, please cite the paper (reference to be added after publication)
and the original datasets.
