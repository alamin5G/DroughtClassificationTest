# Designing the Graphical Abstract (Elsevier Specification)

Elsevier journals (like *Journal of Contaminant Hydrology* or similar Earth Science journals) require a **horizontal (landscape) layout** for the Graphical Abstract.

## 📏 Technical Requirements

* **Aspect Ratio:** **1:2.5** (Landscape format)
* **Dimensions:** Minimum **531 x 1328 pixels** (Height x Width). Or proportionally higher (e.g., **1062 x 2656 pixels** for ultra-high resolution).
* **Print Readability:** Must remain fully legible when shrunk to a print size of **5 x 13 cm**.
* **Preferred Formats:** **PDF** (vector graphics, best for scaling), **TIFF** (300 DPI), or **EPS**.

---

## 🎨 Recommended Design Structure (3-Panel Horizontal Layout)

Since the canvas is wide (landscape), your design should flow naturally from **Left to Right** in three clean, vertical panels.

```
+-------------------------------------------------------------------------------------------------------------+
|                                  GRAPHICAL ABSTRACT (1328 x 531 px)                                         |
+-----------------------------------+-----------------------------------+-------------------------------------+
|              PANEL 1              |              PANEL 2              |               PANEL 3               |
|      Input & Dataset (Left)       |      Methodology Flow (Center)    |      Results & Explainability (Right)|
|                                   |                                   |                                     |
|  * 35 Weather Stations Map        |  * PET & SPEI Calculation         |  * Confusion Matrix/ROC Curve       |
|  * 17,868 BMD Monthly Records     |  * 76-Feature Engineering          |  * Ensemble Performance:            |
|  * Historical Climate Variables   |  * XGBoost + RF + CatBoost        |    - 97.27% Accuracy                |
|                                   |  * Optimized Ensemble Model       |    - 99.69% AUC-ROC                 |
|                                   |                                   |  * SHAP Feature Contributions       |
+-----------------------------------+-----------------------------------+-------------------------------------+
```

---

## 📂 Step-by-Step Asset & Content Breakdown

### 📍 Panel 1: Input & Study Area (Left 30% of Width)

* **Objective:** Show *where* the study is conducted and *what* data is used.
* **Visual Asset to Use:**
  - Crop a clean, high-contrast section of **`figure_1_study_area_map.png`** (only the map of Bangladesh with the 35 station dots; remove the coordinates/grid lines to keep it minimal).
* **Supporting Text (Large, clean font):**
  - **Study Area:** Bangladesh (35 Meteorological Stations)
  - **Dataset:** 17,868 Monthly Records (1961–2023)
  - **Inputs:** Rainfall, Temperature, Humidity, Sunshine duration

---

### ⚙️ Panel 2: Methodology (Center 40% of Width)

* **Objective:** Illustrate the core processing and modeling pipeline.
* **Visual Asset to Use:**
  - A simplified, horizontal version of the **Canva flowchart** you just made:
    `Raw Data` $\rightarrow$ `SPEI Index` $\rightarrow$ `76 Features` $\rightarrow$ `Base Classifiers` $\rightarrow$ `Voting Ensemble`
* **Supporting Text/Icons:**
  - **PET Calculation:** Hargreaves-Samani method
  - **SPEI Scales:** 1 to 24 months (Log-logistic fitting)
  - **Models:** Optimized Ensemble (40% XGBoost, 35% Random Forest, 25% CatBoost)
  - **Validation:** 5-Fold Walk-Forward Temporal CV (No data leakage)

---

### 🏆 Panel 3: Key Outcomes & XAI (Right 30% of Width)

* **Objective:** Show the final performance metrics and model interpretability.
* **Visual Assets to Use:**
  - A clean, cropped version of the **Confusion Matrix (`figure_7_v2_confusion_matrix.png`)** OR the **ROC Curve (`figure_6_v2_roc_curve.png`)**.
  - A small, simplified snippet of the **SHAP summary plot (`figure_9_v2_shap_summary.png`)** showing that Rainfall/Temperature are the top drivers.
* **Supporting Text (Bold key numbers!):**
  - **Ensemble Accuracy:** **`97.27%`** (Mean)
  - **AUC-ROC:** **`99.69%`**
  - **Explainability:** SHAP feature attribution identifies key drought triggers.

---

### ১. ক্যানভাস সাইজ (Canva Custom Size)

* ক্যানভাতে নতুন ডিজাইন খোলার সময় **Custom Size** সিলেক্ট করে Width: **2656 px** এবং Height: **1062 px** দিন (এটি Elsevier-এর রিকোয়ারমেন্ট $1328 \times 531$ এর দ্বিগুণ, যা ইমেজ কোয়ালিটি অনেক বাড়িয়ে দেবে এবং ব্লার হবে না)।

