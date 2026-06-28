# 📋 কাগজের দাবি বনাম বাস্তবতা: Gap Analysis (গ্যাপ বিশ্লেষণ)

**প্রজেক্ট:** Drought Severity Classification Bangladesh (`master_drought_v2.ipynb`)
**উদ্দেশ্য:** কাগজে (paper) যা দাবি করা হয়েছে এবং কোডে/বাস্তবে যা আছে — তার মধ্যকার গ্যাপগুলো চিহ্নিত করা, যাতে জার্নাল সাবমিশনের আগে দাবিগুলো সততার সাথে ফ্রেম করা যায়।

> ⚠️ এই বিশ্লেষণ কোড ও কাগজের প্রকৃত পাঠ থেকে তৈরি। উদ্দেশ্য সমালোচনা নয়, বরং কাগজকে আরও সততাশীল ও প্রকাশযোগ্য করা।

---

## 🎯 সংক্ষিপ্ত সারসংক্ষেপ

আমাদের প্রজেক্ট একটি **শক্তিশালী classification মডেল** (৫-fold walk-forward temporal CV, ৯৭.২৮% accuracy)। কিন্তু কাগজে এটিকে **"forecasting / early-warning / operationally-ready"** হিসেবে উপস্থাপন করা হয়েছে, যা বাস্তবতার চেয়ে বেশি। **সমস্যা পদ্ধতিতে নয়, দাবির ভাষায় (framing)-এ।** নিচে ৭টি গ্যাপ এবং প্রতিটির সমাধান দেওয়া হলো।

---

## Gap ১: "Forecasting" দাবি ⚠️ (সবচেয়ে গুরুত্বপূর্ণ)

| | |
|---|---|
| **কাগজের দাবি** | Section 5.1: "predict droughts a month ahead"; Section 5.4: "3-month / 6-month / 12-month forecasts" |
| **বাস্তবতা** | মডেল **current-month** ফিচার ব্যবহার করে (`Rainfall_Total`, `Temperature_Mean`, `PET_mm_month`, `Humidity_Mean`, `Water_Balance`)। তাই কোনো মাসের খরা শুধু সেই মাস **শেষ হওয়ার পরেই** classify করা সম্ভব। **Effective lead time ≈ ০** (nowcasting)। কোনো আসল future forecasting নেই। |
| **ঝুঁকি** | পরীক্ষক জিজ্ঞেস করবেন: "আপনি ভবিষ্যৎ কীভাবে forecast করছেন, যখন current-month data লাগবে?" — উত্তর নেই। মেজর রিভিশন / রিজেক্টের কারণ হতে পারে। |
| **সমাধান** | "Forecasting" শব্দ বাদ দিন। সততার সাথে বলুন: **"Drought classification model validated with walk-forward temporal cross-validation."** 3/6/12-month forecast-কে স্পষ্টভাবে **Future Work**-এ নিন। |

---

## Gap ২: "Unseen future data" দাবি ⚠️

| | |
|---|---|
| **কাগজের দাবি** | Conclusion: "97.28% represents genuine predictive capability on **unseen future data**" |
| **বাস্তবতা** | টেস্ট ডেটা **ঐতিহাসিক** (১৯৬১–২০২৩)। প্রতিটি টেস্ট মাসের `SPEI_12m` এবং খরা-লেবেল **আগে থেকেই গণনা করা ও CSV-তে বর্তমান** (`climate_data_with_spei_8scales.csv` শেষ সারি Teknaf 2023-12)। "Unseen" মানে শুধু **ট্রেনিংয়ে দেখা হয়নি** — কিন্তু এটি "ভবিষ্যৎ যা ঘটেনি" নয়। মডেল predict করে, আমরা জানা ground truth-এর সাথে match করি → accuracy পাই। |
| **ঝুঁকি** | "unseen future data" ভুল বাক্যাংশ। রিভিউয়ার ধরে ফেললে সততা নিয়ে প্রশ্ন উঠবে। |
| **সমাধান** | লিখুন: **"held-out temporal folds not seen during training"**। "future" শব্দ ব্যবহার করবেন না, কারণ ডেটা ঐতিহাসিক। |

---

## Gap ৩: "Operationally ready" / Deployment দাবি ⚠️

