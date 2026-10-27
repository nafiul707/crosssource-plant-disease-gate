# potato: gate robustness (section 12.2)

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
| kNN | val-CRC | 0.200 / 0.27 | 0.395 / 0.77 | 0.463 / 1.00 | 0.463 / 1.00 |
| kNN | W-CRC | 0.126 / 0.17 | 0.193 / 0.30 | 0.253 / 0.42 | 0.321 / 0.61 |
| kNN | Robust-CRC(rho=0.01) | 0.143 / 0.18 | 0.221 / 0.30 | 0.409 / 0.82 | 0.463 / 1.00 |
| kNN | Robust-CRC(rho=0.05) | 0.055 / 0.07 | 0.165 / 0.22 | 0.212 / 0.28 | 0.366 / 0.67 |
| kNN | Robust-CRC(rho=0.1) | 0.001 / 0.00 | 0.113 / 0.14 | 0.180 / 0.24 | 0.224 / 0.30 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.025 / 0.03 | 0.118 / 0.15 | 0.174 / 0.23 |
| kNN | LOSO-CRC (2 src) | 0.214 / 0.29 | 0.236 / 0.32 | 0.248 / 0.35 | 0.257 / 0.37 |
| kNN | LOSO-CRC | 0.213 / 0.29 | 0.240 / 0.33 | 0.248 / 0.34 | 0.254 / 0.36 |
| kNN | LOSO-CRC-worst | 0.183 / 0.24 | 0.206 / 0.28 | 0.220 / 0.30 | 0.233 / 0.32 |

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
| kNN | val-CRC | 0.228 / 0.43 | 0.368 / 1.00 | 0.368 / 1.00 | 0.368 / 1.00 |
| kNN | W-CRC | 0.064 / 0.19 | 0.131 / 0.44 | 0.252 / 0.75 | 0.358 / 0.96 |
| kNN | Robust-CRC(rho=0.01) | 0.163 / 0.25 | 0.307 / 0.71 | 0.368 / 1.00 | 0.368 / 1.00 |
| kNN | Robust-CRC(rho=0.05) | 0.010 / 0.02 | 0.184 / 0.29 | 0.304 / 0.68 | 0.361 / 0.98 |
| kNN | Robust-CRC(rho=0.1) | 0.001 / 0.00 | 0.042 / 0.07 | 0.191 / 0.32 | 0.311 / 0.73 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.007 / 0.01 | 0.045 / 0.08 | 0.188 / 0.30 |
| kNN | LOSO-CRC (2 src) | 0.059 / 0.20 | 0.110 / 0.37 | 0.153 / 0.50 | 0.204 / 0.64 |
| kNN | LOSO-CRC | 0.058 / 0.21 | 0.108 / 0.36 | 0.157 / 0.51 | 0.197 / 0.63 |
| kNN | LOSO-CRC-worst | 0.027 / 0.11 | 0.061 / 0.22 | 0.111 / 0.36 | 0.161 / 0.51 |

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
| kNN | val-CRC | 0.235 / 0.41 | 0.365 / 0.87 | 0.401 / 1.00 | 0.401 / 1.00 |
| kNN | W-CRC | 0.082 / 0.20 | 0.158 / 0.42 | 0.253 / 0.66 | 0.375 / 0.91 |
| kNN | Robust-CRC(rho=0.01) | 0.129 / 0.20 | 0.299 / 0.62 | 0.368 / 0.89 | 0.401 / 1.00 |
| kNN | Robust-CRC(rho=0.05) | 0.010 / 0.02 | 0.176 / 0.27 | 0.287 / 0.58 | 0.363 / 0.86 |
| kNN | Robust-CRC(rho=0.1) | 0.000 / 0.00 | 0.064 / 0.10 | 0.206 / 0.32 | 0.305 / 0.65 |
| kNN | Robust-CRC(rho=0.2) | 0.000 / 0.00 | 0.004 / 0.01 | 0.071 / 0.11 | 0.199 / 0.31 |
| kNN | LOSO-CRC (2 src) | 0.061 / 0.16 | 0.114 / 0.31 | 0.171 / 0.46 | 0.219 / 0.60 |
| kNN | LOSO-CRC | 0.058 / 0.15 | 0.112 / 0.30 | 0.167 / 0.45 | 0.224 / 0.61 |
| kNN | LOSO-CRC-worst | 0.031 / 0.09 | 0.061 / 0.17 | 0.108 / 0.30 | 0.169 / 0.44 |

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
| 0.050 | LOSO-CRC | 0.155 / 0.26 | 0.000 / 0.00 | 0.000 / 0.00 | 0.463 / 0.64 |
| 0.050 | LOSO-CRC-worst | 0.108 / 0.17 | 0.000 / 0.00 | 0.000 / 0.00 | 0.191 / 0.29 |
| 0.050 | W-CRC | 0.037 / 0.05 | 0.017 / 0.07 | 0.012 / 0.07 | 0.350 / 0.50 |
| 0.050 | val-CRC | 0.130 / 0.20 | 0.024 / 0.10 | 0.012 / 0.07 | 0.751 / 1.00 |
| 0.100 | LOSO-CRC | 0.218 / 0.35 | 0.002 / 0.01 | 0.000 / 0.00 | 0.632 / 0.85 |
| 0.100 | LOSO-CRC-worst | 0.183 / 0.30 | 0.000 / 0.00 | 0.000 / 0.00 | 0.342 / 0.49 |
| 0.100 | W-CRC | 0.075 / 0.11 | 0.054 / 0.19 | 0.032 / 0.15 | 0.545 / 0.74 |
| 0.100 | val-CRC | 0.522 / 1.00 | 0.261 / 0.91 | 0.157 / 0.57 | 0.751 / 1.00 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: SERA@DINOv3-B

