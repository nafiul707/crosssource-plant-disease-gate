# Potato cross-source diagnosis (SERA pipeline): results report

Generated 2026-10-12 15:26 | full run | classes: bacterial, early_blight, fungi_other, healthy, late_blight, nematode, pest, viral | main encoder DINOv3-B | proposed SERA@DINOv3-B | head runs 877 | elapsed 4.39 h

Figures: d1_acquisition_by_source.png, d3_centroid_similarity.png, label_harmonization_grid.png, rq3_gate.png, rq3b_eps_sweep.png, xai_sera_attention.png

## Source datasets (before any cleaning)

| dataset | source_class | images | folders |
|---|---|---|---|
| plantvillage | Potato___Early_blight | 1000 | 2 |
| plantvillage | Potato___Late_blight | 1000 | 2 |
| plantvillage | Potato___healthy | 152 | 2 |
| plantdoc | Potato_leaf_early_blight | 171 | 2 |
| plantdoc | Potato_leaf_late_blight | 208 | 2 |
| pld_pakistan | Early_Blight | 1628 | 3 |
| pld_pakistan | Healthy | 1020 | 3 |
| pld_pakistan | Late_Blight | 1424 | 3 |
| uncontrolled_indonesia | Bacteria | 569 | 1 |
| uncontrolled_indonesia | Fungi | 748 | 1 |
| uncontrolled_indonesia | Healthy | 201 | 1 |
| uncontrolled_indonesia | Nematode | 68 | 1 |
| uncontrolled_indonesia | Pest | 611 | 1 |
| uncontrolled_indonesia | Phytopthora | 347 | 1 |
| uncontrolled_indonesia | Virus | 532 | 1 |

Sources: `plantvillage` = abdallahalidev/plantvillage-dataset (USA (lab)); `plantdoc` = nirmalsankalana/plantdoc-dataset (web (field photos)); `pld_pakistan` = rizwan123456789/potato-disease-leaf-datasetpld (Pakistan); `uncontrolled_indonesia` = warcoder/potato-leaf-disease-dataset (Indonesia)

## Deduplication

- exact duplicates: 7 sets with conflicting labels (all copies dropped), 65 extra copies dropped
  - plantdoc: 2 images dropped
  - pld_pakistan: 16 images dropped
  - uncontrolled_indonesia: 61 images dropped
- near-duplicate pairs (Hamming <= 4): 148; clusters with >1 image: 122
- near-duplicate clusters with conflicting labels: 34 (86 images dropped)
- clusters spanning datasets: 1 (1 images dropped from the minority dataset)
  - plantvillage+pld_pakistan: 3 clusters
- photo groups merged because of near-duplicates: 94

## Harmonized class counts (after dedup)

| label_name | plantvillage | plantdoc | pld_pakistan | uncontrolled_indonesia | total | n_sources |
|---|---|---|---|---|---|---|
| bacterial | 0 | 0 | 0 | 569 | 569 | 1 |
| early_blight | 1000 | 168 | 1593 | 0 | 2761 | 3 |
| fungi_other | 0 | 0 | 0 | 740 | 740 | 1 |
| healthy | 152 | 0 | 986 | 199 | 1337 | 3 |
| late_blight | 998 | 205 | 1396 | 309 | 2908 | 4 |
| nematode | 0 | 0 | 0 | 67 | 67 | 1 |
| pest | 0 | 0 | 0 | 601 | 601 | 1 |
| viral | 0 | 0 | 0 | 530 | 530 | 1 |

Dropped images by reason: {'kept': 9513, 'near_dup_label_conflict': 86, 'exact_dup_extra_copy': 65, 'exact_dup_label_conflict': 14, 'near_dup_cross_dataset': 1}

## Splits (all leakage checks passed)

| protocol | split | train | val | test | test_id | test_unseen_class | train_classes | shared_test_classes |
|---|---|---|---|---|---|---|---|---|
| lodo | plantvillage | 6314 | 1049 | 2150 | 2150 | 0 | 8 | early_blight, healthy, late_blight |
| lodo | plantdoc | 7836 | 1304 | 373 | 373 | 0 | 8 | early_blight, late_blight |
| lodo | pld_pakistan | 4747 | 791 | 3975 | 3975 | 0 | 8 | early_blight, healthy, late_blight |
| lodo | uncontrolled_indonesia | 5572 | 926 | 3015 | 508 | 2507 | 3 | healthy, late_blight |
| inner | plantvillage|plantdoc | 5992 | 998 | 373 | 373 | 0 | 8 | early_blight, late_blight |
| inner | plantvillage|pld_pakistan | 2904 | 484 | 3975 | 3975 | 0 | 8 | early_blight, healthy, late_blight |
| inner | plantvillage|uncontrolled_indonesia | 3727 | 621 | 3015 | 508 | 2507 | 3 | healthy, late_blight |
| inner | plantdoc|plantvillage | 5992 | 998 | 2150 | 2150 | 0 | 8 | early_blight, healthy, late_blight |
| inner | plantdoc|pld_pakistan | 4426 | 739 | 3975 | 3975 | 0 | 8 | early_blight, healthy, late_blight |
| inner | plantdoc|uncontrolled_indonesia | 5255 | 870 | 3015 | 508 | 2507 | 3 | healthy, late_blight |
| inner | pld_pakistan|plantvillage | 2904 | 484 | 2150 | 2150 | 0 | 8 | early_blight, healthy, late_blight |
| inner | pld_pakistan|plantdoc | 4426 | 739 | 373 | 373 | 0 | 8 | early_blight, late_blight |
| inner | pld_pakistan|uncontrolled_indonesia | 2161 | 362 | 3015 | 508 | 2507 | 3 | healthy, late_blight |
| inner | uncontrolled_indonesia|plantvillage | 3727 | 621 | 2150 | 2150 | 0 | 3 | early_blight, healthy, late_blight |
| inner | uncontrolled_indonesia|plantdoc | 5255 | 870 | 373 | 373 | 0 | 3 | early_blight, late_blight |
| inner | uncontrolled_indonesia|pld_pakistan | 2161 | 362 | 3975 | 3975 | 0 | 3 | early_blight, healthy, late_blight |
| cv | fold0 | 6520 | 1087 | 1906 | 1906 | 0 | 8 | bacterial, early_blight, fungi_other, healthy, late_blight, nematode, pest, viral |
| cv | fold1 | 6528 | 1086 | 1899 | 1899 | 0 | 8 | bacterial, early_blight, fungi_other, healthy, late_blight, nematode, pest, viral |
| cv | fold2 | 6526 | 1086 | 1901 | 1901 | 0 | 8 | bacterial, early_blight, fungi_other, healthy, late_blight, nematode, pest, viral |
| cv | fold3 | 6522 | 1087 | 1904 | 1904 | 0 | 8 | bacterial, early_blight, fungi_other, healthy, late_blight, nematode, pest, viral |
| cv | fold4 | 6525 | 1085 | 1903 | 1903 | 0 | 8 | bacterial, early_blight, fungi_other, healthy, late_blight, nematode, pest, viral |

## D1 - acquisition metadata by source (median)

| dataset | native_long | native_short | file_kb | jpeg_qstep | sharpness | saturation | green_frac |
|---|---|---|---|---|---|---|---|
| plantdoc | 437.00 | 379.00 | 73.79 | 11.50 | -5.35 | 0.43 | 0.74 |
| plantvillage | 256.00 | 256.00 | 18.22 | 29.03 | -4.61 | 0.26 | 0.44 |
| pld_pakistan | 256.00 | 256.00 | 9.20 | 29.03 | -6.71 | 0.39 | 0.62 |
| uncontrolled_indonesia | 1500.00 | 1500.00 | 231.49 | 29.03 | -5.19 | 0.35 | 0.71 |

## D1 - what metadata alone can predict (balanced accuracy, grouped CV)

| target | subset | balanced_acc | chance | n | above_chance |
|---|---|---|---|---|---|
| source | all images | 0.993 | 0.250 | 9513 | 0.743 |
| source | within early_blight | 0.994 | 0.333 | 2761 | 0.660 |
| source | within healthy | 0.990 | 0.333 | 1337 | 0.656 |
| source | within late_blight | 0.996 | 0.250 | 2908 | 0.746 |
| disease | within source plantvillage | 0.731 | 0.333 | 2150 | 0.398 |
| disease | within source plantdoc | 0.646 | 0.500 | 373 | 0.146 |
| disease | within source pld_pakistan | 0.681 | 0.333 | 3975 | 0.348 |
| disease | within source uncontrolled_indonesia | 0.388 | 0.143 | 3015 | 0.245 |

## D2 - source / disease identifiability from DINOv3-B global features (balanced accuracy, grouped CV)

| target | subset | probe | class-cond. LEACE | global LEACE | raw | chance |
|---|---|---|---|---|---|---|
| disease | all images | linear | 0.862 | 0.850 | 0.867 | 0.125 |
| source | all images | MLP | 0.981 | 0.976 | 0.994 | 0.250 |
| source | all images | linear | 0.520 | 0.274 | 0.993 | 0.250 |
| source | within early_blight | MLP | 0.961 | 0.962 | 1.000 | 0.333 |
| source | within early_blight | linear | 0.916 | 0.902 | 0.999 | 0.333 |
| source | within healthy | MLP | 0.993 | 0.993 | 1.000 | 0.333 |
| source | within healthy | linear | 0.981 | 0.992 | 0.997 | 0.333 |
| source | within late_blight | MLP | 0.955 | 0.946 | 0.991 | 0.250 |
| source | within late_blight | linear | 0.879 | 0.887 | 0.986 | 0.250 |

## D3 - label-consistency index per class (mean over source pairs; > 0 = same name, same look)

| cls | raw | source-centred | pairs | verdict |
|---|---|---|---|---|
| early_blight | 0.120 | 0.665 | 6 | consistent |
| healthy | 0.331 | 0.374 | 6 | consistent |
| late_blight | -0.059 | 0.008 | 12 | style-shifted (consistent after centring) |

## D3 - nearest-centroid transfer between sources (shared classes only)

| train_src | test_src | raw | source-centred |
|---|---|---|---|
| plantdoc | plantvillage | 0.836 | 0.833 |
| plantdoc | pld_pakistan | 0.582 | 0.798 |
| plantvillage | plantdoc | 0.588 | 0.639 |
| plantvillage | pld_pakistan | 0.645 | 0.716 |
| plantvillage | uncontrolled_indonesia | 0.460 | 0.574 |
| pld_pakistan | plantdoc | 0.631 | 0.636 |
| pld_pakistan | plantvillage | 0.483 | 0.538 |
| pld_pakistan | uncontrolled_indonesia | 0.444 | 0.553 |
| uncontrolled_indonesia | plantvillage | 0.461 | 0.444 |
| uncontrolled_indonesia | pld_pakistan | 0.499 | 0.572 |

## RQ2 - LODO macro-F1 on held-out ID classes, all models (mean ± sd over seeds)

