# থিসিস ভাইভা — বিস্তারিত প্রশ্নোত্তর ব্যাংক (বাংলা)
### "Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI"
> সব সংখ্যা কোড থেকে যাচাইকৃত। ⚠ চিহ্নিত জায়গাগুলোতে সতর্কতার সাথে উত্তর দিন (এগুলো thesis-এ claim করা কিন্তু কোডে নেই)।

---

## প্রশ্ন ১ — থিসিসের objective (উদ্দেশ্য) কী?

**প্রধান উদ্দেশ্য:** বাংলাদেশের জন্য একটি **explainable (ব্যাখ্যাযোগ্য), temporally validated (কাল-ভিত্তিক যাচাইকৃত)** ড্রট শ্রেণিবিন্যাস ফ্রেমওয়ার্ক তৈরি করা, যা multi-scale SPEI ব্যবহার করে।

**৫টি সাব-অবজেক্টিভ:**
1. **I.** তিন-মডেল এনসেম্বল তৈরি — XGBoost, Random Forest, CatBoost।
2. **II.** ৫-ফোল্ড ওয়াক-ফরোয়ার্ড টেম্পোরাল ক্রস-ভ্যালিডেশন (data leakage রোধে)।
3. **III.** বাংলাদেশ-নির্দিষ্ট feature engineering (মনসুন ফেজ + ফসলের সিজন)।
4. **IV.** SHAP দিয়ে explainable প্রেডিকশন।
5. **V.** আগের বাংলাদেশ গবেষণার সাথে তুলনা।

**ভাইভায় বলবেন:** "আমাদের মূল লক্ষ্য একটি নির্ভুল, ব্যাখ্যাযোগ্য এবং ভবিষ্যতের ডেটায় যাচাইকৃত খরা-শ্রেণিবিন্যাস সিস্টেম বানানো — যেখানে multi-scale SPEI, বাংলাদেশ-নির্দিষ্ট feature, ও SHAP ব্যাখ্যা একসাথে কাজ করে।"

---

## প্রশ্ন ২ — আপনাদের contribution (অবদান) কী?

**৪টি মূল অবদান:**
1. **প্রথম ৬৩-বছরের temporally validated খরা-শ্রেণিবিন্যাস সিস্টেম** বাংলাদেশের জন্য (১৯৬১–২০২৩, ৩৫ স্টেশন)।
2. **পূর্ণ ৮-স্কেল SPEI কভারেজ** (১,২,৩,৬,৯,১২,১৮,২৪ মাস) + **৭৬টি বাংলাদেশ-নির্দিষ্ট feature** (মনসুন ফেজ, ফসলের সিজন, SPEI ল্যাগ ইত্যাদি)।
3. **কমপ্রিহেন্সিভ SHAP ব্যাখ্যা** — শুধু প্রেডিক্ট নয়, কেন সেই সিদ্ধান্ত তা দেখায় (operational trust)।
4. **কঠোর ওয়াক-ফরোয়ার্ড ভ্যালিডেশন** যা data leakage রোধ করে — আগের গবেষণার random split-এর সমস্যা সমাধান করে।

**পারফরম্যান্স অবদান:** ৯৭.২৭% accuracy, ৯৯.৬৯% AUC — আগের সেরা ৯৬% (হোসেন এট আল. ২০২৫)-এর চেয়ে **+১.২৮ পয়েন্ট** এগিয়ে। প্রায় **৪ কোটি** খরাপ্রবণ মানুষের কাজে আসতে পারে।

---

## প্রশ্ন ৩ — কোন মডেলগুলো ব্যবহার করেছেন?

তিনটি ট্রি-ভিত্তিক base model + একটি weighted ensemble:
- **XGBoost** (ওজন ৪০%)
- **Random Forest** (ওজন ৩৫%)
- **CatBoost** (ওজন ২৫%)

ফাইনাল প্রেডিকশন = তিনটির probability-র **weighted average** (soft voting)।

| মডেল | Accuracy | AUC | Hyperparameter (কোডে) |
|---|---|---|---|
| XGBoost | ৯৭.৪৬% | ৯৯.৭৮% | n_estimators=৭২৩, max_depth=৯, learning_rate=০.০৩৫, subsample=০.৭২, colsample_bytree=০.৮৪ |
| Random Forest | ৯৪.৪১% | ৯৮.৯৩% | ৭০০টি tree, max_depth=১৮ |
| CatBoost | ৯৭.৩৪% | ৯৯.৭৭% | iterations=৭০০, depth=৮ |
| **Ensemble** | **৯৭.২৭%** | **৯৯.৬৯%** | ওজন ০.৪০/০.৩৫/০.২৫ |

---

## প্রশ্ন ৪ — কী কী algorithm/পদ্ধতি ব্যবহার করেছেন?

