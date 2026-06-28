# Thesis Slide-Generation Brief (AI-Ready)
> **Purpose:** Any AI (PowerPoint / Beamer / reveal.js / Gamma / Pitch generator) given this single file must be able to produce the complete thesis defense slide deck. It is fully self-contained: structure, design rules, per-slide content, exact figure files to embed, and verified numbers.

---

## 0. PROJECT CONTEXT (give the AI this one-paragraph orientation)
**Title:** Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI.
**Authors:** Md. Alamin (ID 21303134) & SK Ikhtear Ahmed Choton (ID 21303136) — BCSE, IUBAT — International University of Business Agriculture and Technology, Dept. of CSE. Term: Spring 2026.
**Supervisor:** Md. Alomgir Hossain (Associate Professor). Co-supervisor: Dr. Md. Rashedul Islam. Chair: Prof. Dr. Utpal Kanti Das.
**One-line summary:** A 3-model weighted ensemble (XGBoost 40%, Random Forest 35%, CatBoost 25%) classifies meteorological drought across 35 Bangladeshi stations (1961–2023) using 8-scale SPEI + 76 engineered features, validated by 5-fold walk-forward temporal CV, achieving **97.27% accuracy / 99.69% AUC**, explained with SHAP.
**Talk length:** ~15–20 minutes → ~32 slides.

---

## 1. OUTPUT & DESIGN INSTRUCTIONS (read before generating)
- **Format:** 16:9 widescreen. Generate native slides (PPTX preferred; Beamer or reveal.js acceptable). Do NOT paste this Markdown onto slides verbatim — convert each "Slide" block below into ONE visual slide.
- **Rule of thumb:** max 6 bullets/slide, max ~12 words/bullet, font ≥ 24 pt body / ≥ 32 pt title. Use the **Title** as the slide header.
- **Layout types:** `TITLE` (centered title slide), `BULLETS`, `FIGURE-LEFT/BULLETS-RIGHT` (or full-bleed figure), `EQUATION`, `TABLE`, `SECTION-DIVIDER`.
- **Color palette:**
  - Primary deep green `#1B5E20` (agriculture/Bangladesh) for titles & headers.
  - Accent terracotta `#E65100` (drought/heat) for highlights, key numbers, warning callouts.
  - Secondary navy `#0D47A1` for data/tables.
  - Background white `#FFFFFF`; muted grey `#F5F5F5` for boxes.
- **Fonts:** Inter / Calibri / Source Sans (sans-serif). Monospace (Consolas) for equations & code.
- **Footer:** small text — left = short deck title, right = slide number / total. Consistent on all content slides.
- **Figures:** always embed the EXACT file named in each slide's `FIGURE:` line (paths relative to project root `/home/alamin/Documents/DroughtClassificationTest/`). Use the figure as full-bleed or half-slide. Add a 1-line figure caption underneath in italic grey.
- **Tables:** render the provided rows as a clean table; bold the header row; highlight "Our Study / Ensemble" row in light terracotta.
- **Speaker notes:** put each slide's `SAY:` text into the slide's NOTES / presenter-notes section (not on the visible slide).
- **Key-number callouts:** display hero numbers (e.g., **97.27%**, **99.69%**, **35 stations**, **8 scales**) in large terracotta text boxes.
- **Citation tags:** keep reference markers like [11], [13] as small superscripts; full list on the final References slide.

---

## 2. GLOBAL VERIFIED NUMBERS (use these EXACT values everywhere — they are code-confirmed)
- Stations: **35**, across **8 divisions**. Bounds 20.7°–26.6°N, 88.0°–92.7°E.
- Period: **1961–2023 (63 years)**, **17,868** monthly observations (from 543,839 daily records).
- SPEI scales: **8** → 1, 2, 3, 6, 9, 12, 18, 24 months.
- Features: **76** total → Base Climate 8, Spatial 6, SPEI-Lag 20, Temporal 18, Rolling 16, Bangladesh-specific 8.
- Drought label: **SPEI-12m < −0.5** = drought (binary). PET method: **Hargreaves-Samani (FAO-56)**. SPEI distribution: **log-logistic** (L-moments).
- Models / hyperparameters (verified in code):
  - **XGBoost:** n_estimators=723, max_depth=9, learning_rate=0.035, subsample=0.72, colsample_bytree=0.84 → **97.46% acc / 99.78% AUC**.
  - **Random Forest:** 700 trees, max_depth=18 → **94.41% acc / 98.93% AUC**.
  - **CatBoost:** iterations=700, depth=8 → **97.34% acc / 99.77% AUC**.
  - **Ensemble (weighted soft voting):** weights **0.40 / 0.35 / 0.25** → **97.27% ± 0.28% acc / 99.69% ± 0.13% AUC**; F1 96.12%, Precision 97.19%, Recall 95.09%.