| model | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia | mean | seeds |
|---|---|---|---|---|---|---|
| SERA@BioCLIP-2 | 0.482 ± 0.022 | 0.938 ± 0.006 | 0.878 ± 0.043 | 0.836 ± 0.122 | 0.784 | 10 |
| LP-global@BioCLIP-2 | 0.373 ± 0.012 | 0.881 ± 0.011 | 0.895 ± 0.007 | 0.845 ± 0.021 | 0.749 | 10 |
| ViTS | 0.328 ± 0.006 | 0.917 ± 0.038 | 0.85 ± 0.048 | 0.796 ± 0.044 | 0.723 | 3 |
| SERA@DINOv3-B | 0.505 ± 0.029 | 0.736 ± 0.025 | 0.808 ± 0.065 | 0.637 ± 0.066 | 0.672 | 10 |
| ConvNeXtT | 0.342 ± 0.011 | 0.834 ± 0.02 | 0.847 ± 0.032 | 0.614 ± 0.042 | 0.659 | 3 |
| SERA@DINOv3-S | 0.518 ± 0.08 | 0.715 ± 0.025 | 0.715 ± 0.103 | 0.688 ± 0.05 | 0.659 | 10 |
| MIL+GE@DINOv3-B | 0.469 ± 0.062 | 0.751 ± 0.031 | 0.763 ± 0.069 | 0.641 ± 0.08 | 0.656 | 10 |
| MIL@DINOv3-B | 0.416 ± 0.013 | 0.866 ± 0.017 | 0.793 ± 0.044 | 0.517 ± 0.067 | 0.648 | 10 |
| DG:SWA | 0.324 ± 0.006 | 0.873 ± 0.016 | 0.722 ± 0.097 | 0.606 ± 0.034 | 0.631 | 3 |
| EfficientNetB0 | 0.318 ± 0.003 | 0.891 ± 0.008 | 0.731 ± 0.09 | 0.558 ± 0.022 | 0.624 | 3 |
| DG:MixStyle | 0.331 ± 0.008 | 0.82 ± 0.041 | 0.806 ± 0.019 | 0.528 ± 0.026 | 0.621 | 3 |
| SERA-5@DINOv3-S | 0.447 ± 0.023 | 0.606 ± 0.016 | 0.661 ± 0.041 | 0.584 ± 0.029 | 0.575 | 10 |
| LP-global+FMM@DINOv3-B | 0.518 ± 0.007 | 0.475 ± 0.012 | 0.663 ± 0.007 | 0.546 ± 0.024 | 0.551 | 10 |
| LP-mean@DINOv3-B | 0.344 ± 0.009 | 0.684 ± 0.013 | 0.762 ± 0.013 | 0.361 ± 0.027 | 0.538 | 10 |
| LP-global@DINOv3-B | 0.332 ± 0.009 | 0.648 ± 0.018 | 0.731 ± 0.007 | 0.434 ± 0.032 | 0.537 | 10 |
| LP-global@DINOv3-S | 0.285 ± 0.007 | 0.61 ± 0.009 | 0.723 ± 0.012 | 0.514 ± 0.024 | 0.533 | 10 |
| LP-global+CCE@DINOv3-B | 0.396 ± 0.006 | 0.408 ± 0.013 | 0.725 ± 0.006 | 0.456 ± 0.009 | 0.496 | 10 |

## RQ2 - SERA ablation on DINOv3-B (LODO macro-F1)

| model | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia | mean | seeds |
|---|---|---|---|---|---|---|
| LP-global@DINOv3-B | 0.332 ± 0.009 | 0.648 ± 0.018 | 0.731 ± 0.007 | 0.434 ± 0.032 | 0.537 | 10 |
| LP-global+FMM@DINOv3-B | 0.518 ± 0.007 | 0.475 ± 0.012 | 0.663 ± 0.007 | 0.546 ± 0.024 | 0.551 | 10 |
| LP-mean@DINOv3-B | 0.344 ± 0.009 | 0.684 ± 0.013 | 0.762 ± 0.013 | 0.361 ± 0.027 | 0.538 | 10 |
| MIL@DINOv3-B | 0.416 ± 0.013 | 0.866 ± 0.017 | 0.793 ± 0.044 | 0.517 ± 0.067 | 0.648 | 10 |
| LP-global+CCE@DINOv3-B | 0.396 ± 0.006 | 0.408 ± 0.013 | 0.725 ± 0.006 | 0.456 ± 0.009 | 0.496 | 10 |
| MIL+GE@DINOv3-B | 0.469 ± 0.062 | 0.751 ± 0.031 | 0.763 ± 0.069 | 0.641 ± 0.08 | 0.656 | 10 |
| SERA@DINOv3-B | 0.505 ± 0.029 | 0.736 ± 0.025 | 0.808 ± 0.065 | 0.637 ± 0.066 | 0.672 | 10 |

## RQ2 - does SERA help every encoder? (LODO macro-F1)

| model | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia | mean | seeds |
|---|---|---|---|---|---|---|
| SERA@BioCLIP-2 | 0.482 ± 0.022 | 0.938 ± 0.006 | 0.878 ± 0.043 | 0.836 ± 0.122 | 0.784 | 10 |
| LP-global@BioCLIP-2 | 0.373 ± 0.012 | 0.881 ± 0.011 | 0.895 ± 0.007 | 0.845 ± 0.021 | 0.749 | 10 |
| SERA@DINOv3-B | 0.505 ± 0.029 | 0.736 ± 0.025 | 0.808 ± 0.065 | 0.637 ± 0.066 | 0.672 | 10 |
| SERA@DINOv3-S | 0.518 ± 0.08 | 0.715 ± 0.025 | 0.715 ± 0.103 | 0.688 ± 0.05 | 0.659 | 10 |
| SERA-5@DINOv3-S | 0.447 ± 0.023 | 0.606 ± 0.016 | 0.661 ± 0.041 | 0.584 ± 0.029 | 0.575 | 10 |
| LP-global@DINOv3-B | 0.332 ± 0.009 | 0.648 ± 0.018 | 0.731 ± 0.007 | 0.434 ± 0.032 | 0.537 | 10 |
| LP-global@DINOv3-S | 0.285 ± 0.007 | 0.61 ± 0.009 | 0.723 ± 0.012 | 0.514 ± 0.024 | 0.533 | 10 |

## RQ1 - in-domain minus LODO macro-F1 (percentage points)

| model | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia | mean |
|---|---|---|---|---|---|
| SERA@DINOv3-B | 24.8 | 24.2 | 17.5 | 24.8 | 22.8 |
| LP-global@DINOv3-B | 39.5 | 31.5 | 23.4 | 34.1 | 32.1 |

## Statistics - SERA@DINOv3-B minus each model (hierarchical bootstrap over photo groups and seeds)

| baseline | diff_macro_f1 | ci_low | ci_high | p_bootstrap | wilcoxon_p | paired_runs | held_out_sets | p_bootstrap_holm | ci_excludes_0 | significant |
|---|---|---|---|---|---|---|---|---|---|---|
| SERA@BioCLIP-2 | -0.1121 | -0.1413 | -0.0812 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |
| LP-global@BioCLIP-2 | -0.0770 | -0.1002 | -0.0526 | 0.0000 | 0.0010 | 40 | 4 | 0.0000 | True | True |
| ViTS | -0.0513 | -0.0816 | -0.0224 | 0.0000 | 0.3804 | 12 | 4 | 0.0000 | True | True |
| ConvNeXtT | 0.0120 | -0.0152 | 0.0397 | 0.3840 | 0.5693 | 12 | 4 | 0.7680 | False | False |
| SERA@DINOv3-S | 0.0126 | -0.0158 | 0.0422 | 0.4520 | 0.6948 | 40 | 4 | 0.7680 | False | False |
| MIL+GE@DINOv3-B | 0.0155 | -0.0111 | 0.0413 | 0.2080 | 0.0408 | 40 | 4 | 0.6240 | False | False |
| MIL@DINOv3-B | 0.0236 | 0.0023 | 0.0464 | 0.0320 | 0.2163 | 40 | 4 | 0.1280 | True | False |
| DG:SWA | 0.0403 | 0.0060 | 0.0780 | 0.0220 | 0.1514 | 12 | 4 | 0.1100 | True | False |
| EfficientNetB0 | 0.0470 | 0.0136 | 0.0842 | 0.0020 | 0.1763 | 12 | 4 | 0.0140 | True | True |
| DG:MixStyle | 0.0503 | 0.0218 | 0.0769 | 0.0020 | 0.1294 | 12 | 4 | 0.0140 | True | True |
| SERA-5@DINOv3-S | 0.0970 | 0.0756 | 0.1186 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |
| LP-global+FMM@DINOv3-B | 0.1209 | 0.0970 | 0.1459 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |
| LP-mean@DINOv3-B | 0.1337 | 0.1131 | 0.1570 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |
| LP-global@DINOv3-B | 0.1349 | 0.1112 | 0.1607 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |
| LP-global@DINOv3-S | 0.1384 | 0.1140 | 0.1628 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |
| LP-global+CCE@DINOv3-B | 0.1750 | 0.1510 | 0.1992 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |

## Per-class F1 on held-out sets (focus models, mean over seeds)

| model | held_out | F1_early_blight | F1_healthy | F1_late_blight |
|---|---|---|---|---|
| LP-global+CCE@DINOv3-B | plantdoc | 0.165 | nan | 0.627 |
| LP-global+CCE@DINOv3-B | plantvillage | 0.604 | 0.311 | 0.309 |
| LP-global+CCE@DINOv3-B | pld_pakistan | 0.818 | 0.696 | 0.662 |
| LP-global+CCE@DINOv3-B | uncontrolled_indonesia | nan | 0.602 | 0.311 |
| LP-global@DINOv3-B | plantdoc | 0.046 | nan | 0.618 |
| LP-global@DINOv3-B | plantvillage | 0.836 | 0.441 | 0.668 |
| LP-global@DINOv3-B | pld_pakistan | 0.815 | 0.751 | 0.629 |
| LP-global@DINOv3-B | uncontrolled_indonesia | nan | 0.373 | 0.496 |
| MIL@DINOv3-B | plantdoc | 0.134 | nan | 0.698 |
| MIL@DINOv3-B | plantvillage | 0.877 | 0.857 | 0.865 |
| MIL@DINOv3-B | pld_pakistan | 0.876 | 0.741 | 0.762 |
| MIL@DINOv3-B | uncontrolled_indonesia | nan | 0.336 | 0.697 |
| SERA@DINOv3-B | plantdoc | 0.276 | nan | 0.733 |
| SERA@DINOv3-B | plantvillage | 0.655 | 0.743 | 0.812 |
| SERA@DINOv3-B | pld_pakistan | 0.861 | 0.769 | 0.794 |
| SERA@DINOv3-B | uncontrolled_indonesia | nan | 0.598 | 0.676 |
| ViTS | plantdoc | 0.000 | nan | 0.656 |
| ViTS | plantvillage | 0.864 | 0.992 | 0.896 |
| ViTS | pld_pakistan | 0.780 | 0.919 | 0.851 |
| ViTS | uncontrolled_indonesia | nan | 0.733 | 0.860 |

## RQ3 - gate summary for SERA@DINOv3-B (target risk eps = 5%; mean over held-out sets and seeds)

| score | calibration | accept | accept_id | risk | violation_rate | wrong_among_issued | withheld_unseen | runs |
|---|---|---|---|---|---|---|---|---|
| - | no gate | 1.000 | 1.000 | 0.368 | 1.000 | 0.368 | 0.000 | 12 |
| MSP | LOSO-CRC | 0.264 | 0.267 | 0.053 | 0.417 | 0.209 | 0.864 | 12 |
| MSP | LOSO-CRC-worst | 0.164 | 0.167 | 0.031 | 0.250 | 0.189 | 0.947 | 12 |
| MSP | val-CRC | 0.858 | 0.858 | 0.318 | 1.000 | 0.343 | 0.000 | 12 |
| Remedy | LOSO-CRC | 0.288 | 0.292 | 0.053 | 0.417 | 0.200 | 0.864 | 12 |
| Remedy | LOSO-CRC-worst | 0.179 | 0.182 | 0.031 | 0.250 | 0.180 | 0.947 | 12 |
| Remedy | val-CRC | 0.898 | 0.898 | 0.320 | 1.000 | 0.338 | 0.000 | 12 |
| Remedy+kNN | LOSO-CRC | 0.235 | 0.248 | 0.052 | 0.417 | 0.250 | 0.920 | 12 |
| Remedy+kNN | LOSO-CRC-worst | 0.170 | 0.182 | 0.035 | 0.333 | 0.225 | 0.949 | 12 |
| Remedy+kNN | val-CRC | 0.675 | 0.675 | 0.275 | 0.833 | 0.340 | 0.000 | 12 |
| Remedy-set | CP-remedy(val) | 0.705 | 0.707 | 0.162 | 1.000 | 0.279 | 0.713 | 12 |
| kNN | LOSO-CRC | 0.203 | 0.215 | 0.057 | 0.500 | 0.322 | 0.924 | 12 |
| kNN | LOSO-CRC-worst | 0.107 | 0.114 | 0.026 | 0.167 | 0.267 | 0.969 | 12 |
| kNN | val-CRC | 0.431 | 0.431 | 0.228 | 0.583 | 0.357 | 0.000 | 12 |