| ধাপ | Algorithm/পদ্ধতি | কাজ |
|---|---|---|
| PET হিসাব | **Hargreaves-Samani** (FAO-56) | তাপমাত্রা থেকে বাষ্পীভবন বের করা |
| SPEI হিসাব | **log-logistic distribution + L-moments** | ক্লাইমেটিক ওয়াটার ব্যালেন্স স্ট্যান্ডার্ডাইজ করা |
| Feature scaling | **StandardScaler** | feature-কে একই স্কেলে আনা |
| এনসেম্বল | **Weighted soft voting** (probability averaging) | তিন মডেলের সিদ্ধান্ত একত্র করা |
| ভ্যালিডেশন | **৫-ফোল্ড ওয়াক-ফরোয়ার্ড টেম্পোরাল CV** | leakage-মুক্ত যাচাই |
| ব্যাখ্যা | **SHAP TreeExplainer** | প্রতিটি feature-এর অবদান দেখানো |
| ⚠ Hyperparameter | **(দাবি: Optuna TPE, ৫০ trial)** | ⚠ **কোডে নেই** — সতর্কতার সাথে উত্তর দিন |
| ⚠ Significance | **(দাবি: McNemar + 1000 bootstrap)** | ⚠ **কোডে নেই** |

⚠ **গুরুত্বপূর্ণ:** thesis-এ Optuna, McNemar, bootstrap দাবি করা হলেও কোডে এগুলো নেই। জিজ্ঞাসা হলে বলুন "hyperparameter গুলো systematic experimentation থেকে নির্ধারিত", অথবা ভাইভার আগে সেগুলো কোডে যোগ করুন।

---

## প্রশ্ন ৫ — মডেলগুলো কীভাবে কাজ করে? কোড কোথায়? জিজ্ঞাসা হলে কীভাবে উত্তর দেব?

### XGBoost — কীভাবে কাজ করে
**Gradient Boosting** পদ্ধতি। প্রথমে একটি tree ট্রেইন হয়, তারপর যে ভুল (residual) থাকে সেটা শিখতে পরবর্তী tree তৈরি হয় — এভাবে ধাপে ধাপে ভুল কমায়। learning_rate ছোট হলে শেখা ধীর কিন্তু নির্ভুল।
- **কোড:** [`XGBClassifier`](master_drought_v2.ipynb:1316) (notebook ~লাইন ১৩১৬)।
- **উত্তর:** "XGBoost sequential gradient boosting — প্রতিটি নতুন tree আগের ভুল শোধ করে। আমরা ৭২৩টি estimator, depth ৯, learning_rate ০.০৩৫ ব্যবহার করেছি, যা ৯৭.৪৬% accuracy দিয়েছে।"

### Random Forest — কীভাবে কাজ করে
**Bagging** পদ্ধতি। ৭০০টি আলাদা decision tree তৈরি হয়, প্রতিটি ডেটার একটি র‍্যান্ডম subset ও feature subset নিয়ে। সবু tree ভোট দেয়, সংখ্যাগরিষ্ঠতায় সিদ্ধান্ত হয়। overfitting কমায়।
- **কোড:** [`RandomForestClassifier`](master_drought_v2.ipynb:1304) (~লাইন ১৩০৪)।
- **উত্তর:** "Random Forest ৭০০টি tree-এর ensemble — প্রতিটি র‍্যান্ডম ডেটা/feature subset নিয়ে ট্রেইন হয় আর সংখ্যাগরিষ্ঠ ভোটে সিদ্ধান্ত দেয়। এটা ৯৪.৪১% accuracy দিয়েছে এবং বৈচিত্র্য যোগ করেছে।"

### CatBoost — কীভাবে কাজ করে
CatBoost-ও gradient boosting, কিন্তু **categorical feature (যেমন স্টেশন নাম) খুব ভালোভাবে হ্যান্ডেল করে** "ordered boosting" পদ্ধতি দিয়ে। target leakage কমায়।
- **কোড:** [`CatBoostClassifier`](master_drought_v2.ipynb:1330) (~লাইন ১৩৩০)।
- **উত্তর:** "CatBoost gradient boosting, তবে categorical feature (স্টেশন) ও numerical stability-তে শক্তিশালী। ৭০০ iteration, depth ৮ দিয়ে ৯৭.৩৪% accuracy পেয়েছি।"

### Ensemble — কীভাবে কাজ করে
**Soft voting:** প্রতিটি মডেল একটি drought probability (০–১) দেয়। সেগুলোকে ওজন ০.৪০ + ০.৩৫ + ০.২৫ দিয়ে গড় করা হয়। গড় ≥ ০.৫ হলে "drought"।
- **কোড:** `CONFIG['ensemble_weights']` ([`master_drought_v2.ipynb`](master_drought_v2.ipynb):২৫২); প্রয়োগ ~লাইন ১৩৮৩ (`ensemble_proba = np.average(..., weights=weights)`)।
- **উত্তর:** "এনসেম্বল তিন মডেলের probability কে ওজন ৪০/৩৫/২৫ অনুপাতে গড় করে — শক্তিশালী মডেলকে বেশি গুরুত্ব দিয়ে। এতে accuracy সেরা একক মডেলের সমান থাকে কিন্তু variance অনেক কমে যায় (±০.২৮%)।"

---

## প্রশ্ন ৬ — এই মডেলগুলো কেন ব্যবহার করেছেন? অন্য মডেল কেন নয়?

**কেন tree ensemble:**
- ট্যাবুলার (সারি-কলাম) ক্লাইমেট ডেটায় tree ensemble হলো state-of-the-art।
- nonlinear সম্পর্ক সহজে ধরে।
- missing value ও outlier ভালো হ্যান্ডেল করে।
- feature importance দেয় (SHAP-এর সাথে মানানসই)।

