# Onion cross-source diagnosis (SERA pipeline): results report

Generated 2026-10-12 14:09 | full run | classes: botrytis, bulb_blight, burn_tip, downy_mildew, fusarium, healthy, purple_blotch, rust, stemphylium, viral, xanthomonas | main encoder DINOv3-B | proposed SERA@DINOv3-B | head runs 922 | elapsed 3.69 h

Figures: d1_acquisition_by_source.png, d3_centroid_similarity.png, label_harmonization_grid.png, rq3_gate.png, rq3b_eps_sweep.png, viral_iyv_vs_virosis.png, xai_sera_attention.png

## Source datasets (before any cleaning)

| source_class | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion |
|---|---|---|---|---|
| Alternaria_D | 0 | 0 | 0 | 515 |
| Botrytis_Leaf_Blight | 0 | 772 | 0 | 0 |
| Bulb_blight-D | 0 | 0 | 0 | 30 |
| Burn_Tip | 0 | 0 | 282 | 0 |
| Downy_Mildew | 0 | 653 | 3854 | 0 |
| Fusarium-D | 0 | 0 | 0 | 738 |
| Healthy | 0 | 737 | 4410 | 0 |
| Healthy_leaf | 0 | 0 | 0 | 679 |
| Iris_yellow_virus | 281 | 0 | 0 | 0 |
| Purple_Blotch | 0 | 421 | 2016 | 0 |
| Rust | 0 | 537 | 0 | 0 |
| Stemphylium_Leaf_Blight | 0 | 392 | 0 | 0 |
| Stemphylium_leaf_blight_and_collectrichum_leaf_blight | 90 | 0 | 0 | 0 |
| Virosis-D | 0 | 0 | 0 | 203 |
| Xanthomonas_Leaf_Blight | 0 | 467 | 0 | 0 |
| healthy | 426 | 0 | 0 | 0 |
| purple_blotch | 18 | 0 | 0 | 0 |

Downloaded this session: none (reused)

## Roboflow augmentation audit

- **roboflow_capstone**: 500 original photos; copies per photo {1: 104, 2: 2, 3: 394}; crops 3979 -> 1544 after keeping one copy per photo
- **roboflow_onionnet**: 1312 original photos; copies per photo {1: 497, 2: 13, 3: 716, 4: 20, 5: 8, 6: 21, 7: 14, 9: 16, 10: 1, 11: 2, 12: 3, 15: 1}; crops 10562 -> 4222 after keeping one copy per photo

## Deduplication

- exact duplicates: 4 sets with conflicting labels (all copies dropped), 39 extra copies dropped
  - cold: 2 images dropped
  - tom2024_onion: 45 images dropped
- near-duplicate pairs (Hamming <= 4): 16; clusters with >1 image: 11
- near-duplicate clusters with conflicting labels: 0 (0 images dropped)
- clusters spanning datasets: 5 (5 images dropped from the minority dataset)
  - roboflow_capstone+roboflow_onionnet: 5 clusters
- photo groups merged because of near-duplicates: 6

## Harmonized class counts (after dedup)

| label_name | cold | tom2024_onion | roboflow_capstone | roboflow_onionnet | total | n_sources |
|---|---|---|---|---|---|---|
| botrytis | 0 | 0 | 294 | 0 | 294 | 1 |
| bulb_blight | 0 | 29 | 0 | 0 | 29 | 1 |
| burn_tip | 0 | 0 | 0 | 122 | 122 | 1 |
| downy_mildew | 0 | 0 | 262 | 1156 | 1418 | 2 |
| fusarium | 0 | 725 | 0 | 0 | 725 | 1 |
| healthy | 426 | 663 | 283 | 2064 | 3436 | 4 |
| purple_blotch | 18 | 504 | 167 | 875 | 1564 | 4 |
| rust | 0 | 0 | 204 | 0 | 204 | 1 |
| stemphylium | 90 | 0 | 146 | 0 | 236 | 2 |
| viral | 279 | 199 | 0 | 0 | 478 | 2 |
| xanthomonas | 0 | 0 | 188 | 0 | 188 | 1 |

Dropped images by reason: {'kept': 8694, 'exact_dup_extra_copy': 39, 'exact_dup_label_conflict': 8, 'near_dup_cross_dataset': 5}

## Splits (all leakage checks passed)

| protocol | split | train | val | test | test_id | test_unseen_class | train_classes | shared_test_classes |
|---|---|---|---|---|---|---|---|---|
| lodo | cold | 6712 | 1169 | 813 | 813 | 0 | 11 | healthy, purple_blotch, stemphylium, viral |
| lodo | tom2024_onion | 5603 | 971 | 2120 | 1366 | 754 | 9 | healthy, purple_blotch, viral |
| lodo | roboflow_capstone | 6112 | 1038 | 1544 | 858 | 686 | 8 | downy_mildew, healthy, purple_blotch, stemphylium |
| lodo | roboflow_onionnet | 3844 | 633 | 4217 | 4095 | 122 | 10 | downy_mildew, healthy, purple_blotch |
| inner | cold|tom2024_onion | 5009 | 752 | 2120 | 1167 | 953 | 8 | healthy, purple_blotch |
| inner | cold|roboflow_capstone | 5407 | 930 | 1544 | 712 | 832 | 7 | downy_mildew, healthy, purple_blotch |
| inner | cold|roboflow_onionnet | 3118 | 546 | 4217 | 4095 | 122 | 10 | downy_mildew, healthy, purple_blotch |
| inner | tom2024_onion|cold | 5009 | 752 | 813 | 534 | 279 | 8 | healthy, purple_blotch, stemphylium |
| inner | tom2024_onion|roboflow_capstone | 4292 | 738 | 1544 | 858 | 686 | 6 | downy_mildew, healthy, purple_blotch, stemphylium |
| inner | tom2024_onion|roboflow_onionnet | 2019 | 338 | 4217 | 4095 | 122 | 8 | downy_mildew, healthy, purple_blotch |
| inner | roboflow_capstone|cold | 5407 | 930 | 813 | 723 | 90 | 7 | healthy, purple_blotch, viral |
| inner | roboflow_capstone|tom2024_onion | 4292 | 738 | 2120 | 1366 | 754 | 6 | healthy, purple_blotch, viral |
| inner | roboflow_capstone|roboflow_onionnet | 2514 | 419 | 4217 | 2939 | 1278 | 6 | healthy, purple_blotch |
| inner | roboflow_onionnet|cold | 3118 | 546 | 813 | 813 | 0 | 10 | healthy, purple_blotch, stemphylium, viral |
| inner | roboflow_onionnet|tom2024_onion | 2019 | 338 | 2120 | 1366 | 754 | 8 | healthy, purple_blotch, viral |
| inner | roboflow_onionnet|roboflow_capstone | 2514 | 419 | 1544 | 596 | 948 | 6 | healthy, purple_blotch, stemphylium |
| cv | fold0 | 5956 | 1023 | 1715 | 1715 | 0 | 11 | botrytis, bulb_blight, burn_tip, downy_mildew, fusarium, healthy, purple_blotch, rust, stemphylium, viral, xanthomonas |
| cv | fold1 | 6106 | 964 | 1624 | 1624 | 0 | 11 | botrytis, bulb_blight, burn_tip, downy_mildew, fusarium, healthy, purple_blotch, rust, stemphylium, viral, xanthomonas |
| cv | fold2 | 5954 | 1001 | 1739 | 1739 | 0 | 11 | botrytis, bulb_blight, burn_tip, downy_mildew, fusarium, healthy, purple_blotch, rust, stemphylium, viral, xanthomonas |
| cv | fold3 | 5906 | 984 | 1804 | 1804 | 0 | 11 | botrytis, bulb_blight, burn_tip, downy_mildew, fusarium, healthy, purple_blotch, rust, stemphylium, viral, xanthomonas |
| cv | fold4 | 5968 | 914 | 1812 | 1812 | 0 | 11 | botrytis, bulb_blight, burn_tip, downy_mildew, fusarium, healthy, purple_blotch, rust, stemphylium, viral, xanthomonas |

## D1 - acquisition metadata by source (median)

| dataset | native_long | native_short | file_kb | jpeg_qstep | sharpness | saturation | green_frac |
|---|---|---|---|---|---|---|---|
| cold | 256.00 | 256.00 | 19.35 | 5.77 | -7.70 | 0.37 | 0.46 |
| roboflow_capstone | 377.00 | 189.50 | 22.76 | 5.77 | -7.06 | 0.38 | 0.64 |
| roboflow_onionnet | 178.00 | 101.00 | 5.81 | 5.77 | -9.18 | 0.30 | 0.68 |
| tom2024_onion | 206.00 | 206.00 | 9.81 | 29.03 | -5.96 | 0.28 | 0.31 |

## D1 - what metadata alone can predict (balanced accuracy, grouped CV)

| target | subset | balanced_acc | chance | n | above_chance |
|---|---|---|---|---|---|
| source | all images | 0.910 | 0.250 | 8694 | 0.660 |
| source | within healthy | 0.955 | 0.250 | 3436 | 0.705 |
| source | within purple_blotch | 0.931 | 0.250 | 1564 | 0.681 |
| disease | within source cold | 0.308 | 0.250 | 813 | 0.058 |
| disease | within source tom2024_onion | 0.477 | 0.200 | 2120 | 0.277 |
| disease | within source roboflow_capstone | 0.340 | 0.143 | 1544 | 0.198 |
| disease | within source roboflow_onionnet | 0.645 | 0.250 | 4217 | 0.395 |

## D2 - source / disease identifiability from DINOv3-B global features (balanced accuracy, grouped CV)

| target | subset | probe | class-cond. LEACE | global LEACE | raw | chance |
|---|---|---|---|---|---|---|
| disease | all images | linear | 0.720 | 0.674 | 0.742 | 0.091 |
| source | all images | MLP | 0.908 | 0.901 | 0.923 | 0.250 |
| source | all images | linear | 0.592 | 0.258 | 0.916 | 0.250 |
| source | within healthy | MLP | 0.918 | 0.935 | 0.951 | 0.250 |
| source | within healthy | linear | 0.877 | 0.905 | 0.956 | 0.250 |
| source | within purple_blotch | MLP | 0.812 | 0.811 | 0.937 | 0.250 |
| source | within purple_blotch | linear | 0.805 | 0.777 | 0.938 | 0.250 |

## D3 - label-consistency index per class (mean over source pairs; > 0 = same name, same look)

| cls | raw | source-centred | pairs | verdict |
|---|---|---|---|---|
| downy_mildew | 0.302 | 0.150 | 2 | consistent |
| healthy | 0.158 | 0.466 | 12 | consistent |
| purple_blotch | -0.080 | 0.139 | 12 | style-shifted (consistent after centring) |
| stemphylium | -0.372 | 0.052 | 2 | style-shifted (consistent after centring) |
| viral | -0.158 | 0.109 | 2 | style-shifted (consistent after centring) |

## D3 - nearest-centroid transfer between sources (shared classes only)

| train_src | test_src | raw | source-centred |
|---|---|---|---|
| cold | roboflow_capstone | 0.541 | 0.608 |
| cold | roboflow_onionnet | 0.676 | 0.844 |
| cold | tom2024_onion | 0.548 | 0.635 |
| roboflow_capstone | cold | 0.341 | 0.340 |
| roboflow_capstone | roboflow_onionnet | 0.522 | 0.572 |
| roboflow_capstone | tom2024_onion | 0.696 | 0.858 |
| roboflow_onionnet | cold | 0.573 | 0.482 |
| roboflow_onionnet | roboflow_capstone | 0.615 | 0.629 |
| roboflow_onionnet | tom2024_onion | 0.900 | 0.918 |
| tom2024_onion | cold | 0.361 | 0.374 |
| tom2024_onion | roboflow_capstone | 0.915 | 0.905 |
| tom2024_onion | roboflow_onionnet | 0.822 | 0.832 |

## RQ2 - LODO macro-F1 on held-out ID classes, all models (mean ± sd over seeds)

