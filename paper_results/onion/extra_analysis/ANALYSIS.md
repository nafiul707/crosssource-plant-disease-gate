# onion: gate robustness (section 12.2)

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
| kNN | val-CRC | 0.125 / 0.29 | 0.389 / 0.71 | 0.479 / 0.87 | 0.538 / 1.00 |
| kNN | W-CRC | 0.077 / 0.19 | 0.213 / 0.43 | 0.347 / 0.65 | 0.418 / 0.77 |
| kNN | Robust-CRC(rho=0.01) | 0.039 / 0.11 | 0.178 / 0.40 | 0.407 / 0.74 | 0.476 / 0.87 |
| kNN | Robust-CRC(rho=0.05) | 0.001 / 0.01 | 0.059 / 0.15 | 0.171 / 0.38 | 0.351 / 0.66 |
| kNN | Robust-CRC(rho=0.1) | 0.000 / 0.00 | 0.019 / 0.06 | 0.078 / 0.19 | 0.187 / 0.41 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.000 / 0.00 | 0.022 / 0.06 | 0.069 / 0.17 |
| kNN | LOSO-CRC (2 src) | 0.061 / 0.15 | 0.114 / 0.27 | 0.159 / 0.36 | 0.207 / 0.46 |
| kNN | LOSO-CRC | 0.042 / 0.12 | 0.102 / 0.24 | 0.155 / 0.36 | 0.215 / 0.48 |
| kNN | LOSO-CRC-worst | 0.007 / 0.03 | 0.023 / 0.08 | 0.049 / 0.13 | 0.078 / 0.20 |

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
| kNN | val-CRC | 0.203 / 0.46 | 0.411 / 0.77 | 0.486 / 0.90 | 0.544 / 1.00 |
| kNN | W-CRC | 0.106 / 0.30 | 0.255 / 0.57 | 0.374 / 0.74 | 0.456 / 0.85 |
| kNN | Robust-CRC(rho=0.01) | 0.080 / 0.24 | 0.271 / 0.56 | 0.419 / 0.79 | 0.484 / 0.90 |
| kNN | Robust-CRC(rho=0.05) | 0.012 / 0.07 | 0.116 / 0.31 | 0.257 / 0.54 | 0.402 / 0.75 |
| kNN | Robust-CRC(rho=0.1) | 0.000 / 0.01 | 0.044 / 0.16 | 0.147 / 0.37 | 0.283 / 0.58 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.003 / 0.03 | 0.047 / 0.17 | 0.132 / 0.34 |
| kNN | LOSO-CRC (2 src) | 0.047 / 0.16 | 0.096 / 0.27 | 0.146 / 0.37 | 0.195 / 0.46 |
| kNN | LOSO-CRC | 0.035 / 0.14 | 0.090 / 0.26 | 0.139 / 0.36 | 0.183 / 0.44 |
| kNN | LOSO-CRC-worst | 0.007 / 0.05 | 0.025 / 0.11 | 0.055 / 0.19 | 0.085 / 0.25 |

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
| kNN | val-CRC | 0.211 / 0.46 | 0.402 / 0.75 | 0.511 / 0.92 | 0.561 / 1.00 |
| kNN | W-CRC | 0.142 / 0.35 | 0.297 / 0.61 | 0.411 / 0.78 | 0.488 / 0.89 |
| kNN | Robust-CRC(rho=0.01) | 0.057 / 0.19 | 0.269 / 0.55 | 0.411 / 0.76 | 0.505 / 0.91 |
| kNN | Robust-CRC(rho=0.05) | 0.001 / 0.02 | 0.094 / 0.26 | 0.261 / 0.53 | 0.389 / 0.73 |
| kNN | Robust-CRC(rho=0.1) | 0.000 / 0.00 | 0.025 / 0.11 | 0.138 / 0.34 | 0.278 / 0.56 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.000 / 0.01 | 0.029 / 0.12 | 0.115 / 0.30 |
| kNN | LOSO-CRC (2 src) | 0.054 / 0.17 | 0.103 / 0.27 | 0.151 / 0.36 | 0.203 / 0.46 |
| kNN | LOSO-CRC | 0.040 / 0.14 | 0.088 / 0.25 | 0.145 / 0.35 | 0.199 / 0.46 |
| kNN | LOSO-CRC-worst | 0.016 / 0.07 | 0.041 / 0.14 | 0.065 / 0.19 | 0.094 / 0.25 |

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
| 0.050 | LOSO-CRC | 0.036 / 0.27 | 0.054 / 0.18 | 0.017 / 0.08 | 0.039 / 0.29 |
| 0.050 | LOSO-CRC-worst | 0.021 / 0.20 | 0.021 / 0.10 | 0.006 / 0.04 | 0.021 / 0.23 |
| 0.050 | W-CRC | 0.146 / 0.51 | 0.271 / 0.49 | 0.043 / 0.16 | 0.076 / 0.37 |
| 0.050 | val-CRC | 0.200 / 0.59 | 0.268 / 0.49 | 0.049 / 0.18 | 0.115 / 0.44 |
| 0.100 | LOSO-CRC | 0.064 / 0.36 | 0.117 / 0.28 | 0.056 / 0.20 | 0.081 / 0.39 |
| 0.100 | LOSO-CRC-worst | 0.045 / 0.31 | 0.057 / 0.18 | 0.019 / 0.08 | 0.053 / 0.32 |
| 0.100 | W-CRC | 0.293 / 0.71 | 0.403 / 0.67 | 0.089 / 0.29 | 0.138 / 0.49 |
| 0.100 | val-CRC | 0.400 / 0.83 | 0.655 / 0.98 | 0.126 / 0.39 | 0.241 / 0.64 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: SERA@DINOv3-B

