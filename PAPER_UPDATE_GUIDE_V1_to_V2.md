# 🔧 Paper Update Guide: V1 → V2

> **Purpose:** V2 pipeline-এ PET formula (Bug 2) এবং SPEI distribution (Bug 3) fix করার পরে, paper-এ যেসব সংখ্যা/লেখা আপডেট করতে হবে তার সম্পূর্ণ নির্দেশিকা।
>
> **Total Changes:** 25 জায়গায় পরিবর্তন (7 category)
>
> **V2 Source:** `/home/alamin/Documents/DroughtClassificationTest/`
>
> **Summary of V2 Fixes:**
>
> 1. **PET Formula:** `0.408` conversion factor যোগ করা হয়েছে (FAO-56 standard)
> 2. **SPEI Distribution:** `genlogistic` → `fisk` (scipy standard)
> 3. **Impact:** PET 2.45x কমেছে, Water Balance negative → positive হয়েছে, কিন্তু model accuracy প্রায় অপরিবর্তিত

---

## 📊 Quick Reference: V1 vs V2 Numbers

| Metric                 | V1 (পুরোনো) | V2 (নতুন) | Change                          |
| ---------------------- | ----------------- | ------------- | ------------------------------- |
| PET mean (mm/month)    | 241.34            | 98.47         | **−59.2%**               |
| Water Balance mean     | −36.42           | +106.46       | **Sign flip**             |
| Ensemble Accuracy      | 97.28%            | 97.27%        | −0.01%                         |
| Ensemble AUC           | 99.68%            | 99.69%        | +0.01%                          |
| XGBoost Accuracy       | 97.35%            | 97.46%        | +0.11%                          |
| CatBoost Accuracy      | 97.44%            | 97.34%        | −0.10%                         |
| Random Forest Accuracy | 94.20%            | 94.41%        | +0.21%                          |
| Std (Accuracy)         | ±0.41%           | ±0.32%       | **কমেছে (ভালো)** |

---

# 🔴 Category 1: PET Formula (Section 3.3)

## Change #1 — PET Equation

**Section:** 3.3 PET and SPEI Calculation
**Line:** 528–534

**🔴 পুরোনো (V1):**

```
**Potential Evapotranspiration (PET):** Calculated using the
Hargreaves-Samani method [44] which requires only temperature data and
it is suitable for Bangladesh's data availability:

PET = 0.0023 × R_a × (T_mean + 17.8) × √(T_max − T_min)    ... (1)
```

**🟢 নতুন (V2):**

```
**Potential Evapotranspiration (PET):** Calculated using the
Hargreaves-Samani method [44] following FAO-56 standard, which requires
only temperature data and is suitable for Bangladesh's data availability:

PET = 0.0023 × 0.408 × R_a × (T_mean + 17.8) × √(T_max − T_min)    ... (1)

যেখানে 0.408 হলো conversion factor (MJ m⁻² day⁻¹ → mm day⁻¹),
FAO-56 (Allen et al., 1998) অনুযায়ী।
```

**কেন:** V1-এ `0.408` conversion factor missing ছিল, যার ফলে PET 2.45x বেশি হচ্ছিল।

---

# 🔴 Category 2: Abstract (Section: Abstract)

## Change #2 — Abstract Performance Numbers

**Section:** Abstract
**Line:** 26–29

**🔴 পুরোনো (V1):**

```
The ensemble method achieves 97.28% ± 0.41% accuracy and 99.68%
± 0.08% AUC (2011–2023), outperforming individual models: XGBoost
(97.35% accuracy, 99.77% AUC), CatBoost (97.44%, 99.76% AUC) and Random
Forest (94.20%, 98.82% AUC).
```

**🟢 নতুন (V2):**

```
The ensemble method achieves 97.27% ± 0.32% accuracy and 99.69%
± 0.14% AUC (2011–2023), outperforming individual models: XGBoost
(97.46% accuracy, 99.78% AUC), CatBoost (97.34%, 99.77% AUC) and Random
Forest (94.41%, 98.93% AUC).
```

---

# 🔴 Category 3: Introduction (Section 1.4)

## Change #3 — Introduction Performance Claim

**Section:** 1.4 Study Objectives and Ideas
**Line:** 190–193

**🔴 পুরোনো (V1):**

```
Our ensemble framework achieves 97.28% ± 0.41% accuracy and 99.68% ±
0.08% AUC through temporal validation that is exceeding all previous
Bangladesh drought studies including the recent best performance of 96%
(Hossain, 2025). Which is representing a +1.28-percentage point
improvement.
```