## RQ3 - gate summary, all focus models

| model | score | calibration | accept | accept_id | risk | violation_rate | wrong_among_issued | withheld_unseen | runs |
|---|---|---|---|---|---|---|---|---|---|
| ConvNeXtT | - | no gate | 1.000 | 1.000 | 0.371 | 1.000 | 0.371 | 0.000 | 12 |
| ConvNeXtT | MSP | val-CRC | 0.962 | 0.962 | 0.359 | 1.000 | 0.363 | 0.000 | 12 |
| ConvNeXtT | Remedy | val-CRC | 0.976 | 0.976 | 0.360 | 1.000 | 0.363 | 0.000 | 12 |
| ConvNeXtT | Remedy+kNN | val-CRC | 0.964 | 0.964 | 0.357 | 1.000 | 0.360 | 0.000 | 12 |
| ConvNeXtT | Remedy-set | CP-remedy(val) | 0.530 | 0.547 | 0.078 | 0.750 | 0.220 | 0.933 | 12 |
| ConvNeXtT | kNN | val-CRC | 0.954 | 0.954 | 0.355 | 0.917 | 0.359 | 0.000 | 12 |
| EfficientNetB0 | - | no gate | 1.000 | 1.000 | 0.400 | 1.000 | 0.400 | 0.000 | 12 |
| EfficientNetB0 | MSP | val-CRC | 0.889 | 0.889 | 0.365 | 0.833 | 0.375 | 0.000 | 12 |
| EfficientNetB0 | Remedy | val-CRC | 0.913 | 0.913 | 0.367 | 0.917 | 0.374 | 0.000 | 12 |
| EfficientNetB0 | Remedy+kNN | val-CRC | 0.904 | 0.904 | 0.368 | 0.917 | 0.376 | 0.000 | 12 |
| EfficientNetB0 | Remedy-set | CP-remedy(val) | 0.548 | 0.576 | 0.099 | 0.917 | 0.301 | 0.893 | 12 |
| EfficientNetB0 | kNN | val-CRC | 0.908 | 0.908 | 0.379 | 1.000 | 0.390 | 0.000 | 12 |
| LP-global+CCE@DINOv3-B | - | no gate | 1.000 | 1.000 | 0.507 | 1.000 | 0.507 | 0.000 | 40 |
| LP-global+CCE@DINOv3-B | MSP | val-CRC | 0.753 | 0.753 | 0.377 | 1.000 | 0.457 | 0.000 | 40 |
| LP-global+CCE@DINOv3-B | Remedy | val-CRC | 0.792 | 0.792 | 0.380 | 1.000 | 0.440 | 0.000 | 40 |
| LP-global+CCE@DINOv3-B | Remedy+kNN | val-CRC | 0.464 | 0.464 | 0.276 | 0.750 | 0.468 | 0.000 | 40 |
| LP-global+CCE@DINOv3-B | Remedy-set | CP-remedy(val) | 0.780 | 0.756 | 0.342 | 1.000 | 0.464 | 0.479 | 40 |
| LP-global+CCE@DINOv3-B | kNN | val-CRC | 0.284 | 0.284 | 0.202 | 0.325 | 0.446 | 0.000 | 40 |
| LP-global@DINOv3-B | - | no gate | 1.000 | 1.000 | 0.463 | 1.000 | 0.463 | 0.000 | 12 |
| LP-global@DINOv3-B | MSP | LOSO-CRC | 0.162 | 0.139 | 0.043 | 0.250 | 0.284 | 0.800 | 12 |
| LP-global@DINOv3-B | MSP | LOSO-CRC-worst | 0.117 | 0.097 | 0.031 | 0.167 | 0.268 | 0.846 | 12 |
| LP-global@DINOv3-B | MSP | val-CRC | 0.830 | 0.830 | 0.364 | 1.000 | 0.412 | 0.000 | 12 |
| LP-global@DINOv3-B | Remedy | LOSO-CRC | 0.180 | 0.157 | 0.043 | 0.250 | 0.264 | 0.800 | 12 |
| LP-global@DINOv3-B | Remedy | LOSO-CRC-worst | 0.132 | 0.112 | 0.030 | 0.167 | 0.239 | 0.846 | 12 |
| LP-global@DINOv3-B | Remedy | val-CRC | 0.839 | 0.839 | 0.363 | 1.000 | 0.407 | 0.000 | 12 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.222 | 0.214 | 0.152 | 0.500 | 0.378 | 0.367 | 12 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.114 | 0.104 | 0.074 | 0.500 | 0.324 | 0.706 | 12 |
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.342 | 0.342 | 0.229 | 0.500 | 0.453 | 0.000 | 12 |
| LP-global@DINOv3-B | Remedy-set | CP-remedy(val) | 0.766 | 0.748 | 0.284 | 1.000 | 0.408 | 0.512 | 12 |
| LP-global@DINOv3-B | kNN | LOSO-CRC | 0.288 | 0.304 | 0.213 | 0.500 | 0.362 | 0.172 | 12 |
| LP-global@DINOv3-B | kNN | LOSO-CRC-worst | 0.240 | 0.263 | 0.182 | 0.500 | 0.371 | 0.305 | 12 |
| LP-global@DINOv3-B | kNN | val-CRC | 0.267 | 0.267 | 0.200 | 0.333 | 0.402 | 0.000 | 12 |
| MIL@DINOv3-B | - | no gate | 1.000 | 1.000 | 0.365 | 1.000 | 0.365 | 0.000 | 40 |
| MIL@DINOv3-B | MSP | val-CRC | 0.941 | 0.941 | 0.338 | 1.000 | 0.348 | 0.000 | 40 |
| MIL@DINOv3-B | Remedy | val-CRC | 0.945 | 0.945 | 0.338 | 1.000 | 0.347 | 0.000 | 40 |
| MIL@DINOv3-B | Remedy+kNN | val-CRC | 0.583 | 0.583 | 0.266 | 0.800 | 0.363 | 0.000 | 40 |
| MIL@DINOv3-B | Remedy-set | CP-remedy(val) | 0.697 | 0.688 | 0.151 | 1.000 | 0.279 | 0.782 | 40 |
| MIL@DINOv3-B | kNN | val-CRC | 0.384 | 0.384 | 0.228 | 0.550 | 0.413 | 0.000 | 40 |
| SERA@DINOv3-B | - | no gate | 1.000 | 1.000 | 0.368 | 1.000 | 0.368 | 0.000 | 12 |
| SERA@DINOv3-B | MSP | LOSO-CRC | 0.264 | 0.267 | 0.053 | 0.417 | 0.209 | 0.864 | 12 |
| SERA@DINOv3-B | MSP | LOSO-CRC-worst | 0.164 | 0.167 | 0.031 | 0.250 | 0.189 | 0.947 | 12 |
| SERA@DINOv3-B | MSP | val-CRC | 0.858 | 0.858 | 0.318 | 1.000 | 0.343 | 0.000 | 12 |
| SERA@DINOv3-B | Remedy | LOSO-CRC | 0.288 | 0.292 | 0.053 | 0.417 | 0.200 | 0.864 | 12 |
| SERA@DINOv3-B | Remedy | LOSO-CRC-worst | 0.179 | 0.182 | 0.031 | 0.250 | 0.180 | 0.947 | 12 |
| SERA@DINOv3-B | Remedy | val-CRC | 0.898 | 0.898 | 0.320 | 1.000 | 0.338 | 0.000 | 12 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.235 | 0.248 | 0.052 | 0.417 | 0.250 | 0.920 | 12 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.170 | 0.182 | 0.035 | 0.333 | 0.225 | 0.949 | 12 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.675 | 0.675 | 0.275 | 0.833 | 0.340 | 0.000 | 12 |
| SERA@DINOv3-B | Remedy-set | CP-remedy(val) | 0.705 | 0.707 | 0.162 | 1.000 | 0.279 | 0.713 | 12 |
| SERA@DINOv3-B | kNN | LOSO-CRC | 0.203 | 0.215 | 0.057 | 0.500 | 0.322 | 0.924 | 12 |
| SERA@DINOv3-B | kNN | LOSO-CRC-worst | 0.107 | 0.114 | 0.026 | 0.167 | 0.267 | 0.969 | 12 |
| SERA@DINOv3-B | kNN | val-CRC | 0.431 | 0.431 | 0.228 | 0.583 | 0.357 | 0.000 | 12 |
| SERA@DINOv3-S | - | no gate | 1.000 | 1.000 | 0.401 | 1.000 | 0.401 | 0.000 | 12 |
| SERA@DINOv3-S | MSP | LOSO-CRC | 0.228 | 0.222 | 0.039 | 0.333 | 0.228 | 0.949 | 12 |
| SERA@DINOv3-S | MSP | LOSO-CRC-worst | 0.158 | 0.156 | 0.026 | 0.250 | 0.223 | 0.978 | 12 |
| SERA@DINOv3-S | MSP | val-CRC | 0.861 | 0.861 | 0.333 | 1.000 | 0.363 | 0.000 | 12 |
| SERA@DINOv3-S | Remedy | LOSO-CRC | 0.259 | 0.254 | 0.040 | 0.333 | 0.223 | 0.949 | 12 |
| SERA@DINOv3-S | Remedy | LOSO-CRC-worst | 0.184 | 0.182 | 0.026 | 0.250 | 0.216 | 0.978 | 12 |
| SERA@DINOv3-S | Remedy | val-CRC | 0.882 | 0.882 | 0.334 | 1.000 | 0.359 | 0.000 | 12 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.183 | 0.183 | 0.052 | 0.417 | 0.299 | 0.938 | 12 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.105 | 0.104 | 0.025 | 0.167 | 0.257 | 0.978 | 12 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.646 | 0.646 | 0.284 | 0.833 | 0.382 | 0.000 | 12 |
| SERA@DINOv3-S | Remedy-set | CP-remedy(val) | 0.710 | 0.697 | 0.194 | 1.000 | 0.325 | 0.766 | 12 |
| SERA@DINOv3-S | kNN | LOSO-CRC | 0.152 | 0.152 | 0.057 | 0.583 | 0.396 | 0.946 | 12 |
| SERA@DINOv3-S | kNN | LOSO-CRC-worst | 0.093 | 0.093 | 0.030 | 0.250 | 0.357 | 0.989 | 12 |
| SERA@DINOv3-S | kNN | val-CRC | 0.405 | 0.405 | 0.235 | 0.750 | 0.454 | 0.000 | 12 |
| ViTS | - | no gate | 1.000 | 1.000 | 0.339 | 1.000 | 0.339 | 0.000 | 12 |
| ViTS | MSP | LOSO-CRC | 0.313 | 0.333 | 0.081 | 0.333 | 0.200 | 0.633 | 12 |
| ViTS | MSP | LOSO-CRC-worst | 0.162 | 0.184 | 0.045 | 0.250 | 0.161 | 0.746 | 12 |
| ViTS | MSP | val-CRC | 0.935 | 0.935 | 0.322 | 0.833 | 0.327 | 0.000 | 12 |
| ViTS | Remedy | LOSO-CRC | 0.309 | 0.329 | 0.082 | 0.333 | 0.202 | 0.633 | 12 |
| ViTS | Remedy | LOSO-CRC-worst | 0.161 | 0.184 | 0.048 | 0.250 | 0.166 | 0.746 | 12 |
| ViTS | Remedy | val-CRC | 0.963 | 0.963 | 0.324 | 1.000 | 0.327 | 0.000 | 12 |
| ViTS | Remedy+kNN | LOSO-CRC | 0.367 | 0.402 | 0.070 | 0.417 | 0.182 | 0.737 | 12 |
| ViTS | Remedy+kNN | LOSO-CRC-worst | 0.219 | 0.248 | 0.031 | 0.167 | 0.139 | 0.848 | 12 |
| ViTS | Remedy+kNN | val-CRC | 0.968 | 0.968 | 0.327 | 1.000 | 0.330 | 0.000 | 12 |
| ViTS | Remedy-set | CP-remedy(val) | 0.519 | 0.534 | 0.060 | 0.500 | 0.183 | 0.902 | 12 |
| ViTS | kNN | LOSO-CRC | 0.392 | 0.402 | 0.049 | 0.417 | 0.161 | 0.926 | 12 |
| ViTS | kNN | LOSO-CRC-worst | 0.268 | 0.267 | 0.020 | 0.167 | 0.119 | 0.977 | 12 |
| ViTS | kNN | val-CRC | 0.953 | 0.953 | 0.327 | 1.000 | 0.331 | 0.000 | 12 |

