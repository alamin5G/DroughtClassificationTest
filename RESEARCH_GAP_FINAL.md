# 🎯 Final Research Gap & What We'll Do — একটি গল্পের মতো

> এই ডকুমেন্টটি থিসিসের **সর্বশেষ research gap** ও **উদ্দেশ্য**-কে একটি scenario-তে সাজিয়ে রাখে — প্রস্তাব/defense/ভূমিকায় সরাসরি ব্যবহারযোগ্য। এটি সৎ, defensible ও reviewer-proof।

---

## 🎬 গল্প: দুই কৃষক, দুই ফল

**২০১০ সাল, রাজশাহী।** কৃষক করিম মিয়া বোরো ধান বুনেছেন। এপ্রিলে বৃষ্টি বন্ধ, মাটি ফেটে যায়, ধান পুড়ে যায়। তিনি আগে জানতে পারেননি। এক মৌসুমের সব শেষ।

**একই রাজশাহী, কাল্পনিক ২০২৬।** কৃষক রহিম মিয়ার ফোনে একটা সতর্কবার্তা এলো: *"আগামী ২ মাসে মাঝারি খরার সম্ভাবনা — সেচের পানি সংরক্ষণ করুন।"* রহিম মিয়া আগে থেকেই সেচের ব্যবস্থা করলেন। ফসল বাঁচলো।

> **এই দুই গল্পের পার্থক্যই আমাদের থিসিস:** করিম মিয়ার মতো হাজার কৃষককে রহিম মিয়ার মতো আগাম সতর্ক করা — এটাই আমাদের লক্ষ্য। বাংলাদেশের ৭০% মানুষ কৃষিনির্ভর, আর জলবায়ু পরিবর্তনে খরা ক্রমশ ভয়ংকর।

---

## 😰 সমস্যা: বাংলাদেশে খরা কেন এত কঠিন ধরা?

বাংলাদেশে খরা এক ধোঁকাবাজী করে — এটি **তিন স্তরে** ছড়ায়:

```
🌧️ বৃষ্টি/PET ঘাটতি (Meteorological, SPEI 1–3m)   ← root cause
        ↓ কয়েক সপ্তাহ পর
🌱 মাটির আর্দ্রতা কমে, ফসল ক্ষতিগ্রস্ত (Agricultural, SPEI 3–6m)
        ↓ কয়েক মাস পর
💧 নদী/ভূগর্ভস্থ পানি শুকায় (Hydrological, SPEI 6–24m)
```

কিন্তু আগের সব গবেষণা ছিল অর্ধেক গল্প।

---

## 🔍 Final Research Gap (সৎ, defensible, reviewer-proof)

আমরা বাংলাদেশের খরা গবেষণার একটি নিজস্ব, নির্দিষ্ট gap শনাক্ত করেছি (একটি review-এর পুনরাবৃত্তি নয়):

### Gap ১ — Leakage-মুক্ত validation নেই, persistence baseline-ও নেই
বেশিরভাগ গবেষণা random split বা সাধারণ CV ব্যবহার করে → data leakage → inflated accuracy। আর কেউ-ই **persistence baseline** ("গত মাসের খরা = এই মাসের খরা") দিয়ে প্রমাণ করেনি যে তাদের মডেল আসলে autocorrelation-এর চেয়ে ভালো।

### Gap ২ — খরাকে এক ধরন হিসেবে দেখা হয়েছে (single-type)
আগের কাজগুলো সাধারণত একটি SPEI scale (যেমন ১২m = hydrological) ব্যবহার করে — **meteorological → agricultural → hydrological** propagation-কে আলাদা করে দেখেনি। ফলে কৃষকের জন্য প্রাসঙ্গিক কৃষি-খরা এড়িয়ে যায়।

### Gap ৩ — আসল early-warning forecasting নেই (lead time ≈ ০)
বিদ্যমান "forecasting" গুলো আসলে current-month classification — current মাসের data দিয়ে current মাস বলে, তাই **lead time ≈ ০**। কৃষক আগে জানতে পারে না → early warning অর্থহীন।