| eps | calibration | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion |
|---|---|---|---|---|---|
| 0.050 | LOSO-CRC | 0.063 / 0.26 | 0.059 / 0.16 | 0.005 / 0.04 | 0.035 / 0.29 |
| 0.050 | LOSO-CRC-worst | 0.026 / 0.15 | 0.037 / 0.11 | 0.001 / 0.02 | 0.019 / 0.23 |
| 0.050 | W-CRC | 0.218 / 0.56 | 0.299 / 0.54 | 0.060 / 0.24 | 0.153 / 0.49 |
| 0.050 | val-CRC | 0.274 / 0.65 | 0.445 / 0.74 | 0.046 / 0.21 | 0.184 / 0.53 |
| 0.100 | LOSO-CRC | 0.125 / 0.41 | 0.123 / 0.27 | 0.019 / 0.11 | 0.080 / 0.38 |
| 0.100 | LOSO-CRC-worst | 0.070 / 0.28 | 0.082 / 0.20 | 0.009 / 0.07 | 0.035 / 0.29 |
| 0.100 | W-CRC | 0.331 / 0.73 | 0.484 / 0.79 | 0.111 / 0.37 | 0.256 / 0.64 |
| 0.100 | val-CRC | 0.431 / 0.88 | 0.652 / 1.00 | 0.135 / 0.42 | 0.335 / 0.74 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: SERA@DINOv3-S