## RQ3 - ranking quality of the risk scores (lower AURC / wrong-at-matched-acceptance is better)

| model | score | aurc | auroc_unseen | wrong_among_issued@30% | wrong_among_issued@50% |
|---|---|---|---|---|---|
| ConvNeXtT | MSP | 0.261 | 0.638 | 0.212 | 0.260 |
| ConvNeXtT | Remedy | 0.253 | 0.638 | 0.209 | 0.255 |
| ConvNeXtT | Remedy+kNN | 0.248 | 0.659 | 0.198 | 0.247 |
| ConvNeXtT | kNN | 0.247 | 0.664 | 0.194 | 0.246 |
| EfficientNetB0 | MSP | 0.308 | 0.589 | 0.275 | 0.315 |
| EfficientNetB0 | Remedy | 0.302 | 0.589 | 0.270 | 0.308 |
| EfficientNetB0 | Remedy+kNN | 0.306 | 0.572 | 0.280 | 0.313 |
| EfficientNetB0 | kNN | 0.330 | 0.546 | 0.310 | 0.346 |
| LP-global+CCE@DINOv3-B | MSP | 0.394 | 0.426 | 0.369 | 0.415 |
| LP-global+CCE@DINOv3-B | Remedy | 0.369 | 0.426 | 0.330 | 0.378 |
| LP-global+CCE@DINOv3-B | Remedy+kNN | 0.466 | 0.607 | 0.472 | 0.487 |
| LP-global+CCE@DINOv3-B | kNN | 0.503 | 0.647 | 0.520 | 0.512 |
| LP-global@DINOv3-B | MSP | 0.334 | 0.433 | 0.283 | 0.339 |
| LP-global@DINOv3-B | Remedy | 0.324 | 0.433 | 0.271 | 0.328 |
| LP-global@DINOv3-B | Remedy+kNN | 0.447 | 0.464 | 0.453 | 0.452 |
| LP-global@DINOv3-B | kNN | 0.495 | 0.596 | 0.519 | 0.485 |
| MIL@DINOv3-B | MSP | 0.268 | 0.463 | 0.237 | 0.271 |
| MIL@DINOv3-B | Remedy | 0.260 | 0.463 | 0.230 | 0.261 |
| MIL@DINOv3-B | Remedy+kNN | 0.324 | 0.463 | 0.319 | 0.337 |
| MIL@DINOv3-B | kNN | 0.380 | 0.464 | 0.399 | 0.370 |
| SERA@DINOv3-B | MSP | 0.274 | 0.502 | 0.237 | 0.274 |
| SERA@DINOv3-B | Remedy | 0.260 | 0.502 | 0.224 | 0.259 |
| SERA@DINOv3-B | Remedy+kNN | 0.306 | 0.521 | 0.291 | 0.320 |
| SERA@DINOv3-B | kNN | 0.340 | 0.529 | 0.347 | 0.350 |
| SERA@DINOv3-S | MSP | 0.290 | 0.456 | 0.248 | 0.291 |
| SERA@DINOv3-S | Remedy | 0.277 | 0.456 | 0.226 | 0.275 |
| SERA@DINOv3-S | Remedy+kNN | 0.346 | 0.463 | 0.341 | 0.359 |
| SERA@DINOv3-S | kNN | 0.396 | 0.480 | 0.409 | 0.401 |
| ViTS | MSP | 0.237 | 0.575 | 0.207 | 0.238 |
| ViTS | Remedy | 0.233 | 0.575 | 0.203 | 0.233 |
| ViTS | Remedy+kNN | 0.224 | 0.630 | 0.189 | 0.236 |
| ViTS | kNN | 0.231 | 0.638 | 0.190 | 0.237 |

## RQ3 headline (SERA@DINOv3-B)

- no gate: wrong-remedy risk **36.8%** of all held-out images
- MSP / val-CRC: risk 31.8% (violations 100% of runs), accepts 86% of images, 34% of issued remedies wrong, withholds 0% of unseen diseases
- Remedy / val-CRC: risk 32.0% (violations 100% of runs), accepts 90% of images, 34% of issued remedies wrong, withholds 0% of unseen diseases
- Remedy-set / CP-remedy(val): risk 16.2% (violations 100% of runs), accepts 70% of images, 28% of issued remedies wrong, withholds 71% of unseen diseases
- Remedy / LOSO-CRC: risk 5.3% (violations 42% of runs), accepts 29% of images, 20% of issued remedies wrong, withholds 86% of unseen diseases
- Remedy+kNN / LOSO-CRC: risk 5.2% (violations 42% of runs), accepts 23% of images, 25% of issued remedies wrong, withholds 92% of unseen diseases
- Remedy+kNN / LOSO-CRC-worst: risk 3.5% (violations 33% of runs), accepts 17% of images, 22% of issued remedies wrong, withholds 95% of unseen diseases

## Single-source reference splits - accuracy (seen classes)

| split | model | macro_f1 | macro_f1_sd | acc | seeds |
|---|---|---|---|---|---|
| plantvillage>plantdoc | LP-global@DINOv3-B | 0.358 | 0.030 | 0.268 | 3 |
| plantvillage>plantdoc | SERA@DINOv3-B | 0.512 | 0.029 | 0.459 | 3 |
| plantvillage>plantdoc | SERA@DINOv3-S | 0.561 | 0.110 | 0.572 | 3 |

## Single-source reference splits - gate (target risk 5%)

| held_out | model | score | calibration | accept | risk | wrong_among_issued | withheld_unseen |
|---|---|---|---|---|---|---|---|
| plantvillage>plantdoc | LP-global@DINOv3-B | - | no gate | 1.000 | 0.732 | 0.732 | nan |
| plantvillage>plantdoc | LP-global@DINOv3-B | MSP | val-CRC | 1.000 | 0.732 | 0.732 | nan |
| plantvillage>plantdoc | LP-global@DINOv3-B | Remedy | val-CRC | 1.000 | 0.732 | 0.732 | nan |
| plantvillage>plantdoc | LP-global@DINOv3-B | Remedy+kNN | val-CRC | 1.000 | 0.732 | 0.732 | nan |
| plantvillage>plantdoc | LP-global@DINOv3-B | Remedy-set | CP-remedy(val) | 0.470 | 0.336 | 0.710 | nan |
| plantvillage>plantdoc | LP-global@DINOv3-B | kNN | val-CRC | 1.000 | 0.732 | 0.732 | nan |
| plantvillage>plantdoc | SERA@DINOv3-B | - | no gate | 1.000 | 0.541 | 0.541 | nan |
| plantvillage>plantdoc | SERA@DINOv3-B | MSP | val-CRC | 1.000 | 0.541 | 0.541 | nan |
| plantvillage>plantdoc | SERA@DINOv3-B | Remedy | val-CRC | 1.000 | 0.541 | 0.541 | nan |
| plantvillage>plantdoc | SERA@DINOv3-B | Remedy+kNN | val-CRC | 1.000 | 0.541 | 0.541 | nan |
| plantvillage>plantdoc | SERA@DINOv3-B | Remedy-set | CP-remedy(val) | 0.286 | 0.134 | 0.457 | nan |
| plantvillage>plantdoc | SERA@DINOv3-B | kNN | val-CRC | 1.000 | 0.541 | 0.541 | nan |
| plantvillage>plantdoc | SERA@DINOv3-S | - | no gate | 1.000 | 0.428 | 0.428 | nan |
| plantvillage>plantdoc | SERA@DINOv3-S | MSP | val-CRC | 1.000 | 0.428 | 0.428 | nan |
| plantvillage>plantdoc | SERA@DINOv3-S | Remedy | val-CRC | 1.000 | 0.428 | 0.428 | nan |
| plantvillage>plantdoc | SERA@DINOv3-S | Remedy+kNN | val-CRC | 1.000 | 0.428 | 0.428 | nan |
| plantvillage>plantdoc | SERA@DINOv3-S | Remedy-set | CP-remedy(val) | 0.586 | 0.202 | 0.353 | nan |
| plantvillage>plantdoc | SERA@DINOv3-S | kNN | val-CRC | 1.000 | 0.428 | 0.428 | nan |

## Worked cases (UNVERIFIED action templates)

| held_out | case | true | top_disease | issued_group | decision | u_risk | lam |
|---|---|---|---|---|---|---|---|
| plantvillage | issued & right | early_blight | early_blight | fungal_foliar | ISSUE | 0.795 | 0.890 |
| plantvillage | withheld (would have been wrong) | early_blight | late_blight | oomycete | WITHHOLD | 0.922 | 0.890 |
| plantvillage | issued & WRONG (failure) | early_blight | late_blight | oomycete | ISSUE | 0.848 | 0.890 |
| plantdoc | issued & right | early_blight | fungi_other | fungal_foliar | ISSUE | 0.937 | 0.944 |
| plantdoc | withheld (would have been wrong) | early_blight | pest | pest_control | WITHHOLD | 0.998 | 0.944 |
| plantdoc | issued & WRONG (failure) | early_blight | late_blight | oomycete | ISSUE | 0.844 | 0.944 |
| pld_pakistan | issued & right | early_blight | early_blight | fungal_foliar | ISSUE | 0.839 | 0.901 |
| pld_pakistan | withheld (would have been wrong) | early_blight | late_blight | oomycete | WITHHOLD | 1.000 | 0.901 |
| pld_pakistan | issued & WRONG (failure) | early_blight | late_blight | oomycete | ISSUE | 0.785 | 0.901 |
| uncontrolled_indonesia | issued & right | fungi_other | early_blight | fungal_foliar | ISSUE | 0.811 | 0.918 |
| uncontrolled_indonesia | withheld (would have been wrong) | bacterial | late_blight | oomycete | WITHHOLD | 0.992 | 0.918 |
| uncontrolled_indonesia | withheld unseen disease | bacterial | late_blight | oomycete | WITHHOLD | 0.992 | 0.918 |
| uncontrolled_indonesia | issued & WRONG (failure) | bacterial | late_blight | oomycete | ISSUE | 0.917 | 0.918 |