- Validation: **5-fold walk-forward temporal CV**, cutoff years 2010, 2013, 2016, 2019, 2015.
- Explainability: **SHAP TreeExplainer** on **1,000** test samples; ensemble SHAP = mean(RF, XGB, CatBoost) SHAP.
- Top feature: **`SPEI_12m_lag1_safe` = 26.09%** importance (#1); `SPEI_12m_lag3_safe` = 10.86% (#2). Source = Random Forest feature importance.
- Processing: <40 minutes for 17,868 records; data completeness 95.30% (station-month); raw coverage 67.5%.
- ⚠ **Defensible wording note:** phrase hyperparameter selection as "systematic experimentation" (do NOT claim Optuna/grid-search/McNemar/bootstrap unless those are implemented). Keep slides defensible.

---

## 3. SLIDE-BY-SLIDE DECK

### SLIDE 1 — TITLE
- **Type:** TITLE
- **Title:** Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI
- **Body (centered, stacked):**
  - Md. Alamin (21303134) · SK Ikhtear Ahmed Choton (21303136)
  - Bachelor of Computer Science and Engineering
  - IUBAT — International University of Business Agriculture and Technology
  - Supervisor: Md. Alomgir Hossain · Co-supervisor: Dr. Md. Rashedul Islam
  - Term: Spring 2026
- **SAY:** "Good morning. Our work builds an explainable, temporally validated drought classification system for Bangladesh using multi-scale SPEI."

### SLIDE 2 — OUTLINE / AGENDA
- **Type:** BULLETS
- **Title:** Presentation Outline
- **Bullets:** 1) Introduction & Motivation · 2) Research Gap & Objectives · 3) Methodology · 4) Results & Discussion · 5) Comparison & Contributions · 6) Limitations & Future Work · 7) Conclusion
- **SAY:** "I'll walk through the problem, our framework, results, and contributions."

### SLIDE 3 — SECTION DIVIDER: INTRODUCTION
- **Type:** SECTION-DIVIDER (deep green background, white text)
- **Title:** 1 · Introduction

### SLIDE 4 — BACKGROUND: DROUGHT IN BANGLADESH
- **Type:** BULLETS (terracotta callout box for key figures)
- **Title:** Why Drought Matters for Bangladesh
- **Bullets:**
  - Population 175.7M; ~70% depend on agriculture; rice covers 75% of arable land.
  - ~80% of annual rain falls in monsoon (Jun–Sep); dry window Nov–Apr.
  - North-West receives 30–40% less rain; groundwater declining 0.5–1.0 m/yr.
  - Drought hits ~35–40% of recent years; 2018–19 hit Boro rice (=55% of rice output).
- **Callout:** "Drought threatens food security for ~40 million people."
- **SAY:** "Drought is a slow, recurring disaster that quietly damages agriculture and water supply, especially in the north-west."

### SLIDE 5 — PROBLEM STATEMENT
- **Type:** BULLETS
- **Title:** The Problem
- **Bullets:**
  - Traditional drought indices (SPI) use rainfall only — ignore temperature & evapotranspiration.
  - Prior studies use only 3–4 SPEI scales, not the recommended 8.
  - Random train/test splits leak future data → overly optimistic accuracy.
  - Bangladesh-specific monsoon/crop patterns rarely engineered as features.
  - No explainable AI (X-AI) → models aren't operationally trustworthy.
- **SAY:** "Four gaps: weak indices, few scales, leaked validation, and no explainability."