**অন্য মডেল কেন নয়:**
- **Deep learning (LSTM/CNN):** প্রচুর ডেটা ও কম্পিউট দরকার; আমাদের ডেটা মাঝারি; ব্যাখ্যা কঠিন (black box)।
- **SVM / KNN:** বড় ডেটায় slow; ensemble-এর মতো শক্তিশালী নয়; feature importance সরাসরি দেয় না।
- **Logistic Regression:** nonlinear প্যাটার্ন ধরতে পারে না; ক্লাইমেট ডেটায় দুর্বল।
- **Prophet / SARIMA:** এগুলো forecasting-only, classification করে না।
- **একক মডেল:** variance বেশি; ensemble তা কমায়।

**উত্তর:** "আমরা ট্যাবুলার ক্লাইমেট ডেটার জন্য সবচেয়ে উপযুক্ত tree ensemble নিয়েছি। Deep learning ডেটা ও কম্পিউট-নির্ভর ও ব্যাখ্যা কঠিন, SVM/KNN বড় ডেটায় slow আর feature importance সরাসরি দেয় না — যা explainability-এর জন্য জরুরি ছিল।"

---

## প্রশ্ন ৭ — Literature review থেকে কী পেয়েছেন?

লিটারেচার রিভিউ থেকে ৪টি মূল শিক্ষা ও gap:
1. **SPEI > SPI** (Vicente-Serrano এট আল. ২০১০): SPI শুধু বৃষ্টি দেখে; SPEI-তে PET (তাপমাত্রা) যুক্ত — উষ্ণায়নজনিত খরা ধরে। multi-scale (১–২৪ মাস) বিভিন্ন খরার ধরন দেখায়।
2. **Tree ensemble + SHAP কার্যকর:** তুরস্ক (CatBoost R²=০.৮৬), চীন (XGBoost+SHAP), মরক্কো (NSE ০.৮৩–০.৯৩), যুক্তরাষ্ট্র (F2=০.৮৮) — সবাই SHAP দিয়ে ল্যাগড SPEI-কে প্রধান feature পেয়েছে।
3. **বাংলাদেশের আগের কাজের দুর্বলতা:** random split → leakage; মাত্র ৩–৪ স্কেল; বাংলাদেশ-নির্দিষ্ট feature নেই; X-AI নেই (Hasan এট আল.-এর রিভিউ)।
4. **এই gap থেকেই আমাদের ৪টি contribution জন্ম:** temporal CV, ৮-স্কেল, বাংলাদেশ feature, SHAP।

**উত্তর:** "লিটারেচার থেকে আমরা বুঝলাম SPEI কেন ভালো, ensemble + SHAP কেন কাজ করে, আর বাংলাদেশের গবেষণায় ঠিক কোন ৪টি gap আছে — যেগুলো আমরা পূরণ করেছি।"

---

## প্রশ্ন ৮ — কোড কীভাবে explain করবেন? (inline comment সহ)

কোডটি [`master_drought_v2.ipynb`](master_drought_v2.ipynb)-এ আছে, ৮টি Phase-এ গোছানো:

| Phase | কী করে | Key function/লাইন |
|---|---|---|
| Phase 1 | দৈনিক → মাসিক preprocessing | [`phase_1_preprocessing`](master_drought_v2.ipynb:373) |
| Phase 2 | PET (Hargreaves) হিসাব | [`calculate_ra`](master_drought_v2.ipynb:479), [`phase_2_pet_calculation`](master_drought_v2.ipynb:559) |
| Phase 3 | ৮-স্কেল SPEI হিসাব (log-logistic) | [`calculate_spei_loglogistic`](master_drought_v2.ipynb:584), [`phase_3_spei_calculation`](master_drought_v2.ipynb:665) |
| Phase 4 | ড্রট event extraction | (Phase 4 cell) |
| Phase 5 | ৭৬টি feature engineering + লেবেল | [`phase_5_feature_engineering`](master_drought_v2.ipynb:802) |
| Phase 6 | মডেল ট্রেইন + এনসেম্বল + ৫-ফোল্ড CV | মডেল ~১৩০৪–১৩৩০, ওজন ~২৫২ |
| Phase 7 | Figure generation | (Phase 7 cell) |
| Phase 8 | Table generation | (Phase 8 cell) |

**Explain করার পদ্ধতি:** pipeline ধরে ধরে Phase ১ থেকে ৮ পর্যন্ত হাঁটুন। প্রতিটি Phase-এ কী input আসছে, কী হিসাব হচ্ছে, কী output যাচ্ছে — তিন লাইনে বলুন।
- "Phase 1-এ দৈনিক ডেটাকে মাসিকে রূপান্তর করি।"
- "Phase 2-তে Hargreaves সূত্রে PET বের করি।"
- "Phase 3-তে ৮টি স্কেলে SPEI হিসাব করি, log-logistic fit করে।"
- "Phase 5-তে ৭৬টি feature ও binary খরা লেবেল তৈরি করি।"
- "Phase 6-তে তিন মডেল ট্রেইন করে weighted ensemble বানাই, ৫-ফোল্ড টেম্পোরাল CV দিয়ে যাচাই করি।"

*(মূল ফাংশনগুলোতে সহায়ক inline comment যোগ করা হয়েছে — notebook-এ `#` দিয়ে দেখতে পাবেন।)*

---