| eps | calibration | cold | roboflow_capstone | roboflow_onionnet | tom2024_onion |
|---|---|---|---|---|---|
| 0.050 | LOSO-CRC | 0.078 / 0.29 | 0.106 / 0.24 | 0.004 / 0.03 | 0.020 / 0.21 |
| 0.050 | LOSO-CRC-worst | 0.040 / 0.19 | 0.070 / 0.17 | 0.001 / 0.02 | 0.008 / 0.14 |
| 0.050 | W-CRC | 0.175 / 0.48 | 0.357 / 0.60 | 0.091 / 0.31 | 0.124 / 0.44 |
| 0.050 | val-CRC | 0.262 / 0.62 | 0.487 / 0.77 | 0.073 / 0.26 | 0.124 / 0.44 |
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
| SERA@DINOv3-B | val-CRC | 0.050 | 0.237 [0.225, 0.250] | 0.53 [0.52, 0.54] |
| SERA@DINOv3-B | val-CRC | 0.100 | 0.388 [0.372, 0.403] | 0.76 [0.75, 0.77] |
| SERA@DINOv3-B | W-CRC | 0.050 | 0.182 [0.172, 0.193] | 0.46 [0.45, 0.47] |
| SERA@DINOv3-B | W-CRC | 0.100 | 0.296 [0.282, 0.309] | 0.63 [0.62, 0.64] |
| SERA@DINOv3-B | LOSO-CRC | 0.050 | 0.040 [0.035, 0.046] | 0.19 [0.18, 0.20] |
| SERA@DINOv3-B | LOSO-CRC | 0.100 | 0.087 [0.079, 0.094] | 0.29 [0.28, 0.30] |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.050 | 0.021 [0.017, 0.025] | 0.13 [0.12, 0.14] |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.100 | 0.049 [0.043, 0.055] | 0.21 [0.20, 0.22] |
| SERA@DINOv3-S | val-CRC | 0.050 | 0.236 [0.223, 0.250] | 0.52 [0.51, 0.53] |
| SERA@DINOv3-S | val-CRC | 0.100 | 0.397 [0.382, 0.411] | 0.76 [0.76, 0.77] |
| SERA@DINOv3-S | W-CRC | 0.050 | 0.187 [0.176, 0.199] | 0.46 [0.44, 0.47] |
| SERA@DINOv3-S | W-CRC | 0.100 | 0.317 [0.303, 0.331] | 0.66 [0.65, 0.67] |
| SERA@DINOv3-S | LOSO-CRC | 0.050 | 0.052 [0.046, 0.059] | 0.19 [0.18, 0.20] |
| SERA@DINOv3-S | LOSO-CRC | 0.100 | 0.100 [0.092, 0.110] | 0.30 [0.29, 0.31] |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.050 | 0.030 [0.025, 0.036] | 0.13 [0.12, 0.14] |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.100 | 0.064 [0.056, 0.071] | 0.22 [0.21, 0.23] |
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
| LP-global@DINOv3-B | Energy | val-CRC | 0.391 | 0.157 | 0.583 | 0.729 |
| LP-global@DINOv3-B | Energy | W-CRC | 0.338 | 0.130 | 0.667 | 0.782 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.261 | 0.109 | 0.333 | 0.809 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.143 | 0.067 | 0.250 | 0.882 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.056 | 0.033 | 0.250 | 0.938 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| LP-global@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.208 | 0.096 | 0.500 | 0.841 |
| LP-global@DINOv3-B | Energy | LOSO-CRC | 0.177 | 0.087 | 0.500 | 0.860 |
| LP-global@DINOv3-B | Energy | LOSO-CRC-worst | 0.071 | 0.043 | 0.250 | 0.923 |
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.425 | 0.158 | 0.833 | 0.745 |
| LP-global@DINOv3-B | Remedy+kNN | W-CRC | 0.385 | 0.134 | 0.833 | 0.773 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.264 | 0.063 | 0.750 | 0.884 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.131 | 0.014 | 0.000 | 0.982 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.049 | 0.002 | 0.000 | 0.995 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.211 | 0.040 | 0.250 | 0.921 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.204 | 0.036 | 0.250 | 0.928 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.141 | 0.017 | 0.000 | 0.971 |
| SERA@DINOv3-B | Energy | val-CRC | 0.481 | 0.210 | 1.000 | 0.590 |
| SERA@DINOv3-B | Energy | W-CRC | 0.376 | 0.151 | 0.833 | 0.717 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.314 | 0.128 | 0.667 | 0.746 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.145 | 0.064 | 0.250 | 0.867 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.059 | 0.030 | 0.250 | 0.937 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.143 | 0.061 | 0.250 | 0.873 |
| SERA@DINOv3-B | Energy | LOSO-CRC | 0.128 | 0.055 | 0.250 | 0.882 |
| SERA@DINOv3-B | Energy | LOSO-CRC-worst | 0.055 | 0.028 | 0.250 | 0.939 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.531 | 0.237 | 0.833 | 0.601 |
| SERA@DINOv3-B | Remedy+kNN | W-CRC | 0.459 | 0.182 | 0.917 | 0.686 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.347 | 0.121 | 0.750 | 0.811 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.170 | 0.034 | 0.333 | 0.956 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.068 | 0.008 | 0.000 | 0.998 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.199 | 0.045 | 0.500 | 0.927 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.190 | 0.040 | 0.333 | 0.935 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.129 | 0.021 | 0.000 | 0.963 |
| SERA@DINOv3-S | Energy | val-CRC | 0.516 | 0.249 | 1.000 | 0.484 |
| SERA@DINOv3-S | Energy | W-CRC | 0.407 | 0.181 | 1.000 | 0.646 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.01) | 0.346 | 0.155 | 1.000 | 0.666 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.05) | 0.173 | 0.078 | 0.250 | 0.843 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.1) | 0.068 | 0.033 | 0.250 | 0.939 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-S | Energy | LOSO-CRC (2 src) | 0.162 | 0.081 | 0.250 | 0.835 |
| SERA@DINOv3-S | Energy | LOSO-CRC | 0.156 | 0.079 | 0.250 | 0.840 |
| SERA@DINOv3-S | Energy | LOSO-CRC-worst | 0.095 | 0.051 | 0.250 | 0.906 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.521 | 0.236 | 1.000 | 0.633 |
| SERA@DINOv3-S | Remedy+kNN | W-CRC | 0.457 | 0.187 | 1.000 | 0.683 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.01) | 0.351 | 0.131 | 0.667 | 0.788 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.05) | 0.179 | 0.051 | 0.500 | 0.928 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.1) | 0.057 | 0.006 | 0.000 | 0.998 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC (2 src) | 0.200 | 0.055 | 0.500 | 0.919 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.193 | 0.052 | 0.500 | 0.925 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.132 | 0.030 | 0.333 | 0.955 |
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
| LP-global@DINOv3-B | Energy | val-CRC | 0.667 | 0.301 | 1.000 | 0.477 |
| LP-global@DINOv3-B | Energy | W-CRC | 0.474 | 0.208 | 0.750 | 0.646 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.454 | 0.187 | 0.417 | 0.676 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.297 | 0.121 | 0.250 | 0.787 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.203 | 0.089 | 0.250 | 0.845 |
| LP-global@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.107 | 0.055 | 0.250 | 0.900 |
| LP-global@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.322 | 0.141 | 0.500 | 0.759 |
| LP-global@DINOv3-B | Energy | LOSO-CRC | 0.311 | 0.135 | 0.500 | 0.782 |
| LP-global@DINOv3-B | Energy | LOSO-CRC-worst | 0.156 | 0.081 | 0.250 | 0.864 |
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.708 | 0.355 | 1.000 | 0.430 |
| LP-global@DINOv3-B | Remedy+kNN | W-CRC | 0.537 | 0.230 | 0.750 | 0.637 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.497 | 0.205 | 0.750 | 0.673 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.304 | 0.086 | 0.500 | 0.850 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.197 | 0.034 | 0.000 | 0.942 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.099 | 0.008 | 0.000 | 0.989 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.312 | 0.085 | 0.250 | 0.831 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.306 | 0.080 | 0.250 | 0.843 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.224 | 0.043 | 0.000 | 0.915 |
| SERA@DINOv3-B | Energy | val-CRC | 0.775 | 0.396 | 1.000 | 0.299 |
| SERA@DINOv3-B | Energy | W-CRC | 0.589 | 0.286 | 0.750 | 0.480 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.553 | 0.253 | 0.917 | 0.509 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.359 | 0.148 | 0.250 | 0.704 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.249 | 0.100 | 0.250 | 0.800 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.110 | 0.051 | 0.250 | 0.892 |
| SERA@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.255 | 0.103 | 0.250 | 0.797 |
| SERA@DINOv3-B | Energy | LOSO-CRC | 0.246 | 0.099 | 0.250 | 0.806 |
| SERA@DINOv3-B | Energy | LOSO-CRC-worst | 0.127 | 0.053 | 0.250 | 0.884 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.761 | 0.388 | 1.000 | 0.362 |
| SERA@DINOv3-B | Remedy+kNN | W-CRC | 0.633 | 0.296 | 1.000 | 0.494 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.601 | 0.282 | 0.750 | 0.531 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.397 | 0.150 | 0.583 | 0.757 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.275 | 0.082 | 0.500 | 0.883 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.117 | 0.019 | 0.000 | 0.985 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.300 | 0.091 | 0.500 | 0.852 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.292 | 0.087 | 0.500 | 0.860 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.210 | 0.049 | 0.083 | 0.921 |
| SERA@DINOv3-S | Energy | val-CRC | 0.758 | 0.400 | 1.000 | 0.258 |
| SERA@DINOv3-S | Energy | W-CRC | 0.581 | 0.285 | 1.000 | 0.457 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.01) | 0.582 | 0.288 | 1.000 | 0.415 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.05) | 0.396 | 0.181 | 0.583 | 0.619 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.1) | 0.277 | 0.122 | 0.250 | 0.738 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.2) | 0.123 | 0.055 | 0.250 | 0.890 |
| SERA@DINOv3-S | Energy | LOSO-CRC (2 src) | 0.263 | 0.123 | 0.250 | 0.738 |
| SERA@DINOv3-S | Energy | LOSO-CRC | 0.259 | 0.120 | 0.250 | 0.746 |
| SERA@DINOv3-S | Energy | LOSO-CRC-worst | 0.175 | 0.085 | 0.250 | 0.821 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.764 | 0.397 | 1.000 | 0.374 |
| SERA@DINOv3-S | Remedy+kNN | W-CRC | 0.657 | 0.317 | 1.000 | 0.480 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.01) | 0.599 | 0.287 | 0.917 | 0.546 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.05) | 0.396 | 0.157 | 0.583 | 0.753 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.1) | 0.269 | 0.088 | 0.250 | 0.858 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.2) | 0.130 | 0.030 | 0.000 | 0.959 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC (2 src) | 0.311 | 0.108 | 0.500 | 0.836 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.300 | 0.100 | 0.500 | 0.847 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.219 | 0.064 | 0.333 | 0.908 |
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