## RQ3b - risk / acceptance at several risk targets: LP-global@DINOv3-B (mean over held-out sources and seeds)

| score | calibration | eps=5% | eps=10% | eps=15% | eps=20% |
|---|---|---|---|---|---|
| Remedy+kNN | val-CRC | 0.229 / 0.34 | 0.423 / 0.87 | 0.463 / 1.00 | 0.463 / 1.00 |
| Remedy+kNN | W-CRC | 0.104 / 0.17 | 0.177 / 0.30 | 0.245 / 0.45 | 0.324 / 0.63 |
| Remedy+kNN | Robust-CRC(rho=0.01) | 0.140 / 0.20 | 0.257 / 0.41 | 0.432 / 0.90 | 0.463 / 1.00 |
| Remedy+kNN | Robust-CRC(rho=0.05) | 0.056 / 0.09 | 0.161 / 0.23 | 0.252 / 0.40 | 0.402 / 0.80 |
| Remedy+kNN | Robust-CRC(rho=0.1) | 0.004 / 0.01 | 0.094 / 0.14 | 0.191 / 0.28 | 0.262 / 0.42 |
| Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.042 / 0.07 | 0.105 / 0.15 | 0.173 / 0.25 |
| Remedy+kNN | LOSO-CRC (2 src) | 0.156 / 0.23 | 0.209 / 0.30 | 0.232 / 0.34 | 0.254 / 0.39 |
| Remedy+kNN | LOSO-CRC | 0.155 / 0.23 | 0.213 / 0.30 | 0.236 / 0.34 | 0.253 / 0.38 |
| Remedy+kNN | LOSO-CRC-worst | 0.075 / 0.11 | 0.131 / 0.20 | 0.173 / 0.25 | 0.198 / 0.29 |
| Remedy+kNN | LOSO+LCO-CRC | 0.089 / 0.13 | 0.167 / 0.23 | 0.202 / 0.29 | 0.229 / 0.33 |
| Remedy+kNN | LOSO+LCO-CRC-worst | 0.015 / 0.02 | 0.024 / 0.04 | 0.042 / 0.07 | 0.073 / 0.11 |
| kNN | val-CRC | 0.200 / 0.27 | 0.395 / 0.77 | 0.463 / 1.00 | 0.463 / 1.00 |
| kNN | W-CRC | 0.126 / 0.17 | 0.193 / 0.30 | 0.253 / 0.42 | 0.321 / 0.61 |
| kNN | Robust-CRC(rho=0.01) | 0.143 / 0.18 | 0.221 / 0.30 | 0.409 / 0.82 | 0.463 / 1.00 |
| kNN | Robust-CRC(rho=0.05) | 0.055 / 0.07 | 0.165 / 0.22 | 0.212 / 0.28 | 0.366 / 0.67 |
| kNN | Robust-CRC(rho=0.1) | 0.001 / 0.00 | 0.113 / 0.14 | 0.180 / 0.24 | 0.224 / 0.30 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.025 / 0.03 | 0.118 / 0.15 | 0.174 / 0.23 |
| kNN | LOSO-CRC (2 src) | 0.214 / 0.29 | 0.236 / 0.32 | 0.248 / 0.35 | 0.257 / 0.37 |
| kNN | LOSO-CRC | 0.213 / 0.29 | 0.240 / 0.33 | 0.248 / 0.34 | 0.254 / 0.36 |
| kNN | LOSO-CRC-worst | 0.183 / 0.24 | 0.206 / 0.28 | 0.220 / 0.30 | 0.233 / 0.32 |
| kNN | LOSO+LCO-CRC | 0.179 / 0.23 | 0.215 / 0.29 | 0.233 / 0.31 | 0.242 / 0.33 |
| kNN | LOSO+LCO-CRC-worst | 0.118 / 0.15 | 0.140 / 0.18 | 0.155 / 0.20 | 0.167 / 0.22 |

## RQ3b - risk / acceptance at several risk targets: SERA@DINOv3-B (mean over held-out sources and seeds)

| score | calibration | eps=5% | eps=10% | eps=15% | eps=20% |
|---|---|---|---|---|---|
| Remedy+kNN | val-CRC | 0.275 / 0.67 | 0.368 / 1.00 | 0.368 / 1.00 | 0.368 / 1.00 |
| Remedy+kNN | W-CRC | 0.075 / 0.30 | 0.150 / 0.53 | 0.267 / 0.80 | 0.358 / 0.97 |
| Remedy+kNN | Robust-CRC(rho=0.01) | 0.189 / 0.42 | 0.322 / 0.83 | 0.368 / 1.00 | 0.368 / 1.00 |
| Remedy+kNN | Robust-CRC(rho=0.05) | 0.037 / 0.12 | 0.226 / 0.50 | 0.320 / 0.82 | 0.363 / 0.99 |
| Remedy+kNN | Robust-CRC(rho=0.1) | 0.016 / 0.06 | 0.075 / 0.21 | 0.240 / 0.56 | 0.325 / 0.84 |
| Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.031 / 0.10 | 0.082 / 0.22 | 0.234 / 0.53 |
| Remedy+kNN | LOSO-CRC (2 src) | 0.056 / 0.25 | 0.107 / 0.41 | 0.155 / 0.54 | 0.218 / 0.69 |
| Remedy+kNN | LOSO-CRC | 0.053 / 0.24 | 0.106 / 0.41 | 0.155 / 0.55 | 0.225 / 0.70 |
| Remedy+kNN | LOSO-CRC-worst | 0.035 / 0.17 | 0.073 / 0.30 | 0.120 / 0.44 | 0.170 / 0.58 |
| Remedy+kNN | LOSO+LCO-CRC | 0.043 / 0.17 | 0.084 / 0.32 | 0.146 / 0.47 | 0.200 / 0.61 |
| Remedy+kNN | LOSO+LCO-CRC-worst | 0.012 / 0.06 | 0.025 / 0.10 | 0.038 / 0.14 | 0.053 / 0.19 |
| kNN | val-CRC | 0.228 / 0.43 | 0.368 / 1.00 | 0.368 / 1.00 | 0.368 / 1.00 |
| kNN | W-CRC | 0.064 / 0.19 | 0.131 / 0.44 | 0.252 / 0.75 | 0.358 / 0.96 |
| kNN | Robust-CRC(rho=0.01) | 0.163 / 0.25 | 0.307 / 0.71 | 0.368 / 1.00 | 0.368 / 1.00 |
| kNN | Robust-CRC(rho=0.05) | 0.010 / 0.02 | 0.184 / 0.29 | 0.304 / 0.68 | 0.361 / 0.98 |
| kNN | Robust-CRC(rho=0.1) | 0.001 / 0.00 | 0.042 / 0.07 | 0.191 / 0.32 | 0.311 / 0.73 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.007 / 0.01 | 0.045 / 0.08 | 0.188 / 0.30 |
| kNN | LOSO-CRC (2 src) | 0.059 / 0.20 | 0.110 / 0.37 | 0.153 / 0.50 | 0.204 / 0.64 |
| kNN | LOSO-CRC | 0.058 / 0.21 | 0.108 / 0.36 | 0.157 / 0.51 | 0.197 / 0.63 |
| kNN | LOSO-CRC-worst | 0.027 / 0.11 | 0.061 / 0.22 | 0.111 / 0.36 | 0.161 / 0.51 |
| kNN | LOSO+LCO-CRC | 0.041 / 0.14 | 0.080 / 0.27 | 0.116 / 0.39 | 0.155 / 0.50 |
| kNN | LOSO+LCO-CRC-worst | 0.011 / 0.05 | 0.021 / 0.08 | 0.036 / 0.13 | 0.056 / 0.20 |

## RQ3b - risk / acceptance at several risk targets: SERA@DINOv3-S (mean over held-out sources and seeds)

| score | calibration | eps=5% | eps=10% | eps=15% | eps=20% |
|---|---|---|---|---|---|
| Remedy+kNN | val-CRC | 0.285 / 0.65 | 0.376 / 0.93 | 0.401 / 1.00 | 0.401 / 1.00 |
| Remedy+kNN | W-CRC | 0.098 / 0.33 | 0.173 / 0.53 | 0.249 / 0.70 | 0.375 / 0.93 |
| Remedy+kNN | Robust-CRC(rho=0.01) | 0.180 / 0.38 | 0.327 / 0.78 | 0.379 / 0.94 | 0.401 / 1.00 |
| Remedy+kNN | Robust-CRC(rho=0.05) | 0.039 / 0.11 | 0.219 / 0.46 | 0.319 / 0.76 | 0.373 / 0.92 |
| Remedy+kNN | Robust-CRC(rho=0.1) | 0.007 / 0.04 | 0.107 / 0.25 | 0.257 / 0.55 | 0.333 / 0.79 |
| Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.022 / 0.08 | 0.114 / 0.26 | 0.249 / 0.52 |
| Remedy+kNN | LOSO-CRC (2 src) | 0.057 / 0.20 | 0.115 / 0.37 | 0.170 / 0.52 | 0.222 / 0.65 |
| Remedy+kNN | LOSO-CRC | 0.052 / 0.18 | 0.109 / 0.36 | 0.172 / 0.53 | 0.221 / 0.66 |
| Remedy+kNN | LOSO-CRC-worst | 0.025 / 0.11 | 0.058 / 0.21 | 0.105 / 0.34 | 0.153 / 0.47 |
| Remedy+kNN | LOSO+LCO-CRC | 0.032 / 0.13 | 0.072 / 0.25 | 0.124 / 0.39 | 0.176 / 0.53 |
| Remedy+kNN | LOSO+LCO-CRC-worst | 0.007 / 0.04 | 0.018 / 0.08 | 0.032 / 0.12 | 0.048 / 0.17 |
| kNN | val-CRC | 0.235 / 0.41 | 0.365 / 0.87 | 0.401 / 1.00 | 0.401 / 1.00 |
| kNN | W-CRC | 0.082 / 0.20 | 0.158 / 0.42 | 0.253 / 0.66 | 0.375 / 0.91 |
| kNN | Robust-CRC(rho=0.01) | 0.129 / 0.20 | 0.299 / 0.62 | 0.368 / 0.89 | 0.401 / 1.00 |
| kNN | Robust-CRC(rho=0.05) | 0.010 / 0.02 | 0.176 / 0.27 | 0.287 / 0.58 | 0.363 / 0.86 |
| kNN | Robust-CRC(rho=0.1) | 0.000 / 0.00 | 0.064 / 0.10 | 0.206 / 0.32 | 0.305 / 0.65 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.004 / 0.01 | 0.071 / 0.11 | 0.199 / 0.31 |
| kNN | LOSO-CRC (2 src) | 0.061 / 0.16 | 0.114 / 0.31 | 0.171 / 0.46 | 0.219 / 0.60 |
| kNN | LOSO-CRC | 0.058 / 0.15 | 0.112 / 0.30 | 0.167 / 0.45 | 0.224 / 0.61 |
| kNN | LOSO-CRC-worst | 0.031 / 0.09 | 0.061 / 0.17 | 0.108 / 0.30 | 0.169 / 0.44 |
| kNN | LOSO+LCO-CRC | 0.050 / 0.13 | 0.096 / 0.25 | 0.132 / 0.37 | 0.165 / 0.47 |
| kNN | LOSO+LCO-CRC-worst | 0.013 / 0.04 | 0.027 / 0.08 | 0.044 / 0.13 | 0.066 / 0.19 |

## RQ3b - risk / acceptance at several risk targets: ViTS (mean over held-out sources and seeds)

