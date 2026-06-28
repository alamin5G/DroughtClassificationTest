# Thesis Defense Preparation Guide
### "Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI"
*(Cross-reference of [`Thesis_Drought_Academic_Presentation.md`](Thesis_Drought_Academic_Presentation.md) ↔ [`master_drought_v2.ipynb`](master_drought_v2.ipynb) ↔ [`generate_all_figures_v2.py`](generate_all_figures_v2.py))*

---

## PART A — Quick Verdict: Does the presentation match the code?

**Mostly YES. The core results are fully reproduced by the code and output files.**
The headline numbers — 35 stations, 1961–2023, 17,868 records, 8 SPEI scales, 76 features, the three model accuracies, the ensemble 97.27% / 99.69% AUC, and the 40/35/25 weights — are all confirmed by the notebook and the JSON outputs.

**BUT you must fix these 6 items before the defense** (the presentation currently OVER-CLAIMS them):

| # | Claim in presentation | Reality in code | Risk | Fix |
|---|---|---|---|---|
| 1 | "Optuna / 50 trials / Bayesian (TPE) hyperparameter search" (§3.5) | **NOT implemented.** Hyperparameters are hard-coded in Phase 6. Optuna only appears as decorative text inside the Figure-3 flowchart box. | HIGH — examiner can ask to see the search logs | Either (a) implement Optuna, or (b) remove the claim and say "hyperparameters were set from prior experimentation / manual tuning". |
| 2 | "Grid-search weight optimization" for the 0.40/0.35/0.25 weights (§3.5) | Weights are **hard-coded** in `CONFIG['ensemble_weights']` ([`master_drought_v2.ipynb`](master_drought_v2.ipynb):252). No grid search code exists. | HIGH | Same: implement a small grid search, or reword to "weights chosen empirically to favour the strongest base learners". |
| 3 | "McNemar's test" for significance (§3.8) | `pingouin` is pip-installed but **never imported/used**. No McNemar computation. | MEDIUM | Either run McNemar (easy: `statsmodels.stats.contingency_tables.mcnemar`) or delete the claim. |
| 4 | "1,000-round bootstrap confidence intervals" (§3.8) | **NOT implemented.** No bootstrap loop anywhere. | MEDIUM | Remove or implement. |
| 5 | "SHAP across **500** test samples" (Abstract, §4.3, Fig 12 caption) | Code computes SHAP on **1,000** rows (`min(1000, len)`; log says "Saved sample test data for SHAP: 1000 records"; [`outputs/shap_test_data.csv`](outputs/shap_test_data.csv) ≈ 1,001 rows). | LOW–MED | Change every "500" to "1,000" in the presentation + Fig 12 caption. |
| 6 | Ensemble "accuracy **±0.32%**, AUC **±0.14%**" (Abstract, §4.1) | The code/JSON/table all give **±0.28%** acc / **±0.13%** AUC (`model_performance.json` → 0.002824 / 0.001267). | LOW | Change to **97.27% ± 0.28%** and **99.69% ± 0.13%**. |

**Plus one internal table error** (not a code issue, a typo in the thesis):
- **Table 4.3 (Feature Importance) is WRONG.** It ranks `SPEI_12m_lag_3` #1 at 0.145. The real code output ([`outputs/feature_importance.json`](outputs/feature_importance.json), [`tables/table_feature_importance_all_76.csv`](tables/table_feature_importance_all_76.csv)) ranks **`SPEI_12m_lag1_safe` #1 at 0.2609 (26.09%)**, and `SPEI_12m_lag3_safe` is **#2 at 0.1086 (10.86%)**. The value 0.145 appears nowhere. → Replace Table 4.3 with the real top-20 from the CSV.

**One accuracy caveat to state honestly if asked:**
- [`outputs/feature_importance.json`](outputs/feature_importance.json) is `RandomForest.feature_importances_` (notebook line ~1501), **not** an ensemble importance. Say "feature importance derived from the Random Forest base learner" to be precise.

---

## PART B — Chapter-by-chapter: what is said, and WHERE in the code to show it