| model | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion | mean | seeds |
|---|---|---|---|---|---|---|
| ViTS | 0.299 ± 0.005 | 0.457 ± 0.016 | 0.761 ± 0.019 | 0.401 ± 0.014 | 0.480 | 3 |
| ViTS-kNN | 0.295 ± 0.008 | 0.451 ± 0.009 | 0.751 ± 0.059 | 0.421 ± 0.007 | 0.479 | 3 |
| ConvNeXtT | 0.319 ± 0.003 | 0.45 ± 0.012 | 0.714 ± 0.004 | 0.403 ± 0.01 | 0.471 | 3 |
| DG:MixStyle | 0.308 ± 0.019 | 0.44 ± 0.004 | 0.651 ± 0.008 | 0.397 ± 0.01 | 0.449 | 3 |
| FM:DINOv3-B | 0.273 ± 0.0 | 0.431 ± 0.0 | 0.612 ± 0.0 | 0.473 ± 0.0 | 0.447 | 1 |
| MobileNetV3L | 0.306 ± 0.0 | 0.411 ± 0.0 | 0.585 ± 0.0 | 0.458 ± 0.0 | 0.440 | 1 |
| MIL+GE@DINOv3-B | 0.287 ± 0.007 | 0.423 ± 0.008 | 0.616 ± 0.021 | 0.431 ± 0.043 | 0.439 | 10 |
| DG:SWA | 0.337 ± 0.006 | 0.426 ± 0.011 | 0.604 ± 0.019 | 0.372 ± 0.003 | 0.435 | 3 |
| SERA@DINOv3-B | 0.269 ± 0.007 | 0.429 ± 0.006 | 0.594 ± 0.012 | 0.44 ± 0.025 | 0.433 | 10 |
| EfficientNetB0 | 0.334 ± 0.022 | 0.436 ± 0.014 | 0.598 ± 0.021 | 0.357 ± 0.023 | 0.431 | 3 |
| FM:DINOv2-B | 0.291 ± 0.0 | 0.419 ± 0.0 | 0.616 ± 0.0 | 0.399 ± 0.0 | 0.431 | 1 |
| FM:BioCLIP-2 | 0.379 ± 0.0 | 0.446 ± 0.0 | 0.544 ± 0.0 | 0.354 ± 0.0 | 0.431 | 1 |
| DG:AmpMix+Cons | 0.315 ± 0.0 | 0.447 ± 0.0 | 0.597 ± 0.0 | 0.357 ± 0.0 | 0.429 | 1 |
| LP-global+CCE@DINOv3-B | 0.243 ± 0.007 | 0.408 ± 0.006 | 0.619 ± 0.013 | 0.445 ± 0.013 | 0.429 | 10 |
| SILA-Net | 0.331 ± 0.0 | 0.424 ± 0.0 | 0.646 ± 0.0 | 0.316 ± 0.0 | 0.429 | 1 |
| LP-global@DINOv3-B | 0.26 ± 0.006 | 0.413 ± 0.004 | 0.591 ± 0.018 | 0.432 ± 0.016 | 0.424 | 10 |
| LP-global+FMM@DINOv3-B | 0.243 ± 0.006 | 0.432 ± 0.005 | 0.55 ± 0.012 | 0.467 ± 0.009 | 0.423 | 10 |
| MIL@DINOv3-B | 0.251 ± 0.008 | 0.426 ± 0.005 | 0.594 ± 0.022 | 0.406 ± 0.013 | 0.419 | 10 |
| LP-global@BioCLIP-2 | 0.366 ± 0.007 | 0.446 ± 0.005 | 0.516 ± 0.017 | 0.341 ± 0.01 | 0.417 | 10 |
| LP-global@DINOv3-S | 0.273 ± 0.006 | 0.387 ± 0.005 | 0.542 ± 0.023 | 0.463 ± 0.015 | 0.416 | 10 |
| ResNet50 | 0.316 ± 0.005 | 0.434 ± 0.017 | 0.526 ± 0.02 | 0.371 ± 0.009 | 0.412 | 2 |
| SERA-5@DINOv3-S | 0.256 ± 0.01 | 0.399 ± 0.006 | 0.531 ± 0.021 | 0.392 ± 0.012 | 0.395 | 10 |
| SERA@BioCLIP-2 | 0.354 ± 0.025 | 0.402 ± 0.012 | 0.49 ± 0.018 | 0.311 ± 0.01 | 0.389 | 10 |
| SERA@DINOv3-S | 0.256 ± 0.006 | 0.403 ± 0.008 | 0.528 ± 0.029 | 0.371 ± 0.012 | 0.389 | 10 |
| LP-mean@DINOv3-B | 0.226 ± 0.005 | 0.358 ± 0.006 | 0.439 ± 0.013 | 0.457 ± 0.013 | 0.370 | 10 |

## RQ2 - SERA ablation on DINOv3-B (LODO macro-F1)

| model | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion | mean | seeds |
|---|---|---|---|---|---|---|
| LP-global@DINOv3-B | 0.26 ± 0.006 | 0.413 ± 0.004 | 0.591 ± 0.018 | 0.432 ± 0.016 | 0.424 | 10 |
| LP-global+FMM@DINOv3-B | 0.243 ± 0.006 | 0.432 ± 0.005 | 0.55 ± 0.012 | 0.467 ± 0.009 | 0.423 | 10 |
| LP-mean@DINOv3-B | 0.226 ± 0.005 | 0.358 ± 0.006 | 0.439 ± 0.013 | 0.457 ± 0.013 | 0.370 | 10 |
| MIL@DINOv3-B | 0.251 ± 0.008 | 0.426 ± 0.005 | 0.594 ± 0.022 | 0.406 ± 0.013 | 0.419 | 10 |
| LP-global+CCE@DINOv3-B | 0.243 ± 0.007 | 0.408 ± 0.006 | 0.619 ± 0.013 | 0.445 ± 0.013 | 0.429 | 10 |
| MIL+GE@DINOv3-B | 0.287 ± 0.007 | 0.423 ± 0.008 | 0.616 ± 0.021 | 0.431 ± 0.043 | 0.439 | 10 |
| SERA@DINOv3-B | 0.269 ± 0.007 | 0.429 ± 0.006 | 0.594 ± 0.012 | 0.44 ± 0.025 | 0.433 | 10 |

## RQ2 - does SERA help every encoder? (LODO macro-F1)

| model | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion | mean | seeds |
|---|---|---|---|---|---|---|
| SERA@DINOv3-B | 0.269 ± 0.007 | 0.429 ± 0.006 | 0.594 ± 0.012 | 0.44 ± 0.025 | 0.433 | 10 |
| LP-global@DINOv3-B | 0.26 ± 0.006 | 0.413 ± 0.004 | 0.591 ± 0.018 | 0.432 ± 0.016 | 0.424 | 10 |
| LP-global@BioCLIP-2 | 0.366 ± 0.007 | 0.446 ± 0.005 | 0.516 ± 0.017 | 0.341 ± 0.01 | 0.417 | 10 |
| LP-global@DINOv3-S | 0.273 ± 0.006 | 0.387 ± 0.005 | 0.542 ± 0.023 | 0.463 ± 0.015 | 0.416 | 10 |
| SERA-5@DINOv3-S | 0.256 ± 0.01 | 0.399 ± 0.006 | 0.531 ± 0.021 | 0.392 ± 0.012 | 0.395 | 10 |
| SERA@BioCLIP-2 | 0.354 ± 0.025 | 0.402 ± 0.012 | 0.49 ± 0.018 | 0.311 ± 0.01 | 0.389 | 10 |
| SERA@DINOv3-S | 0.256 ± 0.006 | 0.403 ± 0.008 | 0.528 ± 0.029 | 0.371 ± 0.012 | 0.389 | 10 |

## RQ1 - in-domain minus LODO macro-F1 (percentage points)

| model | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion | mean |
|---|---|---|---|---|---|
| LP-global@DINOv3-B | 30.0 | 22.3 | 29.6 | 48.7 | 32.6 |
| FM:DINOv3-B | 42.4 | 20.4 | 28.1 | 45.4 | 34.1 |
| FM:BioCLIP-2 | 33.2 | 17.5 | 30.7 | 56.1 | 34.4 |
| SERA@DINOv3-B | 39.1 | 24.1 | 28.3 | 49.2 | 35.2 |
| FM:DINOv2-B | 40.4 | 22.5 | 26.3 | 52.5 | 35.4 |
| SILA-Net | 45.3 | 19.9 | 26.2 | 59.8 | 37.8 |
| ConvNeXtT | 53.5 | 24.8 | 22.0 | 54.2 | 38.6 |
| MobileNetV3L | 49.0 | 25.1 | 33.6 | 47.1 | 38.7 |
| ViTS | 57.3 | 27.0 | 18.9 | 55.3 | 39.6 |
| EfficientNetB0 | 45.2 | 25.7 | 32.8 | 57.6 | 40.3 |
| ResNet50 | 48.5 | 22.3 | 37.5 | 56.8 | 41.3 |

## Statistics - SERA@DINOv3-B minus each model (hierarchical bootstrap over photo groups and seeds)

| baseline | diff_macro_f1 | ci_low | ci_high | p_bootstrap | wilcoxon_p | paired_runs | held_out_sets | p_bootstrap_holm | ci_excludes_0 | significant |
|---|---|---|---|---|---|---|---|---|---|---|
| ViTS | -0.0464 | -0.0620 | -0.0318 | 0.0000 | 0.2036 | 12 | 4 | 0.0000 | True | True |
| ViTS-kNN | -0.0463 | -0.0673 | -0.0243 | 0.0000 | 0.1294 | 12 | 4 | 0.0000 | True | True |
| ConvNeXtT | -0.0383 | -0.0520 | -0.0240 | 0.0000 | 0.1099 | 12 | 4 | 0.0000 | True | True |
| DG:MixStyle | -0.0160 | -0.0328 | 0.0009 | 0.0760 | 0.3394 | 12 | 4 | 0.9120 | False | False |
| FM:DINOv3-B | -0.0140 | -0.0285 | 0.0007 | 0.0660 | nan | 4 | 4 | 0.8580 | False | False |
| MobileNetV3L | -0.0068 | -0.0235 | 0.0110 | 0.4840 | nan | 4 | 4 | 1.0000 | False | False |
| MIL+GE@DINOv3-B | -0.0061 | -0.0178 | 0.0043 | 0.2720 | 0.0566 | 40 | 4 | 1.0000 | False | False |
| DG:SWA | -0.0016 | -0.0189 | 0.0152 | 0.8640 | 0.9697 | 12 | 4 | 1.0000 | False | False |
| EfficientNetB0 | 0.0017 | -0.0168 | 0.0198 | 0.8360 | 0.9697 | 12 | 4 | 1.0000 | False | False |
| FM:DINOv2-B | 0.0019 | -0.0137 | 0.0187 | 0.8220 | nan | 4 | 4 | 1.0000 | False | False |
| FM:BioCLIP-2 | 0.0024 | -0.0137 | 0.0205 | 0.7900 | nan | 4 | 4 | 1.0000 | False | False |
| SILA-Net | 0.0038 | -0.0123 | 0.0220 | 0.6520 | nan | 4 | 4 | 1.0000 | False | False |
| DG:AmpMix+Cons | 0.0041 | -0.0109 | 0.0211 | 0.6120 | nan | 4 | 4 | 1.0000 | False | False |
| LP-global+CCE@DINOv3-B | 0.0043 | -0.0087 | 0.0186 | 0.5100 | 0.1744 | 40 | 4 | 1.0000 | False | False |
| LP-global@DINOv3-B | 0.0090 | -0.0034 | 0.0222 | 0.1620 | 0.0012 | 40 | 4 | 1.0000 | False | False |
| LP-global+FMM@DINOv3-B | 0.0102 | -0.0063 | 0.0257 | 0.2300 | 0.0250 | 40 | 4 | 1.0000 | False | False |
| MIL@DINOv3-B | 0.0140 | 0.0050 | 0.0235 | 0.0020 | 0.0004 | 40 | 4 | 0.0340 | True | True |
| LP-global@BioCLIP-2 | 0.0159 | -0.0002 | 0.0319 | 0.0600 | 0.2591 | 40 | 4 | 0.8400 | False | False |
| LP-global@DINOv3-S | 0.0171 | 0.0037 | 0.0308 | 0.0160 | 0.0079 | 40 | 4 | 0.2560 | True | False |
| ResNet50 | 0.0213 | 0.0037 | 0.0394 | 0.0200 | 0.2500 | 8 | 4 | 0.3000 | True | False |
| SERA-5@DINOv3-S | 0.0386 | 0.0255 | 0.0509 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |
| SERA@DINOv3-S | 0.0437 | 0.0310 | 0.0558 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |
| SERA@BioCLIP-2 | 0.0443 | 0.0301 | 0.0601 | 0.0000 | 0.0035 | 40 | 4 | 0.0000 | True | True |
| LP-mean@DINOv3-B | 0.0630 | 0.0501 | 0.0760 | 0.0000 | 0.0000 | 40 | 4 | 0.0000 | True | True |

## Per-class F1 on held-out sets (focus models, mean over seeds)

| model | held_out | F1_healthy | F1_purple_blotch | F1_stemphylium | F1_viral | F1_downy_mildew |
|---|---|---|---|---|---|---|
| LP-global+CCE@DINOv3-B | cold | 0.789 | 0.177 | 0.004 | 0.003 | nan |
| LP-global+CCE@DINOv3-B | roboflow_capstone | 0.801 | 0.246 | 0.000 | nan | 0.586 |
| LP-global+CCE@DINOv3-B | roboflow_onionnet | 0.741 | 0.517 | nan | nan | 0.600 |
| LP-global+CCE@DINOv3-B | tom2024_onion | 0.953 | 0.114 | nan | 0.268 | nan |
| LP-global@DINOv3-B | cold | 0.788 | 0.227 | 0.002 | 0.021 | nan |
| LP-global@DINOv3-B | roboflow_capstone | 0.820 | 0.231 | 0.000 | nan | 0.603 |
| LP-global@DINOv3-B | roboflow_onionnet | 0.743 | 0.429 | nan | nan | 0.600 |
| LP-global@DINOv3-B | tom2024_onion | 0.961 | 0.152 | nan | 0.184 | nan |
| MIL@DINOv3-B | cold | 0.757 | 0.230 | 0.000 | 0.015 | nan |
| MIL@DINOv3-B | roboflow_capstone | 0.843 | 0.264 | 0.000 | nan | 0.597 |
| MIL@DINOv3-B | roboflow_onionnet | 0.661 | 0.538 | nan | nan | 0.584 |
| MIL@DINOv3-B | tom2024_onion | 0.920 | 0.211 | nan | 0.086 | nan |
| SERA@DINOv3-B | cold | 0.773 | 0.293 | 0.002 | 0.006 | nan |
| SERA@DINOv3-B | roboflow_capstone | 0.842 | 0.279 | 0.000 | nan | 0.597 |
| SERA@DINOv3-B | roboflow_onionnet | 0.645 | 0.585 | nan | nan | 0.552 |
| SERA@DINOv3-B | tom2024_onion | 0.930 | 0.137 | nan | 0.254 | nan |
| SILA-Net | cold | 0.811 | 0.426 | 0.089 | 0.000 | nan |
| SILA-Net | roboflow_capstone | 0.776 | 0.317 | 0.000 | nan | 0.604 |
| SILA-Net | roboflow_onionnet | 0.714 | 0.677 | nan | nan | 0.547 |
| SILA-Net | tom2024_onion | 0.851 | 0.077 | nan | 0.019 | nan |
| ViTS | cold | 0.875 | 0.320 | 0.000 | 0.002 | nan |
| ViTS | roboflow_capstone | 0.900 | 0.305 | 0.000 | nan | 0.623 |
| ViTS | roboflow_onionnet | 0.874 | 0.716 | nan | nan | 0.693 |
| ViTS | tom2024_onion | 0.928 | 0.233 | nan | 0.041 | nan |