| score | calibration | eps=5% | eps=10% | eps=15% | eps=20% |
|---|---|---|---|---|---|
| Remedy+kNN | val-CRC | 0.327 / 0.97 | 0.339 / 1.00 | 0.339 / 1.00 | 0.339 / 1.00 |
| Remedy+kNN | W-CRC | 0.072 / 0.51 | 0.128 / 0.68 | 0.250 / 0.87 | 0.278 / 0.92 |
| Remedy+kNN | Robust-CRC(rho=0.01) | 0.296 / 0.83 | 0.333 / 0.99 | 0.339 / 1.00 | 0.339 / 1.00 |
| Remedy+kNN | Robust-CRC(rho=0.05) | 0.065 / 0.34 | 0.304 / 0.88 | 0.332 / 0.98 | 0.339 / 1.00 |
| Remedy+kNN | Robust-CRC(rho=0.1) | 0.018 / 0.15 | 0.254 / 0.71 | 0.313 / 0.92 | 0.335 / 0.99 |
| Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.038 / 0.23 | 0.257 / 0.72 | 0.310 / 0.91 |
| Remedy+kNN | LOSO-CRC (2 src) | 0.090 / 0.41 | 0.172 / 0.66 | 0.222 / 0.80 | 0.265 / 0.89 |
| Remedy+kNN | LOSO-CRC | 0.072 / 0.37 | 0.147 / 0.63 | 0.208 / 0.80 | 0.321 / 0.96 |
| Remedy+kNN | LOSO-CRC-worst | 0.033 / 0.22 | 0.081 / 0.40 | 0.110 / 0.55 | 0.150 / 0.68 |
| kNN | val-CRC | 0.327 / 0.95 | 0.339 / 1.00 | 0.339 / 1.00 | 0.339 / 1.00 |
| kNN | W-CRC | 0.082 / 0.50 | 0.142 / 0.68 | 0.260 / 0.86 | 0.287 / 0.92 |
| kNN | Robust-CRC(rho=0.01) | 0.308 / 0.84 | 0.334 / 0.99 | 0.339 / 1.00 | 0.339 / 1.00 |
| kNN | Robust-CRC(rho=0.05) | 0.075 / 0.41 | 0.316 / 0.88 | 0.333 / 0.98 | 0.339 / 1.00 |
| kNN | Robust-CRC(rho=0.1) | 0.022 / 0.21 | 0.271 / 0.74 | 0.318 / 0.90 | 0.336 / 0.99 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.041 / 0.31 | 0.273 / 0.75 | 0.317 / 0.89 |
| kNN | LOSO-CRC (2 src) | 0.065 / 0.42 | 0.157 / 0.65 | 0.237 / 0.83 | 0.282 / 0.91 |
| kNN | LOSO-CRC | 0.050 / 0.39 | 0.135 / 0.63 | 0.230 / 0.82 | 0.326 / 0.97 |
| kNN | LOSO-CRC-worst | 0.021 / 0.27 | 0.065 / 0.43 | 0.101 / 0.54 | 0.151 / 0.67 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: LP-global@DINOv3-B

| eps | calibration | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia |
|---|---|---|---|---|---|
| 0.050 | LOSO+LCO-CRC | 0.045 / 0.06 | 0.000 / 0.00 | 0.000 / 0.00 | 0.313 / 0.45 |
| 0.050 | LOSO+LCO-CRC-worst | 0.012 / 0.02 | 0.000 / 0.00 | 0.000 / 0.00 | 0.047 / 0.08 |
| 0.050 | LOSO-CRC | 0.155 / 0.26 | 0.000 / 0.00 | 0.000 / 0.00 | 0.463 / 0.64 |
| 0.050 | LOSO-CRC-worst | 0.108 / 0.17 | 0.000 / 0.00 | 0.000 / 0.00 | 0.191 / 0.29 |
| 0.050 | W-CRC | 0.037 / 0.05 | 0.017 / 0.07 | 0.012 / 0.07 | 0.350 / 0.50 |
| 0.050 | val-CRC | 0.130 / 0.20 | 0.024 / 0.10 | 0.012 / 0.07 | 0.751 / 1.00 |
| 0.100 | LOSO+LCO-CRC | 0.105 / 0.16 | 0.001 / 0.01 | 0.000 / 0.00 | 0.562 / 0.76 |
| 0.100 | LOSO+LCO-CRC-worst | 0.014 / 0.02 | 0.000 / 0.00 | 0.000 / 0.00 | 0.082 / 0.14 |
| 0.100 | LOSO-CRC | 0.218 / 0.35 | 0.002 / 0.01 | 0.000 / 0.00 | 0.632 / 0.85 |
| 0.100 | LOSO-CRC-worst | 0.183 / 0.30 | 0.000 / 0.00 | 0.000 / 0.00 | 0.342 / 0.49 |
| 0.100 | W-CRC | 0.075 / 0.11 | 0.054 / 0.19 | 0.032 / 0.15 | 0.545 / 0.74 |
| 0.100 | val-CRC | 0.522 / 1.00 | 0.261 / 0.91 | 0.157 / 0.57 | 0.751 / 1.00 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: SERA@DINOv3-B

| eps | calibration | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia |
|---|---|---|---|---|---|
| 0.050 | LOSO+LCO-CRC | 0.064 / 0.23 | 0.023 / 0.21 | 0.019 / 0.12 | 0.064 / 0.13 |
| 0.050 | LOSO+LCO-CRC-worst | 0.034 / 0.12 | 0.006 / 0.08 | 0.003 / 0.01 | 0.006 / 0.02 |
| 0.050 | LOSO-CRC | 0.100 / 0.35 | 0.030 / 0.26 | 0.036 / 0.25 | 0.044 / 0.09 |
| 0.050 | LOSO-CRC-worst | 0.064 / 0.24 | 0.018 / 0.18 | 0.031 / 0.22 | 0.028 / 0.06 |
| 0.050 | W-CRC | 0.096 / 0.33 | 0.050 / 0.42 | 0.033 / 0.25 | 0.121 / 0.22 |
| 0.050 | val-CRC | 0.261 / 0.73 | 0.080 / 0.60 | 0.055 / 0.37 | 0.706 / 1.00 |
| 0.100 | LOSO+LCO-CRC | 0.130 / 0.41 | 0.044 / 0.38 | 0.035 / 0.24 | 0.129 / 0.23 |
| 0.100 | LOSO+LCO-CRC-worst | 0.055 / 0.20 | 0.009 / 0.11 | 0.007 / 0.03 | 0.030 / 0.06 |
| 0.100 | LOSO-CRC | 0.185 / 0.54 | 0.058 / 0.48 | 0.059 / 0.39 | 0.120 / 0.21 |
| 0.100 | LOSO-CRC-worst | 0.123 / 0.40 | 0.038 / 0.33 | 0.049 / 0.33 | 0.081 / 0.15 |
| 0.100 | W-CRC | 0.202 / 0.58 | 0.099 / 0.71 | 0.070 / 0.44 | 0.229 / 0.37 |
| 0.100 | val-CRC | 0.387 / 1.00 | 0.154 / 1.00 | 0.225 / 1.00 | 0.706 / 1.00 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: SERA@DINOv3-S

| eps | calibration | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia |
|---|---|---|---|---|---|
| 0.050 | LOSO+LCO-CRC | 0.066 / 0.19 | 0.029 / 0.19 | 0.017 / 0.08 | 0.016 / 0.04 |
| 0.050 | LOSO+LCO-CRC-worst | 0.010 / 0.05 | 0.012 / 0.10 | 0.004 / 0.02 | 0.001 / 0.00 |
| 0.050 | LOSO-CRC | 0.108 / 0.28 | 0.042 / 0.26 | 0.030 / 0.13 | 0.029 / 0.06 |
| 0.050 | LOSO-CRC-worst | 0.040 / 0.13 | 0.030 / 0.19 | 0.021 / 0.09 | 0.009 / 0.02 |
| 0.050 | W-CRC | 0.118 / 0.31 | 0.097 / 0.52 | 0.044 / 0.25 | 0.132 / 0.23 |
| 0.050 | val-CRC | 0.224 / 0.58 | 0.143 / 0.72 | 0.049 / 0.28 | 0.722 / 1.00 |
| 0.100 | LOSO+LCO-CRC | 0.139 / 0.36 | 0.053 / 0.32 | 0.040 / 0.20 | 0.056 / 0.11 |
| 0.100 | LOSO+LCO-CRC-worst | 0.038 / 0.11 | 0.020 / 0.14 | 0.010 / 0.05 | 0.005 / 0.02 |
| 0.100 | LOSO-CRC | 0.183 / 0.47 | 0.078 / 0.44 | 0.065 / 0.32 | 0.110 / 0.19 |
| 0.100 | LOSO-CRC-worst | 0.115 / 0.31 | 0.046 / 0.28 | 0.036 / 0.18 | 0.035 / 0.07 |
| 0.100 | W-CRC | 0.215 / 0.56 | 0.149 / 0.76 | 0.088 / 0.44 | 0.240 / 0.38 |
| 0.100 | val-CRC | 0.406 / 1.00 | 0.224 / 1.00 | 0.151 / 0.71 | 0.722 / 1.00 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: ViTS

| eps | calibration | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia |
|---|---|---|---|---|---|
| 0.050 | LOSO-CRC | 0.143 / 0.44 | 0.005 / 0.53 | 0.005 / 0.23 | 0.137 / 0.30 |
| 0.050 | LOSO-CRC-worst | 0.057 / 0.19 | 0.002 / 0.44 | 0.002 / 0.09 | 0.072 / 0.19 |
| 0.050 | W-CRC | 0.201 / 0.56 | 0.024 / 0.73 | 0.020 / 0.57 | 0.043 / 0.16 |
| 0.050 | val-CRC | 0.432 / 1.00 | 0.105 / 1.00 | 0.072 / 0.88 | 0.701 / 1.00 |
| 0.100 | LOSO-CRC | 0.326 / 0.83 | 0.031 / 0.77 | 0.015 / 0.51 | 0.215 / 0.43 |
| 0.100 | LOSO-CRC-worst | 0.122 / 0.38 | 0.008 / 0.59 | 0.006 / 0.26 | 0.188 / 0.35 |
| 0.100 | W-CRC | 0.291 / 0.76 | 0.060 / 0.89 | 0.048 / 0.77 | 0.111 / 0.29 |
| 0.100 | val-CRC | 0.432 / 1.00 | 0.107 / 1.00 | 0.117 / 1.00 | 0.701 / 1.00 |

## RQ3b - gate risk and acceptance with 95% bootstrap intervals (Remedy+kNN)