| eps | calibration | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia |
|---|---|---|---|---|---|
| 0.050 | LOSO-CRC | 0.100 / 0.35 | 0.030 / 0.26 | 0.036 / 0.25 | 0.044 / 0.09 |
| 0.050 | LOSO-CRC-worst | 0.064 / 0.24 | 0.018 / 0.18 | 0.031 / 0.22 | 0.028 / 0.06 |
| 0.050 | W-CRC | 0.096 / 0.33 | 0.050 / 0.42 | 0.033 / 0.25 | 0.121 / 0.22 |
| 0.050 | val-CRC | 0.261 / 0.73 | 0.080 / 0.60 | 0.055 / 0.37 | 0.706 / 1.00 |
| 0.100 | LOSO-CRC | 0.185 / 0.54 | 0.058 / 0.48 | 0.059 / 0.39 | 0.120 / 0.21 |
| 0.100 | LOSO-CRC-worst | 0.123 / 0.40 | 0.038 / 0.33 | 0.049 / 0.33 | 0.081 / 0.15 |
| 0.100 | W-CRC | 0.202 / 0.58 | 0.099 / 0.71 | 0.070 / 0.44 | 0.229 / 0.37 |
| 0.100 | val-CRC | 0.387 / 1.00 | 0.154 / 1.00 | 0.225 / 1.00 | 0.706 / 1.00 |

## RQ3b - per held-out source, Remedy+kNN, risk / acceptance: SERA@DINOv3-S