---

### ২. প্যানেলভিত্তিক ডিজাইন ম্যাপিং (Flow from Left to Right)

#### **বাম প্যানেল (Panel 1: Input & Dataset - ৩০% জায়গা)**

* **কী ইমেজ দিবেন:** `figure_1_study_area_map.png` (আমাদের স্টেশন ম্যাপটি) থেকে কোঅর্ডিনেট লাইনগুলো বাদ দিয়ে শুধু বাংলাদেশের মানচিত্র এবং ৩৫টি স্টেশনের লাল ডট অংশটুকু ক্রপ করে বসিয়ে দিন।
* **টেক্সট (বড় ফন্টে):**
  - **Study Area:** Bangladesh (35 Meteorological Stations)
  - **Dataset:** 17,868 Monthly Records (1961–2023)
  - **Parameters:** Rainfall, Temperature, Humidity, Sunshine

#### **মাঝের প্যানেল (Panel 2: Methodology - ৪০% জায়গা)**

* **কী ইমেজ দিবেন:** আপনার তৈরি করা ক্যানভা ফ্লোচার্টের একটি খুব সিম্পল এবং অনুভূমিক (Horizontal) ভার্সন এখানে বসান:
  `Raw Data` $\rightarrow$ `SPEI Index` $\rightarrow$ `76 Features` $\rightarrow$ `Base Models` $\rightarrow$ `Voting Ensemble`
* **টেক্সট (পয়েন্ট আকারে):**
  - Hargreaves-Samani PET & Multi-scale SPEI
  - XGBoost (40%) + RF (35%) + CatBoost (25%) Ensemble
  - 5-Fold Walk-Forward Temporal CV (No data leakage)

#### **ডান প্যানেল (Panel 3: Outcomes & Explainability - ৩০% জায়গা)**

* **কী ইমেজ দিবেন:** আমাদের পেপারের কনফিউশন ম্যাট্রিক্স (`figure_7_v2_confusion_matrix.png`) অথবা রোক কার্ভের (`figure_6_v2_roc_curve.png`) একটি ছোট অংশ এবং SHAP Summary Plot-এর টপ ৩/৪টি ফিচারের একটি ক্রপ করা অংশ।
* **হাইলাইট টেক্সট (বড় ও বোল্ড ফন্টে):**
  - **Mean Accuracy:** **`97.27%`**
  - **AUC-ROC:** **`99.69%`**
  - **Explainability:** SHAP feature attribution identifies key drought drivers.

---

### ৩. ফাইল এক্সপোর্ট (Export Guidelines)

* ক্যানভা থেকে ডাউনলোড করার সময় **PDF Print** সিলেক্ট করবেন (এতে ভেক্টর কোয়ালিটি বজায় থাকে)। এরপর সেটাকে Elsevier-এর রিকোয়ারমেন্ট অনুযায়ী সরাসরি PDF হিসেবে আপলোড করতে পারেন অথবা EPS/TIFF-এ কনভার্ট করে নিতে পারেন।

বিস্তারিত সব নির্দেশনার জন্য আপনি ওয়ার্কস্পেসের [GRAPHICAL_ABSTRACT_GUIDE.md](file:///home/alamin/Documents/DroughtClassificationTest/GRAPHICAL_ABSTRACT_GUIDE.md) ফাইলটি চেক করতে পারেন। ক্যানভাতে এটি ড্র করার সময় কোনো টপিক বা ডেটা নিয়ে কনফিউশন থাকলে আমাকে জানাবেন!

## 💡 Top Canva Design Tips for Graphical Abstracts

1. **Start with a Custom Size Template:**
   - In Canva, click "Create a design" $\rightarrow$ **Custom size** $\rightarrow$ Enter Width: **2656**, Height: **1062** pixels (this is exactly $1328 \times 531$ doubled for high-resolution DPI).
2. **Use Minimalist Backgrounds:**
   - Keep the background pure white (`#FFFFFF`) or very light gray (`#F8FAFC`). Do not use dark modes or textured backgrounds for academic abstracts.
3. **Limit Text & Maximize Visuals:**
   - Use large numbers (e.g., **97.27%** in 36pt font).
   - Use icons/diagrams instead of long sentences.
4. **Export as PDF Print:**
   - When downloading from Canva, select **PDF Print** (and check "Flatten PDF" for best vector/raster compatibility). This can be converted to high-DPI TIFF or uploaded directly as PDF as preferred by Elsevier.