| model | calibration | eps | risk [95% CI] | accept [95% CI] |
|---|---|---|---|---|
| LP-global@DINOv3-B | val-CRC | 0.050 | 0.229 [0.221, 0.238] | 0.34 [0.33, 0.35] |
| LP-global@DINOv3-B | val-CRC | 0.100 | 0.423 [0.408, 0.437] | 0.87 [0.87, 0.87] |
| LP-global@DINOv3-B | W-CRC | 0.050 | 0.104 [0.097, 0.110] | 0.17 [0.17, 0.18] |
| LP-global@DINOv3-B | W-CRC | 0.100 | 0.177 [0.169, 0.185] | 0.30 [0.29, 0.31] |
| LP-global@DINOv3-B | LOSO-CRC | 0.050 | 0.155 [0.145, 0.164] | 0.23 [0.21, 0.24] |
| LP-global@DINOv3-B | LOSO-CRC | 0.100 | 0.213 [0.203, 0.224] | 0.30 [0.29, 0.31] |
| LP-global@DINOv3-B | LOSO-CRC-worst | 0.050 | 0.075 [0.067, 0.082] | 0.11 [0.11, 0.13] |
| LP-global@DINOv3-B | LOSO-CRC-worst | 0.100 | 0.131 [0.122, 0.141] | 0.20 [0.19, 0.21] |
| LP-global@DINOv3-B | LOSO+LCO-CRC | 0.050 | 0.089 [0.083, 0.096] | 0.13 [0.12, 0.14] |
| LP-global@DINOv3-B | LOSO+LCO-CRC | 0.100 | 0.167 [0.159, 0.175] | 0.23 [0.22, 0.24] |
| LP-global@DINOv3-B | LOSO+LCO-CRC-worst | 0.050 | 0.015 [0.012, 0.018] | 0.02 [0.02, 0.03] |
| LP-global@DINOv3-B | LOSO+LCO-CRC-worst | 0.100 | 0.024 [0.021, 0.028] | 0.04 [0.04, 0.04] |
| SERA@DINOv3-B | val-CRC | 0.050 | 0.275 [0.266, 0.286] | 0.67 [0.66, 0.68] |
| SERA@DINOv3-B | val-CRC | 0.100 | 0.368 [0.356, 0.380] | 1.00 [1.00, 1.00] |
| SERA@DINOv3-B | W-CRC | 0.050 | 0.075 [0.069, 0.082] | 0.30 [0.29, 0.31] |
| SERA@DINOv3-B | W-CRC | 0.100 | 0.150 [0.141, 0.160] | 0.53 [0.52, 0.54] |
| SERA@DINOv3-B | LOSO-CRC | 0.050 | 0.053 [0.047, 0.059] | 0.24 [0.23, 0.25] |
| SERA@DINOv3-B | LOSO-CRC | 0.100 | 0.106 [0.097, 0.115] | 0.41 [0.39, 0.42] |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.050 | 0.035 [0.030, 0.040] | 0.17 [0.16, 0.18] |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.100 | 0.073 [0.066, 0.080] | 0.30 [0.29, 0.31] |
| SERA@DINOv3-B | LOSO+LCO-CRC | 0.050 | 0.043 [0.038, 0.048] | 0.17 [0.16, 0.18] |
| SERA@DINOv3-B | LOSO+LCO-CRC | 0.100 | 0.084 [0.077, 0.092] | 0.32 [0.30, 0.33] |
| SERA@DINOv3-B | LOSO+LCO-CRC-worst | 0.050 | 0.012 [0.009, 0.016] | 0.06 [0.05, 0.07] |
| SERA@DINOv3-B | LOSO+LCO-CRC-worst | 0.100 | 0.025 [0.021, 0.030] | 0.10 [0.09, 0.11] |
| SERA@DINOv3-S | val-CRC | 0.050 | 0.285 [0.274, 0.295] | 0.65 [0.64, 0.66] |
| SERA@DINOv3-S | val-CRC | 0.100 | 0.376 [0.363, 0.389] | 0.93 [0.93, 0.93] |
| SERA@DINOv3-S | W-CRC | 0.050 | 0.098 [0.091, 0.105] | 0.33 [0.32, 0.34] |
| SERA@DINOv3-S | W-CRC | 0.100 | 0.173 [0.163, 0.184] | 0.53 [0.52, 0.54] |
| SERA@DINOv3-S | LOSO-CRC | 0.050 | 0.052 [0.046, 0.058] | 0.18 [0.17, 0.19] |
| SERA@DINOv3-S | LOSO-CRC | 0.100 | 0.109 [0.101, 0.118] | 0.36 [0.34, 0.37] |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.050 | 0.025 [0.021, 0.029] | 0.11 [0.10, 0.11] |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.100 | 0.058 [0.052, 0.065] | 0.21 [0.20, 0.22] |
| SERA@DINOv3-S | LOSO+LCO-CRC | 0.050 | 0.032 [0.028, 0.037] | 0.13 [0.12, 0.13] |
| SERA@DINOv3-S | LOSO+LCO-CRC | 0.100 | 0.072 [0.066, 0.080] | 0.25 [0.24, 0.26] |
| SERA@DINOv3-S | LOSO+LCO-CRC-worst | 0.050 | 0.007 [0.005, 0.009] | 0.04 [0.04, 0.05] |
| SERA@DINOv3-S | LOSO+LCO-CRC-worst | 0.100 | 0.018 [0.015, 0.022] | 0.08 [0.07, 0.08] |
| ViTS | val-CRC | 0.050 | 0.327 [0.316, 0.340] | 0.97 [0.97, 0.97] |
| ViTS | val-CRC | 0.100 | 0.339 [0.327, 0.352] | 1.00 [1.00, 1.00] |
| ViTS | W-CRC | 0.050 | 0.072 [0.063, 0.081] | 0.51 [0.49, 0.52] |
| ViTS | W-CRC | 0.100 | 0.128 [0.118, 0.138] | 0.68 [0.67, 0.68] |
| ViTS | LOSO-CRC | 0.050 | 0.072 [0.064, 0.081] | 0.37 [0.36, 0.39] |
| ViTS | LOSO-CRC | 0.100 | 0.147 [0.137, 0.158] | 0.63 [0.62, 0.64] |
| ViTS | LOSO-CRC-worst | 0.050 | 0.033 [0.029, 0.038] | 0.22 [0.22, 0.23] |
| ViTS | LOSO-CRC-worst | 0.100 | 0.081 [0.073, 0.089] | 0.40 [0.38, 0.41] |

## RQ3b - shift-aware calibrations compared at eps = 5% (mean over held-out sources and seeds)

| model | score | calibration | accept | risk | share_of_runs_over_eps | withheld_unseen |
|---|---|---|---|---|---|---|
| LP-global@DINOv3-B | Energy | val-CRC | 0.695 | 0.326 | 0.750 | 0.000 |
| LP-global@DINOv3-B | Energy | W-CRC | 0.232 | 0.109 | 0.500 | 0.492 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.423 | 0.192 | 0.750 | 0.338 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.181 | 0.063 | 0.500 | 0.770 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.060 | 0.015 | 0.000 | 0.911 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| LP-global@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.139 | 0.044 | 0.500 | 0.818 |
| LP-global@DINOv3-B | Energy | LOSO-CRC | 0.122 | 0.041 | 0.500 | 0.826 |
| LP-global@DINOv3-B | Energy | LOSO-CRC-worst | 0.073 | 0.020 | 0.083 | 0.890 |
| LP-global@DINOv3-B | Energy | LOSO+LCO-CRC | 0.065 | 0.015 | 0.083 | 0.976 |
| LP-global@DINOv3-B | Energy | LOSO+LCO-CRC-worst | 0.021 | 0.002 | 0.000 | 0.992 |
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.342 | 0.229 | 0.500 | 0.000 |
| LP-global@DINOv3-B | Remedy+kNN | W-CRC | 0.174 | 0.104 | 0.250 | 0.492 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.200 | 0.140 | 0.333 | 0.299 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.086 | 0.056 | 0.250 | 0.676 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.008 | 0.004 | 0.000 | 0.970 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.226 | 0.156 | 0.500 | 0.361 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.225 | 0.155 | 0.500 | 0.355 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.115 | 0.075 | 0.500 | 0.701 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC | 0.130 | 0.089 | 0.250 | 0.541 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC-worst | 0.025 | 0.015 | 0.083 | 0.909 |
| SERA@DINOv3-B | Energy | val-CRC | 0.855 | 0.320 | 1.000 | 0.000 |
| SERA@DINOv3-B | Energy | W-CRC | 0.441 | 0.117 | 0.750 | 0.704 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.638 | 0.256 | 0.750 | 0.031 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.245 | 0.068 | 0.500 | 0.752 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.098 | 0.024 | 0.250 | 0.959 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.241 | 0.052 | 0.333 | 0.905 |
| SERA@DINOv3-B | Energy | LOSO-CRC | 0.226 | 0.048 | 0.333 | 0.913 |
| SERA@DINOv3-B | Energy | LOSO-CRC-worst | 0.164 | 0.034 | 0.250 | 0.959 |
| SERA@DINOv3-B | Energy | LOSO+LCO-CRC | 0.138 | 0.027 | 0.250 | 0.993 |
| SERA@DINOv3-B | Energy | LOSO+LCO-CRC-worst | 0.042 | 0.009 | 0.083 | 1.000 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.675 | 0.275 | 0.833 | 0.000 |
| SERA@DINOv3-B | Remedy+kNN | W-CRC | 0.304 | 0.075 | 0.667 | 0.791 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.417 | 0.189 | 0.583 | 0.120 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.119 | 0.037 | 0.333 | 0.836 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.060 | 0.016 | 0.083 | 0.917 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.247 | 0.056 | 0.417 | 0.912 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.239 | 0.053 | 0.417 | 0.918 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.173 | 0.035 | 0.333 | 0.947 |
| SERA@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC | 0.173 | 0.043 | 0.250 | 0.882 |
| SERA@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC-worst | 0.058 | 0.012 | 0.083 | 0.982 |
| SERA@DINOv3-S | Energy | val-CRC | 0.849 | 0.329 | 1.000 | 0.000 |
| SERA@DINOv3-S | Energy | W-CRC | 0.379 | 0.093 | 0.750 | 0.829 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.01) | 0.612 | 0.211 | 0.833 | 0.282 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.05) | 0.246 | 0.050 | 0.417 | 0.888 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.1) | 0.131 | 0.019 | 0.083 | 0.971 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-S | Energy | LOSO-CRC (2 src) | 0.218 | 0.039 | 0.250 | 0.961 |
| SERA@DINOv3-S | Energy | LOSO-CRC | 0.204 | 0.035 | 0.250 | 0.975 |
| SERA@DINOv3-S | Energy | LOSO-CRC-worst | 0.144 | 0.024 | 0.167 | 0.992 |
| SERA@DINOv3-S | Energy | LOSO+LCO-CRC | 0.074 | 0.018 | 0.250 | 0.998 |
| SERA@DINOv3-S | Energy | LOSO+LCO-CRC-worst | 0.028 | 0.007 | 0.000 | 1.000 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.647 | 0.285 | 0.833 | 0.000 |
| SERA@DINOv3-S | Remedy+kNN | W-CRC | 0.327 | 0.098 | 0.833 | 0.770 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.01) | 0.383 | 0.180 | 0.750 | 0.247 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.05) | 0.115 | 0.039 | 0.250 | 0.819 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.1) | 0.041 | 0.007 | 0.000 | 0.974 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC (2 src) | 0.198 | 0.057 | 0.500 | 0.928 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.184 | 0.052 | 0.417 | 0.937 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.106 | 0.025 | 0.167 | 0.976 |
| SERA@DINOv3-S | Remedy+kNN | LOSO+LCO-CRC | 0.125 | 0.032 | 0.250 | 0.960 |
| SERA@DINOv3-S | Remedy+kNN | LOSO+LCO-CRC-worst | 0.042 | 0.007 | 0.000 | 0.996 |
| ViTS | Energy | val-CRC | 0.876 | 0.315 | 0.750 | 0.000 |
| ViTS | Energy | W-CRC | 0.347 | 0.062 | 0.417 | 0.863 |
| ViTS | Energy | Robust-CRC(rho=0.01) | 0.708 | 0.285 | 0.500 | 0.000 |
| ViTS | Energy | Robust-CRC(rho=0.05) | 0.225 | 0.073 | 0.500 | 0.734 |
| ViTS | Energy | Robust-CRC(rho=0.1) | 0.055 | 0.019 | 0.167 | 0.957 |
| ViTS | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| ViTS | Energy | LOSO-CRC (2 src) | 0.245 | 0.049 | 0.417 | 0.847 |
| ViTS | Energy | LOSO-CRC | 0.215 | 0.036 | 0.250 | 0.913 |
| ViTS | Energy | LOSO-CRC-worst | 0.093 | 0.022 | 0.083 | 0.947 |
| ViTS | Remedy+kNN | val-CRC | 0.968 | 0.327 | 1.000 | 0.000 |
| ViTS | Remedy+kNN | W-CRC | 0.505 | 0.072 | 0.333 | 0.867 |
| ViTS | Remedy+kNN | Robust-CRC(rho=0.01) | 0.835 | 0.296 | 0.583 | 0.000 |
| ViTS | Remedy+kNN | Robust-CRC(rho=0.05) | 0.335 | 0.065 | 0.500 | 0.743 |
| ViTS | Remedy+kNN | Robust-CRC(rho=0.1) | 0.151 | 0.018 | 0.083 | 0.941 |
| ViTS | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| ViTS | Remedy+kNN | LOSO-CRC (2 src) | 0.414 | 0.090 | 0.417 | 0.694 |
| ViTS | Remedy+kNN | LOSO-CRC | 0.373 | 0.072 | 0.417 | 0.728 |
| ViTS | Remedy+kNN | LOSO-CRC-worst | 0.224 | 0.033 | 0.250 | 0.838 |