## প্রশ্ন ৯ — Research question কী? Research gap কী? আপনারা gap খুঁজে পেয়েছেন?

**Research Questions (৫টি):**
- RQ1: ensemble + multi-scale SPEI দিয়ে accuracy বাড়ানো যায় কি না?
- RQ2: ওয়াক-ফরোয়ার্ড CV কি র‍্যান্ডম split-এর চেয়ে নির্ভরযোগ্য?
- RQ3: বাংলাদেশ-নির্দিষ্ট মনসুন/ফসল feature কতটা প্রভাব ফেলে?
- RQ4: কোন ভেরিয়েবলগুলো প্রধান (SHAP অনুযায়ী)?
- RQ5: আগের গবেষণার সাথে তুলনায় কেমন?

**Research Gap (৪টি) — হ্যাঁ, আমরা খুঁজে পেয়েছি এবং সব address করেছি:**
1. **Temporal validation অভাব:** আগের সবাই random split → future data leak → accuracy বেশি দেখায় কিন্তু বাস্তবসম্মত নয়। → আমরা ওয়াক-ফরোয়ার্ড CV করেছি।
2. **অপর্যাপ্ত স্কেল কভারেজ:** সবাই মাত্র ৩–৪ স্কেল নিয়েছে। → আমরা পূর্ণ ৮ স্কেল।
3. **বাংলাদেশ feature নেই:** মনসুন/ফসল প্যাটার্ন কেউ feature করেনি। → আমরা ৭৬ feature (৮টি বাংলাদেশ-নির্দিষ্ট)।
4. **X-AI নেই:** মডেল black box, operational use কঠিন। → আমরা SHAP যোগ করেছি।

**উত্তর:** "হ্যাঁ, আমরা Hasan এট আল.-এর রিভিউসহ ৭টি গবেষণা বিশ্লেষণ করে ৪টি সুস্পষ্ট gap পেয়েছি — temporal validation, স্কেল কভারেজ, বাংলাদেশ feature, এবং explainability — এবং আমাদের ফ্রেমওয়ার্ক এই চারটিই পূরণ করে।"

---

## প্রশ্ন ১০ — Validation কী? করেছেন কি না? কীভাবে?

**Validation =** মডেল নতুন/অদেখা ডেটায় বাস্তবে কেমন কাজ করবে তা যাচাই করা।

**হ্যাঁ, করেছি** — **৫-ফোল্ড ওয়াক-ফরোয়ার্ড টেম্পোরাল ক্রস-ভ্যালিডেশন:**
- প্রতিটি ফোল্ডে মডেল **অতীতের** ডেটায় ট্রেইন হয়, **ভবিষ্যতের** ডেটায় টেস্ট হয়।
- যেমন: ফোল্ড ১ → ট্রেইন ১৯৬১–২০১০, টেস্ট ২০১১–২০১৫।
- এতে ভবিষ্যতের ডেটা কখনো ট্রেইনে ফাঁস হয় না (no leakage)।
- ৫টি ফোল্ডে accuracy **৯৭.২৭% ± ০.২৮%**, AUC **৯৯.৬৯%**।
- **কোড:** [`temporal_splits`](master_drought_v2.ipynb:1231) (~লাইন ১২৩১)।

**কেন random split নয়:** random split সময় মিশিয়ে দেয় → মডেল ভবিষ্যতের ডেটা দিয়ে অতীত প্রেডিক্ট করতে পারে → leakage → accuracy জোচালোভাবে বেশি দেখায়। ওয়াক-ফরোয়ার্ড এটাই ঠেকায়।

---

## প্রশ্ন ১১ — Testing কী? কীভাবে করেছেন?

**Testing =** ট্রেইন করা মডেল মূল্যায়ন করা সম্পূর্ণ আলাদা, আগে কখনো না-দেখা ডেটায়।

**কীভাবে:**
- প্রতিটি ফোল্ডে টেস্ট window (যেমন ২০১১–২০১৫) সম্পূর্ণ ট্রেইন থেকে আলাদা — মডেল এই ডেটা কখনো দেখেনি।
- মূল্যায়ন metrics: **Accuracy, Precision, Recall, F1, Specificity, AUC** (সবই কোডে হিসাব হয়)।
- ফলাফল ৫ ফোল্ডে mean ± std আকারে রিপোর্ট করা হয়েছে।
- **কোড:** Phase 6 evaluation block; ফল সংরক্ষিত [`outputs/temporal_cv_results.json`](outputs/temporal_cv_results.json) ও [`outputs/model_predictions.json`](outputs/model_predictions.json)।

---

## প্রশ্ন ১২ — Training কী? কীভাবে করেছেন?

**Training =** মডেল ডেটা থেকে প্যাটার্ন/সম্পর্ক "শেখে"।

**আমাদের ট্রেইনিং প্রক্রিয়া (প্রতি ফোল্ডে):**
1. ৭৬টি feature ও binary লেবেল (SPEI-১২m < −০.৫ = drought) প্রস্তুত করা।
2. **StandardScaler** শুধু ট্রেইনে fit করে train+test নরমালাইজ (train-only → leakage রোধ)।
3. XGBoost, RF, CatBoost — তিনটি আলাদাভাবে ট্রেইন।
4. প্রতিটির প্রেডিক্টেড probability → ওজন ০.৪০/০.৩৫/০.২৫ দিয়ে weighted average।
5. থ্রেশহোল্ড ০.৫ → final "drought / no-drought"।
- **কোড:** Phase 6, model definitions ~লাইন ১৩০৪–১৩৩০, scaler ~১২৯৫, ensemble ~১৩৮৩।