| | |
|---|---|
| **কাগজের দাবি** | Abstract: "operationally ready drought monitoring solution"; Section 5.3: SMS alerts, dashboard, BMD integration |
| **বাস্তবতা** | কোনো `app.py`, Streamlit/Flask/FastAPI সার্ভার, API, dashboard, বা SMS মডিউল **নেই**। `study_guides/web_app_integration.md` শুধু একটি **কল্পিত/প্রস্তাবিত** ডিজাইন (এমনকি ২০২৪–২০২৫ ডেটা গ্যাপ পূরণের পরামর্শ দেয়, অর্থাৎ এখনো কিছু নেই)। |
| **ঝুঁকি** | "operationally ready" সরাসরি মিথ্যা। রিভিউয়ার কোড চাইলে deployment খুঁজে পাবেন না। |
| **সমাধান** | বাক্যাংশ পরিবর্তন করুন: **"a research-grade model suitable for future operational deployment"**। অথবা deployment আসলেই বানিয়ে নিন (নিচে রোডম্যাপ)। |

---

## Gap ৪: কৃষক/ব্যবহারকারীর access দাবি ⚠️

| | |
|---|---|
| **কাগজের দাবি** | "predictions can be shared through agricultural extension services, mobile SMS alerts, and websites" |
| **বাস্তবতা** | কৃষক বা পানি ব্যবস্থাপক বর্তমানে এই মডেলের আউটপুট পাওয়ার **কোনো উপায় নেই** — কোনো চ্যানেল বানানো হয়নি। উপরন্তু, যেহেতু lead time ≈ ০, খরা শনাক্ত হয় মাস শেষে — তখন কৃষকের সিদ্ধান্ত নেওয়ার (যেমন বপন) অনেক দেরি হয়ে যায়। |
| **ঝুঁকি** | কৃষক-কেন্দ্রিক সুবিধার দাবি প্রমাণহীন। |
| **সমাধান** | (ক) দাবি কমিয়ে বলুন "potential applications include..."; (খ) lead time বাড়ানোর ফিচার ইঞ্জিনিয়ারিং যোগ করুন (শুধু lagged feature); (গ) ভবিষ্যতে একটি সহজ ড্যাশবোর্ড/SMS prototype বানান। |

---

## Gap ৫: Lead time ≈ ০ (early warning অসম্ভব) ⚠️

| | |
|---|---|
| **কাগজের দাবি** | "early warning system", "month ahead" |
| **বাস্তবতা** | Current-month climate feature (Rainfall, Temp, PET) লাগে → মাস শেষ না হলে classify করা যায় না। ফলে **আসল আগাম বার্তা (lead time) নেই**। এটি early warning-এর মূল শর্তের বিপরীত। |
| **ঝুঁকি** | Early-warning দাবি অযৌক্তিক। |
| **সমাধান** | একটি **lagged-only ভার্সন** তৈরি করুন (শুধু SPEI lag + past climate), যা ১–৩ মাস আগে predict করতে পারে — তাহলে early-warning সত্যিকারের হবে। এটি কাগজের মূল্য বহুগুণ বাড়াবে। |

---

## Gap ৬: "Ensemble = best" দাবি (ছোট গ্যাপ)

| | |
|---|---|
| **কাগজের দাবি** | Ensemble কে "best overall model" বলা হয়েছে |
| **বাস্তবতা** | আসলে XGBoost এককভাবে সামান্য বেশি নিখুঁত (৯৭.৪৬% vs Ensemble ৯৭.২৮%)। এছাড়া std-এ অসঙ্গতি (কাগজে ±০.৪১%, JSON-এ ±০.২৮%)। |
| **ঝুঁকি** | ছোট অসঙ্গতি — কডা রিভিউয়ার ধরতে পারেন। |
| **সমাধান** | "best/most robust" হিসেবে Ensemble-কে রাখুন (robustness, কম variance) — কিন্তু সততার সাথে জানান XGBoost এককভাবে সামান্য বেশি accuracy দেয়। std সংখ্যা ঠিক করুন। |

---

## Gap ৭: Table 5 পুনরুৎপাদনযোগ্যতা

| | |
|---|---|
| **কাগজের দাবি** | Table 5 (Regional Drought Vulnerability): Rajshahi ৩৮.৫%, ইত্যাদি |
| **বাস্তবতা** | কোনো স্ক্রিপ্ট Table 5 তৈরি করে না — সংখ্যাগুলো কাগজে **হাতে লেখা**। সূত্র সঠিক (`mean(SPEI_12m < -0.5)×100` per division) কিন্তু পুনরুৎপাদনযোগ্য নয়। |
| **ঝুঁকি** | Reproducibility প্রশ্ন উঠলে সমস্যা। |
| **সমাধান** | একটি ছোট স্ক্রিপ্ট লিখে Table 5 অটো-জেনারেট করুন। |