## RQ3b - shift-aware calibrations compared at eps = 10% (mean over held-out sources and seeds)

| model | score | calibration | accept | risk | share_of_runs_over_eps | withheld_unseen |
|---|---|---|---|---|---|---|
| LP-global@DINOv3-B | Energy | val-CRC | 0.966 | 0.445 | 1.000 | 0.000 |
| LP-global@DINOv3-B | Energy | W-CRC | 0.531 | 0.234 | 0.583 | 0.225 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.777 | 0.360 | 0.750 | 0.000 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.501 | 0.231 | 0.583 | 0.200 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.304 | 0.126 | 0.500 | 0.579 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.132 | 0.043 | 0.000 | 0.845 |
| LP-global@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.238 | 0.088 | 0.500 | 0.695 |
| LP-global@DINOv3-B | Energy | LOSO-CRC | 0.218 | 0.082 | 0.500 | 0.706 |
| LP-global@DINOv3-B | Energy | LOSO-CRC-worst | 0.136 | 0.049 | 0.167 | 0.792 |
| LP-global@DINOv3-B | Energy | LOSO+LCO-CRC | 0.125 | 0.037 | 0.167 | 0.934 |
| LP-global@DINOv3-B | Energy | LOSO+LCO-CRC-worst | 0.029 | 0.003 | 0.000 | 0.989 |
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.870 | 0.423 | 1.000 | 0.000 |
| LP-global@DINOv3-B | Remedy+kNN | W-CRC | 0.298 | 0.177 | 0.250 | 0.253 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.407 | 0.257 | 0.500 | 0.000 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.230 | 0.161 | 0.250 | 0.218 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.139 | 0.094 | 0.250 | 0.494 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.066 | 0.042 | 0.250 | 0.748 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.300 | 0.209 | 0.500 | 0.166 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.303 | 0.213 | 0.500 | 0.147 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.199 | 0.131 | 0.500 | 0.501 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC | 0.234 | 0.167 | 0.417 | 0.232 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC-worst | 0.040 | 0.024 | 0.000 | 0.852 |
| SERA@DINOv3-B | Energy | val-CRC | 1.000 | 0.368 | 1.000 | 0.000 |
| SERA@DINOv3-B | Energy | W-CRC | 0.689 | 0.205 | 0.750 | 0.464 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.921 | 0.339 | 0.833 | 0.000 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.710 | 0.280 | 0.583 | 0.000 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.418 | 0.126 | 0.500 | 0.574 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.185 | 0.051 | 0.167 | 0.795 |
| SERA@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.409 | 0.104 | 0.417 | 0.754 |
| SERA@DINOv3-B | Energy | LOSO-CRC | 0.401 | 0.102 | 0.333 | 0.755 |
| SERA@DINOv3-B | Energy | LOSO-CRC-worst | 0.276 | 0.066 | 0.250 | 0.879 |
| SERA@DINOv3-B | Energy | LOSO+LCO-CRC | 0.237 | 0.049 | 0.250 | 0.967 |
| SERA@DINOv3-B | Energy | LOSO+LCO-CRC-worst | 0.084 | 0.018 | 0.000 | 1.000 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.999 | 0.368 | 1.000 | 0.000 |
| SERA@DINOv3-B | Remedy+kNN | W-CRC | 0.527 | 0.150 | 0.583 | 0.635 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.830 | 0.322 | 0.667 | 0.000 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.500 | 0.226 | 0.500 | 0.000 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.211 | 0.075 | 0.250 | 0.673 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.096 | 0.031 | 0.083 | 0.847 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.408 | 0.107 | 0.500 | 0.792 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.405 | 0.106 | 0.500 | 0.795 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.301 | 0.073 | 0.250 | 0.859 |
| SERA@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC | 0.315 | 0.084 | 0.417 | 0.780 |
| SERA@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC-worst | 0.102 | 0.025 | 0.000 | 0.937 |
| SERA@DINOv3-S | Energy | val-CRC | 0.979 | 0.388 | 1.000 | 0.000 |
| SERA@DINOv3-S | Energy | W-CRC | 0.585 | 0.162 | 0.583 | 0.691 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.01) | 0.913 | 0.358 | 0.833 | 0.000 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.05) | 0.708 | 0.267 | 0.583 | 0.089 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.1) | 0.432 | 0.114 | 0.417 | 0.683 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.2) | 0.197 | 0.038 | 0.000 | 0.920 |
| SERA@DINOv3-S | Energy | LOSO-CRC (2 src) | 0.365 | 0.077 | 0.250 | 0.894 |
| SERA@DINOv3-S | Energy | LOSO-CRC | 0.346 | 0.070 | 0.250 | 0.915 |
| SERA@DINOv3-S | Energy | LOSO-CRC-worst | 0.247 | 0.045 | 0.167 | 0.973 |
| SERA@DINOv3-S | Energy | LOSO+LCO-CRC | 0.177 | 0.035 | 0.167 | 0.982 |
| SERA@DINOv3-S | Energy | LOSO+LCO-CRC-worst | 0.050 | 0.014 | 0.000 | 1.000 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.928 | 0.376 | 1.000 | 0.000 |
| SERA@DINOv3-S | Remedy+kNN | W-CRC | 0.533 | 0.173 | 0.833 | 0.614 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.01) | 0.776 | 0.327 | 0.750 | 0.000 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.05) | 0.464 | 0.219 | 0.500 | 0.107 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.1) | 0.253 | 0.107 | 0.250 | 0.533 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.2) | 0.077 | 0.022 | 0.000 | 0.901 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC (2 src) | 0.368 | 0.115 | 0.500 | 0.781 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.355 | 0.109 | 0.500 | 0.803 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.211 | 0.058 | 0.167 | 0.925 |
| SERA@DINOv3-S | Remedy+kNN | LOSO+LCO-CRC | 0.248 | 0.072 | 0.250 | 0.890 |
| SERA@DINOv3-S | Remedy+kNN | LOSO+LCO-CRC-worst | 0.077 | 0.018 | 0.000 | 0.985 |
| ViTS | Energy | val-CRC | 1.000 | 0.339 | 0.750 | 0.000 |
| ViTS | Energy | W-CRC | 0.543 | 0.125 | 0.500 | 0.693 |
| ViTS | Energy | Robust-CRC(rho=0.01) | 0.912 | 0.320 | 0.583 | 0.000 |
| ViTS | Energy | Robust-CRC(rho=0.05) | 0.749 | 0.292 | 0.500 | 0.000 |
| ViTS | Energy | Robust-CRC(rho=0.1) | 0.569 | 0.251 | 0.500 | 0.000 |
| ViTS | Energy | Robust-CRC(rho=0.2) | 0.147 | 0.047 | 0.250 | 0.838 |
| ViTS | Energy | LOSO-CRC (2 src) | 0.447 | 0.117 | 0.500 | 0.629 |
| ViTS | Energy | LOSO-CRC | 0.405 | 0.080 | 0.333 | 0.760 |
| ViTS | Energy | LOSO-CRC-worst | 0.213 | 0.033 | 0.083 | 0.936 |
| ViTS | Remedy+kNN | val-CRC | 1.000 | 0.339 | 0.750 | 0.000 |
| ViTS | Remedy+kNN | W-CRC | 0.676 | 0.128 | 0.500 | 0.743 |
| ViTS | Remedy+kNN | Robust-CRC(rho=0.01) | 0.986 | 0.333 | 0.667 | 0.000 |
| ViTS | Remedy+kNN | Robust-CRC(rho=0.05) | 0.879 | 0.304 | 0.500 | 0.000 |
| ViTS | Remedy+kNN | Robust-CRC(rho=0.1) | 0.707 | 0.254 | 0.500 | 0.000 |
| ViTS | Remedy+kNN | Robust-CRC(rho=0.2) | 0.230 | 0.038 | 0.083 | 0.809 |
| ViTS | Remedy+kNN | LOSO-CRC (2 src) | 0.663 | 0.172 | 0.500 | 0.464 |
| ViTS | Remedy+kNN | LOSO-CRC | 0.634 | 0.147 | 0.417 | 0.602 |
| ViTS | Remedy+kNN | LOSO-CRC-worst | 0.396 | 0.081 | 0.417 | 0.669 |

## RQ4 - probability drop when views are removed (top-attended vs random; keep-top = only top-k kept)

| model | mode | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| MIL@DINOv3-B | keep-top | 0.043 | 0.012 | 0.000 | -0.003 |
| MIL@DINOv3-B | random | 0.009 | 0.016 | 0.026 | 0.037 |
| MIL@DINOv3-B | top | 0.098 | 0.150 | 0.200 | 0.234 |
| SERA@DINOv3-B | keep-top | 0.051 | 0.010 | 0.001 | -0.003 |
| SERA@DINOv3-B | random | 0.010 | 0.018 | 0.032 | 0.043 |
| SERA@DINOv3-B | top | 0.115 | 0.180 | 0.229 | 0.271 |

## RQ4 - attention statistics (held-out ID images, seed 0)

| model | correct | entropy | global_share | finest_share |
|---|---|---|---|---|
| MIL@DINOv3-B | False | 0.637 | 0.049 | 0.677 |
| MIL@DINOv3-B | True | 0.655 | 0.042 | 0.641 |
| SERA@DINOv3-B | False | 0.580 | 0.078 | 0.659 |
| SERA@DINOv3-B | True | 0.577 | 0.075 | 0.642 |

## RQ4 - attention of correct vs wrong cross-source predictions

| model | metric | correct_mean | wrong_mean | mannwhitney_p |
|---|---|---|---|---|
| MIL@DINOv3-B | entropy | 0.6549 | 0.6370 | 0.0011 |
| MIL@DINOv3-B | global_share | 0.0421 | 0.0486 | 0.0483 |
| MIL@DINOv3-B | finest_share | 0.6405 | 0.6774 | 0.0000 |
| SERA@DINOv3-B | entropy | 0.5771 | 0.5797 | 0.3432 |
| SERA@DINOv3-B | global_share | 0.0747 | 0.0775 | 0.1276 |
| SERA@DINOv3-B | finest_share | 0.6418 | 0.6587 | 0.0035 |

## Efficiency (encoder; 224x224 views; CPU 4 threads)

| encoder | views | params_M | GFLOPs | cpu_ms |
|---|---|---|---|---|
| DINOv3-S | 1 | 21.59 | 4.33 | 71.76 |
| DINOv3-S | 5 | 21.59 | 21.63 | 270.78 |
| DINOv3-S | 14 | 21.59 | 60.56 | 696.96 |
| DINOv3-B | 1 | 85.64 | 17.19 | 222.65 |
| DINOv3-B | 5 | 85.64 | 85.94 | 865.36 |
| DINOv3-B | 14 | 85.64 | 240.62 | 2652.80 |