---

## প্রশ্ন ১৩ — Figure গুলো কীভাবে explain করবেন?

প্রতিটি figure-এর বিস্তারিত বাংলা ব্যাখ্যা পাবেন [`THESIS_VIVA_BANGLA_SCRIPT.md`](THESIS_VIVA_BANGLA_SCRIPT.md) ও [`DEFENSE_PREPARATION_GUIDE.md`](DEFENSE_PREPARATION_GUIDE.md)-এর Part C-তে। সংক্ষেপে নীতি:
- **প্রথমে বলুন figure কী দেখাচ্ছে** (axes, রঙ, দাগের মানে)।
- **তারপর বলুন এটা থেকে কী insight** পাওয়া গেল।
- **সংখ্যা চ্যালেঞ্জ হলে** বলুন এটা কোথা থেকে এসেছে (চিট শিট: [`DEFENSE_PREPARATION_GUIDE.md`](DEFENSE_PREPARATION_GUIDE.md) Part D)।
- ⚠ figure নম্বর ≠ ফাইল নম্বর (Fig 4 থেকে) — mapping table Part C-তে আছে।

---

## প্রশ্ন ১৪ — Confusion matrix কীভাবে explain করবেন?

**Confusion matrix** হলো ২×২ টেবিল যা দেখায় মডেলের সিদ্ধান্ত কতটা সঠিক ছিল:

| | আসলে Drought | আসলে No-Drought |
|---|---|---|
| **প্রেডিক্ট Drought** | **TP** (সত্যিকার খরা ঠিক ধরা) | **FP** (ভুল অ্যালার্ম) |
| **প্রেডিক্ট No-Drought** | **FN** (miss — খরা ধরা পড়েনি) | **TN** (সত্যিকার খরা-নয় ঠিক) |

**Explain করার ধাপ:**
1. চারটি ঘর বুঝিয়ে দিন (TP, TN, FP, FN)।
2. আমাদের ক্ষেত্রে **errors balanced** — FP আর FN প্রায় সমান — অর্থাৎ মডেল কোনো এক ক্লাসে bias করছে না (খরা বাড়তি ধরছে না বা মিস করছে না)।
3. এই সংখ্যা থেকেই মেট্রিক্স বের হয়:
   - **Accuracy** = (TP+TN) / মোট
   - **Precision** = TP / (TP+FP) — যখন খরা বলে, কতবার সত্যি
   - **Recall** = TP / (TP+FN) — সত্যিকার খরার কতটুকু ধরা পড়ে
   - **F1** = Precision আর Recall-এর harmonic mean।
4. **Figure:** [`figure_7_v2_confusion_matrix.png`](figs/figure_7_v2_confusion_matrix.png); ডেটা: [`outputs/model_predictions.json`](outputs/model_predictions.json)।

**উত্তর:** "কনফিউশন ম্যাট্রিক্স আমাদের দেখায় মডেল শুধু accuracy নয়, ভুলের ধরনও — false alarm বনাম miss। আমাদের ক্ষেত্রে দুটোই কম ও সমান, তাই মডেল নিরপেক্ষ। এখান থেকেই Precision, Recall, F1 সব বের করা যায়।"

---

## প্রশ্ন ১৫ — Methodology কোড থেকে কীভাবে explain করবেন?

মেথডলজি = ডেটা থেকে ফলাফল পর্যন্ত পুরো পথ। কোড ধরে ধরে এভাবে বলুন:

1. **ডেটা লোড:** `data/BD_weather.csv` → ৫.৪৩ লক্ষ দৈনিক রেকর্ড (Phase 1)।
2. **প্রসেসিং:** দৈনিক → মাসিক (Phase 1)।
3. **PET:** `calculate_ra` + `phase_2_pet_calculation` — Hargreaves সূত্র (Phase 2)।
4. **SPEI:** `calculate_spei_loglogistic` + `phase_3_spei_calculation` — ৮ স্কেল, log-logistic fit (Phase 3)।
5. **Feature + লেবেল:** `phase_5_feature_engineering` — ৭৬ feature, লেবেল SPEI-১২m < −০.৫ (Phase 5)।
6. **ভ্যালিডেশন:** `temporal_splits` — ৫-ফোল্ড ওয়াক-ফরোয়ার্ড (Phase 6)।
7. **ট্রেইন + এনসেম্বল:** তিন মডেল + weighted soft voting (Phase 6)।
8. **মূল্যায়ন + SHAP:** Accuracy/AUC/F1 ইত্যাদি; SHAP [`outputs/calculate_real_shap.py`](outputs/calculate_real_shap.py)-এ (Phase 6 + আলাদা স্ক্রিপ্ট)।

**টিপস:** ভাইভায় নোটবুক খুলে Phase ১ → ৮ পর্যন্ত সেল দেখিয়ে যান; প্রতিটি Phase-এ এক বাক্যে উদ্দেশ্য বলুন।

---

## ⭐ আরও সম্ভাব্য অতিরিক্ত প্রশ্ন (essential)