### SLIDE 6 — RESEARCH GAP
- **Type:** TABLE
- **Title:** Gap in Existing Bangladesh Studies
- **Table:** Study | Data/Method | Key Limitation
  - Rahman & Lateh (2016) | 35 stns, SPI/GIS | No ML, no explainability
  - Mashuq/Khan (2024) | 1 station, XGBoost | 1 station, 4 scales, random split
  - Paul et al. (2024) | 38 districts, ensemble | No temporal ordering (leakage)
  - Hossain et al. (2025) | 4 districts, Prophet/SARIMA | Forecasting only
  - Hossain et al. (2025) | Central BD, RF/XGB/SVM | No X-AI, no temporal CV
- **SAY:** "Each prior work misses at least one of: scale coverage, temporal validation, BD features, or explainability."

### SLIDE 7 — OBJECTIVES
- **Type:** BULLETS (numbered, terracotta numbers)
- **Title:** Research Objectives
- **Bullets:**
  1. Build a 3-model weighted ensemble (XGBoost, RF, CatBoost).
  2. Validate with 5-fold walk-forward temporal cross-validation.
  3. Engineer 76 Bangladesh-specific features (monsoon phases + crop seasons).
  4. Provide SHAP-based explainability.
  5. Benchmark against prior Bangladesh drought studies.
- **SAY:** "Five objectives spanning accuracy, validation, features, explainability, and comparison."

### SLIDE 8 — RESEARCH QUESTIONS
- **Type:** BULLETS
- **Title:** Research Questions
- **Bullets:**
  - RQ1: Can an ensemble + 8-scale SPEI improve drought classification accuracy?
  - RQ2: Is walk-forward CV more reliable than random splits?
  - RQ3: How much do Bangladesh-specific monsoon/crop features matter?
  - RQ4: Which variables dominate predictions (per SHAP)?
  - RQ5: How does our system compare with existing BD studies?
- **SAY:** "Each question maps directly to an objective and a results slide."

### SLIDE 9 — SECTION DIVIDER: METHODOLOGY
- **Type:** SECTION-DIVIDER
- **Title:** 3 · Research Methodology

### SLIDE 10 — STUDY AREA & DATA
- **Type:** FIGURE-LEFT/BULLETS-RIGHT
- **Title:** Study Area & Dataset
- **FIGURE:** `figs/figure_1_study_area_map.png`
- **Caption (italic grey):** Figure 1 — 35 BMD meteorological stations across 8 divisions (1961–2023).
- **Bullets:**
  - 35 stations, 8 divisions, 63 years (1961–2023).
  - 543,839 daily → 17,868 monthly records.
  - Source: Bangladesh Meteorological Department (BMD).
  - Validated against documented drought years (1979, 1994, 2009, 2018–19).
- **SAY:** "Thirty-five stations give nationwide coverage; we matched all major documented drought events."

### SLIDE 11 — DATA PROCESSING & QC
- **Type:** BULLETS
- **Title:** Data Processing & Quality Control
- **Bullets:**
  - Daily → monthly: sum rainfall, mean temperature/humidity/sunshine.
  - 95.30% completeness after aggregation.
  - Missing values: mean imputation (training-derived → applied to test, no leakage).
  - Full pipeline runtime < 40 minutes for all 17,868 records.
- **SAY:** "We aggregate to monthly, ensure completeness, and impute safely to prevent leakage."

### SLIDE 12 — PET: HARGREAVES-SAMANI
- **Type:** EQUATION
- **Title:** Potential Evapotranspiration (PET)
- **Equation (centered, large):** `PET = 0.0023 × 0.408 × Ra × (Tmean + 17.8) × √(Tmax − Tmin)`
- **Bullets (below equation):**
  - Hargreaves-Samani method (FAO-56) — temperature-driven, data-light.
  - Ra = extraterrestrial radiation (computed from latitude & day-of-year).
  - Captures warming-driven water demand that SPI ignores.
- **SAY:** "PET turns temperature into water demand; this is what makes SPEI superior to SPI."