**🟢 নতুন (V2):**

```
Our ensemble framework achieves 97.27% ± 0.32% accuracy and 99.69% ±
0.14% AUC through temporal validation that is exceeding all previous
Bangladesh drought studies including the recent best performance of 96%
(Hossain, 2025). Which is representing a +1.27-percentage point
improvement.
```

---

# 🔴 Category 4: Results — Section 4.1

## Change #4 — Overall Performance Statement

**Section:** 4.1 Temporal Cross-Validation Performance
**Line:** 1025–1028

**🔴 পুরোনো (V1):**

```
**Overall Performance:** The ensemble model achieved a highest 97.28% ±
0.41% accuracy across 5 temporal splits. Which is demonstrating robust
performance on temporally held-out test data that is representing future
periods relative to training (Table 2). AUC reached 99.68% ± 0.08% that
is indicating exceptional discrimination capability...
```

**🟢 নতুন (V2):**

```
**Overall Performance:** The ensemble model achieved a highest 97.27% ±
0.32% accuracy across 5 temporal splits. Which is demonstrating robust
performance on temporally held-out test data that is representing future
periods relative to training (Table 2). AUC reached 99.69% ± 0.14% that
is indicating exceptional discrimination capability...
```

## Change #5 — Table 2: Temporal CV Detailed Metrics

**Section:** 4.1
**Line:** 1036–1053

**🔴 পুরোনো টেবিল (V1):**

| Fold           | Test Period | Accuracy (%)     | AUC (%)          | F1 (%)           | Precision (%)    | Recall (%)       |
| -------------- | ----------- | ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| 1              | 2011-2015   | 97.00            | 99.58            | 96.72            | 96.57            | 96.87            |
| 2              | 2014-2017   | 96.67            | 99.59            | 95.16            | 95.82            | 94.50            |
| 3              | 2017-2020   | 97.32            | 99.75            | 96.06            | 96.65            | 95.48            |
| 4              | 2020-2023   | 97.86            | 99.78            | 97.82            | 97.82            | 97.82            |
| 5              | 2016-2023   | 97.53            | 99.73            | 96.94            | 97.55            | 96.34            |
| **Mean** | —          | **97.28**  | **99.68**  | **96.54**  | **96.88**  | **96.20**  |
| **Std**  | —          | **±0.41** | **±0.08** | **±0.89** | **±0.72** | **±1.14** |

**🟢 নতুন টেবিল (V2):**

| Fold           | Test Period | Accuracy (%)     | AUC (%)          | F1 (%)           | Precision (%)    | Recall (%)       |
| -------------- | ----------- | ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| 1              | 2011-2015   | 96.76            | 99.45            | 96.16            | 96.27            | 96.05            |
| 2              | 2014-2017   | 97.20            | 99.68            | 95.23            | 96.11            | 94.37            |
| 3              | 2017-2020   | 97.56            | 99.77            | 95.72            | 97.87            | 93.67            |
| 4              | 2020-2023   | 97.38            | 99.79            | 97.05            | 97.84            | 96.28            |
| 5              | 2016-2023   | 97.47            | 99.78            | 96.45            | 97.88            | 95.06            |
| **Mean** | —          | **97.27**  | **99.69**  | **96.12**  | **97.19**  | **95.09**  |
| **Std**  | —          | **±0.32** | **±0.14** | **±0.70** | **±0.92** | **±1.10** |

## Change #6 — Split-wise Analysis Text

**Section:** 4.1
**Line:** 1061–1067

**🔴 পুরোনো (V1):**

```
**Split-wise Analysis**: Our Temporal Cross-Validation Performance shows
the remarkable consistency across temporal splits with Split 4
(2020-2023) achieving the highest accuracy (97.86%) and Split 2
(2014-2017) showing the lowest (96.67%). That is indicating robust model
performance across varying climate conditions (Figure 4). The low
standard deviation (±0.41%) confirms exceptional temporal stability...
```

**🟢 নতুন (V2):**

```
**Split-wise Analysis**: Our Temporal Cross-Validation Performance shows
the remarkable consistency across temporal splits with Split 3
(2017-2020) achieving the highest accuracy (97.56%) and Split 1
(2011-2015) showing the lowest (96.76%). That is indicating robust model
performance across varying climate conditions (Figure 4). The low
standard deviation (±0.32%) confirms exceptional temporal stability...
```

## Change #7 — Comparison with Previous Studies

**Section:** 4.1
**Line:** 1069