| eps | calibration | plantdoc | plantvillage | pld_pakistan | uncontrolled_indonesia |
|---|---|---|---|---|---|
| 0.050 | LOSO-CRC | 0.108 / 0.28 | 0.042 / 0.26 | 0.030 / 0.13 | 0.029 / 0.06 |
| 0.050 | LOSO-CRC-worst | 0.040 / 0.13 | 0.030 / 0.19 | 0.021 / 0.09 | 0.009 / 0.02 |
| 0.050 | W-CRC | 0.118 / 0.31 | 0.097 / 0.52 | 0.044 / 0.25 | 0.132 / 0.23 |
| 0.050 | val-CRC | 0.224 / 0.58 | 0.143 / 0.72 | 0.049 / 0.28 | 0.722 / 1.00 |
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
| SERA@DINOv3-B | val-CRC | 0.050 | 0.275 [0.266, 0.286] | 0.67 [0.66, 0.68] |
| SERA@DINOv3-B | val-CRC | 0.100 | 0.368 [0.356, 0.380] | 1.00 [1.00, 1.00] |
| SERA@DINOv3-B | W-CRC | 0.050 | 0.075 [0.069, 0.082] | 0.30 [0.29, 0.31] |
| SERA@DINOv3-B | W-CRC | 0.100 | 0.150 [0.141, 0.160] | 0.53 [0.52, 0.54] |
| SERA@DINOv3-B | LOSO-CRC | 0.050 | 0.053 [0.047, 0.059] | 0.24 [0.23, 0.25] |
| SERA@DINOv3-B | LOSO-CRC | 0.100 | 0.106 [0.097, 0.115] | 0.41 [0.39, 0.42] |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.050 | 0.035 [0.030, 0.040] | 0.17 [0.16, 0.18] |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.100 | 0.073 [0.066, 0.080] | 0.30 [0.29, 0.31] |
| SERA@DINOv3-S | val-CRC | 0.050 | 0.285 [0.274, 0.295] | 0.65 [0.64, 0.66] |
| SERA@DINOv3-S | val-CRC | 0.100 | 0.376 [0.363, 0.389] | 0.93 [0.93, 0.93] |
| SERA@DINOv3-S | W-CRC | 0.050 | 0.098 [0.091, 0.105] | 0.33 [0.32, 0.34] |
| SERA@DINOv3-S | W-CRC | 0.100 | 0.173 [0.163, 0.184] | 0.53 [0.52, 0.54] |
| SERA@DINOv3-S | LOSO-CRC | 0.050 | 0.052 [0.046, 0.058] | 0.18 [0.17, 0.19] |
| SERA@DINOv3-S | LOSO-CRC | 0.100 | 0.109 [0.101, 0.118] | 0.36 [0.34, 0.37] |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.050 | 0.025 [0.021, 0.029] | 0.11 [0.10, 0.11] |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.100 | 0.058 [0.052, 0.065] | 0.21 [0.20, 0.22] |
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
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.342 | 0.229 | 0.500 | 0.000 |
| LP-global@DINOv3-B | Remedy+kNN | W-CRC | 0.174 | 0.104 | 0.250 | 0.492 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.200 | 0.140 | 0.333 | 0.299 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.086 | 0.056 | 0.250 | 0.676 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.008 | 0.004 | 0.000 | 0.970 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.226 | 0.156 | 0.500 | 0.361 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.225 | 0.155 | 0.500 | 0.355 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.115 | 0.075 | 0.500 | 0.701 |
| SERA@DINOv3-B | Energy | val-CRC | 0.855 | 0.320 | 1.000 | 0.000 |
| SERA@DINOv3-B | Energy | W-CRC | 0.441 | 0.117 | 0.750 | 0.704 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.638 | 0.256 | 0.750 | 0.031 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.245 | 0.068 | 0.500 | 0.752 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.098 | 0.024 | 0.250 | 0.959 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.241 | 0.052 | 0.333 | 0.905 |
| SERA@DINOv3-B | Energy | LOSO-CRC | 0.226 | 0.048 | 0.333 | 0.913 |
| SERA@DINOv3-B | Energy | LOSO-CRC-worst | 0.164 | 0.034 | 0.250 | 0.959 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.675 | 0.275 | 0.833 | 0.000 |
| SERA@DINOv3-B | Remedy+kNN | W-CRC | 0.304 | 0.075 | 0.667 | 0.791 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.417 | 0.189 | 0.583 | 0.120 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.119 | 0.037 | 0.333 | 0.836 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.060 | 0.016 | 0.083 | 0.917 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.247 | 0.056 | 0.417 | 0.912 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.239 | 0.053 | 0.417 | 0.918 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.173 | 0.035 | 0.333 | 0.947 |
| SERA@DINOv3-S | Energy | val-CRC | 0.849 | 0.329 | 1.000 | 0.000 |
| SERA@DINOv3-S | Energy | W-CRC | 0.379 | 0.093 | 0.750 | 0.829 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.01) | 0.612 | 0.211 | 0.833 | 0.282 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.05) | 0.246 | 0.050 | 0.417 | 0.888 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.1) | 0.131 | 0.019 | 0.083 | 0.971 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-S | Energy | LOSO-CRC (2 src) | 0.218 | 0.039 | 0.250 | 0.961 |
| SERA@DINOv3-S | Energy | LOSO-CRC | 0.204 | 0.035 | 0.250 | 0.975 |
| SERA@DINOv3-S | Energy | LOSO-CRC-worst | 0.144 | 0.024 | 0.167 | 0.992 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.647 | 0.285 | 0.833 | 0.000 |
| SERA@DINOv3-S | Remedy+kNN | W-CRC | 0.327 | 0.098 | 0.833 | 0.770 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.01) | 0.383 | 0.180 | 0.750 | 0.247 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.05) | 0.115 | 0.039 | 0.250 | 0.819 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.1) | 0.041 | 0.007 | 0.000 | 0.974 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.2) | 0.000 | 0.000 | 0.000 | 1.000 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC (2 src) | 0.198 | 0.057 | 0.500 | 0.928 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.184 | 0.052 | 0.417 | 0.937 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.106 | 0.025 | 0.167 | 0.976 |
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
| LP-global@DINOv3-B | Remedy+kNN | val-CRC | 0.870 | 0.423 | 1.000 | 0.000 |
| LP-global@DINOv3-B | Remedy+kNN | W-CRC | 0.298 | 0.177 | 0.250 | 0.253 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.407 | 0.257 | 0.500 | 0.000 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.230 | 0.161 | 0.250 | 0.218 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.139 | 0.094 | 0.250 | 0.494 |
| LP-global@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.066 | 0.042 | 0.250 | 0.748 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.300 | 0.209 | 0.500 | 0.166 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.303 | 0.213 | 0.500 | 0.147 |
| LP-global@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.199 | 0.131 | 0.500 | 0.501 |
| SERA@DINOv3-B | Energy | val-CRC | 1.000 | 0.368 | 1.000 | 0.000 |
| SERA@DINOv3-B | Energy | W-CRC | 0.689 | 0.205 | 0.750 | 0.464 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.01) | 0.921 | 0.339 | 0.833 | 0.000 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.05) | 0.710 | 0.280 | 0.583 | 0.000 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.1) | 0.418 | 0.126 | 0.500 | 0.574 |
| SERA@DINOv3-B | Energy | Robust-CRC(rho=0.2) | 0.185 | 0.051 | 0.167 | 0.795 |
| SERA@DINOv3-B | Energy | LOSO-CRC (2 src) | 0.409 | 0.104 | 0.417 | 0.754 |
| SERA@DINOv3-B | Energy | LOSO-CRC | 0.401 | 0.102 | 0.333 | 0.755 |
| SERA@DINOv3-B | Energy | LOSO-CRC-worst | 0.276 | 0.066 | 0.250 | 0.879 |
| SERA@DINOv3-B | Remedy+kNN | val-CRC | 0.999 | 0.368 | 1.000 | 0.000 |
| SERA@DINOv3-B | Remedy+kNN | W-CRC | 0.527 | 0.150 | 0.583 | 0.635 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.01) | 0.830 | 0.322 | 0.667 | 0.000 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.05) | 0.500 | 0.226 | 0.500 | 0.000 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.1) | 0.211 | 0.075 | 0.250 | 0.673 |
| SERA@DINOv3-B | Remedy+kNN | Robust-CRC(rho=0.2) | 0.096 | 0.031 | 0.083 | 0.847 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC (2 src) | 0.408 | 0.107 | 0.500 | 0.792 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC | 0.405 | 0.106 | 0.500 | 0.795 |
| SERA@DINOv3-B | Remedy+kNN | LOSO-CRC-worst | 0.301 | 0.073 | 0.250 | 0.859 |
| SERA@DINOv3-S | Energy | val-CRC | 0.979 | 0.388 | 1.000 | 0.000 |
| SERA@DINOv3-S | Energy | W-CRC | 0.585 | 0.162 | 0.583 | 0.691 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.01) | 0.913 | 0.358 | 0.833 | 0.000 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.05) | 0.708 | 0.267 | 0.583 | 0.089 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.1) | 0.432 | 0.114 | 0.417 | 0.683 |
| SERA@DINOv3-S | Energy | Robust-CRC(rho=0.2) | 0.197 | 0.038 | 0.000 | 0.920 |
| SERA@DINOv3-S | Energy | LOSO-CRC (2 src) | 0.365 | 0.077 | 0.250 | 0.894 |
| SERA@DINOv3-S | Energy | LOSO-CRC | 0.346 | 0.070 | 0.250 | 0.915 |
| SERA@DINOv3-S | Energy | LOSO-CRC-worst | 0.247 | 0.045 | 0.167 | 0.973 |
| SERA@DINOv3-S | Remedy+kNN | val-CRC | 0.928 | 0.376 | 1.000 | 0.000 |
| SERA@DINOv3-S | Remedy+kNN | W-CRC | 0.533 | 0.173 | 0.833 | 0.614 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.01) | 0.776 | 0.327 | 0.750 | 0.000 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.05) | 0.464 | 0.219 | 0.500 | 0.107 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.1) | 0.253 | 0.107 | 0.250 | 0.533 |
| SERA@DINOv3-S | Remedy+kNN | Robust-CRC(rho=0.2) | 0.077 | 0.022 | 0.000 | 0.901 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC (2 src) | 0.368 | 0.115 | 0.500 | 0.781 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC | 0.355 | 0.109 | 0.500 | 0.803 |
| SERA@DINOv3-S | Remedy+kNN | LOSO-CRC-worst | 0.211 | 0.058 | 0.167 | 0.925 |
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