### SLIDE 13 — MULTI-SCALE SPEI
- **Type:** EQUATION + BULLETS
- **Title:** Multi-Scale SPEI (Log-Logistic)
- **Equation:** `D = Σ(P − PET)`; fit log-logistic F(x); standardize to SPEI.
- **Bullets:**
  - 8 timescales: 1, 2, 3, 6, 9, 12, 18, 24 months.
  - Log-logistic distribution fitted via L-moments.
  - Each scale = different drought type: 1–3m meteorological · 6m agricultural · 12m hydrological · 18–24m socio-economic.
  - Binary drought label: **SPEI-12m < −0.5**.
- **Callout:** "8 scales vs 3–4 in prior BD work."
- **SAY:** "Multiple scales let us see the same drought from meteorological to socio-economic viewpoints."

### SLIDE 14 — SPEI TIME SERIES
- **Type:** FIGURE (full or 2-up)
- **Title:** Drought Evolution Across Scales (Rajshahi, NW)
- **FIGURE (primary):** `figs/figure_2e_v2_spei_summary.png`
- **Optional second image:** `figs/figure_2_v2_spei_short_term.png` and `figs/figure_2d_v2_spei_very_long_term.png`
- **Caption:** Figure 2 — SPEI time series; red = −0.5 (Moderate), dark-red = −1.5 (Severe).
- **SAY:** "Longer scales smooth noise and reveal multi-year droughts (1979, 1994, 2009, 2018–19). This justifies using 8 scales."

### SLIDE 15 — FEATURE ENGINEERING (76 FEATURES)
- **Type:** BULLETS (6 colored category chips)
- **Title:** 76 Engineered Features
- **Bullets (one per category with count):**
  - 🟦 Base Climate (8): rainfall, temps, humidity, PET, water balance, Ra.
  - 🟪 Spatial (6): lat/lon, distance-to-Bay, station encoding.
  - 🟥 SPEI Lag (20): all 8 scales at multiple lags.
  - 🟩 Temporal (18): seasonal decomposition, Fourier, monsoon/crop markers.
  - 🟧 Rolling Statistics (16): 3/6/12-month mean & std for rainfall/temp/PET.
  - 🟫 Bangladesh-Specific (8): 4 monsoon phases + 3 crop seasons + Is_Monsoon.
- **Callout:** "Leakage prevention: SPEI_6m/12m & target excluded; safe lags ≥ 3 months."
- **SAY:** "Six families, 76 features — the Bangladesh-specific monsoon and crop features are our novel contribution."

### SLIDE 16 — METHODOLOGY FLOWCHART
- **Type:** FIGURE (full-bleed)
- **Title:** End-to-End Framework
- **FIGURE:** `figs/figure_3_methodology_flowchart.png`
- **Caption:** Figure 3 — Pipeline: data → PET → SPEI → features → ensemble → temporal CV → explainability.
- **SAY:** "Data flows left to right; the temporal CV and SHAP blocks are our key additions."

### SLIDE 17 — ML ENSEMBLE ARCHITECTURE
- **Type:** FIGURE-LEFT/BULLETS-RIGHT
- **Title:** Weighted Ensemble Classifier
- **FIGURE:** `figs/figure_15_v2_ensemble_architecture.png`
- **Caption:** Figure 4 — Soft voting: P = 0.40·XGB + 0.35·RF + 0.25·CatBoost.
- **Bullets:**
  - Three gradient-boosted / bagged tree models.
  - Weighted soft voting on predicted probabilities.
  - Weights favour strongest learners (XGBoost) while keeping diversity.
  - Decision threshold 0.5; features StandardScaler-normalized (fit on train only).
- **SAY:** "Each model votes with a probability; weights 40/35/25 maximise robustness."

### SLIDE 18 — WALK-FORWARD TEMPORAL CV
- **Type:** TABLE
- **Title:** 5-Fold Walk-Forward Validation
- **Table:** Fold | Train | Test
  - 1 | 1961–2010 | 2011–2015
  - 2 | 1961–2013 | 2014–2017
  - 3 | 1961–2016 | 2017–2020
  - 4 | 1961–2019 | 2020–2023
  - 5 | 1961–2015 | 2016–2023
- **Callout:** "Train only on the PAST, test on a strictly LATER window → no leakage."
- **SAY:** "This is our main methodological novelty — realistic, leak-free evaluation."