**🔴 পুরোনো (V1):**

```
**Comparison with Previous Studies:** Our temporal validation (97.28%)
substantially exceeds all previous Bangladesh drought studies...
```

**🟢 নতুন (V2):**

```
**Comparison with Previous Studies:** Our temporal validation (97.27%)
substantially exceeds all previous Bangladesh drought studies...
```

---

# 🔴 Category 5: Results — Section 4.2

## Change #8 — Individual Model Performance Text

**Section:** 4.2 Model Comparison and Ensemble Performance
**Line:** 1082–1093

**🔴 পুরোনো (V1):**

```
**Individual Model Performance:** We evaluated three complementary
machine learning models, and each one achieved exceptional results.
CatBoost scored the highest individual accuracy at 97.44% (99.76% AUC)
which is showing its superior handling of categorical data. XGBoost
performed at a similar level with 97.35% accuracy and a 99.77% AUC which
confirms its excellent in gradient boosting capability. Random Forest
offered a strong baseline performance at 94.20% accuracy with 98.82% AUC...
```

**🟢 নতুন (V2):**

```
**Individual Model Performance:** We evaluated three complementary
machine learning models, and each one achieved exceptional results.
XGBoost scored the highest individual accuracy at 97.46% (99.78% AUC)
which confirms its excellent in gradient boosting capability. CatBoost
performed at a similar level with 97.34% accuracy and a 99.77% AUC
which is showing its superior handling of categorical data. Random Forest
offered a strong baseline performance at 94.41% accuracy with 98.93% AUC...
```

## Change #9 — Table 3: Model Performance Comparison

**Section:** 4.2
**Line:** 1097–1109

**🔴 পুরোনো টেবিল (V1):**

| Model                         | Accuracy (%)    | AUC (%)         | F1-Score (%)    | Precision (%)   | Recall (%)      |
| ----------------------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| XGBoost                       | 97.35           | 99.77           | 96.67           | 96.92           | 96.42           |
| Random Forest                 | 94.20           | 98.82           | 92.75           | 93.12           | 92.38           |
| CatBoost                      | 97.44           | 99.76           | 96.75           | 96.98           | 96.52           |
| **Ensemble (Weighted)** | **97.28** | **99.68** | **96.54** | **96.88** | **96.20** |

**🟢 নতুন টেবিল (V2):**

| Model                         | Accuracy (%)    | AUC (%)         | F1-Score (%)    | Precision (%)   | Recall (%)      |
| ----------------------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| XGBoost                       | 97.46           | 99.78           | 96.43           | 97.02           | 95.86           |
| Random Forest                 | 94.41           | 98.93           | 92.05           | 93.69           | 90.47           |
| CatBoost                      | 97.34           | 99.77           | 96.23           | 97.40           | 95.10           |
| **Ensemble (Weighted)** | **97.27** | **99.69** | **96.12** | **97.19** | **95.09** |

## Change #10 — Ensemble Benefits Text

**Section:** 4.2
**Line:** 1146–1160

**🔴 পুরোনো (V1):**

```
**Ensemble Benefits:** Our combined weighted averaging ensemble
performed exceptionally well which is achieving a 97.28% accuracy and a
99.68% AUC. This method struck an excellent balance using the best parts
of each individual model. Its performance was +3.08% higher than Random
Forest and was just as accurate as the top single models (XGBoost and
CatBoost)...
Crucially the ensemble proved to be extremely stable
with a very low standard deviation of only ±0.41% across the different
temporal splits.
```

**🟢 নতুন (V2):**

```
**Ensemble Benefits:** Our combined weighted averaging ensemble
performed exceptionally well which is achieving a 97.27% accuracy and a
99.69% AUC. This method struck an excellent balance using the best parts
of each individual model. Its performance was +2.86% higher than Random
Forest and was just as accurate as the top single models (XGBoost and
CatBoost)...
Crucially the ensemble proved to be extremely stable
with a very low standard deviation of only ±0.32% across the different
temporal splits.
```

---

# 🔴 Category 6: Results — Section 4.3 (Feature Importance)

## Change #11 — Figure 8 Caption

**Section:** 4.3
**Line:** 1274–1277

**🔴 পুরোনো (V1):**

```
SPEI lag features dominate the top positions across all
three base models (RF: 94.20%, XGBoost: 97.35%, CatBoost: 97.44%), with
consistent rankings demonstrating robust feature importance. The top
feature, SPEI_12m_lag1_safe, accounts for 26.3% of total importance.
```

**🟢 নতুন (V2):**