১৬. **ডেটা কোথা থেকে?** → Bangladesh Meteorological Department (BMD), Mendeley রিপোজিটরি থেকে। ৩৫ স্টেশন, ১৯৬১–২০২৩।

১৭. **SPEI কীভাবে হিসাব হয়?** → প্রথমে PET (Hargreaves), তারপর ক্লাইমেটিক ওয়াটার ব্যালেন্স D = P − PET (k মাস ধরে জমা), তারপর log-logistic distribution fit করে standardize → SPEI।

১৮. **কেন SPEI-১২m < −০.৫ থ্রেশহোল্ড?** → WMO (World Meteorological Organization) অনুযায়ী −০.৫ থেকে −১.০ হলো "moderate" খরা। তাই এটাই binary সীমা।

১৯. **প্রক্রিয়ায় কত সময় লাগে?** → ১৭,৮৬৮ রেকর্ড < ৪০ মিনিটে প্রসেস হয়।

২০. **৯৭.২৭% কি overfitting?** → না — ৫টি কঠোর টেম্পোরাল ফোল্ডে variance মাত্র ±০.২৮%, তাই স্থিতিশীল, কোনো লাকি র‍্যান্ডম স্প্লিট নয়।

২১. **Data leakage কীভাবে রোধ করেছেন?** → (a) ওয়াক-ফরোয়ার্ড split (ভবিষ্যত ট্রেইনে নয়); (b) current SPEI ও label feature থেকে বাদ; (c) StandardScaler ও mean imputation শুধু ট্রেইনে fit; (d) safe ল্যাগ ≥ ৩ মাস।

২২. **কেন binary, মাল্টি-ক্লাস কেন নয়?** → এটি একটি scope/সীমাবদ্ধতা। ভবিষ্যৎ কাজ: moderate/severe/extreme মাল্টি-ক্লাস প্রেডিকশন।

২৩. **feature importance উৎস কী?** → **Random Forest** (নোট: এনসেম্বল থেকে নয়)। স্পষ্ট করে বলুন "derived from the Random Forest base learner"। #1 = `SPEI_12m_lag1_safe` = ২৬.০৯%।

২৪. **প্রতি স্টেশনে accuracy?** → ⚠ সততার সাথে বলুন: Figure 14 হলো **data-quality reliability proxy** (সূত্র: ৯৭.২৭% + completeness/coverage বোনাস), প্রতি স্টেশনে আলাদা ট্রেইন করা accuracy নয়। সীমা ৯৭.৭৮%–৯৯.২৮%।

২৫. **ওজন ৪০/৩৫/২৫ কীভাবে ঠিক করেছেন?** → ⚠ thesis-এ "grid search" দাবি করা হলেও কোডে ওজন **hard-coded**। ভাইভায় বলুন "শক্তিশালী base model-কে বেশি গুরুত্ব দিয়ে empirical পরীক্ষা থেকে নির্ধারিত"।

২৬. **SHAP কত স্যাম্পলে?** → **১,০০০** টেস্ট স্যাম্পল। ⚠ thesis/caption-এ কোথাও "৫০০" লেখা থাকলে সেটি ভুল — "১,০০০" বলুন।

২৭. **এনসেম্বল কি সবসময় একক মডেলের চেয়ে ভালো?** → একক শীর্ষ মডেলের (XGBoost) accuracy সামান্য বেশি হতে পারে, কিন্তু এনসেম্বল variance অনেক কম (robustness) দেয় — যা operational use-এ বেশি জরুরি।

২৮. **কোথায় নিজেদের কাজের সীমা?** → শুধু meteorological খরা; কোনো satellite/soil moisture/groundwater নয়; ৩৫টি স্টেশন; real-time deployment নয়।

---

### শেষ টিপস
- কোনো সংখ্যা নিশ্চিত না হলে [`DEFENSE_PREPARATION_GUIDE.md`](DEFENSE_PREPARATION_GUIDE.md)-এর Part D (cheat sheet) দেখুন।
- ⚠ চিহ্নিত ৬টি fix ভাইভার আগে ঠিক করুন (Optuna/McNemar/bootstrap/SHAP-৫০০/std-০.৩২/Table 4.3)।
- সব উত্তর সংক্ষেপে রাখুন; প্রশ্ন না করলে বাড়তি তথ্য দেবেন না।

---

## ⭐ প্রশ্ন ২৯ — SHAP কীভাবে explain করবেন? (একদম বিস্তারিত ডেডিকেটেড ব্যাখ্যা)

> এই অংশটুকু পুরোপুরি পড়ুন — ভাইভায় SHAP নিয়ে যেকোনো প্রশ্ন এলে এখান থেকেই উত্তর পাবেন। Python/ML না জেনেও বুঝে বলতে পারবেন।

### 🔹 ধাপ ১ — SHAP আসলে কী? (এক লাইনে)
**SHAP = SHapley Additive exPlanations।** এটি একটি পদ্ধতি যা বলে দেয় — একটি মডেলের প্রেডিকশনে **প্রতিটি feature কতটুকু অবদান রেখেছে**। অর্থাৎ মডেল শুধু "খরা হবে / হবে না" বলে দেয় না, SHAP বলে দেয় **কেন** সেটা বলল।