## RQ3 - gate summary for SERA@DINOv3-B (target risk eps = 5%; mean over held-out sets and seeds)

| score | calibration | accept | accept_id | risk | violation_rate | wrong_among_issued | withheld_unseen | runs |
|---|---|---|---|---|---|---|---|---|
| - | no gate | 1.000 | 1.000 | 0.544 | 1.000 | 0.544 | 0.000 | 12 |
| MSP | LOSO-CRC | 0.163 | 0.185 | 0.051 | 0.250 | 0.233 | 0.896 | 12 |
| MSP | LOSO-CRC-worst | 0.101 | 0.112 | 0.036 | 0.250 | 0.207 | 0.921 | 12 |
| MSP | val-CRC | 0.549 | 0.570 | 0.245 | 1.000 | 0.409 | 0.557 | 12 |
| Remedy | LOSO-CRC | 0.149 | 0.171 | 0.047 | 0.250 | 0.252 | 0.907 | 12 |
| Remedy | LOSO-CRC-worst | 0.082 | 0.091 | 0.028 | 0.250 | 0.223 | 0.937 | 12 |
| Remedy | val-CRC | 0.545 | 0.570 | 0.240 | 1.000 | 0.398 | 0.574 | 12 |
| Remedy+kNN | LOSO-CRC | 0.189 | 0.230 | 0.040 | 0.333 | 0.211 | 0.936 | 12 |
| Remedy+kNN | LOSO-CRC-worst | 0.127 | 0.162 | 0.021 | 0.000 | 0.161 | 0.963 | 12 |
| Remedy+kNN | val-CRC | 0.530 | 0.553 | 0.237 | 0.833 | 0.398 | 0.602 | 12 |
| Remedy-set | CP-remedy(val) | 0.723 | 0.738 | 0.360 | 1.000 | 0.463 | 0.403 | 12 |
| kNN | LOSO-CRC | 0.141 | 0.166 | 0.034 | 0.250 | 0.277 | 0.982 | 12 |
| kNN | LOSO-CRC-worst | 0.047 | 0.060 | 0.006 | 0.000 | 0.202 | 0.996 | 12 |
| kNN | val-CRC | 0.461 | 0.497 | 0.203 | 0.750 | 0.426 | 0.738 | 12 |

## RQ3 - gate summary, all focus models

| model | score | calibration | accept | accept_id | risk | violation_rate | wrong_among_issued | withheld_unseen | runs |
|---|---|---|---|---|---|---|---|---|---|
| ConvNeXtT | - | no gate | 1.000 | 1.000 | 0.488 | 1.000 | 0.488 | 0.000 | 12 |
| ConvNeXtT | MSP | val-CRC | 0.737 | 0.756 | 0.315 | 1.000 | 0.392 | 0.412 | 12 |
| ConvNeXtT | Remedy | val-CRC | 0.753 | 0.774 | 0.322 | 1.000 | 0.393 | 0.407 | 12 |
| ConvNeXtT | Remedy-set | CP-remedy(val) | 0.838 | 0.854 | 0.364 | 1.000 | 0.443 | 0.236 | 12 |
| EfficientNetB0 | - | no gate | 1.000 | 1.000 | 0.540 | 1.000 | 0.540 | 0.000 | 4 |
| EfficientNetB0 | MSP | LOSO-CRC | 0.184 | 0.192 | 0.055 | 0.250 | 0.259 | 0.885 | 4 |
| EfficientNetB0 | MSP | LOSO-CRC-worst | 0.137 | 0.141 | 0.046 | 0.250 | 0.300 | 0.890 | 4 |
| EfficientNetB0 | MSP | val-CRC | 0.622 | 0.644 | 0.277 | 1.000 | 0.423 | 0.486 | 4 |
| EfficientNetB0 | Remedy | LOSO-CRC | 0.180 | 0.187 | 0.054 | 0.250 | 0.250 | 0.882 | 4 |
| EfficientNetB0 | Remedy | LOSO-CRC-worst | 0.126 | 0.130 | 0.043 | 0.250 | 0.303 | 0.899 | 4 |
| EfficientNetB0 | Remedy | val-CRC | 0.640 | 0.663 | 0.284 | 1.000 | 0.423 | 0.462 | 4 |
| EfficientNetB0 | Remedy-set | CP-remedy(val) | 0.824 | 0.837 | 0.411 | 1.000 | 0.492 | 0.265 | 4 |
| FM:DINOv2-B | - | no gate | 1.000 | 1.000 | 0.546 | 1.000 | 0.546 | 0.000 | 4 |
| FM:DINOv2-B | MSP | LOSO-CRC | 0.148 | 0.161 | 0.043 | 0.250 | 0.217 | 0.905 | 4 |
| FM:DINOv2-B | MSP | LOSO-CRC-worst | 0.081 | 0.084 | 0.027 | 0.250 | 0.203 | 0.936 | 4 |
| FM:DINOv2-B | MSP | val-CRC | 0.511 | 0.535 | 0.210 | 1.000 | 0.382 | 0.591 | 4 |
| FM:DINOv2-B | Remedy | LOSO-CRC | 0.144 | 0.156 | 0.041 | 0.250 | 0.220 | 0.909 | 4 |
| FM:DINOv2-B | Remedy | LOSO-CRC-worst | 0.068 | 0.069 | 0.022 | 0.250 | 0.206 | 0.953 | 4 |
| FM:DINOv2-B | Remedy | val-CRC | 0.507 | 0.532 | 0.205 | 1.000 | 0.372 | 0.608 | 4 |
| FM:DINOv2-B | Remedy-set | CP-remedy(val) | 0.739 | 0.758 | 0.367 | 1.000 | 0.467 | 0.401 | 4 |
| FM:DINOv3-B | - | no gate | 1.000 | 1.000 | 0.514 | 1.000 | 0.514 | 0.000 | 4 |
| FM:DINOv3-B | MSP | val-CRC | 0.525 | 0.557 | 0.197 | 1.000 | 0.341 | 0.598 | 4 |
| FM:DINOv3-B | Remedy | val-CRC | 0.520 | 0.551 | 0.191 | 1.000 | 0.330 | 0.606 | 4 |
| FM:DINOv3-B | Remedy-set | CP-remedy(val) | 0.723 | 0.745 | 0.329 | 1.000 | 0.425 | 0.407 | 4 |
| LP-global+CCE@DINOv3-B | - | no gate | 1.000 | 1.000 | 0.536 | 1.000 | 0.536 | 0.000 | 40 |
| LP-global+CCE@DINOv3-B | MSP | val-CRC | 0.531 | 0.564 | 0.214 | 1.000 | 0.362 | 0.602 | 40 |
| LP-global+CCE@DINOv3-B | Remedy | val-CRC | 0.536 | 0.572 | 0.212 | 1.000 | 0.350 | 0.616 | 40 |
| LP-global+CCE@DINOv3-B | Remedy+kNN | val-CRC | 0.455 | 0.499 | 0.175 | 0.950 | 0.351 | 0.711 | 40 |
| LP-global+CCE@DINOv3-B | Remedy-set | CP-remedy(val) | 0.701 | 0.725 | 0.333 | 1.000 | 0.436 | 0.452 | 40 |
| LP-global+CCE@DINOv3-B | kNN | val-CRC | 0.374 | 0.391 | 0.163 | 0.750 | 0.415 | 0.772 | 40 |
| LP-global@DINOv3-B | - | no gate | 1.000 | 1.000 | 0.538 | 1.000 | 0.538 | 0.000 | 12 |
| LP-global@DINOv3-B | MSP | LOSO-CRC | 0.184 | 0.207 | 0.061 | 0.250 | 0.188 | 0.883 | 12 |
| LP-global@DINOv3-B | MSP | LOSO-CRC-worst | 0.094 | 0.098 | 0.040 | 0.250 | 0.174 | 0.919 | 12 |
| LP-global@DINOv3-B | MSP | val-CRC | 0.520 | 0.550 | 0.209 | 1.000 | 0.358 | 0.600 | 12 |
| LP-global@DINOv3-B | Remedy | LOSO-CRC | 0.175 | 0.196 | 0.058 | 0.250 | 0.190 | 0.887 | 12 |
| LP-global@DINOv3-B | Remedy | LOSO-CRC-worst | 0.079 | 0.082 | 0.034 | 0.250 | 0.173 | 0.930 | 12 |
| LP-global@DINOv3-B | Remedy | val-CRC | 0.526 | 0.560 | 0.206 | 1.000 | 0.348 | 0.616 | 12 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.204 | 0.248 | 0.036 | 0.250 | 0.197 | 0.928 | 12 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.140 | 0.178 | 0.017 | 0.000 | 0.141 | 0.972 | 12 |
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.425 | 0.462 | 0.158 | 0.833 | 0.356 | 0.745 | 12 |
| LP-global@DINOv3-B | Remedy-set | CP-remedy(val) | 0.712 | 0.734 | 0.341 | 1.000 | 0.443 | 0.419 | 12 |
| LP-global@DINOv3-B | kNN | LOSO-CRC | 0.116 | 0.124 | 0.041 | 0.500 | 0.325 | 0.923 | 12 |
| LP-global@DINOv3-B | kNN | LOSO-CRC-worst | 0.033 | 0.043 | 0.006 | 0.000 | 0.217 | 0.995 | 12 |
| LP-global@DINOv3-B | kNN | val-CRC | 0.290 | 0.306 | 0.125 | 0.583 | 0.396 | 0.893 | 12 |
| MIL@DINOv3-B | - | no gate | 1.000 | 1.000 | 0.548 | 1.000 | 0.548 | 0.000 | 40 |
| MIL@DINOv3-B | MSP | val-CRC | 0.582 | 0.595 | 0.268 | 1.000 | 0.423 | 0.503 | 40 |
| MIL@DINOv3-B | Remedy | val-CRC | 0.593 | 0.611 | 0.271 | 1.000 | 0.420 | 0.519 | 40 |
| MIL@DINOv3-B | Remedy+kNN | val-CRC | 0.511 | 0.528 | 0.228 | 0.875 | 0.415 | 0.622 | 40 |
| MIL@DINOv3-B | Remedy-set | CP-remedy(val) | 0.753 | 0.765 | 0.382 | 1.000 | 0.475 | 0.355 | 40 |
| MIL@DINOv3-B | kNN | val-CRC | 0.376 | 0.394 | 0.167 | 0.775 | 0.443 | 0.807 | 40 |
| SERA@DINOv3-B | - | no gate | 1.000 | 1.000 | 0.544 | 1.000 | 0.544 | 0.000 | 12 |
| SERA@DINOv3-B | MSP | LOSO-CRC | 0.163 | 0.185 | 0.051 | 0.250 | 0.233 | 0.896 | 12 |
| SERA@DINOv3-B | MSP | LOSO-CRC-worst | 0.101 | 0.112 | 0.036 | 0.250 | 0.207 | 0.921 | 12 |
| SERA@DINOv3-B | MSP | val-CRC | 0.549 | 0.570 | 0.245 | 1.000 | 0.409 | 0.557 | 12 |
| SERA@DINOv3-B | Remedy | LOSO-CRC | 0.149 | 0.171 | 0.047 | 0.250 | 0.252 | 0.907 | 12 |
| SERA@DINOv3-B | Remedy | LOSO-CRC-worst | 0.082 | 0.091 | 0.028 | 0.250 | 0.223 | 0.937 | 12 |
| SERA@DINOv3-B | Remedy | val-CRC | 0.545 | 0.570 | 0.240 | 1.000 | 0.398 | 0.574 | 12 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.189 | 0.230 | 0.040 | 0.333 | 0.211 | 0.936 | 12 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.127 | 0.162 | 0.021 | 0.000 | 0.161 | 0.963 | 12 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.530 | 0.553 | 0.237 | 0.833 | 0.398 | 0.602 | 12 |
| SERA@DINOv3-B | Remedy-set | CP-remedy(val) | 0.723 | 0.738 | 0.360 | 1.000 | 0.463 | 0.403 | 12 |
| SERA@DINOv3-B | kNN | LOSO-CRC | 0.141 | 0.166 | 0.034 | 0.250 | 0.277 | 0.982 | 12 |
| SERA@DINOv3-B | kNN | LOSO-CRC-worst | 0.047 | 0.060 | 0.006 | 0.000 | 0.202 | 0.996 | 12 |
| SERA@DINOv3-B | kNN | val-CRC | 0.461 | 0.497 | 0.203 | 0.750 | 0.426 | 0.738 | 12 |
| SERA@DINOv3-S | - | no gate | 1.000 | 1.000 | 0.561 | 1.000 | 0.561 | 0.000 | 12 |
| SERA@DINOv3-S | MSP | LOSO-CRC | 0.156 | 0.171 | 0.060 | 0.250 | 0.276 | 0.876 | 12 |
| SERA@DINOv3-S | MSP | LOSO-CRC-worst | 0.112 | 0.121 | 0.047 | 0.250 | 0.263 | 0.909 | 12 |
| SERA@DINOv3-S | MSP | val-CRC | 0.555 | 0.577 | 0.261 | 1.000 | 0.438 | 0.519 | 12 |
| SERA@DINOv3-S | Remedy | LOSO-CRC | 0.143 | 0.156 | 0.054 | 0.250 | 0.279 | 0.892 | 12 |
| SERA@DINOv3-S | Remedy | LOSO-CRC-worst | 0.090 | 0.099 | 0.035 | 0.250 | 0.260 | 0.933 | 12 |
| SERA@DINOv3-S | Remedy | val-CRC | 0.554 | 0.579 | 0.252 | 1.000 | 0.422 | 0.529 | 12 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.192 | 0.227 | 0.052 | 0.500 | 0.235 | 0.926 | 12 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.130 | 0.158 | 0.030 | 0.333 | 0.184 | 0.955 | 12 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.521 | 0.550 | 0.236 | 1.000 | 0.403 | 0.633 | 12 |
| SERA@DINOv3-S | Remedy-set | CP-remedy(val) | 0.755 | 0.771 | 0.388 | 1.000 | 0.495 | 0.322 | 12 |
| SERA@DINOv3-S | kNN | LOSO-CRC | 0.140 | 0.160 | 0.040 | 0.333 | 0.233 | 0.970 | 12 |
| SERA@DINOv3-S | kNN | LOSO-CRC-worst | 0.073 | 0.085 | 0.016 | 0.083 | 0.175 | 0.987 | 12 |
| SERA@DINOv3-S | kNN | val-CRC | 0.457 | 0.493 | 0.211 | 0.750 | 0.414 | 0.729 | 12 |
| SILA-Net | - | no gate | 1.000 | 1.000 | 0.532 | 1.000 | 0.532 | 0.000 | 4 |
| SILA-Net | MSP | LOSO-CRC | 0.231 | 0.236 | 0.087 | 0.500 | 0.262 | 0.842 | 4 |
| SILA-Net | MSP | LOSO-CRC-worst | 0.189 | 0.189 | 0.072 | 0.500 | 0.249 | 0.865 | 4 |
| SILA-Net | MSP | val-CRC | 0.606 | 0.628 | 0.262 | 1.000 | 0.393 | 0.529 | 4 |
| SILA-Net | Remedy | LOSO-CRC | 0.226 | 0.230 | 0.087 | 0.500 | 0.268 | 0.844 | 4 |
| SILA-Net | Remedy | LOSO-CRC-worst | 0.183 | 0.182 | 0.073 | 0.500 | 0.263 | 0.865 | 4 |
| SILA-Net | Remedy | val-CRC | 0.621 | 0.646 | 0.271 | 1.000 | 0.397 | 0.552 | 4 |
| SILA-Net | Remedy-set | CP-remedy(val) | 0.865 | 0.872 | 0.440 | 1.000 | 0.501 | 0.207 | 4 |
| ViTS | - | no gate | 1.000 | 1.000 | 0.464 | 1.000 | 0.464 | 0.000 | 12 |
| ViTS | MSP | val-CRC | 0.801 | 0.821 | 0.338 | 1.000 | 0.396 | 0.351 | 12 |
| ViTS | Remedy | val-CRC | 0.809 | 0.834 | 0.335 | 1.000 | 0.390 | 0.367 | 12 |
| ViTS | Remedy-set | CP-remedy(val) | 0.784 | 0.819 | 0.298 | 1.000 | 0.393 | 0.365 | 12 |
| ViTS-kNN | - | no gate | 1.000 | 1.000 | 0.465 | 1.000 | 0.465 | 0.000 | 12 |
| ViTS-kNN | MSP | LOSO-CRC | 0.253 | 0.274 | 0.070 | 0.250 | 0.188 | 0.852 | 12 |
| ViTS-kNN | MSP | LOSO-CRC-worst | 0.136 | 0.147 | 0.052 | 0.250 | 0.209 | 0.882 | 12 |
| ViTS-kNN | MSP | val-CRC | 0.790 | 0.813 | 0.333 | 1.000 | 0.392 | 0.388 | 12 |
| ViTS-kNN | Remedy | LOSO-CRC | 0.225 | 0.243 | 0.071 | 0.250 | 0.212 | 0.859 | 12 |
| ViTS-kNN | Remedy | LOSO-CRC-worst | 0.122 | 0.132 | 0.049 | 0.250 | 0.264 | 0.890 | 12 |
| ViTS-kNN | Remedy | val-CRC | 0.809 | 0.834 | 0.340 | 1.000 | 0.391 | 0.383 | 12 |
| ViTS-kNN | Remedy+kNN | LOSO-CRC | 0.325 | 0.363 | 0.072 | 0.500 | 0.179 | 0.874 | 12 |
| ViTS-kNN | Remedy+kNN | LOSO-CRC-worst | 0.242 | 0.271 | 0.045 | 0.333 | 0.153 | 0.925 | 12 |
| ViTS-kNN | Remedy+kNN | val-CRC | 0.766 | 0.794 | 0.322 | 0.833 | 0.379 | 0.433 | 12 |
| ViTS-kNN | Remedy-set | CP-remedy(val) | 0.791 | 0.825 | 0.305 | 1.000 | 0.398 | 0.351 | 12 |
| ViTS-kNN | kNN | LOSO-CRC | 0.317 | 0.356 | 0.068 | 0.500 | 0.172 | 0.889 | 12 |
| ViTS-kNN | kNN | LOSO-CRC-worst | 0.244 | 0.280 | 0.035 | 0.333 | 0.131 | 0.952 | 12 |
| ViTS-kNN | kNN | val-CRC | 0.712 | 0.741 | 0.305 | 0.750 | 0.365 | 0.489 | 12 |