## RQ3c - label n images of the new source vs label-free LOSO gate (Remedy+kNN, eps = 5%): risk / acceptance / P(risk > eps)

| model | calibration | n=25 | n=50 | n=100 | n=200 | n=400 |
|---|---|---|---|---|---|---|
| LP-global@DINOv3-B | LOSO-CRC | 0.036 / 0.20 / 0.25 | 0.036 / 0.20 / 0.24 | 0.036 / 0.20 / 0.22 | 0.036 / 0.20 / 0.21 | 0.036 / 0.20 / 0.20 |
| LP-global@DINOv3-B | LOSO-CRC-worst | 0.017 / 0.14 / 0.00 | 0.017 / 0.14 / 0.00 | 0.017 / 0.14 / 0.00 | 0.017 / 0.14 / 0.00 | 0.017 / 0.14 / 0.00 |
| LP-global@DINOv3-B | target-CRC | 0.045 / 0.21 / 0.31 | 0.043 / 0.21 / 0.32 | 0.051 / 0.24 / 0.46 | 0.050 / 0.24 / 0.45 | 0.050 / 0.25 / 0.47 |
| SERA@DINOv3-B | LOSO-CRC | 0.040 / 0.19 / 0.33 | 0.040 / 0.19 / 0.33 | 0.040 / 0.19 / 0.33 | 0.040 / 0.19 / 0.34 | 0.041 / 0.19 / 0.35 |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.021 / 0.13 / 0.00 | 0.021 / 0.13 / 0.01 | 0.021 / 0.13 / 0.03 | 0.021 / 0.13 / 0.03 | 0.021 / 0.13 / 0.04 |
| SERA@DINOv3-B | target-CRC | 0.046 / 0.20 / 0.33 | 0.046 / 0.21 / 0.35 | 0.052 / 0.23 / 0.47 | 0.051 / 0.23 / 0.46 | 0.050 / 0.23 / 0.47 |
| SERA@DINOv3-S | LOSO-CRC | 0.052 / 0.19 / 0.50 | 0.052 / 0.19 / 0.50 | 0.052 / 0.19 / 0.50 | 0.052 / 0.19 / 0.50 | 0.052 / 0.19 / 0.50 |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.030 / 0.13 / 0.33 | 0.030 / 0.13 / 0.33 | 0.030 / 0.13 / 0.33 | 0.030 / 0.13 / 0.33 | 0.030 / 0.13 / 0.33 |
| SERA@DINOv3-S | target-CRC | 0.047 / 0.19 / 0.35 | 0.046 / 0.19 / 0.35 | 0.051 / 0.21 / 0.46 | 0.051 / 0.21 / 0.47 | 0.050 / 0.22 / 0.47 |
| ViTS-kNN | LOSO-CRC | 0.072 / 0.33 / 0.50 | 0.072 / 0.33 / 0.50 | 0.072 / 0.33 / 0.50 | 0.072 / 0.33 / 0.50 | 0.072 / 0.33 / 0.50 |
| ViTS-kNN | LOSO-CRC-worst | 0.045 / 0.24 / 0.33 | 0.045 / 0.24 / 0.33 | 0.045 / 0.24 / 0.33 | 0.045 / 0.24 / 0.33 | 0.045 / 0.24 / 0.33 |
| ViTS-kNN | target-CRC | 0.046 / 0.32 / 0.33 | 0.045 / 0.34 / 0.33 | 0.052 / 0.37 / 0.47 | 0.051 / 0.37 / 0.47 | 0.051 / 0.37 / 0.49 |