---

## 🚨 জার্নাল reject হবে কি?

**সরাসরি উত্তর: স্বয়ংক্রিয়ভাবে reject হবে না — কিন্তু গুরুত্বপূর্ণ over-claim আছে যা ধরা পড়লে মেজর রিভিশন বা রিজেক্ট হতে পারে।**

**কেন reject হবে না:**
- Walk-forward temporal CV একটি **সম্মানিত ও বৈধ** validation পদ্ধতি। অনেক প্রকাশিত পেপার এটি ব্যবহার করে।
- ৯৭.২৮% accuracy বৈধভাবে গণনাকৃত (Ensemble-এর ৫-fold গড়)।
- SHAP interpretability, ৮-স্কেল SPEI, ৩৫ স্টেশন — এগুলো শক্তিশালী অবদান।

**কেন ঝুঁকি আছে (over-claim):**
- "Forecasting / month-ahead / 3-6-12 month forecast" — কিন্তু আসলে classification, lead time ≈ ০।
- "Operationally ready" — কিন্তু কোনো deployment নেই।
- "Unseen future data" — কিন্তু ডেটা ঐতিহাসিক।

**সুপারিশ:** কাগজের framing সততার সাথে ঠিক করুন (উপরের সমাধানগুলো)। তাহলে এটি একটি **দৃঢ়, প্রকাশযোগ্য** paper হবে — forecasting দাবি ছাড়াই।

---

## 🛠️ সমাধান রোডম্যাপ (priority অনুযায়ী)

### 🔴 Priority 1 (আবশ্যক — submission এর আগে):
1. "Forecasting/early-warning/month-ahead" ভাষা → "Classification with temporal validation"-এ পরিবর্তন।
2. "Unseen future data" → "held-out temporal folds"।
3. "Operationally ready" → "research-grade, suitable for future deployment"।
4. Conclusion-এর ৯৭.২৮% বাক্যাংশ সংশোধন।

### 🟡 Priority 2 (মূল্য বাড়াবে — করলে ভালো):
5. Lagged-only model তৈরি করে **আসল lead time (১–৩ মাস)** দেখান → তাহলে forecasting দাবি সত্য হয়।
6. Table 5 অটো-জেনারেট করার স্ক্রিপ্ট।

### 🟢 Priority 3 (ভবিষ্যতের জন্য):
7. একটি সহজ Streamlit ড্যাশবোর্ড prototype।
8. Multi-class severity (mild/moderate/severe/extreme) classification।

---

---

## 🚀 পরিশিষ্ট: Option B — Lagged-Only Forecasting মডেল বানানোর সম্পূর্ণ পরিকল্পনা

### 🎯 লক্ষ্য
বর্তমান **classification** মডেলকে (lead time ≈ ০) একটি সত্যিকারের **forecasting** মডেলে রূপান্তর করা — যা পরের মাসের (বা N-মাস আগের) খরা **ঘটার আগেই** বলতে পারে। তাহলে কাগজের "forecasting / early-warning" দাবি সত্য হবে এবং কৃষক/ব্যবহারকারী আগে থেকেই প্রস্তুতি নিতে পারবে।

### 📐 মূল নীতি
শুধুমাত্র **"আগে থেকে জানা যায় এমন (available-in-advance)"** ফিচার ব্যবহার করা। যেকোনো ফিচার যা predict করার মুহূর্তে এখনো তৈরিই হয়নি — সেটা বাদ দেওয়া।

---

### ধাপ ১ — ফিচার পরিবর্তন: কোনগুলো রাখবেন, কোনগুলো বাদ