## RQ3 - ranking quality of the risk scores (lower AURC / wrong-at-matched-acceptance is better)

| model | score | aurc | auroc_unseen | wrong_among_issued@30% | wrong_among_issued@50% |
|---|---|---|---|---|---|
| ConvNeXtT | MSP | 0.327 | 0.632 | 0.230 | 0.307 |
| ConvNeXtT | Remedy | 0.332 | 0.643 | 0.241 | 0.303 |
| EfficientNetB0 | MSP | 0.386 | 0.579 | 0.309 | 0.388 |
| EfficientNetB0 | Remedy | 0.384 | 0.582 | 0.309 | 0.381 |
| FM:DINOv2-B | MSP | 0.385 | 0.595 | 0.315 | 0.394 |
| FM:DINOv2-B | Remedy | 0.380 | 0.602 | 0.312 | 0.387 |
| FM:DINOv3-B | MSP | 0.340 | 0.605 | 0.261 | 0.349 |
| FM:DINOv3-B | Remedy | 0.337 | 0.614 | 0.259 | 0.343 |
| LP-global+CCE@DINOv3-B | MSP | 0.365 | 0.614 | 0.275 | 0.375 |
| LP-global+CCE@DINOv3-B | Remedy | 0.358 | 0.632 | 0.270 | 0.364 |
| LP-global+CCE@DINOv3-B | Remedy+kNN | 0.342 | 0.623 | 0.266 | 0.367 |
| LP-global+CCE@DINOv3-B | kNN | 0.415 | 0.533 | 0.390 | 0.442 |
| LP-global@DINOv3-B | MSP | 0.362 | 0.630 | 0.265 | 0.372 |
| LP-global@DINOv3-B | Remedy | 0.355 | 0.647 | 0.260 | 0.362 |
| LP-global@DINOv3-B | Remedy+kNN | 0.345 | 0.629 | 0.259 | 0.370 |
| LP-global@DINOv3-B | kNN | 0.438 | 0.524 | 0.416 | 0.460 |
| MIL@DINOv3-B | MSP | 0.371 | 0.604 | 0.286 | 0.399 |
| MIL@DINOv3-B | Remedy | 0.370 | 0.618 | 0.290 | 0.394 |
| MIL@DINOv3-B | Remedy+kNN | 0.368 | 0.610 | 0.294 | 0.397 |
| MIL@DINOv3-B | kNN | 0.435 | 0.586 | 0.403 | 0.444 |
| SERA@DINOv3-B | MSP | 0.388 | 0.590 | 0.310 | 0.407 |
| SERA@DINOv3-B | Remedy | 0.388 | 0.603 | 0.314 | 0.399 |
| SERA@DINOv3-B | Remedy+kNN | 0.360 | 0.623 | 0.275 | 0.391 |
| SERA@DINOv3-B | kNN | 0.393 | 0.625 | 0.331 | 0.409 |
| SERA@DINOv3-S | MSP | 0.423 | 0.581 | 0.357 | 0.439 |
| SERA@DINOv3-S | Remedy | 0.415 | 0.595 | 0.349 | 0.423 |
| SERA@DINOv3-S | Remedy+kNN | 0.378 | 0.636 | 0.303 | 0.411 |
| SERA@DINOv3-S | kNN | 0.398 | 0.641 | 0.345 | 0.427 |
| SILA-Net | MSP | 0.383 | 0.572 | 0.311 | 0.383 |
| SILA-Net | Remedy | 0.385 | 0.593 | 0.317 | 0.376 |
| ViTS | MSP | 0.302 | 0.663 | 0.196 | 0.278 |
| ViTS | Remedy | 0.310 | 0.677 | 0.217 | 0.280 |
| ViTS-kNN | MSP | 0.300 | 0.667 | 0.193 | 0.281 |
| ViTS-kNN | Remedy | 0.306 | 0.679 | 0.210 | 0.282 |
| ViTS-kNN | Remedy+kNN | 0.266 | 0.688 | 0.168 | 0.277 |
| ViTS-kNN | kNN | 0.260 | 0.685 | 0.162 | 0.272 |

## RQ3 headline (SERA@DINOv3-B)

- no gate: wrong-remedy risk **54.4%** of all held-out images
- MSP / val-CRC: risk 24.5% (violations 100% of runs), accepts 55% of images, 41% of issued remedies wrong, withholds 56% of unseen diseases
- Remedy / val-CRC: risk 24.0% (violations 100% of runs), accepts 55% of images, 40% of issued remedies wrong, withholds 57% of unseen diseases
- Remedy-set / CP-remedy(val): risk 36.0% (violations 100% of runs), accepts 72% of images, 46% of issued remedies wrong, withholds 40% of unseen diseases
- Remedy / LOSO-CRC: risk 4.7% (violations 25% of runs), accepts 15% of images, 25% of issued remedies wrong, withholds 91% of unseen diseases
- Remedy+kNN / LOSO-CRC: risk 4.0% (violations 33% of runs), accepts 19% of images, 21% of issued remedies wrong, withholds 94% of unseen diseases
- Remedy+kNN / LOSO-CRC-worst: risk 2.1% (violations 0% of runs), accepts 13% of images, 16% of issued remedies wrong, withholds 96% of unseen diseases
- v1 reference (SILA-Net, cross-source conformal level): accepted 11%, 23% of issued remedies wrong

## Worked cases (UNVERIFIED action templates)

| held_out | case | true | top_disease | issued_group | decision | u_risk | lam |
|---|---|---|---|---|---|---|---|
| cold | issued & right | stemphylium | botrytis | fungal_foliar | ISSUE | 0.538 | 0.549 |
| cold | withheld (would have been wrong) | viral | healthy | none | WITHHOLD | 0.737 | 0.549 |
| cold | issued & WRONG (failure) | viral | healthy | none | ISSUE | 0.314 | 0.549 |
| tom2024_onion | issued & right | purple_blotch | stemphylium | fungal_foliar | ISSUE | 0.502 | 0.506 |
| tom2024_onion | withheld (would have been wrong) | purple_blotch | downy_mildew | oomycete | WITHHOLD | 0.853 | 0.506 |
| tom2024_onion | withheld unseen disease | bulb_blight | viral | vector_control | WITHHOLD | 1.000 | 0.506 |
| tom2024_onion | issued & WRONG (failure) | purple_blotch | healthy | none | ISSUE | 0.451 | 0.506 |
| roboflow_capstone | issued & right | botrytis | purple_blotch | fungal_foliar | ISSUE | 0.576 | 0.705 |
| roboflow_capstone | withheld (would have been wrong) | botrytis | downy_mildew | oomycete | WITHHOLD | 0.850 | 0.705 |
| roboflow_capstone | withheld unseen disease | botrytis | downy_mildew | oomycete | WITHHOLD | 0.850 | 0.705 |
| roboflow_capstone | issued & WRONG (failure) | botrytis | downy_mildew | oomycete | ISSUE | 0.561 | 0.705 |
| roboflow_onionnet | issued & right | downy_mildew | downy_mildew | oomycete | ISSUE | 0.548 | 0.551 |
| roboflow_onionnet | withheld (would have been wrong) | burn_tip | fusarium | soilborne | WITHHOLD | 0.875 | 0.551 |
| roboflow_onionnet | withheld unseen disease | burn_tip | fusarium | soilborne | WITHHOLD | 0.875 | 0.551 |
| roboflow_onionnet | issued & WRONG (failure) | burn_tip | fusarium | soilborne | ISSUE | 0.537 | 0.551 |