## RQ3c - label n images of the new source vs label-free LOSO gate (Remedy+kNN, eps = 10%): risk / acceptance / P(risk > eps)

| model | calibration | n=25 | n=50 | n=100 | n=200 | n=400 |
|---|---|---|---|---|---|---|
| LP-global@DINOv3-B | LOSO-CRC | 0.080 / 0.31 / 0.25 | 0.080 / 0.31 / 0.25 | 0.080 / 0.31 / 0.25 | 0.080 / 0.31 / 0.25 | 0.080 / 0.31 / 0.25 |
| LP-global@DINOv3-B | LOSO-CRC-worst | 0.043 / 0.22 / 0.00 | 0.043 / 0.22 / 0.00 | 0.044 / 0.22 / 0.00 | 0.043 / 0.22 / 0.00 | 0.044 / 0.22 / 0.00 |
| LP-global@DINOv3-B | target-CRC | 0.086 / 0.31 / 0.32 | 0.103 / 0.36 / 0.44 | 0.101 / 0.35 / 0.46 | 0.100 / 0.35 / 0.45 | 0.100 / 0.35 / 0.46 |
| SERA@DINOv3-B | LOSO-CRC | 0.087 / 0.29 / 0.50 | 0.087 / 0.29 / 0.50 | 0.087 / 0.29 / 0.49 | 0.087 / 0.29 / 0.49 | 0.087 / 0.29 / 0.46 |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.049 / 0.21 / 0.08 | 0.049 / 0.21 / 0.06 | 0.049 / 0.21 / 0.06 | 0.049 / 0.21 / 0.07 | 0.049 / 0.21 / 0.07 |
| SERA@DINOv3-B | target-CRC | 0.091 / 0.31 / 0.36 | 0.102 / 0.33 / 0.45 | 0.101 / 0.33 / 0.46 | 0.100 / 0.34 / 0.47 | 0.100 / 0.33 / 0.46 |
| SERA@DINOv3-S | LOSO-CRC | 0.100 / 0.30 / 0.50 | 0.100 / 0.30 / 0.50 | 0.100 / 0.30 / 0.50 | 0.101 / 0.30 / 0.50 | 0.100 / 0.30 / 0.49 |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.064 / 0.22 / 0.33 | 0.064 / 0.22 / 0.33 | 0.064 / 0.22 / 0.33 | 0.064 / 0.22 / 0.33 | 0.064 / 0.22 / 0.33 |
| SERA@DINOv3-S | target-CRC | 0.092 / 0.29 / 0.36 | 0.102 / 0.32 / 0.46 | 0.099 / 0.32 / 0.44 | 0.101 / 0.32 / 0.49 | 0.100 / 0.32 / 0.46 |
| ViTS-kNN | LOSO-CRC | 0.114 / 0.43 / 0.50 | 0.114 / 0.43 / 0.50 | 0.114 / 0.43 / 0.50 | 0.114 / 0.43 / 0.49 | 0.114 / 0.43 / 0.46 |
| ViTS-kNN | LOSO-CRC-worst | 0.084 / 0.34 / 0.25 | 0.084 / 0.34 / 0.25 | 0.085 / 0.34 / 0.26 | 0.085 / 0.34 / 0.27 | 0.084 / 0.34 / 0.28 |
| ViTS-kNN | target-CRC | 0.091 / 0.44 / 0.35 | 0.102 / 0.48 / 0.46 | 0.100 / 0.47 / 0.46 | 0.102 / 0.48 / 0.49 | 0.099 / 0.48 / 0.46 |