### Gap ৪ — short-term early warning ও long-term outlook-এর একত্রিত কাঠামো নেই
কেউ ১–১২ মাসের নির্ভরযোগ্য early warning ও ১০-বছরের climate outlook একসাথে দেয়নি — যা policy-নির্ধারণ ও কৃষি-পরিকল্পনা দুটোরই দরকার।

> **এক বাক্যে gap:** *বাংলাদেশের খরা গবেষণায় এখনো এমন কোনো framework নেই যা leakage-মুক্তভাবে validated, খরার তিন ধরনকে layered করে দেখে, আসল ১–১২ মাসের early warning দেয়, এবং একটি ১০-বছরের outlook সরবরাহ করে।*

---

## 🚀 What We'll Do (আমাদের থিসিসের উদ্দেশ্য)

আমরা একটি **explainable ML framework** তৈরি করব যা:

| # | কী করবে | কীভাবে |
|---|---|---|
| ১ | **Meteorological খরা classification (primary)** | SPEI-3m label, XGBoost/RF/CatBoost ensemble, walk-forward temporal CV + **persistence baseline** |
| ২ | **Agricultural ও Hydrological extension** | SPEI-6m (agri) ও SPEI-12m (hydro, আগের ৯৭.২৮% কাজ) derived layer |
| ৩ | **Short-term early warning (মূল মূল্য)** | lagged-only ML + ARIMA/SARIMA/LSTM, ১/৩/৬/১২-মাস horizon — আসল lead time |
| ৪ | **১০-বছর climate outlook (ভিশন)** | SARIMA/LSTM projection, uncertainty band সহ |
| ৫ | **ব্যাখ্যা** | SHAP — কেন খরা, transparent |
| ৬ | **বিভাগ-ভিত্তিক বিশ্লেষণ** | ৮ বিভাগ, ৩৫ স্টেশন, Taylor diagram, NSE/KGE, Kruskal-Wallis |

### 🏗️ আর্কিটেকচার (এক নজরে)
```
🎯 Primary:    Meteorological Drought (SPEI-3m)         ← থিসিসের মূল প্রশ্ন
📥 Features:   8-scale SPEI lags + climate + BD-specific (multi-scale এখানে)
🔗 Extension:  Agricultural (SPEI-6m) + Hydrological (SPEI-12m)
🔮 Forecast:   1–12 মাস early warning (main value) + 10-বছর outlook (vision)
✅ Validation: walk-forward temporal CV + persistence baseline (leakage-মুক্ত, সৎ)
```

---

## 🏆 প্রত্যাশিত ফলাফল

একটি **বিজ্ঞান-ভিত্তিক, সৎ, কাজে লাগার মতো** খরা ব্যবস্থা, যা বলতে পারবে:

> *"আগামী ২ মাসে রাজশাহী বিভাগে মাঝারি meteorological খরার সম্ভাবনা (confidence X%) — কারণ গত ৩ মাসের বৃষ্টিপাত গড়ের চেয়ে কম ও তাপমাত্রা বেশি। সেচের প্রস্তুতি নেওয়ার পরামর্শ দেওয়া হলো। দীর্ঘমেয়াদে (১০-বছর outlook), উত্তর-পশ্চিম অঞ্চলে খরার প্রবণতা বাড়ছে।"*

**এটাই কৃষকের জীবন, খাদ্য নিরাপত্তা ও নীতি-নির্ধারণে সত্যিকারের পার্থক্য ফেলবে।**

---

## ✨ এক বাক্ষে থিসিস (final pitch)

> *আমরা একটি leakage-মুক্ত, ব্যাখ্যাযোগ্য ML framework তৈরি করছি যা **meteorological খরাকে root cause** হিসেবে শ্রেণিবিন্যাস করে, সেটিকে **agricultural ও hydrological** স্তরে প্রসারিত করে, এবং **১–১২ মাসের নির্ভরযোগ্য early warning** ও **১০-বছরের climate outlook** সরবরাহ করে — বাংলাদেশের ৩৫টি স্টেশনে, ১৯৬১–২০২৩ সময়কালে।*

---