## RQ3b - risk / acceptance at several risk targets: LP-global@DINOv3-B (mean over held-out sources and seeds)

| score | calibration | eps=5% | eps=10% | eps=15% | eps=20% |
|---|---|---|---|---|---|
| Remedy+kNN | val-CRC | 0.158 / 0.43 | 0.355 / 0.71 | 0.464 / 0.87 | 0.538 / 1.00 |
| Remedy+kNN | W-CRC | 0.134 / 0.38 | 0.230 / 0.54 | 0.344 / 0.69 | 0.418 / 0.80 |
| Remedy+kNN | Robust-CRC(rho=0.01) | 0.063 / 0.26 | 0.205 / 0.50 | 0.368 / 0.73 | 0.459 / 0.86 |
| Remedy+kNN | Robust-CRC(rho=0.05) | 0.014 / 0.13 | 0.086 / 0.30 | 0.198 / 0.49 | 0.329 / 0.67 |
| Remedy+kNN | Robust-CRC(rho=0.1) | 0.002 / 0.05 | 0.034 / 0.20 | 0.115 / 0.35 | 0.213 / 0.51 |
| Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.008 / 0.10 | 0.036 / 0.20 | 0.105 / 0.34 |
| Remedy+kNN | LOSO-CRC (2 src) | 0.040 / 0.21 | 0.085 / 0.31 | 0.139 / 0.41 | 0.196 / 0.51 |
| Remedy+kNN | LOSO-CRC | 0.036 / 0.20 | 0.080 / 0.31 | 0.133 / 0.40 | 0.192 / 0.51 |
| Remedy+kNN | LOSO-CRC-worst | 0.017 / 0.14 | 0.043 / 0.22 | 0.077 / 0.30 | 0.116 / 0.37 |
| Remedy+kNN | LOSO+LCO-CRC | 0.021 / 0.16 | 0.050 / 0.24 | 0.086 / 0.32 | 0.132 / 0.41 |
| Remedy+kNN | LOSO+LCO-CRC-worst | 0.004 / 0.06 | 0.010 / 0.10 | 0.017 / 0.13 | 0.024 / 0.16 |
| kNN | val-CRC | 0.125 / 0.29 | 0.389 / 0.71 | 0.479 / 0.87 | 0.538 / 1.00 |
| kNN | W-CRC | 0.077 / 0.19 | 0.213 / 0.43 | 0.347 / 0.65 | 0.418 / 0.77 |
| kNN | Robust-CRC(rho=0.01) | 0.039 / 0.11 | 0.178 / 0.40 | 0.407 / 0.74 | 0.476 / 0.87 |
| kNN | Robust-CRC(rho=0.05) | 0.001 / 0.01 | 0.059 / 0.15 | 0.171 / 0.38 | 0.351 / 0.66 |
| kNN | Robust-CRC(rho=0.1) | 0.000 / 0.00 | 0.019 / 0.06 | 0.078 / 0.19 | 0.187 / 0.41 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.000 / 0.00 | 0.022 / 0.06 | 0.069 / 0.17 |
| kNN | LOSO-CRC (2 src) | 0.061 / 0.15 | 0.114 / 0.27 | 0.159 / 0.36 | 0.207 / 0.46 |
| kNN | LOSO-CRC | 0.042 / 0.12 | 0.102 / 0.24 | 0.155 / 0.36 | 0.215 / 0.48 |
| kNN | LOSO-CRC-worst | 0.007 / 0.03 | 0.023 / 0.08 | 0.049 / 0.13 | 0.078 / 0.20 |
| kNN | LOSO+LCO-CRC | 0.029 / 0.09 | 0.087 / 0.21 | 0.132 / 0.30 | 0.182 / 0.41 |
| kNN | LOSO+LCO-CRC-worst | 0.001 / 0.00 | 0.002 / 0.02 | 0.008 / 0.04 | 0.025 / 0.08 |

## RQ3b - risk / acceptance at several risk targets: SERA@DINOv3-B (mean over held-out sources and seeds)

| score | calibration | eps=5% | eps=10% | eps=15% | eps=20% |
|---|---|---|---|---|---|
| Remedy+kNN | val-CRC | 0.237 / 0.53 | 0.388 / 0.76 | 0.487 / 0.91 | 0.544 / 1.00 |
| Remedy+kNN | W-CRC | 0.182 / 0.46 | 0.296 / 0.63 | 0.380 / 0.76 | 0.455 / 0.86 |
| Remedy+kNN | Robust-CRC(rho=0.01) | 0.121 / 0.35 | 0.282 / 0.60 | 0.397 / 0.78 | 0.482 / 0.90 |
| Remedy+kNN | Robust-CRC(rho=0.05) | 0.034 / 0.17 | 0.150 / 0.40 | 0.277 / 0.59 | 0.380 / 0.75 |
| Remedy+kNN | Robust-CRC(rho=0.1) | 0.008 / 0.07 | 0.082 / 0.27 | 0.180 / 0.45 | 0.288 / 0.61 |
| Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.019 / 0.12 | 0.089 / 0.29 | 0.169 / 0.43 |
| Remedy+kNN | LOSO-CRC (2 src) | 0.045 / 0.20 | 0.091 / 0.30 | 0.142 / 0.39 | 0.196 / 0.48 |
| Remedy+kNN | LOSO-CRC | 0.040 / 0.19 | 0.087 / 0.29 | 0.136 / 0.39 | 0.191 / 0.47 |
| Remedy+kNN | LOSO-CRC-worst | 0.021 / 0.13 | 0.049 / 0.21 | 0.077 / 0.28 | 0.114 / 0.35 |
| Remedy+kNN | LOSO+LCO-CRC | 0.033 / 0.17 | 0.068 / 0.25 | 0.107 / 0.33 | 0.150 / 0.41 |
| Remedy+kNN | LOSO+LCO-CRC-worst | 0.011 / 0.08 | 0.023 / 0.13 | 0.035 / 0.17 | 0.049 / 0.21 |
| kNN | val-CRC | 0.203 / 0.46 | 0.411 / 0.77 | 0.486 / 0.90 | 0.544 / 1.00 |
| kNN | W-CRC | 0.106 / 0.30 | 0.255 / 0.57 | 0.374 / 0.74 | 0.456 / 0.85 |
| kNN | Robust-CRC(rho=0.01) | 0.080 / 0.24 | 0.271 / 0.56 | 0.419 / 0.79 | 0.484 / 0.90 |
| kNN | Robust-CRC(rho=0.05) | 0.012 / 0.07 | 0.116 / 0.31 | 0.257 / 0.54 | 0.402 / 0.75 |
| kNN | Robust-CRC(rho=0.1) | 0.000 / 0.01 | 0.044 / 0.16 | 0.147 / 0.37 | 0.283 / 0.58 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.003 / 0.03 | 0.047 / 0.17 | 0.132 / 0.34 |
| kNN | LOSO-CRC (2 src) | 0.047 / 0.16 | 0.096 / 0.27 | 0.146 / 0.37 | 0.195 / 0.46 |
| kNN | LOSO-CRC | 0.035 / 0.14 | 0.090 / 0.26 | 0.139 / 0.36 | 0.183 / 0.44 |
| kNN | LOSO-CRC-worst | 0.007 / 0.05 | 0.025 / 0.11 | 0.055 / 0.19 | 0.085 / 0.25 |
| kNN | LOSO+LCO-CRC | 0.039 / 0.15 | 0.089 / 0.26 | 0.132 / 0.34 | 0.171 / 0.41 |
| kNN | LOSO+LCO-CRC-worst | 0.001 / 0.01 | 0.006 / 0.04 | 0.022 / 0.10 | 0.046 / 0.16 |

## RQ3b - risk / acceptance at several risk targets: SERA@DINOv3-S (mean over held-out sources and seeds)

| score | calibration | eps=5% | eps=10% | eps=15% | eps=20% |
|---|---|---|---|---|---|
| Remedy+kNN | val-CRC | 0.236 / 0.52 | 0.397 / 0.76 | 0.513 / 0.93 | 0.561 / 1.00 |
| Remedy+kNN | W-CRC | 0.187 / 0.46 | 0.317 / 0.66 | 0.404 / 0.78 | 0.481 / 0.88 |
| Remedy+kNN | Robust-CRC(rho=0.01) | 0.131 / 0.35 | 0.287 / 0.60 | 0.408 / 0.78 | 0.510 / 0.93 |
| Remedy+kNN | Robust-CRC(rho=0.05) | 0.051 / 0.18 | 0.157 / 0.40 | 0.281 / 0.59 | 0.384 / 0.75 |
| Remedy+kNN | Robust-CRC(rho=0.1) | 0.006 / 0.06 | 0.088 / 0.27 | 0.192 / 0.45 | 0.295 / 0.61 |
| Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.030 / 0.13 | 0.093 / 0.28 | 0.174 / 0.42 |
| Remedy+kNN | LOSO-CRC (2 src) | 0.055 / 0.20 | 0.108 / 0.31 | 0.161 / 0.41 | 0.216 / 0.50 |
| Remedy+kNN | LOSO-CRC | 0.052 / 0.19 | 0.100 / 0.30 | 0.157 / 0.41 | 0.212 / 0.50 |
| Remedy+kNN | LOSO-CRC-worst | 0.030 / 0.13 | 0.064 / 0.22 | 0.098 / 0.30 | 0.138 / 0.37 |
| Remedy+kNN | LOSO+LCO-CRC | 0.037 / 0.16 | 0.074 / 0.25 | 0.116 / 0.34 | 0.166 / 0.42 |
| Remedy+kNN | LOSO+LCO-CRC-worst | 0.009 / 0.07 | 0.020 / 0.10 | 0.029 / 0.13 | 0.040 / 0.17 |
| kNN | val-CRC | 0.211 / 0.46 | 0.402 / 0.75 | 0.511 / 0.92 | 0.561 / 1.00 |
| kNN | W-CRC | 0.142 / 0.35 | 0.297 / 0.61 | 0.411 / 0.78 | 0.488 / 0.89 |
| kNN | Robust-CRC(rho=0.01) | 0.057 / 0.19 | 0.269 / 0.55 | 0.411 / 0.76 | 0.505 / 0.91 |
| kNN | Robust-CRC(rho=0.05) | 0.001 / 0.02 | 0.094 / 0.26 | 0.261 / 0.53 | 0.389 / 0.73 |
| kNN | Robust-CRC(rho=0.1) | 0.000 / 0.00 | 0.025 / 0.11 | 0.138 / 0.34 | 0.278 / 0.56 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.000 / 0.01 | 0.029 / 0.12 | 0.115 / 0.30 |
| kNN | LOSO-CRC (2 src) | 0.054 / 0.17 | 0.103 / 0.27 | 0.151 / 0.36 | 0.203 / 0.46 |
| kNN | LOSO-CRC | 0.040 / 0.14 | 0.088 / 0.25 | 0.145 / 0.35 | 0.199 / 0.46 |
| kNN | LOSO-CRC-worst | 0.016 / 0.07 | 0.041 / 0.14 | 0.065 / 0.19 | 0.094 / 0.25 |
| kNN | LOSO+LCO-CRC | 0.028 / 0.11 | 0.074 / 0.22 | 0.127 / 0.32 | 0.182 / 0.42 |
| kNN | LOSO+LCO-CRC-worst | 0.002 / 0.02 | 0.008 / 0.05 | 0.017 / 0.08 | 0.030 / 0.12 |

## RQ3b - risk / acceptance at several risk targets: ViTS-kNN (mean over held-out sources and seeds)

| score | calibration | eps=5% | eps=10% | eps=15% | eps=20% |
|---|---|---|---|---|---|
| Remedy+kNN | val-CRC | 0.324 / 0.77 | 0.445 / 0.97 | 0.465 / 1.00 | 0.465 / 1.00 |
| Remedy+kNN | W-CRC | 0.202 / 0.58 | 0.313 / 0.76 | 0.406 / 0.90 | 0.432 / 0.94 |
| Remedy+kNN | Robust-CRC(rho=0.01) | 0.167 / 0.52 | 0.388 / 0.86 | 0.454 / 0.98 | 0.465 / 1.00 |
| Remedy+kNN | Robust-CRC(rho=0.05) | 0.054 / 0.31 | 0.210 / 0.59 | 0.380 / 0.85 | 0.435 / 0.95 |
| Remedy+kNN | Robust-CRC(rho=0.1) | 0.015 / 0.16 | 0.119 / 0.44 | 0.251 / 0.65 | 0.404 / 0.88 |
| Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.034 / 0.26 | 0.121 / 0.45 | 0.230 / 0.62 |
| Remedy+kNN | LOSO-CRC (2 src) | 0.074 / 0.33 | 0.119 / 0.44 | 0.161 / 0.52 | 0.203 / 0.59 |
| Remedy+kNN | LOSO-CRC | 0.072 / 0.33 | 0.114 / 0.43 | 0.156 / 0.51 | 0.194 / 0.58 |
| Remedy+kNN | LOSO-CRC-worst | 0.045 / 0.24 | 0.085 / 0.34 | 0.113 / 0.41 | 0.140 / 0.46 |
| kNN | val-CRC | 0.305 / 0.71 | 0.440 / 0.96 | 0.465 / 1.00 | 0.465 / 1.00 |
| kNN | W-CRC | 0.180 / 0.54 | 0.306 / 0.73 | 0.405 / 0.88 | 0.431 / 0.94 |
| kNN | Robust-CRC(rho=0.01) | 0.129 / 0.45 | 0.384 / 0.83 | 0.451 / 0.97 | 0.465 / 1.00 |
| kNN | Robust-CRC(rho=0.05) | 0.030 / 0.26 | 0.175 / 0.52 | 0.377 / 0.82 | 0.432 / 0.94 |
| kNN | Robust-CRC(rho=0.1) | 0.015 / 0.19 | 0.077 / 0.36 | 0.215 / 0.58 | 0.399 / 0.85 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.023 / 0.23 | 0.083 / 0.37 | 0.194 / 0.55 |
| kNN | LOSO-CRC (2 src) | 0.070 / 0.33 | 0.120 / 0.42 | 0.165 / 0.50 | 0.201 / 0.57 |
| kNN | LOSO-CRC | 0.068 / 0.32 | 0.116 / 0.41 | 0.158 / 0.49 | 0.197 / 0.56 |
| kNN | LOSO-CRC-worst | 0.035 / 0.24 | 0.084 / 0.34 | 0.117 / 0.40 | 0.144 / 0.45 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: LP-global@DINOv3-B