### SLIDE 19 — SECTION DIVIDER: RESULTS
- **Type:** SECTION-DIVIDER
- **Title:** 4 · Results & Discussion

### SLIDE 20 — TEMPORAL CV RESULTS
- **Type:** FIGURE-LEFT/BULLETS-RIGHT
- **Title:** Ensemble Stability Across 5 Splits
- **FIGURE:** `figs/figure_4_v2_temporal_cv_results.png`
- **Caption:** Figure 5 — Accuracy/AUC/F1 per split with ±1 SD error bars.
- **Bullets:**
  - Ensemble: **97.27% ± 0.28% accuracy**, **99.69% ± 0.13% AUC**.
  - Best split 2017–2020 (97.56%); tightest spread confirms robustness.
  - No lucky random split — every fold is strictly temporal.
- **SAY:** "Variance under 0.3% across five temporal folds proves the result is stable, not coincidental."

### SLIDE 21 — MODEL COMPARISON
- **Type:** TABLE + callouts
- **Title:** Model Performance Comparison
- **Table:** Model | Accuracy | AUC | F1
  - XGBoost | 97.46% | 99.78% | 96.43%
  - Random Forest | 94.41% | 98.93% | 92.05%
  - CatBoost | 97.34% | 99.77% | 96.23%
  - **Ensemble** | **97.27%** | **99.69%** | **96.12%**
- **Callout:** "Ensemble lifts RF by +2.86% while matching the best single models."
- **SAY:** "Individually XGBoost and CatBoost are strongest; the ensemble adds stability, especially over Random Forest."
- **FIGURE (optional):** `figs/figure_5_v2_model_comparison_auc.png`

### SLIDE 22 — ROC & DISCRIMINATION
- **Type:** FIGURE
- **Title:** ROC Curve — Excellent Discrimination
- **FIGURE:** `figs/figure_6_v2_roc_curve.png`
- **Caption:** Figure 7 — All models hug the top-left; ensemble in red.
- **SAY:** "AUC near 0.997 means the model almost perfectly separates drought from non-drought months."

### SLIDE 23 — CONFUSION MATRIX
- **Type:** FIGURE-LEFT/BULLETS-RIGHT
- **Title:** Confusion Matrix (Ensemble)
- **FIGURE:** `figs/figure_7_v2_confusion_matrix.png`
- **Caption:** Figure 8 — Pooled across all splits.
- **Bullets:**
  - Balanced errors: few false alarms, few misses.
  - No systematic bias toward either class.
- **SAY:** "Mistakes are balanced — the model isn't over-predicting drought."

### SLIDE 24 — FEATURE IMPORTANCE
- **Type:** FIGURE-LEFT/BULLETS-RIGHT
- **Title:** What Drives Drought Predictions
- **FIGURE:** `figs/figure_8_v2_feature_importance.png`
- **Caption:** Figure 11 — Top 20 features (Random Forest importance).
- **Bullets:**
  - **#1: `SPEI_12m_lag1_safe` = 26.09%** — last year's long-term deficit.
  - **#2: `SPEI_12m_lag3_safe` = 10.86%.**
  - SPEI lag features (red) dominate → validates multi-scale design.
  - Bangladesh-specific monsoon/crop features add meaningful signal.
- **SAY:** "Multi-scale lagged SPEI is by far the strongest predictor — exactly what we designed for."

### SLIDE 25 — SHAP EXPLAINABILITY
- **Type:** FIGURE-LEFT/BULLETS-RIGHT
- **Title:** SHAP: Explaining Every Prediction
- **FIGURE:** `figs/figure_9_v2_shap_summary.png`
- **Caption:** Figure 12 — SHAP beeswarm across 1,000 test samples.
- **Bullets:**
  - Each dot = one prediction; color = feature value (red high / blue low).
  - Low SPEI values push predictions toward drought (right).
  - High rainfall & humidity reduce risk (left).
- **SAY:** "We don't just predict drought — SHAP shows exactly which variables pushed each decision, enabling trust in operational use."