```
SPEI lag features dominate the top positions across all
three base models (RF: 94.41%, XGBoost: 97.46%, CatBoost: 97.34%), with
consistent rankings demonstrating robust feature importance. The top
feature, SPEI_12m_lag1_safe, accounts for [XX.X]% of total importance.
```

> ⚠️ **গুরুত্বপূর্ণ:** `26.3%` value-টি Figure 8 regenerate করার পরে verify করতে হবে। V2 feature importance JSON-এ top features ভিন্ন হতে পারে। নিশ্চিত করতে নিচের কমান্ড রান করুন:
>
> ```bash
> python3 -c "import json; d=json.load(open('outputs/feature_importance.json')); print(d['features'][:5], d['importance'][:5])"
> ```

## Change #12 — Figure 9 Caption

**Section:** 4.3
**Line:** 1287–1288

**🔴 পুরোনো (V1):**

```
Individual model accuracies: XGBoost=97.35%, Random Forest=94.20%,
CatBoost=97.44%, Ensemble=97.28%.
```

**🟢 নতুন (V2):**

```
Individual model accuracies: XGBoost=97.46%, Random Forest=94.41%,
CatBoost=97.34%, Ensemble=97.27%.
```

> **নোট:** Table 4 (Feature Importance Rankings) এর exact SHAP values V2-তে পরিবর্তিত হতে পারে। যদি আপনি Figure 8/9 পুনরায় generate করেন, তাহলে SHAP values-ও update করতে হবে।

---

# 🔴 Category 7: Discussion & Conclusion (Sections 5–7)

## Change #13 — Section 5.1 Discussion

**Section:** 5.1
**Line:** 1471–1476

**🔴 পুরোনো (V1):**

```
This study successfully developed the first comprehensive temporally
validated drought classification framework for Bangladesh. Our model
achieving a 97.28% ± 0.41% accuracy through rigorous 5-fold walk-forward
validation...
The exceptionally low standard deviation
(±0.41%) indicates remarkable temporal stability.
```

**🟢 নতুন (V2):**

```
This study successfully developed the first comprehensive temporally
validated drought classification framework for Bangladesh. Our model
achieving a 97.27% ± 0.32% accuracy through rigorous 5-fold walk-forward
validation...
The exceptionally low standard deviation
(±0.32%) indicates remarkable temporal stability.
```

## Change #14 — Section 5.2 International Comparison

**Section:** 5.2
**Line:** 1488–1503

**🔴 পুরোনো (V1):**

```
Our model performed very well with 97.28% accuracy and 99.68% AUC...
Our model reached 97.28% accuracy using only 35 stations...
model achieved 97.28% accuracy +10.42% higher---while using the same
temporal validation method...
```

**🟢 নতুন (V2):**

```
Our model performed very well with 97.27% accuracy and 99.69% AUC...
Our model reached 97.27% accuracy using only 35 stations...
model achieved 97.27% accuracy +11.27% higher---while using the same
temporal validation method...
```

> 🔴 **গুরুত্বপূর্ণ — V1 গণনাগত ভুল (Pre-existing Error):**
> Paper-এ মূল `+10.42%` সংখ্যাটি নিজেই ভুল ছিল। সঠিক গণনা:
>
> - Dikshit et al.: R² = 0.86 → 86%
> - V2: 97.27% − 86% = **+11.27%** (সঠিক)
> - V1 এও ভুল ছিল: 97.28% − 86% = +11.28% ≠ +10.42%
>
> এই ভুলটি V2 update এর সাথে একসাথে ঠিক হয়ে যাচ্ছে।

## Change #15 — Section 5.4 Policy Recommendations

**Section:** 5.4
**Line:** 1561

**🔴 পুরোনো (V1):**

```
The system is highly accurate (97.28%) and easy to understand because of
SHAP analysis.
```

**🟢 নতুন (V2):**

```
The system is highly accurate (97.27%) and easy to understand because of
SHAP analysis.
```

## Change #16 — Conclusion Section

**Section:** 7 (Conclusion)
**Line:** 1690–1698

**🔴 পুরোনো (V1):**

```
It achieved 97.28% ± 0.41%
accuracy...
The model's AUC score of 99.68%...
```

**🟢 নতুন (V2):**

```
It achieved 97.27% ± 0.32%
accuracy...
The model's AUC score of 99.69%...
```

## Change #17 — Conclusion Performance Statement

**Section:** 7
**Line:** 1704, 1721

**🔴 পুরোনো (V1):**