## RQ3c - label n images of the new source vs label-free LOSO gate (Remedy+kNN, eps = 5%): risk / acceptance / P(risk > eps)

| model | calibration | n=25 | n=50 | n=100 | n=200 | n=400 |
|---|---|---|---|---|---|---|
| LP-global@DINOv3-B | LOSO-CRC | 0.155 / 0.23 / 0.50 | 0.155 / 0.23 / 0.50 | 0.155 / 0.22 / 0.50 | 0.154 / 0.21 / 0.33 | 0.154 / 0.21 / 0.33 |
| LP-global@DINOv3-B | LOSO-CRC-worst | 0.075 / 0.12 / 0.50 | 0.075 / 0.12 / 0.50 | 0.075 / 0.11 / 0.50 | 0.064 / 0.10 / 0.33 | 0.064 / 0.10 / 0.33 |
| LP-global@DINOv3-B | target-CRC | 0.038 / 0.11 / 0.28 | 0.038 / 0.11 / 0.27 | 0.049 / 0.14 / 0.42 | 0.048 / 0.16 / 0.41 | 0.049 / 0.16 / 0.43 |
| SERA@DINOv3-B | LOSO-CRC | 0.053 / 0.24 / 0.42 | 0.053 / 0.24 / 0.42 | 0.052 / 0.24 / 0.42 | 0.037 / 0.20 / 0.22 | 0.037 / 0.20 / 0.22 |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.035 / 0.17 / 0.32 | 0.035 / 0.17 / 0.32 | 0.035 / 0.17 / 0.33 | 0.025 / 0.15 / 0.22 | 0.025 / 0.15 / 0.22 |
| SERA@DINOv3-B | target-CRC | 0.038 / 0.20 / 0.27 | 0.039 / 0.21 / 0.26 | 0.048 / 0.25 / 0.42 | 0.049 / 0.29 / 0.42 | 0.049 / 0.29 / 0.43 |
| SERA@DINOv3-S | LOSO-CRC | 0.052 / 0.18 / 0.42 | 0.052 / 0.18 / 0.41 | 0.052 / 0.18 / 0.42 | 0.033 / 0.15 / 0.22 | 0.033 / 0.15 / 0.21 |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.025 / 0.11 / 0.16 | 0.025 / 0.11 / 0.15 | 0.025 / 0.11 / 0.15 | 0.020 / 0.10 / 0.09 | 0.020 / 0.10 / 0.08 |
| SERA@DINOv3-S | target-CRC | 0.038 / 0.16 / 0.27 | 0.038 / 0.17 / 0.27 | 0.048 / 0.21 / 0.42 | 0.049 / 0.23 / 0.45 | 0.050 / 0.24 / 0.46 |
| ViTS | LOSO-CRC | 0.072 / 0.37 / 0.42 | 0.072 / 0.37 / 0.42 | 0.072 / 0.37 / 0.42 | 0.049 / 0.35 / 0.22 | 0.049 / 0.35 / 0.22 |
| ViTS | LOSO-CRC-worst | 0.033 / 0.22 / 0.25 | 0.033 / 0.22 / 0.26 | 0.033 / 0.22 / 0.29 | 0.025 / 0.24 / 0.21 | 0.025 / 0.24 / 0.20 |
| ViTS | target-CRC | 0.037 / 0.40 / 0.28 | 0.039 / 0.43 / 0.27 | 0.047 / 0.48 / 0.42 | 0.048 / 0.59 / 0.42 | 0.048 / 0.59 / 0.43 |