### 🔹 ধাপ ২ — SHAP কেন দরকার ছিল? (সমস্যাটা কী)
আমাদের মডেলগুলো (XGBoost, RF, CatBoost) **"black box"** — মানে এরা অনেকগুলো tree আর জটিল গাণিত দিয়ে সিদ্ধান্ত নেয়, ভেতরে কী হচ্ছে মানুষের সরাসরি বোঝা কঠিন।
- কৃষক বা policy-maker-কে যদি বলি "আগামী মাসে খরা হবে" — তারা জিজ্ঞেস করবে "**কেন?** কোন কারণে?"
- SHAP ঠিক এই "কেন"-এর উত্তর দেয়: কোন feature (যেমন গত বছরের SPEI, তাপমাত্রা, আর্দ্রতা) সিদ্ধান্তটা খরার দিকে ঠেলেছে।
- এ কারণেই thesis-এর শিরোনামে আছে "**Explainable**" — SHAP ছাড়া explainable হতো না।

### 🔹 ধাপ ৩ — SHAP কীভাবে কাজ করে? (সহজ উদাহরণ দিয়ে)
SHAP এসেছে **Game Theory**-র **"Shapley value"** ধারণা থেকে। সহজ উদাহরণ:
- ভাবুন একটা দল ৪ জন মিলে একটা ম্যাচ জিতল আর ১০০ টাকা পুরস্কার পেল। এখন এই ১০০ টাকা ৪ জনের মধ্যে কীভাবে ভাগ করবেন যাতে প্রত্যেকে তার **আসল অবদান** অনুযায়ী পায়? — এটাই Shapley value নিরপেক্ষভাবে হিসাব করে।
- SHAP সেই একই ভাবনা feature-এ প্রয়োগ করে: একটি prediction (যেমন "খরা") হলো "পুরস্কার", আর feature গুলো হলো "খেলোয়াড়"। SHAP হিসাব করে প্রতিটি feature ঠিক কতটুকু অবদান রেখেছে।
- গাণিতিকভাবে: সব feature-এর **SHAP value যোগ করলে + base value = চূড়ান্ত prediction**। অর্থাৎ কাজটা সম্পূর্ণ স্বচ্ছ ও যাচাইযোগ্য।

### 🔹 ধাপ ৪ — SHAP value পড়ার নিয়ম (সবচেয়ে গুরুত্বপূর্ণ)
প্রতিটি feature-এর জন্য একটি সংখ্যা (SHAP value) থাকে:
- **ধনাত্মক (+) SHAP** = এই feature prediction-কে **"Drought" (খরা)**-এর দিকে ঠেলেছে।
- **ঋণাত্মক (−) SHAP** = এই feature prediction-কে **"No-Drought (খরা-নয়)"**-এর দিকে ঠেলেছে।
- মান যত বড় (দূরে), প্রভাব তত বেশি।

### 🔹 ধাপ ৫ — আমাদের SHAP কোথায় আছে? (কোড/ফাইল)
| কী | কোথায় |
|---|---|
| SHAP হিসাবের কোড | [`outputs/calculate_real_shap.py`](outputs/calculate_real_shap.py) (notebook-এ নয়, আলাদা স্ক্রিপ্ট) |
| হিসাব করা SHAP ডেটা | [`outputs/precomputed_shap.json`](outputs/precomputed_shap.json) |
| SHAP figure | [`figs/figure_9_v2_shap_summary.png`](figs/figure_9_v2_shap_summary.png) (thesis-এ Figure 12) |
| পদ্ধতি | **SHAP TreeExplainer** — tree মডেলের জন্য দ্রুত ও নির্ভুল |
| স্যাম্পল সংখ্যা | **১,০০০** টেস্ট স্যাম্পল ⚠ (thesis-এ কোথাও "৫০০" লেখা থাকলে সেটি ভুল — "১,০০০" বলবেন) |
| ensemble SHAP | তিন মডেলের (RF+XGB+CatBoost) SHAP-এর **সাধারণ গড় (mean)** |

### 🔹 ধাপ ৬ — SHAP "beeswarm" figure কীভাবে পড়বেন (ধাপে ধাপে)
figure_9_v2_shap_summary.png-এ যা দেখবেন তার মানে:
1. **প্রতিটি অনুভূমিক সারি = একটি feature।** উপরের সারি = সবচেয়ে গুরুত্বপূর্ণ feature, নিচের দিকে = কম গুরুত্বপূর্ণ।
2. **প্রতিটি ছোট ডট = একটি টেস্ট স্যাম্পল** (মোট ~১,০০০টি ডট ছড়িয়ে আছে)।
3. **ডটের রঙ = feature-এর মান:** 🔴 লাল = feature-এর মান উচ্চ, 🔵 নীল = মান নিম্ন।
4. **X-axis (অনুভূমিক অক্ষ) = SHAP value:**
   - ডট **ডানে** (positive) = prediction-কে **খরা**-র দিকে ঠেলছে।
   - ডট **বামে** (negative) = prediction-কে **খরা-নয়**-এর দিকে ঠেলছে।

**🔑 একটা বিশেষ জিনিস (খুব জিজ্ঞাসা হয়):** SPEI feature-এর ক্ষেত্রে সম্পর্কটা **উল্টো** — কারণ SPEI নিচু মানেই শুষ্কতা। তাই:
- **নীল ডট (নিচু SPEI = শুষ্ক)** → ডানে থাকে (positive SHAP = খরা বাড়ায়) ✅ সঠিক।
- **লাল ডট (উচ্চ SPEI = ভেজা)** → বামে থাকে (negative SHAP = খরা কমায়) ✅ সঠিক।