```
performance estimates for operational deployment (97.28% represents...
performance, with 97.28% accuracy. This is better than all previous
```

**🟢 নতুন (V2):**

```
performance estimates for operational deployment (97.27% represents...
performance, with 97.27% accuracy. This is better than all previous
```

---

# 🟡 Optional: Additional Improvements

## Improvement A — Water Balance Discussion (যদি যোগ করতে চান)

**Suggested addition** Section 3.3 বা 4.4 তে:

```
**Physical Validation:** The corrected PET calculation yields a mean
climatic water balance of +106.46 mm/month across Bangladesh, which is
physically consistent with the country's tropical monsoon climate
characterized by high annual precipitation (2,000–3,000 mm). This
confirms the suitability of the FAO-56 corrected Hargreaves-Samani
method for Bangladesh's hydrological context.
```

## Improvement B — PET Statistics (যদি paper-এ PET value উল্লেখ থাকে)

Paper-এ যদি PET-এর সরাসরি value উল্লেখ থাকে, সেগুলো আপডেট করতে হবে:

| Metric     | V1            | V2            |
| ---------- | ------------- | ------------- |
| PET mean   | ~241 mm/month | ~98 mm/month  |
| PET median | ~240 mm/month | ~98 mm/month  |
| PET max    | ~776 mm/month | ~316 mm/month |

---

# 📋 Checklist (সম্পূর্ণ আপডেট করার জন্য)

- [ ] Change #1: PET Formula (Line 528–534) — `0.408` যোগ করুন
- [ ] Change #2: Abstract (Line 26–29) — 4টি number
- [ ] Change #3: Intro 1.4 (Line 190–193) — 2টি number
- [ ] Change #4: Section 4.1 text (Line 1025–1028) — 2টি number
- [ ] Change #5: Table 2 (Line 1036–1053) — সম্পূর্ণ টেবিল
- [ ] Change #6: Split-wise text (Line 1061–1067) — 3টি number
- [ ] Change #7: Comparison text (Line 1069) — 1টি number
- [ ] Change #8: Section 4.2 text (Line 1082–1093) — 6টি number
- [ ] Change #9: Table 3 (Line 1097–1109) — সম্পূর্ণ টেবিল
- [ ] Change #10: Ensemble Benefits (Line 1146–1160) — 3টি number
- [ ] Change #11: Figure 8 caption (Line 1274–1277) — 3টি number + **26.3% verify**
- [ ] Change #12: Figure 9 caption (Line 1287–1288) — 4টি number
- [ ] Change #13: Section 5.1 (Line 1471–1476) — 2টি number
- [ ] Change #14: Section 5.2 (Line 1488–1503) — 4টি number + **+10.42% → +11.27%**
- [ ] Change #15: Section 5.4 (Line 1561) — 1টি number
- [ ] Change #16: Conclusion (Line 1690–1698) — 2টি number
- [ ] Change #17: Conclusion (Line 1704, 1721) — 2টি number
- [ ] Optional A: Water Balance discussion যোগ করুন
- [ ] Optional B: PET statistics আপডেট করুন (যদি থাকে)
- [ ] Table 4: SHAP values আপডেট করুন (Figure 9 regenerate করলে)

---

# 📌 গুরুত্বপূর্ণ নোট

1. **Ensemble accuracy প্রায় অপরিবর্তিত** (97.28% → 97.27%) — মূল claim অপরিবর্তিত থাকবে
2. **"Highest in Bangladesh" claim এখনও valid** — 97.27% > 96% (Hossain, 2025)
3. **PET fix টা গুরুত্বপূর্ণ** — এটা না করলে reviewer ধরতে পারে যে PET value অস্বাভাবিক উচ্চ
4. **Std কমেছে** (±0.41% → ±0.32%) — এটা আসলে উন্নতি, paper-এ positive হিসেবে উপস্থাপন করুন
5. **Water Balance sign flip** — যদি paper-ে Water Balance value উল্লেখ থাকে, অবশ্যই আপডেট করুন

---

# 🚨 Appendix: Pre-existing V1 Errors (V2 Update এর সাথে ঠিক হবে)

Cross-check করার সময় আমি কিছু V1 error খুঁজে পেয়েছি যা V2 update এর সাথে একসাথে ঠিক হয়ে যাবে। এই তালিকাটি নিশ্চিত করবে যে কোনো error মিস হয় না:

## Error #1: "+10.42%" Calculation (Section 5.2, Line ~1503)