### SLIDE 26 — SPATIAL & SEASONAL PATTERNS
- **Type:** FIGURE (2-up) + bullets
- **Title:** Where & When Drought Strikes
- **FIGURES:** `figs/figure_10_v2_agricultural_seasons.png` and `figs/figure_10b_v2_monsoon_phases.png`
- **Caption:** Figure 13 — Agricultural seasons (left) & monsoon phases (right), drought frequency with ±1 SD.
- **Bullets:**
  - NW (Rajshahi) most severe; Sylhet highest frequency (33.2%).
  - Drought frequency ~28% across all three crop seasons — large year-to-year variation.
- **SAY:** "Drought risk is geographically uneven and seasonally variable — useful for targeted, crop-specific early warning."

### SLIDE 27 — STATION-WISE RELIABILITY
- **Type:** FIGURE
- **Title:** Station-Wise Model Reliability
- **FIGURE:** `figs/figure_14_v2_station_performance.png`
- **Caption:** Figure 14 — Reliability scored by data completeness & coverage.
- **Bullets (small print / footer):**
  - Reliability range 97.78% (Ambaganctg) → 99.28% (Dhaka, Bogra, Sylhet).
  - Longer, more complete station records → higher confidence band.
- **SAY (notes):** "These are data-quality-weighted reliability scores around the overall 97.27% accuracy, reflecting per-station record length and completeness."

### SLIDE 28 — COMPARISON WITH PRIOR WORK
- **Type:** TABLE
- **Title:** Outperforming Existing Bangladesh Studies
- **Table:** Study | Method | Validation | Accuracy
  - Sadiq et al. (2023) | RF + SPI | cross-val | 81–95%
  - Hossain et al. (2025) | Hybrid Ensemble + SPEI | hold-out | 96%
  - Hossain et al. (2025) | RF + SPI/SPEI | hold-out | 94%
  - Paul et al. (2024) | Satellite + RF/KNN | acc score | 92%
  - **Ours (2026)** | **8-scale SPEI + Ensemble + XAI** | **5-fold temporal CV** | **97.27%**
- **Callout:** "First 63-year temporally validated BD drought system; +1.28 pp over best prior."
- **SAY:** "We beat the best prior accuracy, and ours is the only one with strict temporal validation plus explainability."

### SLIDE 29 — PRACTICAL APPLICATIONS
- **Type:** BULLETS (icon-style)
- **Title:** Real-World Impact
- **Bullets:**
  - 🌾 Month-ahead drought forecasts for crop planning (Boro, Dec–May).
  - 🚨 Early-warning system for farmers & irrigation scheduling.
  - 🗺️ Station-wise targeting of north-western interventions.
  - 📈 Operationally ready framework for BMD/agencies.
- **SAY:** "The model is directly usable for agricultural planning and early warning."

### SLIDE 30 — CONTRIBUTIONS
- **Type:** BULLETS (numbered)
- **Title:** Key Contributions
- **Bullets:**
  1. First 63-year temporally validated drought classifier for Bangladesh.
  2. Full 8-scale SPEI coverage + 76 Bangladesh-specific features.
  3. Comprehensive SHAP explainability for operational trust.
  4. Rigorous walk-forward validation preventing data leakage.
- **Callout:** "Serves ~40 million people in drought-prone regions."
- **SAY:** "Four contributions spanning coverage, validation, features, and explainability."

### SLIDE 31 — LIMITATIONS
- **Type:** BULLETS
- **Title:** Study Limitations
- **Bullets:**
  - Meteorological drought (SPEI) only — not hydrological/agricultural indices.
  - Relies on 35 ground stations; sparse areas less certain.
  - No satellite/soil-moisture/groundwater/remote-sensing inputs.
  - Binary classification; no real-time deployment yet.
  - Historical data (1960s–70s) has fewer active stations (~15–20).
- **SAY:** "We're transparent: this is a strong first step, scoped to meteorological drought on station data."

### SLIDE 32 — FUTURE WORK
- **Type:** BULLETS
- **Title:** Future Directions
- **Bullets:**
  - Multi-class severity prediction (moderate / severe / extreme).
  - Longer lead-time forecasts from seasonal climate outlooks.
  - Custom per-station ensemble weights.
  - Integrate satellite data (MODIS, GRACE, GPM).
  - Online / continual learning for real-time deployment.