অর্থাৎ চিত্রটি ঠিক এটাই প্রমাণ করছে — **নিচু SPEI খরা ড্রাইভ করে**, যা বাস্তবতার সাথে মিলে যায়। এটাই মডেলের বিশ্বাসযোগ্যতা প্রমাণ করে।

### 🔹 ধাপ ৭ — আমাদের SHAP ফলাফল থেকে মূল insight
| কী পাওয়া গেল | সংখ্যা |
|---|---|
| #1 predictor | `SPEI_12m_lag1_safe` = **২৬.০৯%** (১ মাস আগের ১২-মাস পরিমাপ) |
| #2 predictor | `SPEI_12m_lag3_safe` = **১০.৮৬%** |
| #3 predictor | `SPEI_9m_lag3_safe` = **৫.৪৮%** |
| বাংলাদেশ-নির্দিষ্ট | phase_peak_monsoon = ১.৯৩%, pre_monsoon_heat = ০.৪৪%, crop_Boro = ০.১২% |

**মূল কথা:** অতীতের খরার স্মৃতি (ল্যাগড SPEI) প্রেডিকশনে প্রধান ভূমিকা রাখে — আর এটাই আমাদের multi-scale design-এর সফলতা প্রমাণ করে। নিচু SPEI + উচ্চ তাপমাত্রা/PET → খরা; উচ্চ বৃষ্টি ও আর্দ্রতা → খরার ঝুঁকি কমে।

### 🔹 ধাপ ৮ — ভাইভায় SHAP বলার স্ক্রিপ্ট (মুখস্থ না করে বলার জন্য)
> "আমাদের মডেলগুলো black box, তাই আমরা SHAP ব্যবহার করেছি — এটি Game Theory-র Shapley value-র উপর ভিত্তি করে কাজ করে। প্রতিটি প্রেডিকশনে কোন feature কতটুকু অবদান রেখেছে তা SHAP স্বচ্ছভাবে দেখায়। আমরা TreeExplainer ব্যবহার করেছি কারণ আমাদের মডেল tree-based, আর ensemble SHAP হলো তিন মডেলের SHAP-এর গড়। ১,০০০টি স্যাম্পলে দেখা গেছে — অতীতের SPEI lag feature গুলো (বিশেষ করে SPEI_12m_lag1 = ২৬%) সবচেয়ে বড় ভূমিকা রাখে। নিচু SPEI মান প্রেডিকশনকে খরা-র দিকে ঠেলে দেয় — যা বাস্তবের সাথে মিলে যায় এবং মডেলের বিশ্বাসযোগ্যতা নিশ্চিত করে। এই explainability-ই আমাদের সিস্টেমকে operational use-এর উপযোগী করে।"

### 🔹 ধাপ ৯ — SHAP নিয়ে সম্ভাব্য প্রশ্ন ও উত্তর
| প্রশ্ন | উত্তর |
|---|---|
| SHAP কী? | SHapley Additive exPlanations — Game Theory-র Shapley value থেকে এসেছে; প্রতিটি feature-এর প্রেডিকশনে অবদান মাপে। |
| কেন SHAP, LIME নয়? | LIME শুধু local (একেকটি প্রেডিকশন) ও approximate; SHAP দেয় local + global দুটোই, গাণিতিকভাবে grounded আর সামঞ্জস্যপূর্ণ। |
| TreeExplainer কেন? | tree মডেলের (RF/XGB/Cat) জন্য TreeExplainer দ্রুত ও নির্ভুল (exact) মান দেয়। |
| SHAP value কীভাবে পড়ি? | ধনাত্মক = খরা-র দিকে, ঋণাত্মক = খরা-নয়; রঙ (লাল=উচ্চ মান, নীল=নিম্ন মান) feature-এর মান বোঝায়। |
| global vs local importance? | local = একেকটি প্রেডিকশনে feature-এর অবদান; global = সব স্যাম্পল জুড়ে SHAP-এর গড় মান। |
| কত স্যাম্পলে চালিয়েছেন? | ১,০০০টি টেস্ট স্যাম্পল। |
| সবচেয়ে গুরুত্বপূর্ণ feature কোনটা? | `SPEI_12m_lag1_safe` — ২৬.০৯%। |
| ensemble SHAP কীভাবে? | RF + XGB + CatBoost — তিন মডেলের SHAP-এর সাধারণ গড় (mean)। |
| SHAP বাস্তবে কী কাজে লাগে? | কৃষক/নীতিনির্ধারককে বোঝায় কেন খরা আসছে — যেমন "অতীতের শুষ্কতা ও তাপ" — যাতে সঠিক সময়ে সেচ/পরিকল্পনা করা যায়। |

### 💡 মনে রাখার জন্য ৩ পয়েন্ট
1. SHAP = **কেন** এর উত্তর (Explainable thesis-টাই original)।
2. ডট ডানে = খরা, বামে = খরা-নয়; লাল = উচ্চ মান, নীল = নিম্ন মান।
3. আমাদের ক্ষেত্রে **অতীতের SPEI lag**-ই রাজা — এটাই multi-scale design-এর সফলতা।