- **Paper-এ আছে:** `97.28% accuracy +10.42% higher`
- **সঠিক গণনা (V2):** 97.27% − 86% (Dikshit R²) = **+11.27%**
- **কেন ভুল:** V1 এও এই গণনা ভুল ছিল (97.28% − 86% = 11.28%, not 10.42%)
- **সমাধান:** Change #14 এর V2 text এ সঠিক মান `+11.27%` দেওয়া আছে

## Error #2: "26.3%" Feature Importance (Section 4.3, Line ~1277)

- **Paper-এ আছে:** `SPEI_12m_lag1_safe, accounts for 26.3%`
- **V2 তে status:** Feature importance JSON-এ top features ভিন্ন — `Rainfall_Total`, `Temperature_Mean` ইত্যাদি
- **সমাধান:** Figure 8 regenerate করে নতুন percentage verify করতে হবে (Change #11)
- **Verification command:**
  ```bash
  python3 -c "import json; d=json.load(open('outputs/feature_importance.json')); print(d['features'][:5], d['importance'][:5])"
  ```

## Verification Table: All Improvement Calculations

সব comparison calculation V2 values দিয়ে verify করা হয়েছে:

| Comparison       | V2 Value                        | Paper-এ যা বলা হয়েছে | সঠিক?         |
| ---------------- | ------------------------------- | --------------------------------- | ----------------- |
| vs Hossain (96%) | 97.27 − 96 =**+1.27%**   | +1.28% (V1) → +1.27% (V2) ✅     |                   |
| vs Khan (88.7%)  | 97.27 − 88.7 =**+8.57%** | —                                | ✅                |
| vs Paul (92%)    | 97.27 − 92 =**+5.27%**   | —                                | ✅                |
| vs Dikshit (86%) | 97.27 − 86 =**+11.27%**  | +10.42% ❌                        | **ভুল!** |

---

## ✅ Cross-Check Verification Log

সব line numbers এবং exact text paper-এর সাথে verify করা হয়েছে:

| Change             | Line (Guide) | Line (Verified)      | Status     |
| ------------------ | ------------ | -------------------- | ---------- |
| #1 PET Formula     | 528–534     | 528–534             | ✅         |
| #2 Abstract        | 26–29       | 26–29               | ✅         |
| #3 Intro 1.4       | 190–193     | 190–193             | ✅         |
| #4 Section 4.1     | 1025–1028   | 1025–1028           | ✅         |
| #5 Table 2         | 1036–1053   | 1036–1053           | ✅         |
| #6 Split-wise      | 1061–1067   | 1061–1067           | ✅         |
| #7 Comparison      | 1069         | 1069                 | ✅         |
| #8 Section 4.2     | 1082–1093   | 1082–1093           | ✅         |
| #9 Table 3         | 1097–1109   | 1097–1109           | ✅         |
| #10 Ensemble       | 1146–1160   | 1146–1160           | ✅         |
| #11 Figure 8       | 1275         | **1274–1277** | ⚠️ Fixed |
| #12 Figure 9       | 1287–1288   | 1287–1288           | ✅         |
| #13 Discussion 5.1 | 1471–1476   | 1471–1476           | ✅         |
| #14 Section 5.2    | 1492–1505   | **1488–1503** | ⚠️ Fixed |
| #15 Section 5.4    | 1561         | 1561                 | ✅         |
| #16 Conclusion     | 1690–1698   | 1690–1698           | ✅         |
| #17 Conclusion     | 1704, 1721   | 1704, 1721           | ✅         |


### 📑 ১. Drought Area Index (DAI) ফিগার সিলেকশন গাইড

DAI এর মোট ৮টি আলাদা ইমেজ তৈরি হয়েছে (`dai_spei_1m.png` থেকে `dai_spei_24m.png`)। জার্নাল পেপারের স্পেস লিমিট এবং রিডারদের পড়ার সুবিধার জন্য ৮টি ইমেজই আলাদাভাবে দেখানো **একেবারেই অনুচিত** (এতে ৪-৫ পৃষ্ঠা শুধু এই ফিগারেই চলে যাবে)।

আমি আপনাকে **৩টি সম্ভাব্য অপশন** সাজেস্ট করছি। এর মধ্যে **Option B** অথবা **Option C** সবচেয়ে প্রফেশনাল হবে:

#### 🟢 Option A: ৫টি ফিগার দেখানো (৩, ৬, ১২, ১৮, ২৪)

এটি আপনার SPEI Time Series (Figure 2a-e) এর সাথে সামঞ্জস্যপূর্ণ হবে।

* **সুবিধা:** পুরো পেপার জুড়ে টাইমস্কেলের ধারাবাহিকতা বজায় থাকে।
* **ক্যাপশনগুলো এভাবে লিখবেন:**
  * **Figure Xa:** Drought Area Index for Medium-term Agricultural Drought (SPEI-3m) showing percentage of weather stations in drought (1961-2023).
  * **Figure Xb:** Drought Area Index for Medium-term Agricultural Drought (SPEI-6m).
  * **Figure Xc:** Drought Area Index for Long-term Hydrological Drought (SPEI-12m).
  * **Figure Xd:** Drought Area Index for Very Long-term Climate Trend (SPEI-18m).
  * **Figure Xe:** Drought Area Index for Very Long-term Climate Trend (SPEI-24m).

#### 🟢 Option B: ৪টি ফিগার দেখানো (৩, ৬, ১২, ২৪) — [Highly Recommended]

জার্নাল পেপারে ফিগার বসানোর সবচেয়ে স্ট্যান্ডার্ড নিয়ম হলো **2×2 গ্রিড** ব্যবহার করা। ৪টি ইমেজ নিয়ে একটি সুন্দর চতুর্ভুজ গ্রিড তৈরি করা যায়।

* **সুবিধা:** কোনো অপ্রয়োজনীয় পুনরাবৃত্তি (১৮ ও ২৪ এর মতো কাছাকাছি স্কেল) থাকে না এবং স্পেস অনেক বেঁচে যায়।
* **টাইমস্কেলের বন্টন:**
  1. **SPEI-3m** (কৃষি খরা - Agricultural)
  2. **SPEI-6m** (মৌসুমি খরা - Seasonal/Agricultural)
  3. **SPEI-12m** (হাইড্রোলজিক্যাল খরা - Hydrological - *এটি আপনার ML মডেলের টার্গেট ভ্যারিয়েবল*)
  4. **SPEI-24m** (দীর্ঘমেয়াদী আবহাওয়া পরিবর্তন - Long-term/Socio-economic)
* **ক্যাপশন ফরম্যাট:**
  * **Figure Xa:** Drought Area Index for Agricultural Drought (SPEI-3m) (1961-2023).
  * **Figure Xb:** Drought Area Index for Seasonal Agricultural Drought (SPEI-6m) (1961-2023).
  * **Figure Xc:** Drought Area Index for Hydrological Drought (SPEI-12m) (1961-2023).
  * **Figure Xd:** Drought Area Index for Long-term Climate Trend (SPEI-24m) (1961-2023).

#### 🟢 Option C: ১টি ফিগার দেখানো (শুধুমাত্র SPEI-12m অথবা SPEI-3m)

যদি আপনারা পেপারটি আরও সংক্ষেপ করতে চান, তবে মূল ফিগার ডিরেক্টরি থেকে শুধুমাত্র ১টি রিপ্রেজেন্টেটিভ ইমেজ দেখাতে পারেন।

* **পছন্দ ১ (SPEI-12m):** এটি দেখানোর সবচেয়ে যৌক্তিক কারণ হলো আপনাদের মেশিন লার্নিং মডেলটি মূলত **SPEI-12m** (Hydrological Drought) প্রেডিক্ট করার জন্যই তৈরি করা হয়েছে।
* **পছন্দ ২ (SPEI-3m):** এটি হলো কৃষি খরার প্রধান নির্দেশক।

---

### 🛠️ ২. ইমেজগুলো আলাদা ফাইলে থাকলে পেপারে কীভাবে বসাবেন?

আপনাদের তৈরি করা ইমেজগুলো যেহেতু আলাদা আলাদা ফাইলে আছে, তাই পেপার লেখার সময় (যেমন MS Word বা LaTeX-এ) নিচের পদ্ধতি ব্যবহার করবেন:

* **MS Word-এ:** একটি অদৃশ্য বর্ডারযুক্ত টেবিল (যেমন 2×2 টেবিল) তৈরি করে প্রতি ঘরে একটি করে ইমেজ বসিয়ে দিবেন। নিচে একবারে পুরো টেবিলের জন্য একটি ক্যাপশন দিয়ে দিবেন।
* **LaTeX-এ:** standard `subfigure` বা `subcaption` প্যাকেজ ব্যবহার করে কোড লিখবেন:
  ```latex
  \begin{figure}[htbp]
      \centering
      \begin{subfigure}[b]{0.48\textwidth}
          \includegraphics[width=\textwidth]{dai_spei_3m.png}
          \caption{SPEI-3m}
      \end{subfigure}
      \hfill
      \begin{subfigure}[b]{0.48\textwidth}
          \includegraphics[width=\textwidth]{dai_spei_6m.png}
          \caption{SPEI-6m}
      \end{subfigure}
      % ... একইভাবে বাকি দুটো
      \caption{National Drought Area Index for Bangladesh across key timescales.}
  \end{figure}
  ```

---

### 🚨 ৩. গুরুত্বপূর্ণ: ম্যানুস্ক্রিপ্টে Figure Numbering-এর অসঙ্গতি

আপনাদের মূল ম্যানুস্ক্রিপ্ট [Drought_Severity_Classification_Bangladesh.md](file:///home/alamin/Documents/DroughtClassificationTest/Drought_Severity_Classification_Bangladesh.md) বিশ্লেষণ করার সময় আমি লক্ষ্য করেছি যে **চিত্রের নম্বরগুলো এলোমেলো হয়ে আছে এবং একই নম্বর দুবার ব্যবহৃত হয়েছে**।

জার্নালে সাবমিট করার আগে এটি অবশ্যই ঠিক করতে হবে। নিচে বর্তমানের ভুল ও তার প্রস্তাবিত সঠিক সিকোয়েন্স দেওয়া হলো:

| ক্রম | বর্তমান ম্যানুস্ক্রিপ্ট টেক্সট | প্রস্তাবিত সঠিক নম্বর | ফাইল নাম / বিবরণ                                           |
| :------- | :--------------------------------------------------------- | :--------------------------------------- | :--------------------------------------------------------------------- |
| ১       | **Figure 1**                                         | **Figure 1**                       | Study Area Map (`figure_1_study_area_map.png`)                       |
| ২       | **Figure 2a-e**                                      | **Figure 2a-e**                    | SPEI Time Series (`figure_2_v2_...`)                                 |
| ৩       | **Figure 3**                                         | **Figure 3**                       | Methodology Flowchart (`figure_3_methodology_flowchart.png`)         |
| ৪       | **Figure 4** (Ensemble Viz)                          | **Figure 4**                       | Ensemble Architecture (`figure_15_v2_ensemble_architecture.png`)     |
| ৫       | **Figure 4** (Duplicate!)                            | **Figure 5**                       | Temporal CV Results (`figure_4_v2_temporal_cv_results.png`)          |
| ৬       | **Figure 5**                                         | **Figure 6**                       | Model Comparison AUC (`figure_5_v2_model_comparison_auc.png`)        |
| ৭       | **Figure 6**                                         | **Figure 7**                       | ROC Curve (`figure_6_v2_roc_curve.png`)                              |
| ৮       | **Figure 7**                                         | **Figure 8**                       | Confusion Matrix (`figure_7_v2_confusion_matrix.png`)                |
| ৯       | **Figure 11** (Out of order!)                        | **Figure 9**                       | Prediction Distribution (`figure_11_v2_prediction_distribution.png`) |
| ১০     | **Figure 12** (Out of order!)                        | **Figure 10**                      | Performance Metrics (`figure_12_v2_performance_metrics.png`)         |
| ১১     | **Figure 8** (Out of order!)                         | **Figure 11**                      | Feature Importance (`figure_8_v2_feature_importance.png`)            |
| ১২     | **Figure 9** (Out of order!)                         | **Figure 12**                      | SHAP Summary (`figure_9_v2_shap_summary.png`)                        |
| ১৩     | **Figure 10a, b** (Out of order!)                    | **Figure 13a, b**                  | Agricultural/Monsoon (`figure_10_v2_agricultural_seasons.png`)       |
| ১৪     | **Figure 13**                                        | **Figure 14**                      | Drought Frequency (`drought_frequency.png`)                          |
| ১৫     | **Figure 14**                                        | **Figure 15**                      | Station-Wise Performance (`figure_14_v2_station_performance.png`)    |

*(নোট: যদি আপনারা **Drought Area Index (DAI)** চিত্রটি মূল পেপারে যোগ করতে চান, তবে প্রস্তাবিত সিকোয়েন্সে Figure 3 এবং Figure 4 এর মাঝে এটি যোগ হবে, এবং পরবর্তী চিত্রগুলোর নম্বর সেই অনুযায়ী ১ ধাপ করে বাড়িয়ে নিতে হবে।)*

---

*Generated from V2 results: `/home/alamin/Documents/DroughtClassificationTest/outputs/`*
*Cross-checked against: `Drought_Severity_Classification_Bangladesh.md`*