| eps | calibration | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion |
|---|---|---|---|---|---|
| 0.050 | LOSO+LCO-CRC | 0.030 / 0.25 | 0.025 / 0.11 | 0.007 / 0.04 | 0.021 / 0.23 |
| 0.050 | LOSO+LCO-CRC-worst | 0.005 / 0.10 | 0.008 / 0.06 | 0.000 / 0.00 | 0.002 / 0.09 |
| 0.050 | LOSO-CRC | 0.036 / 0.27 | 0.054 / 0.18 | 0.017 / 0.08 | 0.039 / 0.29 |
| 0.050 | LOSO-CRC-worst | 0.021 / 0.20 | 0.021 / 0.10 | 0.006 / 0.04 | 0.021 / 0.23 |
| 0.050 | W-CRC | 0.146 / 0.51 | 0.271 / 0.49 | 0.043 / 0.16 | 0.076 / 0.37 |
| 0.050 | val-CRC | 0.200 / 0.59 | 0.268 / 0.49 | 0.049 / 0.18 | 0.115 / 0.44 |
| 0.100 | LOSO+LCO-CRC | 0.052 / 0.33 | 0.061 / 0.19 | 0.031 / 0.12 | 0.056 / 0.33 |
| 0.100 | LOSO+LCO-CRC-worst | 0.015 / 0.16 | 0.019 / 0.09 | 0.001 / 0.01 | 0.006 / 0.14 |
| 0.100 | LOSO-CRC | 0.064 / 0.36 | 0.117 / 0.28 | 0.056 / 0.20 | 0.081 / 0.39 |
| 0.100 | LOSO-CRC-worst | 0.045 / 0.31 | 0.057 / 0.18 | 0.019 / 0.08 | 0.053 / 0.32 |
| 0.100 | W-CRC | 0.293 / 0.71 | 0.403 / 0.67 | 0.089 / 0.29 | 0.138 / 0.49 |
| 0.100 | val-CRC | 0.400 / 0.83 | 0.655 / 0.98 | 0.126 / 0.39 | 0.241 / 0.64 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: SERA@DINOv3-B

| eps | calibration | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion |
|---|---|---|---|---|---|
| 0.050 | LOSO+LCO-CRC | 0.059 / 0.26 | 0.043 / 0.12 | 0.002 / 0.03 | 0.027 / 0.27 |
| 0.050 | LOSO+LCO-CRC-worst | 0.023 / 0.14 | 0.016 / 0.06 | 0.000 / 0.01 | 0.004 / 0.13 |
| 0.050 | LOSO-CRC | 0.063 / 0.26 | 0.059 / 0.16 | 0.005 / 0.04 | 0.035 / 0.29 |
| 0.050 | LOSO-CRC-worst | 0.026 / 0.15 | 0.037 / 0.11 | 0.001 / 0.02 | 0.019 / 0.23 |
| 0.050 | W-CRC | 0.218 / 0.56 | 0.299 / 0.54 | 0.060 / 0.24 | 0.153 / 0.49 |
| 0.050 | val-CRC | 0.274 / 0.65 | 0.445 / 0.74 | 0.046 / 0.21 | 0.184 / 0.53 |
| 0.100 | LOSO+LCO-CRC | 0.113 / 0.38 | 0.086 / 0.21 | 0.011 / 0.07 | 0.062 / 0.35 |
| 0.100 | LOSO+LCO-CRC-worst | 0.053 / 0.24 | 0.031 / 0.10 | 0.001 / 0.02 | 0.008 / 0.17 |
| 0.100 | LOSO-CRC | 0.125 / 0.41 | 0.123 / 0.27 | 0.019 / 0.11 | 0.080 / 0.38 |
| 0.100 | LOSO-CRC-worst | 0.070 / 0.28 | 0.082 / 0.20 | 0.009 / 0.07 | 0.035 / 0.29 |
| 0.100 | W-CRC | 0.331 / 0.73 | 0.484 / 0.79 | 0.111 / 0.37 | 0.256 / 0.64 |
| 0.100 | val-CRC | 0.431 / 0.88 | 0.652 / 1.00 | 0.135 / 0.42 | 0.335 / 0.74 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: SERA@DINOv3-S

| eps | calibration | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion |
|---|---|---|---|---|---|
| 0.050 | LOSO+LCO-CRC | 0.060 / 0.25 | 0.074 / 0.18 | 0.003 / 0.03 | 0.013 / 0.17 |
| 0.050 | LOSO+LCO-CRC-worst | 0.018 / 0.13 | 0.016 / 0.06 | 0.001 / 0.01 | 0.001 / 0.06 |
| 0.050 | LOSO-CRC | 0.078 / 0.29 | 0.106 / 0.24 | 0.004 / 0.03 | 0.020 / 0.21 |
| 0.050 | LOSO-CRC-worst | 0.040 / 0.19 | 0.070 / 0.17 | 0.001 / 0.02 | 0.008 / 0.14 |
| 0.050 | W-CRC | 0.175 / 0.48 | 0.357 / 0.60 | 0.091 / 0.31 | 0.124 / 0.44 |
| 0.050 | val-CRC | 0.262 / 0.62 | 0.487 / 0.77 | 0.073 / 0.26 | 0.124 / 0.44 |
| 0.100 | LOSO+LCO-CRC | 0.111 / 0.37 | 0.136 / 0.28 | 0.015 / 0.08 | 0.033 / 0.27 |
| 0.100 | LOSO+LCO-CRC-worst | 0.038 / 0.19 | 0.037 / 0.11 | 0.002 / 0.02 | 0.003 / 0.09 |
| 0.100 | LOSO-CRC | 0.132 / 0.41 | 0.203 / 0.38 | 0.023 / 0.11 | 0.044 / 0.30 |
| 0.100 | LOSO-CRC-worst | 0.092 / 0.32 | 0.132 / 0.28 | 0.007 / 0.05 | 0.024 / 0.23 |
| 0.100 | W-CRC | 0.325 / 0.71 | 0.543 / 0.84 | 0.169 / 0.47 | 0.233 / 0.61 |
| 0.100 | val-CRC | 0.430 / 0.85 | 0.666 / 1.00 | 0.189 / 0.51 | 0.301 / 0.70 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: ViTS-kNN

| eps | calibration | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion |
|---|---|---|---|---|---|
| 0.050 | LOSO-CRC | 0.071 / 0.51 | 0.211 / 0.39 | 0.003 / 0.18 | 0.004 / 0.23 |
| 0.050 | LOSO-CRC-worst | 0.048 / 0.45 | 0.132 / 0.26 | 0.001 / 0.10 | 0.000 / 0.16 |
| 0.050 | W-CRC | 0.238 / 0.76 | 0.401 / 0.67 | 0.023 / 0.41 | 0.146 / 0.49 |
| 0.050 | val-CRC | 0.335 / 0.88 | 0.609 / 0.97 | 0.042 / 0.51 | 0.311 / 0.71 |
| 0.100 | LOSO-CRC | 0.114 / 0.59 | 0.318 / 0.54 | 0.009 / 0.29 | 0.015 / 0.30 |
| 0.100 | LOSO-CRC-worst | 0.076 / 0.52 | 0.257 / 0.45 | 0.002 / 0.17 | 0.003 / 0.21 |
| 0.100 | W-CRC | 0.362 / 0.91 | 0.543 / 0.87 | 0.054 / 0.56 | 0.294 / 0.69 |
| 0.100 | val-CRC | 0.431 / 1.00 | 0.634 / 1.00 | 0.175 / 0.87 | 0.538 / 1.00 |

## RQ3b - gate risk and acceptance with 95% bootstrap intervals (Remedy+kNN)

| model | calibration | eps | risk [95% CI] | accept [95% CI] |
|---|---|---|---|---|
| LP-global@DINOv3-B | val-CRC | 0.050 | 0.158 [0.147, 0.170] | 0.43 [0.41, 0.44] |
| LP-global@DINOv3-B | val-CRC | 0.100 | 0.355 [0.340, 0.369] | 0.71 [0.70, 0.72] |
| LP-global@DINOv3-B | W-CRC | 0.050 | 0.134 [0.123, 0.145] | 0.38 [0.37, 0.40] |
| LP-global@DINOv3-B | W-CRC | 0.100 | 0.230 [0.217, 0.243] | 0.54 [0.52, 0.55] |
| LP-global@DINOv3-B | LOSO-CRC | 0.050 | 0.036 [0.031, 0.042] | 0.20 [0.19, 0.22] |
| LP-global@DINOv3-B | LOSO-CRC | 0.100 | 0.080 [0.072, 0.087] | 0.31 [0.29, 0.32] |
| LP-global@DINOv3-B | LOSO-CRC-worst | 0.050 | 0.017 [0.014, 0.020] | 0.14 [0.13, 0.15] |
| LP-global@DINOv3-B | LOSO-CRC-worst | 0.100 | 0.043 [0.038, 0.049] | 0.22 [0.21, 0.24] |
| LP-global@DINOv3-B | LOSO+LCO-CRC | 0.050 | 0.021 [0.017, 0.025] | 0.16 [0.15, 0.17] |
| LP-global@DINOv3-B | LOSO+LCO-CRC | 0.100 | 0.050 [0.044, 0.056] | 0.24 [0.23, 0.26] |
| LP-global@DINOv3-B | LOSO+LCO-CRC-worst | 0.050 | 0.004 [0.002, 0.005] | 0.06 [0.06, 0.07] |
| LP-global@DINOv3-B | LOSO+LCO-CRC-worst | 0.100 | 0.010 [0.008, 0.013] | 0.10 [0.09, 0.11] |
| SERA@DINOv3-B | val-CRC | 0.050 | 0.237 [0.225, 0.250] | 0.53 [0.52, 0.54] |
| SERA@DINOv3-B | val-CRC | 0.100 | 0.388 [0.372, 0.403] | 0.76 [0.75, 0.77] |
| SERA@DINOv3-B | W-CRC | 0.050 | 0.182 [0.172, 0.193] | 0.46 [0.45, 0.47] |
| SERA@DINOv3-B | W-CRC | 0.100 | 0.296 [0.282, 0.309] | 0.63 [0.62, 0.64] |
| SERA@DINOv3-B | LOSO-CRC | 0.050 | 0.040 [0.035, 0.046] | 0.19 [0.18, 0.20] |
| SERA@DINOv3-B | LOSO-CRC | 0.100 | 0.087 [0.079, 0.094] | 0.29 [0.28, 0.30] |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.050 | 0.021 [0.017, 0.025] | 0.13 [0.12, 0.14] |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.100 | 0.049 [0.043, 0.055] | 0.21 [0.20, 0.22] |
| SERA@DINOv3-B | LOSO+LCO-CRC | 0.050 | 0.033 [0.028, 0.038] | 0.17 [0.16, 0.18] |
| SERA@DINOv3-B | LOSO+LCO-CRC | 0.100 | 0.068 [0.060, 0.075] | 0.25 [0.24, 0.26] |
| SERA@DINOv3-B | LOSO+LCO-CRC-worst | 0.050 | 0.011 [0.008, 0.014] | 0.08 [0.08, 0.09] |
| SERA@DINOv3-B | LOSO+LCO-CRC-worst | 0.100 | 0.023 [0.019, 0.028] | 0.13 [0.12, 0.14] |
| SERA@DINOv3-S | val-CRC | 0.050 | 0.236 [0.223, 0.250] | 0.52 [0.51, 0.53] |
| SERA@DINOv3-S | val-CRC | 0.100 | 0.397 [0.382, 0.411] | 0.76 [0.76, 0.77] |
| SERA@DINOv3-S | W-CRC | 0.050 | 0.187 [0.176, 0.199] | 0.46 [0.44, 0.47] |
| SERA@DINOv3-S | W-CRC | 0.100 | 0.317 [0.303, 0.331] | 0.66 [0.65, 0.67] |
| SERA@DINOv3-S | LOSO-CRC | 0.050 | 0.052 [0.046, 0.059] | 0.19 [0.18, 0.20] |
| SERA@DINOv3-S | LOSO-CRC | 0.100 | 0.100 [0.092, 0.110] | 0.30 [0.29, 0.31] |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.050 | 0.030 [0.025, 0.036] | 0.13 [0.12, 0.14] |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.100 | 0.064 [0.056, 0.071] | 0.22 [0.21, 0.23] |
| SERA@DINOv3-S | LOSO+LCO-CRC | 0.050 | 0.037 [0.032, 0.044] | 0.16 [0.15, 0.17] |
| SERA@DINOv3-S | LOSO+LCO-CRC | 0.100 | 0.074 [0.066, 0.082] | 0.25 [0.24, 0.26] |
| SERA@DINOv3-S | LOSO+LCO-CRC-worst | 0.050 | 0.009 [0.006, 0.012] | 0.07 [0.06, 0.07] |
| SERA@DINOv3-S | LOSO+LCO-CRC-worst | 0.100 | 0.020 [0.016, 0.025] | 0.10 [0.09, 0.11] |
| ViTS-kNN | val-CRC | 0.050 | 0.324 [0.310, 0.338] | 0.77 [0.76, 0.78] |
| ViTS-kNN | val-CRC | 0.100 | 0.445 [0.429, 0.459] | 0.97 [0.96, 0.97] |
| ViTS-kNN | W-CRC | 0.050 | 0.202 [0.190, 0.215] | 0.58 [0.57, 0.59] |
| ViTS-kNN | W-CRC | 0.100 | 0.313 [0.299, 0.327] | 0.76 [0.75, 0.77] |
| ViTS-kNN | LOSO-CRC | 0.050 | 0.072 [0.063, 0.081] | 0.33 [0.31, 0.34] |
| ViTS-kNN | LOSO-CRC | 0.100 | 0.114 [0.104, 0.125] | 0.43 [0.42, 0.44] |
| ViTS-kNN | LOSO-CRC-worst | 0.050 | 0.045 [0.039, 0.053] | 0.24 [0.23, 0.25] |
| ViTS-kNN | LOSO-CRC-worst | 0.100 | 0.085 [0.075, 0.095] | 0.34 [0.32, 0.35] |