| ফিচার ক্যাটাগরি (বর্তমান ৭৬-এর মধ্যে) | আগে জানা যায়? | Forecasting মডেলে করণীয় |
|---|---|---|
| Spatial (`Latitude`, `Longitude`, `Distance_to_Bay`, `Station_encoded`) | ✅ হ্যাঁ (স্থির) | **রাখুন** |
| Fourier / month (`sin_month`, `cos_month`, `Year_normalized`) | ✅ হ্যাঁ (ক্যালেন্ডার) | **রাখুন** |
| Monsoon/crop phase (বাইনারি ০/১) | ✅ হ্যাঁ (ক্যালেন্ডার মাস) | **রাখুন** |
| `Ra_MJ_m2_day` (extraterrestrial radiation) | ✅ হ্যাঁ (lat + month থেকে নির্ণয়যোগ্য) | **রাখুন** |
| `SPEI_*_lag*_safe` (২০টি lagged SPEI) | ✅ হ্যাঁ (অতীত SPEI) | **রাখুন — এগুলোই মূল ফিচার** |
| `Rainfall_Total` (current মাস) | ❌ না | **বাদ** → `Rainfall_lag1/lag2/lag3` যোগ করুন |
| `Temperature_Mean` (current) | ❌ না | **বাদ** → `Temp_lag1/lag2/lag3` যোগ করুন |
| `PET_mm_month` (current) | ❌ না | **বাদ** → `PET_lag1` যোগ করুন |
| `Humidity_Mean` (current) | ❌ না | **বাদ** → `Humidity_lag1` যোগ করুন |
| `Water_Balance` (current) | ❌ না | **বাদ** → বা `Water_Balance_lag1` যোগ করুন |
| `Max_Temperature` / `Min_Temperature` (current) | ❌ না | **বাদ** → lag করুন |
| Rolling (current মাস সহ) | ❌ আংশিক | **বাদ** → `shift(1)` দিয়ে আগের মাস পর্যন্ত rolling বানান |

---

### ধাপ ২ — নতুন lagged ক্লাইমেট ফিচার তৈরি (কোড স্কেচ)

```python
# প্রতি স্টেশনে আলাদাভাবে shift করে অতীত মাসের ক্লাইমেট (সময়ক্রম ঠিক রাখতে)
for station in df['Station'].unique():
    mask = df['Station'] == station
    s = df.loc[mask].sort_values(['Year', 'Month'])
    for col in ['Rainfall_Total', 'Temperature_Mean', 'PET_mm_month', 'Humidity_Mean']:
        for lag in [1, 2, 3]:
            df.loc[mask, f'{col}_lag{lag}'] = s[col].shift(lag).values
    # rolling যেটা current মাস ধরে না — আগের মাস পর্যন্ত
    df.loc[mask, 'Rainfall_roll3_past'] = (
        s['Rainfall_Total'].shift(1).rolling(3, min_periods=1).mean().values
    )
```

> **মূল পয়েন্ট:** প্রতিটি lagged ক্লাইমেট ফিচার predict করার সময় (মাস T-এর শেষে) আগে থেকেই জানা থাকে, কারণ সে মাস T-1 বা তার আগের তথ্য।

---

### ধাপ ৩ — Target পরিবর্তন (পরের মাস predict)

```python
# বর্তমান (classification):  y = (SPEI_12m < -0.5)   ← একই মাস
# Forecasting:                y = এক মাস পরের খরা
df['Drought_next1'] = df.groupby('Station')['Is_Drought_Binary'].shift(-1)   # ১-মাস lead
df['Drought_next3'] = df.groupby('Station')['Is_Drought_Binary'].shift(-3)   # ৩-মাস lead
```

- **১-মাস lead:** ৩১ জানুয়ারিতে ফেব্রুয়ারির খরা predict
- **৩-মাস lead:** মার্চে জুনের খরা predict
- প্রতিটি horizon-এর জন্য আলাদা মডেল ট্রেন করুন

---

### ধাপ ৪ — একই Walk-Forward Temporal CV (পদ্ধতি অপরিবর্তিত)

- বিদ্যমান ৫-fold split পুনরায় ব্যবহার করুন (১৯৬১ থেকে expanding train)।
- পার্থক্য: এখন **feature = past-only**, **target = next-month**।
- **এবারই সত্যিকার "predict future → match"** — কারণ predict করার মুহূর্তে next month-এর ক্লাইমেট data বা label, কোনোটাই ইনপুটে নেই।

---

### ধাপ ৫ — প্রত্যাশিত ফলাফল (বাস্তবসম্মত অনুমান)

- `SPEI_12m_lag1` একাই **২৬% importance** ছিল → খরা **persistent** (একবার শুরু হলে মাসের পর মাস থাকে)।
- তাই current ফিচার বাদ দিলেও সম্ভবত accuracy **৯০–৯৫%** থাকবে (বর্তমান ৯৭.২৮%-এর চেয়ে সামান্য কম)।
- কিন্তু এবার **সত্যিকার forecasting** — lead time ১–৩ মাস, যা বাস্তব প্রস্তুতির জন্য যথেষ্ট।