- **SAY:** "Next: finer severity levels, satellite fusion, and live deployment."

### SLIDE 33 — CONCLUSION
- **Type:** BULLETS + hero numbers
- **Title:** Conclusion
- **Bullets:**
  - Explainable ensemble + multi-scale SPEI + temporal CV = robust drought classification.
  - **97.27% accuracy · 99.69% AUC** — beats prior Bangladesh studies.
  - SHAP makes predictions trustworthy for operational use.
  - A scientifically rigorous, operationally ready monitoring solution.
- **Hero numbers (large terracotta):** 97.27% · 99.69% · 35 stations · 63 years
- **SAY:** "To summarise: an accurate, validated, and explainable drought system for Bangladesh."

### SLIDE 34 — THANK YOU / Q&A
- **Type:** TITLE (centered)
- **Title:** Thank You
- **Body:** Questions & Discussion
- **Footer:** Authors + emails + IUBAT
- **SAY:** "Thank you. We welcome your questions."

### SLIDE 35 — REFERENCES (optional appendix)
- **Type:** BULLETS (small font)
- **Title:** Selected References
- **Bullets:**
  - Vicente-Serrano et al. (2010) — SPEI & log-logistic.
  - Hargreaves & Samani (1985) — PET; FAO-56.
  - Lundberg & Lee (2017) — SHAP / Shapley values.
  - Chen & Guestrin (2016) — XGBoost.
  - Prokhorenkova et al. (2018) — CatBoost.
  - Breiman (2001) — Random Forest.
  - Rahman & Lateh (2016); Mashuq et al. (2024); Paul et al. (2024); Hossain et al. (2025) — BD drought studies.
  - Bangladesh Meteorological Department (BMD) — station data (Mendeley data repository).

---

## 4. FIGURE ASSET MANIFEST (exact files to embed)
| Slide | Figure file (relative path) | What it shows |
|---|---|---|
| 10 | `figs/figure_1_study_area_map.png` | 35-station map |
| 14 | `figs/figure_2e_v2_spei_summary.png` (+ short/very_long optional) | SPEI time series |
| 16 | `figs/figure_3_methodology_flowchart.png` | Framework flowchart |
| 17 | `figs/figure_15_v2_ensemble_architecture.png` | Ensemble architecture |
| 20 | `figs/figure_4_v2_temporal_cv_results.png` | Temporal CV results |
| 21 | `figs/figure_5_v2_model_comparison_auc.png` (optional) | Model AUC comparison |
| 22 | `figs/figure_6_v2_roc_curve.png` | ROC curves |
| 23 | `figs/figure_7_v2_confusion_matrix.png` | Confusion matrix |
| 24 | `figs/figure_8_v2_feature_importance.png` | Top-20 features |
| 25 | `figs/figure_9_v2_shap_summary.png` | SHAP summary |
| 26 | `figs/figure_10_v2_agricultural_seasons.png` + `figs/figure_10b_v2_monsoon_phases.png` | Seasonal/monsoon patterns |
| 27 | `figs/figure_14_v2_station_performance.png` | Station reliability map |
| *(bonus)* | `figs/figure_3_v2_drought_area_index.png` | % stations in drought/year (appendix) |
| *(bonus)* | `figs/figure_8_v2_feature_importance_all_76.png` | All-76 features (appendix) |

> **Note for the AI:** figure FILE numbers differ from slide/thesis figure numbers — always use the path in this table.

---

## 5. FINAL DIRECTIVE TO THE AI GENERATING THE SLIDES
1. Produce ~34 slides in 16:9, applying the Section-1 design system.
2. Embed the EXACT figure files from Section 4 (do not invent images).
3. Use ONLY the verified numbers in Section 2 — do not round or alter.
4. Keep the defensible wording (Section 2 note) — no Optuna/McNemar/bootstrap claims.
5. Put every `SAY:` line into the slide's presenter notes.
6. Make hero numbers large and terracotta; keep ≤6 bullets/slide.
7. Output a polished, defense-ready deck (PPTX preferred).