## RQ3b - shift-aware calibrations compared at eps = 5% (mean over held-out sources and seeds)

| model | score | calibration | accept | risk | share_of_runs_over_eps | withheld_unseen |
|---|---|---|---|---|---|---|
| EfficientNetB0 | Energy | val-CRC | 0.485 | 0.202 | 1.000 | 0.644 |
| EfficientNetB0 | Energy | W-CRC | 0.380 | 0.139 | 1.000 | 0.747 |
| EfficientNetB0 | Energy | Robust-CRC(rho=0.01) | 0.315 | 0.111 | 0.750 | 0.812 |
| EfficientNetB0 | Energy | Robust-CRC(rho=0.05) | 0.129 | 0.040 | 0.250 | 0.925 |
| EfficientNetB0 | Energy | Robust-CRC(rho=0.1) | 0.030 | 0.010 | 0.000 | 0.980 |
| EfficientNetB0 | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| EfficientNetB0 | Energy | LOSO-CRC (2 src) | 0.145 | 0.044 | 0.250 | 0.921 |
| EfficientNetB0 | Energy | LOSO-CRC | 0.139 | 0.041 | 0.250 | 0.929 |
| EfficientNetB0 | Energy | LOSO-CRC-worst | 0.070 | 0.021 | 0.250 | 0.957 |
| FM:DINOv2-B | Energy | val-CRC | 0.386 | 0.170 | 1.000 | 0.676 |
| FM:DINOv2-B | Energy | W-CRC | 0.344 | 0.141 | 1.000 | 0.732 |
| FM:DINOv2-B | Energy | Robust-CRC(rho=0.01) | 0.248 | 0.105 | 0.500 | 0.797 |
| FM:DINOv2-B | Energy | Robust-CRC(rho=0.05) | 0.121 | 0.056 | 0.250 | 0.881 |
| FM:DINOv2-B | Energy | Robust-CRC(rho=0.1) | 0.024 | 0.012 | 0.000 | 0.969 |
| FM:DINOv2-B | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| FM:DINOv2-B | Energy | LOSO-CRC (2 src) | 0.130 | 0.055 | 0.250 | 0.890 |
| FM:DINOv2-B | Energy | LOSO-CRC | 0.114 | 0.047 | 0.250 | 0.902 |
| FM:DINOv2-B | Energy | LOSO-CRC-worst | 0.057 | 0.025 | 0.250 | 0.947 |
| LP-global@DINOv3-B | Energy | val-CRC | 0.391 | 0.157 | 0.583 | 0.729 |
| LP-global@DINOv3-B | Energy | W-CRC | 0.338 | 0.130 | 0.667 | 0.782 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.261 | 0.109 | 0.333 | 0.809 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.143 | 0.067 | 0.250 | 0.882 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.056 | 0.033 | 0.250 | 0.938 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| LP-global@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.208 | 0.096 | 0.500 | 0.841 |
| LP-global@DINOv3-B | Energy | LOSO-CRC | 0.177 | 0.087 | 0.500 | 0.860 |
| LP-global@DINOv3-B | Energy | LOSO-CRC-worst | 0.071 | 0.043 | 0.250 | 0.923 |
| LP-global@DINOv3-B | Energy | LOSO+LCO-CRC | 0.147 | 0.071 | 0.417 | 0.886 |
| LP-global@DINOv3-B | Energy | LOSO+LCO-CRC-worst | 0.032 | 0.020 | 0.250 | 0.963 |
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.425 | 0.158 | 0.833 | 0.745 |
| LP-global@DINOv3-B | Remedy+kNN | W-CRC | 0.385 | 0.134 | 0.833 | 0.773 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.264 | 0.063 | 0.750 | 0.884 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.131 | 0.014 | 0.000 | 0.982 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.049 | 0.002 | 0.000 | 0.995 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.211 | 0.040 | 0.250 | 0.921 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.204 | 0.036 | 0.250 | 0.928 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.141 | 0.017 | 0.000 | 0.971 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC | 0.157 | 0.021 | 0.000 | 0.969 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC-worst | 0.062 | 0.004 | 0.000 | 0.993 |
| SERA@DINOv3-B | Energy | val-CRC | 0.481 | 0.210 | 1.000 | 0.590 |
| SERA@DINOv3-B | Energy | W-CRC | 0.376 | 0.151 | 0.833 | 0.717 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.314 | 0.128 | 0.667 | 0.746 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.145 | 0.064 | 0.250 | 0.867 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.059 | 0.030 | 0.250 | 0.937 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.143 | 0.061 | 0.250 | 0.873 |
| SERA@DINOv3-B | Energy | LOSO-CRC | 0.128 | 0.055 | 0.250 | 0.882 |
| SERA@DINOv3-B | Energy | LOSO-CRC-worst | 0.055 | 0.028 | 0.250 | 0.939 |
| SERA@DINOv3-B | Energy | LOSO+LCO-CRC | 0.090 | 0.037 | 0.250 | 0.918 |
| SERA@DINOv3-B | Energy | LOSO+LCO-CRC-worst | 0.013 | 0.007 | 0.000 | 0.988 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.531 | 0.237 | 0.833 | 0.601 |
| SERA@DINOv3-B | Remedy+kNN | W-CRC | 0.459 | 0.182 | 0.917 | 0.686 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.347 | 0.121 | 0.750 | 0.811 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.170 | 0.034 | 0.333 | 0.956 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.068 | 0.008 | 0.000 | 0.998 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.199 | 0.045 | 0.500 | 0.927 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.190 | 0.040 | 0.333 | 0.935 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.129 | 0.021 | 0.000 | 0.963 |
| SERA@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC | 0.169 | 0.033 | 0.250 | 0.953 |
| SERA@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC-worst | 0.084 | 0.011 | 0.000 | 0.987 |
| SERA@DINOv3-S | Energy | val-CRC | 0.516 | 0.249 | 1.000 | 0.484 |
| SERA@DINOv3-S | Energy | W-CRC | 0.407 | 0.181 | 1.000 | 0.646 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.01) | 0.346 | 0.155 | 1.000 | 0.666 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.05) | 0.173 | 0.078 | 0.250 | 0.843 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.1) | 0.068 | 0.033 | 0.250 | 0.939 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-S | Energy | LOSO-CRC (2 src) | 0.162 | 0.081 | 0.250 | 0.835 |
| SERA@DINOv3-S | Energy | LOSO-CRC | 0.156 | 0.079 | 0.250 | 0.840 |
| SERA@DINOv3-S | Energy | LOSO-CRC-worst | 0.095 | 0.051 | 0.250 | 0.906 |
| SERA@DINOv3-S | Energy | LOSO+LCO-CRC | 0.129 | 0.064 | 0.250 | 0.871 |
| SERA@DINOv3-S | Energy | LOSO+LCO-CRC-worst | 0.052 | 0.031 | 0.167 | 0.942 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.521 | 0.236 | 1.000 | 0.633 |
| SERA@DINOv3-S | Remedy+kNN | W-CRC | 0.457 | 0.187 | 1.000 | 0.683 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.01) | 0.351 | 0.131 | 0.667 | 0.788 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.05) | 0.179 | 0.051 | 0.500 | 0.928 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.1) | 0.057 | 0.006 | 0.000 | 0.998 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC (2 src) | 0.200 | 0.055 | 0.500 | 0.919 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.193 | 0.052 | 0.500 | 0.925 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.132 | 0.030 | 0.333 | 0.955 |
| SERA@DINOv3-S | Remedy+kNN | LOSO+LCO-CRC | 0.158 | 0.037 | 0.500 | 0.949 |
| SERA@DINOv3-S | Remedy+kNN | LOSO+LCO-CRC-worst | 0.065 | 0.009 | 0.000 | 0.989 |
| SILA-Net | Energy | val-CRC | 0.375 | 0.194 | 0.750 | 0.600 |
| SILA-Net | Energy | W-CRC | 0.363 | 0.165 | 1.000 | 0.709 |
| SILA-Net | Energy | Robust-CRC(rho=0.01) | 0.199 | 0.127 | 0.750 | 0.737 |
| SILA-Net | Energy | Robust-CRC(rho=0.05) | 0.107 | 0.078 | 0.250 | 0.849 |
| SILA-Net | Energy | Robust-CRC(rho=0.1) | 0.043 | 0.028 | 0.250 | 0.945 |
| SILA-Net | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SILA-Net | Energy | LOSO-CRC (2 src) | 0.189 | 0.124 | 0.500 | 0.736 |
| SILA-Net | Energy | LOSO-CRC | 0.180 | 0.120 | 0.500 | 0.745 |
| SILA-Net | Energy | LOSO-CRC-worst | 0.140 | 0.095 | 0.500 | 0.807 |
| ViTS-kNN | Energy | val-CRC | 0.731 | 0.304 | 0.750 | 0.458 |
| ViTS-kNN | Energy | W-CRC | 0.580 | 0.199 | 0.750 | 0.654 |
| ViTS-kNN | Energy | Robust-CRC(rho=0.01) | 0.514 | 0.169 | 0.750 | 0.689 |
| ViTS-kNN | Energy | Robust-CRC(rho=0.05) | 0.215 | 0.057 | 0.250 | 0.878 |
| ViTS-kNN | Energy | Robust-CRC(rho=0.1) | 0.046 | 0.023 | 0.167 | 0.952 |
| ViTS-kNN | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| ViTS-kNN | Energy | LOSO-CRC (2 src) | 0.223 | 0.066 | 0.333 | 0.875 |
| ViTS-kNN | Energy | LOSO-CRC | 0.194 | 0.061 | 0.333 | 0.878 |
| ViTS-kNN | Energy | LOSO-CRC-worst | 0.133 | 0.047 | 0.333 | 0.906 |
| ViTS-kNN | Remedy+kNN | val-CRC | 0.769 | 0.324 | 0.833 | 0.431 |
| ViTS-kNN | Remedy+kNN | W-CRC | 0.582 | 0.202 | 0.750 | 0.655 |
| ViTS-kNN | Remedy+kNN | Robust-CRC(rho=0.01) | 0.521 | 0.167 | 0.750 | 0.705 |
| ViTS-kNN | Remedy+kNN | Robust-CRC(rho=0.05) | 0.309 | 0.054 | 0.417 | 0.910 |
| ViTS-kNN | Remedy+kNN | Robust-CRC(rho=0.1) | 0.162 | 0.015 | 0.167 | 0.989 |
| ViTS-kNN | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| ViTS-kNN | Remedy+kNN | LOSO-CRC (2 src) | 0.332 | 0.074 | 0.500 | 0.868 |
| ViTS-kNN | Remedy+kNN | LOSO-CRC | 0.325 | 0.072 | 0.500 | 0.874 |
| ViTS-kNN | Remedy+kNN | LOSO-CRC-worst | 0.242 | 0.045 | 0.333 | 0.924 |

## RQ3b - shift-aware calibrations compared at eps = 10% (mean over held-out sources and seeds)