> **Trade-off:** সামান্য কম accuracy, কিন্তু বিশাল বেশি ব্যবহারিক মূল্য (আসল early warning)।

---

### ধাপ ৬ — কাগজে যা বদলাবে (দাবি এখন সত্য হবে)

| দাবি | আগে | Forecasting মডেলের পর |
|---|---|---|
| "Forecasting" | ❌ অতি-দাবি | ✅ **সত্য** |
| "Early warning" | ❌ অর্থহীন | ✅ **বৈধ** |
| "Month-ahead prediction" | ❌ ভুল | ✅ **সত্য (১-মাস lead)** |
| "Operationally useful" | ❌ প্রস্তাবিত | ✅ **বাস্তব প্রয়োগ সম্ভব** |

নতুন headline: **"1-month-ahead drought forecasting with ~9X% accuracy using only past information"**

---

### 📁 তৈরি করতে হবে এমন ফাইল

1. নতুন notebook সেল (বা স্ক্রিপ্ট `build_forecast_model.py`) — ধাপ ১–৪ বাস্তবায়ন।
2. নতুন outputs: `outputs/forecast_model_performance.json`, `outputs/forecast_cv_results.json`।
3. নতুন Figure: per-horizon (১/৩-মাস) accuracy + lead-time vs accuracy trade-off curve।

---

### ✅ Implementation Checklist

- [ ] current-month ক্লাইমেট ফিচার চিহ্নিত করে বাদ দাও
- [ ] lagged ক্লাইমেট ফিচার (lag ১/২/৩) যোগ করো
- [ ] rolling ফিচার `shift(1)` দিয়ে past-only করো
- [ ] target কে `shift(-1)` / `shift(-3)` করে next-month বানাও
- [ ] একই ৫-fold walk-forward CV চালাও
- [ ] ১-মাস ও ৩-মাস horizon-এর accuracy তুলনা করো
- [ ] কাগজের forecasting দাবিগুলো নতুন ফলাফল দিয়ে প্রতিস্থাপন করো

---

---

## 🚀 Improvement Plan & Rating Roadmap (পরে শুরু করার জন্য মাস্টার প্ল্যান)

> এই অংশটি পরে কাজ শুরু করার সময় রেফারেন্স হিসেবে ব্যবহার করা হবে। এখানে রয়েছে: (ক) প্রতিটা ধাপে কাগজের সম্ভাব্য rating, (খ) graph/visualization strategy, (গ) priority অনুযায়ী top-quality roadmap।

### 📊 ১. Rating Trajectory (প্রতিটা ধাপে কাগজ কতটা ভালো হবে)

| ধাপ | কী করবে | সৎ Rating | সম্ভাব্য জার্নাল টায়ার |
|---|---|---|---|
| **ধাপ ০ (বর্তমান)** | classification + over-claim + leakage risk | ৩–৪/১০ ⚠️ | Q3/Q4 তেও ঝুঁকিপূর্ণ |
| **ধাপ ১** | framing ঠিক + persistence baseline (leakage প্রশ্ন বন্ধ) | ৬/১০ | Q2/Q3 — মাঝারি জার্নালে প্রকাশ্য |
| **ধাপ ২** | + আসল forecasting (lagged-only + ARIMA/SARIMA/LSTM তুলনা) | ৭.৫/১০ | Q1/Q2 — "Theoretical and Applied Climatology", "Natural Hazards" |
| **ধাপ ৩** | + পুরো study guide (agricultural drought + Taylor + KGE/NSE + Kruskal-Wallis) | ৮.৫–৯/১০ ⭐ | Q1 — "Int. J. of Climatology", "J. of Hydrology: Regional Studies" |

---

### 🗺️ ২. Graph/Visualization Strategy (৩৫ স্টেশনের বদলে Division-wise) ⭐

> 💡 **মূল সিদ্ধান্ত:** ৩৫টি স্টেশনের ৩৫টি আলাদা graph মূল পেপারে দিলে data **হজিবিজি (cluttered)** হয়ে যায়। তাই **division-wise aggregation** ব্যবহার করা উত্তম — বাংলাদেশের ~৮টি বিভাগ (রাজশাহী, রংপুর, ঢাকা, চট্টগ্রাম, খুলনা, বরিশাল, সিলেট, ময়মনসিংহ) অনেক বেশি পরিষ্কার ও অর্থবহ।