The notebook [`master_drought_v2.ipynb`](master_drought_v2.ipynb) has 22 cells. All methodology logic lives in **one giant definitions cell (code cell #3 / execution_count 2, lines ~74–3568)**. Functions are called in phases via 11 execution cells.

| Presentation section | What it claims | Show in code (notebook function / line) | Supporting figure(s) | Supporting output |
|---|---|---|---|---|
| **§1.1–1.3 Background/Motivation** | 80% rain in monsoon; NW 30–40% drier; groundwater 0.5–1 m/yr decline; single-scale SPI limitations | [`phase_1_preprocessing`](master_drought_v2.ipynb:373) — 35 stations loaded from `data/BD_weather.csv` | Fig 1 | [`tables/table_1_dataset_summary_enhanced.md`](tables/table_1_dataset_summary_enhanced.md) |
| **§3.1 Study area & data** | 35 stations, 8 divisions, 1961–2023, 17,868 monthly obs, BMD/Mendeley source, 67.5% coverage | [`phase_1_preprocessing`](master_drought_v2.ipynb:373) (log: "Loaded 543,839 daily records", 1961–2023, 35 stations) | Fig 1 ([`figure_1_study_area_map.png`](figs/figure_1_study_area_map.png)) | [`data/processed/monthly_climate.csv`](data/processed/monthly_climate.csv) |
| **§3.2 Data processing / QC** | daily→monthly; sum rain / mean temp; 95.3% completeness; mean imputation | [`phase_1_preprocessing`](master_drought_v2.ipynb:373)–466 (nested year/month aggregation loops) | — | [`monthly_climate.csv`](data/processed/monthly_climate.csv); [`Table 3.1`](tables/table_1_dataset_summary_enhanced.md) |
| **§3.3 PET & SPEI** | Hargreaves-Samani PET (Eq 1); Ra (Eq 2); multi-scale SPEI k=1,2,3,6,9,12,18,24; log-logistic (Eq 4) via L-moments; drought label SPEI-12m < −0.5 (Eq 6) | PET: [`calculate_ra`](master_drought_v2.ipynb:479) + [`phase_2_pet_calculation`](master_drought_v2.ipynb:559). SPEI: [`calculate_spei_loglogistic`](master_drought_v2.ipynb:584) + [`phase_3_spei_calculation`](master_drought_v2.ipynb:665) (`scales=[1,2,3,6,9,12,18,24]`). Label: [`phase_5_feature_engineering`](master_drought_v2.ipynb:1140) (`drought_threshold_moderate=-0.5`) | Figs 2a–2e ([`figure_2*_spei_*.png`](figs)) | [`climate_data_with_spei_8scales.csv`](data/processed/climate_data_with_spei_8scales.csv); [`monthly_climate_with_pet.csv`](data/processed/monthly_climate_with_pet.csv) |
| **§3.4 Feature engineering** | 76 features in 6 categories: Base 8, Spatial 6, SPEI-lag 20, Temporal 18, Rolling 16, Bangladesh-specific 8; leakage prevention (drop SPEI_6m/12m/Drought_Class) | [`phase_5_feature_engineering`](master_drought_v2.ipynb:802)–1169 | Fig 3 (flowchart) | [`enhanced_temporal_features.csv`](data/processed/enhanced_temporal_features.csv); [`tables/table_feature_importance_all_76.csv`](tables/table_feature_importance_all_76.csv) |
| **§3.5 ML ensemble** | XGBoost (n_est=723, depth=9, lr=0.035, subsample=0.72, colsample=0.84); RF (700 trees, depth=18); CatBoost (iters=700, depth=8); weights 0.40/0.35/0.25; soft voting; StandardScaler; (⚠ Optuna/grid-search NOT real) | Models: [`RandomForestClassifier`](master_drought_v2.ipynb:1304), [`XGBClassifier`](master_drought_v2.ipynb:1316), [`CatBoostClassifier`](master_drought_v2.ipynb:1330). Weights: `CONFIG['ensemble_weights']` ([`master_drought_v2.ipynb`](master_drought_v2.ipynb):252), applied ~1383. Scaler: ~1295 | Fig 4 (architecture) ([`figure_15_v2_ensemble_architecture.png`](figs/figure_15_v2_ensemble_architecture.png)) | [`models/*.joblib`](models); [`outputs/model_performance.json`](outputs/model_performance.json) |
| **§3.6 Temporal CV** | 5-fold walk-forward; cutoff years 2010,2013,2016,2019,2015 (test windows 11–15/14–17/17–20/20–23/16–23); metrics Acc/Prec/Rec/F1/Spec/AUC | [`temporal_splits`](master_drought_v2.ipynb:1231)–1257 | Fig 5 ([`figure_4_v2_temporal_cv_results.png`](figs/figure_4_v2_temporal_cv_results.png)) | [`outputs/temporal_cv_results.json`](outputs/temporal_cv_results.json); [`Table 4.1`](tables/table_2_temporal_cv_metrics.csv) |
| **§3.7 Explainability** | SHAP TreeExplainer; Shapley value (Eq 35); global importance (Eq 36) | **NOT in notebook cells** — runs in separate script [`outputs/calculate_real_shap.py`](outputs/calculate_real_shap.py):30–67 (ensemble SHAP = simple mean of RF+XGB+Cat SHAP) | Fig 12 ([`figure_9_v2_shap_summary.png`](figs/figure_9_v2_shap_summary.png)) | [`outputs/precomputed_shap.json`](outputs/precomputed_shap.json) |
| **§3.8 Stats / eval** | core metrics; (⚠ McNemar + 1000-bootstrap NOT implemented) | Phase 6 evaluation block | — | [`outputs/temporal_cv_results.json`](outputs/temporal_cv_results.json) |
| **§4.1 Temporal CV results** | Ensemble 97.27%±0.28% acc, 99.69%±0.13% AUC (⚠ presentation says ±0.32/0.14); split 3 highest | Phase 6 run log + [`outputs/temporal_cv_results.json`](outputs/temporal_cv_results.json) | Fig 5 | [`Table 4.1`](tables/table_2_temporal_cv_metrics.csv) |
| **§4.2 Model comparison** | XGB 97.46/99.78, Cat 97.34/99.77, RF 94.41/98.93, Ensemble 97.27/99.69; +2.86% over RF | [`outputs/model_performance.json`](outputs/model_performance.json); [`outputs/temporal_cv_results.json`](outputs/temporal_cv_results.json) | Figs 6,7,8,9,10 | [`Table 4.2`](tables/table_3_model_performance_enhanced.md) |
| **§4.3 Feature importance & SHAP** | SPEI lags dominate; top `SPEI_12m_lag1_safe`=26.09%; SHAP over samples | [`outputs/feature_importance.json`](outputs/feature_importance.json) (RF importance); [`outputs/precomputed_shap.json`](outputs/precomputed_shap.json) (⚠ 1000 samples not 500) | Figs 11, 12 | [`Table 4.3`](tables/table_feature_importance_all_76.csv) (⚠ Table 4.3 numbers are wrong — replace) |
| **§4.4 Spatial & seasonal** | NW/Rajshahi most severe; Sylhet highest freq 33.2%, Rangpur lowest 26.7%; Aman 28.45%, Boro 28.31%, Aus 27.85%; station reliability 97.78–99.28% | [`create_bangladesh_features_v2`](generate_all_figures_v2.py:954); [`create_station_performance_v2`](generate_all_figures_v2.py:1670) (⚠ reliability is a proxy formula, not measured per-station accuracy) | Figs 13a,13b,14 | [`enhanced_temporal_features.csv`](data/processed/enhanced_temporal_features.csv); [`Table 4.4`](tables/table_4_station_performance.md) |
| **§4.5 Result comparison** | beats Sadiq 81–95%, Hossain 96%, Paul 92% | (literature comparison — no code) | — | Table 4.5 |
| **§5 Conclusion** | 4 innovations; 97.27% beats prior best 96% by +1.28pp; serves 40M people | (summary of above) | — | — |

---

## PART C — Figure-by-figure speaking notes
*(Note: presentation figure numbers ≠ figs/ file numbers from Fig 4 onward. Each entry lists BOTH.)*

### Fig 1 — Study Area Map  →  [`figure_1_study_area_map.png`](figs/figure_1_study_area_map.png)
**What it shows:** Bangladesh map (8 divisions shaded pastel), 35 red station dots with labels; footer "35 Stations (1961–2023) • N Records • 67.5% Coverage".
**Say:** "These 35 BMD stations span all 8 divisions and give a continuous 63-year record. Note the denser coverage in the south-east (Chittagong division) and the north-west drought belt (Rajshahi/Rangpur)."
**Watch out:** the "67.5% Coverage" string is hard-coded, not computed here — if asked, say it's the raw-station completeness reported in §3.1/§5.4.

### Figs 2a–2e — Multi-scale SPEI time series (Rajshahi)  →  [`figure_2*_spei_*.png`](figs)
**What they show:** 3-month-smoothed SPEI for Rajshahi (NW representative) at 5 scale groups (1–2m, 3–6m, 9–12m, 18–24m, summary); red dashed line at −0.5 (Moderate), dark-red dotted at −1.5 (Severe); major-drought years marked.
**Say:** "Each timescale captures a different drought type — short-term (1–3m) = meteorological, 6m = agricultural, 12m = hydrological, 18–24m = socio-economic. Notice how longer scales smooth out the noise and make the multi-year droughts (1979, 1994, 2009, 2018–19) clearly visible."
**Key teaching point:** this justifies WHY we need 8 scales instead of the 3–4 used by prior Bangladesh studies.

### Fig 3 — Methodology Flowchart  →  [`figure_3_methodology_flowchart.png`](figs/figure_3_methodology_flowchart.png)
**What it shows:** 10-box pipeline: Raw Data → Processing → PET → SPEI → Feature Eng (76) → ML (40/35/25) → Ensemble → (⚠ "Hyperparameter Tuning / Optuna" box) → 5-fold Temporal CV → Results.
**Say:** Walk left-to-right; emphasise the temporal CV box (our novelty) and the explainability.
**⚠ Defense fix:** either remove the "Optuna / 50 trials" box text, or actually implement Optuna. Currently it's decorative only.

### Fig 4 — Ensemble Architecture  →  [`figure_15_v2_ensemble_architecture.png`](figs/figure_15_v2_ensemble_architecture.png)
**What it shows:** 3 base boxes (XGBoost/RF/CatBoost with Acc+AUC) → weight pills 40/35/25 → "Weighted Ensemble" box; formula `P = 0.40·XGB + 0.35·RF + 0.25·Cat`.
**Say:** "Soft-voting probability averaging. XGBoost gets the highest weight because it is the strongest single model; RF adds diversity; CatBoost handles categorical station encoding well."
**Watch out:** all numbers on this figure are hard-coded in the function (they match the JSON, but aren't read live). If challenged on the weights, point to `CONFIG['ensemble_weights']` in the notebook.

### Fig 5 — Temporal CV Results  →  [`figure_4_v2_temporal_cv_results.png`](figs/figure_4_v2_temporal_cv_results.png)
**What it shows:** LEFT — accuracy/AUC/F1 of the ensemble across the 5 walk-forward splits (value-annotated); RIGHT — 3 summary bars with ±1 SD error bars.
**Say:** "Five temporal splits, each training on the past and testing on a strictly later window — no future leaks in. Accuracy stays within ±0.28%, showing stability. This is the key methodological contribution vs random-split studies."
**Where the numbers live:** [`outputs/temporal_cv_results.json`](outputs/temporal_cv_results.json).

### Fig 6 — Model Comparison AUC  →  [`figure_5_v2_model_comparison_auc.png`](figs/figure_5_v2_model_comparison_auc.png)
**What it shows:** bar chart of mean AUC for the 4 models (ensemble bar bold red border); each labelled "AUC x% / Acc y%".
**Say:** "XGBoost (99.78%) and CatBoost (99.77%) are nearly tied; RF is weakest (98.93%); the ensemble (99.69%) trades a hair of peak AUC for robustness — note the much lower variance."

### Fig 7 — ROC Curves  →  [`figure_6_v2_roc_curve.png`](figs/figure_6_v2_roc_curve.png)
**What it shows:** ROC for 4 models; ensemble thick red; random diagonal; legend AUCs to 4 decimals.
**Say:** "All curves hug the top-left corner = excellent discrimination. The ensemble curve sits between XGBoost and RF — combining models."
**Note:** the legend AUCs are the CV-mean values from [`temporal_cv_results.json`](outputs/temporal_cv_results.json); the curve *shape* comes from pooled [`model_predictions.json`](outputs/model_predictions.json).

### Fig 8 — Confusion Matrix  →  [`figure_7_v2_confusion_matrix.png`](figs/figure_7_v2_confusion_matrix.png)
**What it shows:** 2×2 heatmap (No-Drought/Drought), integer counts pooled across all splits; green box with CV-mean metrics.
**Say:** "Errors are balanced between false alarms and misses — the model isn't biased toward one class. Read the TP/TN counts off the cells."

### Fig 9 — Prediction Distribution  →  [`figure_11_v2_prediction_distribution.png`](figs/figure_11_v2_prediction_distribution.png)
**What it shows:** KDE of predicted drought probability; blue = true No-Drought, red = true Drought; vertical threshold line at 0.5.
**Say:** "Two well-separated peaks — the model is very confident. The small overlap near 0.5 is where errors occur."
**⚠ Note:** if [`model_predictions.json`](outputs/model_predictions.json) is missing the figure falls back to a SYNTHETIC distribution; confirm the file exists before relying on it.

### Fig 10 — Performance Metrics (all models)  →  [`figure_12_v2_performance_metrics.png`](figs/figure_12_v2_performance_metrics.png)
**What it shows:** grouped bars — 4 models × 5 metrics (Acc/Prec/Rec/F1/AUC).
**Say:** "Across every metric the ensemble is competitive with the best single model while beating RF clearly. RF's lower recall (90.47%) is what the ensemble fixes."

### Fig 11 — Top 20 Features  →  [`figure_8_v2_feature_importance.png`](figs/figure_8_v2_feature_importance.png)
**What it shows:** horizontal bars (top 20), coloured by family (red=SPEI, blue=Climate, green=Temporal, orange=Spatial); info box with top-3 plain-English.
**Say:** "SPEI lag features — especially `SPEI_12m_lag1_safe` (26%) — dominate. This proves the multi-scale lag design is the biggest driver. The Bangladesh-specific monsoon/crop features (orange family) contribute smaller but meaningful signals."
**⚠ Be precise:** importance source = Random Forest. (There is also an all-76 variant [`figure_8_v2_feature_importance_all_76.png`](figs/figure_8_v2_feature_importance_all_76.png) — not in the List of Figures; useful as an appendix.)

### Fig 12 — SHAP Summary  →  [`figure_9_v2_shap_summary.png`](figs/figure_9_v2_shap_summary.png)
**What it shows:** SHAP beeswarm — each dot = one test sample; colour = feature value (red high/blue low); x = SHAP value (right = pushes toward drought).
**Say:** "Low SPEI values (blue dots on the right... actually negative SHAP) drive drought prediction. High rainfall/humidity reduce risk. This is the explainability layer — we don't just predict, we show WHY."
**⚠ Defense fix:** change the caption from "500 samples" to "**1,000** samples" everywhere. Source: [`outputs/precomputed_shap.json`](outputs/precomputed_shap.json) (ensemble SHAP = mean of 3 models' SHAP, from [`calculate_real_shap.py`](outputs/calculate_real_shap.py)).

### Fig 13a — Agricultural Seasons  →  [`figure_10_v2_agricultural_seasons.png`](figs/figure_10_v2_agricultural_seasons.png)
**What it shows:** grouped bars for Boro/Aus/Aman — drought frequency (coral) beside model accuracy (blue) with ±1 SD error bars.
**Say:** "Drought frequency is similar across seasons (~28%) but the error bars show large year-to-year variability — some years hit certain crops hard. The model accuracy stays high regardless of season."

### Fig 13b — Monsoon Phases  →  [`figure_10b_v2_monsoon_phases.png`](figs/figure_10b_v2_monsoon_phases.png)
**What it shows:** 4 bars (Dry/Pre/Peak/Post monsoon) of drought frequency with ±1 SD.
**Say:** "Despite 80% of rain in peak monsoon, drought still occurs ~30% of the time on average — because we classify monthly deficits. The dry phase (Dec–Feb) is the natural risk window for the Boro crop."

### Fig 14 — Station-wise Reliability  →  [`figure_14_v2_station_performance.png`](figs/figure_14_v2_station_performance.png)
**What it shows:** Bangladesh map; 35 dots coloured by "Model Reliability Score" (RdYlGn, 90–100%).
**⚠ IMPORTANT — be honest here:** these scores are a **proxy/heuristic**, NOT measured per-station CV accuracy. Formula: `97.27% + (2·completeness − 1) + (2·coverage_ratio − 1)`, clipped to [90,100]. Range 97.78% (Ambaganctg) → 99.28% (Dhaka/Bogra/etc.).
**If asked "how did you measure per-station accuracy?":** Answer: "We did not retrain per station; this map encodes data-quality-driven confidence — stations with longer, more complete records get a higher reliability band around the overall 97.27%." (Documented in [`tables/table_4_station_performance.md`](tables/table_4_station_performance.md).)

### EXTRA figures NOT in the List of Figures (know they exist):
- [`figure_3_v2_drought_area_index.png`](figs/figure_3_v2_drought_area_index.png) — % of stations in drought per year (SPEI-3m). **Great to mention** for the "spatial/temporal pattern" question.
- [`figure_8_v2_feature_importance_all_76.png`](figs/figure_8_v2_feature_importance_all_76.png) — all 76 features (appendix).
- [`figure_10*_stationwise.png`](figs) — per-station season/phase breakdowns (appendix).
- Folders: [`drought_area_index/`](figs/drought_area_index) (8 scales), [`agricultural_seasons_stations/`](figs/agricultural_seasons_stations) (35), [`monsoon_phases_stations/`](figs/monsoon_phases_stations) (35), [`spei_stations/`](figs/spei_stations) (per-station SPEI — generated by a different script).

---

## PART D — "Where does the number live?" cheat sheet (for live questions)

| If asked about… | Open this file |
|---|---|
| Any model Accuracy / AUC / F1 (Figs 5,6,7,8,10) | [`outputs/temporal_cv_results.json`](outputs/temporal_cv_results.json) → mirror [`tables/table_2_temporal_cv_metrics.csv`](tables/table_2_temporal_cv_metrics.csv) |
| Mean±std per model (the 97.27% etc.) | [`outputs/model_performance.json`](outputs/model_performance.json) ⚠ (note: figures don't read this, but it holds the clean means) |
| Confusion-matrix counts / ROC shape / probabilities | [`outputs/model_predictions.json`](outputs/model_predictions.json) |
| Feature importance bars | [`outputs/feature_importance.json`](outputs/feature_importance.json) → [`tables/table_feature_importance_all_76.csv`](tables/table_feature_importance_all_76.csv) |
| SHAP dots | [`outputs/precomputed_shap.json`](outputs/precomputed_shap.json) |
| Season/phase drought frequencies | [`data/processed/enhanced_temporal_features.csv`](data/processed/enhanced_temporal_features.csv) |
| Per-station reliability formula | [`tables/table_4_station_performance.md`](tables/table_4_station_performance.md) |

---

## PART E — Likely examiner questions & ready answers

1. **"Why walk-forward and not k-fold?"** → Random k-fold shuffles time, letting the model train on future data to predict the past = leakage. Walk-forward always trains on older, tests on newer windows — realistic for early warning.
2. **"Why only 3 base models? Why these weights?"** → Tree ensembles (XGB/CatBoost/RF) are SOTA for tabular climate data; weights 40/35/25 favour the strongest learners while keeping diversity. (If pushed on "grid search" — see Part A fix #2.)
3. **"Where is your hyperparameter tuning?"** → State they are set from systematic manual experimentation; if you claim Optuna, implement it first.
4. **"Is 97.27% realistic / overfit?"** → ±0.28% across 5 strictly temporal splits = stable, not a lucky random split. Cite the walk-forward design.
5. **"Why SPEI and not SPI?"** → SPI uses rainfall only; SPEI adds PET (temperature) → captures warming-driven drought, critical under climate change.
6. **"How is this explainable?"** → SHAP (Fig 12) shows each feature's contribution per prediction; top drivers are interpretable SPEI lags.
7. **"What about per-station accuracy?"** → Be honest: Fig 14 is a reliability proxy from data quality, not retrained accuracy (Part C, Fig 14).
8. **"Binary drought — why not multi-class?"** → Stated limitation (§5.5): future work is multi-class severity (moderate/severe/extreme).

---

## PART F — Minimum to-do before submitting the thesis
1. Fix Table 4.3 with the real top-20 feature values from [`table_feature_importance_all_76.csv`](tables/table_feature_importance_all_76.csv).
2. Change "500 samples" → "1,000 samples" (Abstract, §4.3, Fig 12 caption).
3. Change "±0.32% / ±0.14%" → "±0.28% / ±0.13%" (Abstract, §4.1).
4. Decide on Optuna / McNemar / bootstrap: **either implement or remove** from §3.5/§3.8 (highest-risk over-claims).
5. Add missing Figure 2b & 2c to the List of Figures; fix Figure 2e caption (it duplicates 12m — should reflect very-long-term/24m).
6. Fix the citation-number drift in §4.5 (e.g. "[11]" points to multiple different studies).
7. Reconcile Table 3.1's "Total Features 92 (Enhanced)" vs "76" used for training (raw columns vs engineered features) — add a one-line clarifying note.