| model | score | calibration | accept | risk | share_of_runs_over_eps | withheld_unseen |
|---|---|---|---|---|---|---|
| EfficientNetB0 | Energy | val-CRC | 0.902 | 0.481 | 1.000 | 0.161 |
| EfficientNetB0 | Energy | W-CRC | 0.572 | 0.254 | 1.000 | 0.579 |
| EfficientNetB0 | Energy | Robust-CRC(rho=0.01) | 0.621 | 0.287 | 1.000 | 0.521 |
| EfficientNetB0 | Energy | Robust-CRC(rho=0.05) | 0.348 | 0.128 | 0.500 | 0.782 |
| EfficientNetB0 | Energy | Robust-CRC(rho=0.1) | 0.245 | 0.081 | 0.250 | 0.856 |
| EfficientNetB0 | Energy | Robust-CRC(rho=0.2) | 0.072 | 0.020 | 0.000 | 0.960 |
| EfficientNetB0 | Energy | LOSO-CRC (2 src) | 0.239 | 0.080 | 0.250 | 0.858 |
| EfficientNetB0 | Energy | LOSO-CRC | 0.237 | 0.080 | 0.250 | 0.860 |
| EfficientNetB0 | Energy | LOSO-CRC-worst | 0.153 | 0.051 | 0.250 | 0.905 |
| FM:DINOv2-B | Energy | val-CRC | 0.705 | 0.349 | 1.000 | 0.384 |
| FM:DINOv2-B | Energy | W-CRC | 0.535 | 0.246 | 1.000 | 0.561 |
| FM:DINOv2-B | Energy | Robust-CRC(rho=0.01) | 0.465 | 0.212 | 0.500 | 0.597 |
| FM:DINOv2-B | Energy | Robust-CRC(rho=0.05) | 0.291 | 0.124 | 0.250 | 0.768 |
| FM:DINOv2-B | Energy | Robust-CRC(rho=0.1) | 0.196 | 0.085 | 0.250 | 0.829 |
| FM:DINOv2-B | Energy | Robust-CRC(rho=0.2) | 0.080 | 0.035 | 0.250 | 0.924 |
| FM:DINOv2-B | Energy | LOSO-CRC (2 src) | 0.229 | 0.098 | 0.250 | 0.810 |
| FM:DINOv2-B | Energy | LOSO-CRC | 0.221 | 0.093 | 0.250 | 0.823 |
| FM:DINOv2-B | Energy | LOSO-CRC-worst | 0.111 | 0.047 | 0.250 | 0.902 |
| LP-global@DINOv3-B | Energy | val-CRC | 0.667 | 0.301 | 1.000 | 0.477 |
| LP-global@DINOv3-B | Energy | W-CRC | 0.474 | 0.208 | 0.750 | 0.646 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.454 | 0.187 | 0.417 | 0.676 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.297 | 0.121 | 0.250 | 0.787 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.203 | 0.089 | 0.250 | 0.845 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.107 | 0.055 | 0.250 | 0.900 |
| LP-global@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.322 | 0.141 | 0.500 | 0.759 |
| LP-global@DINOv3-B | Energy | LOSO-CRC | 0.311 | 0.135 | 0.500 | 0.782 |
| LP-global@DINOv3-B | Energy | LOSO-CRC-worst | 0.156 | 0.081 | 0.250 | 0.864 |
| LP-global@DINOv3-B | Energy | LOSO+LCO-CRC | 0.260 | 0.109 | 0.417 | 0.835 |
| LP-global@DINOv3-B | Energy | LOSO+LCO-CRC-worst | 0.083 | 0.049 | 0.250 | 0.917 |
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.708 | 0.355 | 1.000 | 0.430 |
| LP-global@DINOv3-B | Remedy+kNN | W-CRC | 0.537 | 0.230 | 0.750 | 0.637 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.497 | 0.205 | 0.750 | 0.673 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.304 | 0.086 | 0.500 | 0.850 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.197 | 0.034 | 0.000 | 0.942 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.099 | 0.008 | 0.000 | 0.989 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.312 | 0.085 | 0.250 | 0.831 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.306 | 0.080 | 0.250 | 0.843 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.224 | 0.043 | 0.000 | 0.915 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC | 0.244 | 0.050 | 0.000 | 0.902 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC-worst | 0.102 | 0.010 | 0.000 | 0.985 |
| SERA@DINOv3-B | Energy | val-CRC | 0.775 | 0.396 | 1.000 | 0.299 |
| SERA@DINOv3-B | Energy | W-CRC | 0.589 | 0.286 | 0.750 | 0.480 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.553 | 0.253 | 0.917 | 0.509 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.359 | 0.148 | 0.250 | 0.704 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.249 | 0.100 | 0.250 | 0.800 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.110 | 0.051 | 0.250 | 0.892 |
| SERA@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.255 | 0.103 | 0.250 | 0.797 |
| SERA@DINOv3-B | Energy | LOSO-CRC | 0.246 | 0.099 | 0.250 | 0.806 |
| SERA@DINOv3-B | Energy | LOSO-CRC-worst | 0.127 | 0.053 | 0.250 | 0.884 |
| SERA@DINOv3-B | Energy | LOSO+LCO-CRC | 0.196 | 0.073 | 0.250 | 0.854 |
| SERA@DINOv3-B | Energy | LOSO+LCO-CRC-worst | 0.037 | 0.014 | 0.000 | 0.971 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.761 | 0.388 | 1.000 | 0.362 |
| SERA@DINOv3-B | Remedy+kNN | W-CRC | 0.633 | 0.296 | 1.000 | 0.494 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.601 | 0.282 | 0.750 | 0.531 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.397 | 0.150 | 0.583 | 0.757 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.275 | 0.082 | 0.500 | 0.883 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.117 | 0.019 | 0.000 | 0.985 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.300 | 0.091 | 0.500 | 0.852 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.292 | 0.087 | 0.500 | 0.860 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.210 | 0.049 | 0.083 | 0.921 |
| SERA@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC | 0.253 | 0.068 | 0.250 | 0.898 |
| SERA@DINOv3-B | Remedy+kNN | LOSO+LCO-CRC-worst | 0.131 | 0.023 | 0.000 | 0.976 |
| SERA@DINOv3-S | Energy | val-CRC | 0.758 | 0.400 | 1.000 | 0.258 |
| SERA@DINOv3-S | Energy | W-CRC | 0.581 | 0.285 | 1.000 | 0.457 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.01) | 0.582 | 0.288 | 1.000 | 0.415 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.05) | 0.396 | 0.181 | 0.583 | 0.619 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.1) | 0.277 | 0.122 | 0.250 | 0.738 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.2) | 0.123 | 0.055 | 0.250 | 0.890 |
| SERA@DINOv3-S | Energy | LOSO-CRC (2 src) | 0.263 | 0.123 | 0.250 | 0.738 |
| SERA@DINOv3-S | Energy | LOSO-CRC | 0.259 | 0.120 | 0.250 | 0.746 |
| SERA@DINOv3-S | Energy | LOSO-CRC-worst | 0.175 | 0.085 | 0.250 | 0.821 |
| SERA@DINOv3-S | Energy | LOSO+LCO-CRC | 0.225 | 0.102 | 0.250 | 0.778 |
| SERA@DINOv3-S | Energy | LOSO+LCO-CRC-worst | 0.097 | 0.050 | 0.167 | 0.902 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.764 | 0.397 | 1.000 | 0.374 |
| SERA@DINOv3-S | Remedy+kNN | W-CRC | 0.657 | 0.317 | 1.000 | 0.480 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.01) | 0.599 | 0.287 | 0.917 | 0.546 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.05) | 0.396 | 0.157 | 0.583 | 0.753 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.1) | 0.269 | 0.088 | 0.250 | 0.858 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.2) | 0.130 | 0.030 | 0.000 | 0.959 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC (2 src) | 0.311 | 0.108 | 0.500 | 0.836 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.300 | 0.100 | 0.500 | 0.847 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.219 | 0.064 | 0.333 | 0.908 |
| SERA@DINOv3-S | Remedy+kNN | LOSO+LCO-CRC | 0.249 | 0.074 | 0.417 | 0.893 |
| SERA@DINOv3-S | Remedy+kNN | LOSO+LCO-CRC-worst | 0.102 | 0.020 | 0.000 | 0.976 |
| SILA-Net | Energy | val-CRC | 0.814 | 0.407 | 1.000 | 0.227 |
| SILA-Net | Energy | W-CRC | 0.537 | 0.258 | 1.000 | 0.512 |
| SILA-Net | Energy | Robust-CRC(rho=0.01) | 0.479 | 0.231 | 0.750 | 0.528 |
| SILA-Net | Energy | Robust-CRC(rho=0.05) | 0.231 | 0.142 | 0.500 | 0.699 |
| SILA-Net | Energy | Robust-CRC(rho=0.1) | 0.156 | 0.108 | 0.250 | 0.783 |
| SILA-Net | Energy | Robust-CRC(rho=0.2) | 0.078 | 0.057 | 0.250 | 0.885 |
| SILA-Net | Energy | LOSO-CRC (2 src) | 0.271 | 0.165 | 0.500 | 0.630 |
| SILA-Net | Energy | LOSO-CRC | 0.256 | 0.159 | 0.500 | 0.646 |
| SILA-Net | Energy | LOSO-CRC-worst | 0.202 | 0.129 | 0.500 | 0.719 |
| ViTS-kNN | Energy | val-CRC | 0.975 | 0.453 | 1.000 | 0.107 |
| ViTS-kNN | Energy | W-CRC | 0.740 | 0.303 | 0.750 | 0.483 |
| ViTS-kNN | Energy | Robust-CRC(rho=0.01) | 0.863 | 0.393 | 0.750 | 0.274 |
| ViTS-kNN | Energy | Robust-CRC(rho=0.05) | 0.573 | 0.203 | 0.750 | 0.634 |
| ViTS-kNN | Energy | Robust-CRC(rho=0.1) | 0.412 | 0.118 | 0.333 | 0.789 |
| ViTS-kNN | Energy | Robust-CRC(rho=0.2) | 0.145 | 0.035 | 0.083 | 0.922 |
| ViTS-kNN | Energy | LOSO-CRC (2 src) | 0.342 | 0.102 | 0.333 | 0.806 |
| ViTS-kNN | Energy | LOSO-CRC | 0.349 | 0.102 | 0.333 | 0.804 |
| ViTS-kNN | Energy | LOSO-CRC-worst | 0.246 | 0.083 | 0.250 | 0.835 |
| ViTS-kNN | Remedy+kNN | val-CRC | 0.967 | 0.445 | 1.000 | 0.131 |
| ViTS-kNN | Remedy+kNN | W-CRC | 0.758 | 0.313 | 0.750 | 0.467 |
| ViTS-kNN | Remedy+kNN | Robust-CRC(rho=0.01) | 0.862 | 0.388 | 0.750 | 0.293 |
| ViTS-kNN | Remedy+kNN | Robust-CRC(rho=0.05) | 0.588 | 0.210 | 0.750 | 0.634 |
| ViTS-kNN | Remedy+kNN | Robust-CRC(rho=0.1) | 0.445 | 0.119 | 0.417 | 0.785 |
| ViTS-kNN | Remedy+kNN | Robust-CRC(rho=0.2) | 0.256 | 0.034 | 0.083 | 0.955 |
| ViTS-kNN | Remedy+kNN | LOSO-CRC (2 src) | 0.437 | 0.119 | 0.500 | 0.786 |
| ViTS-kNN | Remedy+kNN | LOSO-CRC | 0.429 | 0.114 | 0.500 | 0.792 |
| ViTS-kNN | Remedy+kNN | LOSO-CRC-worst | 0.338 | 0.085 | 0.250 | 0.850 |

## RQ4 - probability drop when views are removed (top-attended vs random; keep-top = only top-k kept)

| model | mode | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| MIL@DINOv3-B | keep-top | 0.041 | 0.008 | -0.000 | -0.002 |
| MIL@DINOv3-B | random | 0.007 | 0.013 | 0.022 | 0.029 |
| MIL@DINOv3-B | top | 0.083 | 0.118 | 0.141 | 0.162 |
| SERA@DINOv3-B | keep-top | 0.042 | 0.008 | -0.002 | -0.005 |
| SERA@DINOv3-B | random | 0.007 | 0.016 | 0.023 | 0.031 |
| SERA@DINOv3-B | top | 0.088 | 0.122 | 0.147 | 0.174 |

## RQ4 - attention statistics (held-out ID images, seed 0)

| model | correct | entropy | global_share | finest_share |
|---|---|---|---|---|
| MIL@DINOv3-B | False | 0.580 | 0.283 | 0.393 |
| MIL@DINOv3-B | True | 0.577 | 0.325 | 0.362 |
| SERA@DINOv3-B | False | 0.592 | 0.273 | 0.386 |
| SERA@DINOv3-B | True | 0.582 | 0.333 | 0.338 |

## RQ4 - attention of correct vs wrong cross-source predictions

| model | metric | correct_mean | wrong_mean | mannwhitney_p |
|---|---|---|---|---|
| MIL@DINOv3-B | entropy | 0.5772 | 0.5796 | 0.9521 |
| MIL@DINOv3-B | global_share | 0.3247 | 0.2833 | 0.0000 |
| MIL@DINOv3-B | finest_share | 0.3618 | 0.3928 | 0.0000 |
| SERA@DINOv3-B | entropy | 0.5821 | 0.5923 | 0.2180 |
| SERA@DINOv3-B | global_share | 0.3330 | 0.2734 | 0.0000 |
| SERA@DINOv3-B | finest_share | 0.3376 | 0.3856 | 0.0000 |

## Efficiency (encoder; 224x224 views; CPU 4 threads)

| encoder | views | params_M | GFLOPs | cpu_ms |
|---|---|---|---|---|
| DINOv3-S | 1 | 21.59 | 4.33 | 72.91 |
| DINOv3-S | 5 | 21.59 | 21.63 | 273.83 |
| DINOv3-S | 14 | 21.59 | 60.56 | 709.35 |
| DINOv3-B | 1 | 85.64 | 17.19 | 234.71 |
| DINOv3-B | 5 | 85.64 | 85.94 | 885.96 |
| DINOv3-B | 14 | 85.64 | 240.62 | 2722.90 |