| কোথায় | কী দেখাবে | কেন |
|---|---|---|
| **মূল পেপার** | 🌍 **Division-wise aggregated** views (৮ বিভাগ — bar/map/heatmap) | পরিষ্কার, region-এর পার্থক্য এক নজরে |
| **মূল পেপার** | 🎯 ৪–৬টি **প্রতিনিধি স্টেশন** (প্রতি বিভাগের ১টা) | বিস্তারিত উদাহরণ |
| **মূল পেপার** | 📦 একটা **boxplot/heatmap** (সব ৩৫ একসাথে) বা **Taylor diagram** | সামগ্রিক তুলনা |
| **Supplementary (appendix)** | 📎 বাকি সব ৩৫ স্টেশনের বিস্তারিত graph | বিস্তারিত প্রমাণ |

> **প্রস্তাবিত:** division-wise আগে (মূল পেপার), station-wise পরে (supplementary)। এতে reviewer পরিষ্কার region-ভিত্তিক গল্প পাবেন।

---

### 🎯 ৩. Top-Quality Roadmap (priority অনুযায়ী)

#### 🔴 Tier 1 — মরণ-ঘাত ফিক্স (না করলে কাগজ টিকবে না)
1. **Persistence baseline** ⭐⭐⭐ — naive model "গত মাসের খরা = এই মাসের খরা"; তারপর দেখাও তোমার মডেল এর চেয়ে কত ভালো → leakage/autocorrelation critique বন্ধ। **এক নম্বর দরকারি।**
2. **Honest framing** — "forecasting/operational/first-ever/highest" ভাষা সরাও বা বাস্তবায়ন করো।
3. **সব অভ্যন্তরীণ সংখ্যা এক করো** (accuracy, std, study period, station count)।

#### 🟡 Tier 2 — বড় মূল্য বৃদ্ধি (real forecasting paper)
4. **Lagged-only forecasting (Option B)** → real ১–৩ মাস lead time।
5. **ARIMA / SARIMA / LSTM তুলনা** (NSE/KGE দিয়ে)।
6. **NSE + KGE evaluation** — hydrological standard metric।

#### 🟢 Tier 3 — comprehensive + novel (top-tier করে)
7. **Agricultural drought এক্সটেনশন** ⭐ — SPEI ৩–৬m + Boro/Aus/Aman। **সবচেয়ে বড় novelty** (একই ডেটা থেকে দুই ধরনের খরা)।
8. **Taylor diagram** — ৮ scale + ৮ division এক গ্রাফে।
9. **Kruskal-Wallis** — ঋতু/অঞ্চলে খরার পার্থক্য প্রমাণ (p-value)।
10. **ADF + EDA** rigor যোগ।

---

### 💡 ৪. Topic-ভিত্তিক মূল্য (কোনটা কতটা দামি)

| Topic | পেপারে মূল্য |
|---|---|
| Persistence baseline | 🔴🔴🔴 (সবচেয়ে দরকারি) |
| Lagged-only forecasting | 🔴🔴🔴 |
| Agricultural drought | 🔴🔴🔴 (সবচেয়ে বড় novelty) |
| ARIMA/SARIMA/LSTM | 🟡🟡🟡 |
| NSE/KGE | 🟡🟡🟡 |
| Taylor diagram | 🟡🟡 |
| Kruskal-Wallis | 🟡🟡 |
| ADF/EDA | 🟢 |
| ACF/PACF | 🟢 |
| SPEI table / tuning | ⚪ (ইতিমধ্যে আছে) |

---

### 🚦 ৫. শুরু করার সুপারিশ (start order)

> **সবচেয়ে কম পরিশ্রমে সবচেয়ে বেশি মূল্য:** Tier 1 (persistence baseline + honest framing) আগে → কাগজ একই সাথে ৬/১০-এ যায় আর সবচেয়ে বড় ঝুঁকি (leakage) দূর হয়।
> তারপর **agricultural drought (Tier 3 #7)** — সবচেয়ে বড় novelty, gap-ও শক্ত হয় ("আগের সব BD study শুধু hydrological, কেউ একসাথে agricultural করেনি")।
> তারপর **forecasting (Tier 2)** — real early warning।

---