## RQ3c - label n images of the new source vs label-free LOSO gate (Remedy+kNN, eps = 10%): risk / acceptance / P(risk > eps)

| model | calibration | n=25 | n=50 | n=100 | n=200 | n=400 |
|---|---|---|---|---|---|---|
| LP-global@DINOv3-B | LOSO-CRC | 0.213 / 0.30 / 0.50 | 0.213 / 0.30 / 0.50 | 0.213 / 0.30 / 0.50 | 0.211 / 0.29 / 0.33 | 0.211 / 0.29 / 0.33 |
| LP-global@DINOv3-B | LOSO-CRC-worst | 0.131 / 0.20 / 0.50 | 0.131 / 0.20 / 0.50 | 0.131 / 0.20 / 0.50 | 0.114 / 0.17 / 0.33 | 0.114 / 0.17 / 0.33 |
| LP-global@DINOv3-B | target-CRC | 0.074 / 0.20 / 0.25 | 0.096 / 0.25 / 0.41 | 0.097 / 0.25 / 0.42 | 0.097 / 0.29 / 0.42 | 0.097 / 0.29 / 0.42 |
| SERA@DINOv3-B | LOSO-CRC | 0.105 / 0.41 / 0.50 | 0.105 / 0.41 / 0.50 | 0.106 / 0.41 / 0.50 | 0.079 / 0.36 / 0.33 | 0.079 / 0.36 / 0.33 |
| SERA@DINOv3-B | LOSO-CRC-worst | 0.073 / 0.30 / 0.30 | 0.073 / 0.30 / 0.28 | 0.073 / 0.30 / 0.28 | 0.056 / 0.27 / 0.11 | 0.056 / 0.27 / 0.11 |
| SERA@DINOv3-B | target-CRC | 0.074 / 0.34 / 0.26 | 0.095 / 0.43 / 0.41 | 0.098 / 0.45 / 0.43 | 0.097 / 0.49 / 0.42 | 0.098 / 0.49 / 0.40 |
| SERA@DINOv3-S | LOSO-CRC | 0.109 / 0.36 / 0.50 | 0.109 / 0.36 / 0.50 | 0.109 / 0.36 / 0.50 | 0.084 / 0.32 / 0.33 | 0.084 / 0.32 / 0.34 |
| SERA@DINOv3-S | LOSO-CRC-worst | 0.058 / 0.21 / 0.17 | 0.058 / 0.21 / 0.17 | 0.058 / 0.21 / 0.16 | 0.039 / 0.18 / 0.00 | 0.039 / 0.18 / 0.00 |
| SERA@DINOv3-S | target-CRC | 0.075 / 0.29 / 0.26 | 0.096 / 0.37 / 0.43 | 0.097 / 0.37 / 0.42 | 0.098 / 0.41 / 0.42 | 0.098 / 0.41 / 0.43 |
| ViTS | LOSO-CRC | 0.147 / 0.63 / 0.42 | 0.147 / 0.63 / 0.42 | 0.147 / 0.63 / 0.42 | 0.087 / 0.57 / 0.22 | 0.087 / 0.57 / 0.22 |
| ViTS | LOSO-CRC-worst | 0.081 / 0.40 / 0.42 | 0.081 / 0.40 / 0.41 | 0.081 / 0.40 / 0.40 | 0.067 / 0.40 / 0.22 | 0.067 / 0.40 / 0.22 |
| ViTS | target-CRC | 0.069 / 0.53 / 0.20 | 0.088 / 0.59 / 0.30 | 0.090 / 0.60 / 0.30 | 0.090 / 0.71 / 0.26 | 0.090 / 0.72 / 0.23 |
