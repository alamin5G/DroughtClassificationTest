# Guide: Elsevier Journal Submission & Formatting Checklist

This document provides a step-by-step guide to publishing your paper in an Elsevier journal (such as *Journal of Contaminant Hydrology* or *Environmental Modelling & Software*) and reviews the structural readiness of your manuscript file: [Drought_Severity_Classification_Bangladesh.md](file:///home/alamin/Documents/DroughtClassificationTest/Drought_Severity_Classification_Bangladesh.md).

---

## 📑 Part 1: Structural Analysis of Your Manuscript File

Your current `.md` file is highly comprehensive, scientifically detailed, and properly formatted into Introduction, Data & Methods, Results, and References. However, **several mandatory Elsevier sections are currently missing**.

You must add the following sections at the very end of your manuscript (just before the **References** section):

### 1. CRediT Authorship Contribution Statement (Mandatory)

Elsevier requires the CRediT (Contributor Roles Taxonomy) details. Copy and paste this at the end of the paper:

```markdown
## CRediT Authorship Contribution Statement
**Md. Alamin:** Conceptualization, Methodology, Software, Data Curation, Formal Analysis, Writing - Original Draft. **SK Ikhtear Choton:** Validation, Investigation, Visualizations, Writing - Review & Editing. **Md. Alomgir Hossain:** Supervision, Funding Acquisition, Project Administration, Writing - Review & Editing.
```

### 2. Declaration of Competing Interest (Mandatory)

Every Elsevier paper must declare conflicts of interest. Copy and paste this:

```markdown
## Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
```

### 3. Data Availability Statement (Mandatory)

You must declare where your data is. Copy and paste this:

```markdown
## Data Availability
The raw climate data used in this study is sourced from the Bangladesh Meteorological Department (BMD). The processed datasets, trained models, and implementation code developed for the drought pipeline are available upon request to the corresponding author or can be accessed via the repository at [insert link if public].
```

---

## 📝 Part 2: Highlights (Mandatory Separate File)

Elsevier requires a separate **Highlights** file containing **3 to 5 bullet points**. Each bullet point must be **maximum 85 characters including spaces**.

Create a new file named `highlights.docx` or `highlights.txt` containing the following exact bullet points (each is pre-calculated to be under 85 characters):

1. `An explainable 3-model ensemble framework is proposed for drought classification.` (79 chars)
2. `Incorporates 76 features capturing temporal lags and Bangladesh crop seasons.` (77 chars)
3. `Achieves 97.27% accuracy and 99.69% AUC using 5-fold temporal cross-validation.` (80 chars)
4. `SHAP-based explainability identifies key climate drivers of regional droughts.` (78 chars)
5. `Utilizes 63 years of station records to ensure robust early warning capability.` (80 chars)

---

## 📁 Part 3: What Files to Submit

When submitting in the online portal (Elsevier Editorial Manager), upload the following files separately:

1. **Cover Letter** (A brief letter to the Editor-in-Chief introducing your paper and declaring it is not submitted elsewhere).
2. **Title Page** (Containing title, author names, affiliations, and corresponding email).
3. **Manuscript File** (Your text document. Figures/Tables can be embedded inline for the initial review).
4. **Highlights File** (The 3-5 bullet points under 85 characters).
5. **Graphical Abstract File** (The 531 x 1328 pixels image you created in Canva).
6. **High-Resolution Figures** (Separate TIFF/EPS/PDF files for `figure_1_study_area_map.png`, `figure_3_methodology_flowchart.png`, etc., exported at 300 DPI).

### ১. পেপারে যে অংশগুলো যুক্ত করতে হবে (Mandatory Additions)

Elsevier-এর পেপারগুলোতে কিছু নির্দিষ্ট একাডেমিক ডিক্লেয়ারেশন থাকা বাধ্যতামূলক, যা আপনার বর্তমান ড্রাফটে নেই। আপনি পেপারের একদম শেষে (**References** সেকশনের ঠিক ওপরে) এই ৩টি সেকশন কপি-পেস্ট করে দিন:

* **CRediT Authorship Contribution Statement** (কে কোন কাজে অবদান রেখেছেন):
  ```markdown
  ## CRediT Authorship Contribution Statement
  **Md. Alamin:** Conceptualization, Methodology, Software, Data Curation, Formal Analysis, Writing - Original Draft. **SK Ikhtear Choton:** Validation, Investigation, Visualizations, Writing - Review & Editing. **Md. Alomgir Hossain:** Supervision, Funding Acquisition, Project Administration, Writing - Review & Editing.
  ```
* **Declaration of Competing Interest** (স্বার্থের সংঘাতের ঘোষণা):
  ```markdown
  ## Declaration of Competing Interest
  The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
  ```
* **Data Availability Statement** (ডেটার সহজলভ্যতা):
  ```markdown
  ## Data Availability
  The raw climate data used in this study is sourced from the Bangladesh Meteorological Department (BMD). The processed datasets, trained models, and implementation code developed for the V2 pipeline are available upon request to the corresponding author.
  ```

---

### ২. Highlights (আলাদা ফাইলে সাবমিট করতে হবে)

Elsevier-এর নিয়ম অনুযায়ী ৩ থেকে ৫টি বুলেট পয়েন্টের একটি **Highlights** ফাইল দিতে হবে, যার প্রতিটির ক্যারেক্টার লিমিট **সর্বোচ্চ ৮৫ ক্যারেক্টার (স্পেসসহ)** হতে হবে।

আমি আপনার পেপারের রেজাল্ট অনুযায়ী ৫টি বুলেট পয়েন্ট লিখে দিয়েছি (সবগুলোই লিমিটের ভেতরে আছে):

1. `An explainable 3-model ensemble framework is proposed for drought classification.` (৭৯ ক্যারেক্টার)
2. `Incorporates 76 features capturing temporal lags and Bangladesh crop seasons.` (৭৭ ক্যারেক্টার)
3. `Achieves 97.27% accuracy and 99.69% AUC using 5-fold temporal cross-validation.` (৮০ ক্যারেক্টার)
4. `SHAP-based explainability identifies key climate drivers of regional droughts.` (৭৮ ক্যারেক্টার)
5. `Utilizes 63 years of station records to ensure robust early warning capability.` (৮০ ক্যারেক্টার)

---

### ৩. অনলাইন সাবমিশনের ফাইল চেকলিস্ট

সাবমিশন পোর্টালে (Editorial Manager) নিচের ফাইলগুলো আলাদাভাবে আপলোড করতে হবে:

1. **Cover Letter** (সম্পাদককে লেখা চিঠি)
2. **Title Page** (টাইটেল, সব লেখকের নাম, এফিলিয়েশন ও ইমেইলসহ)
3. **Manuscript File** (মূল পেপারের টেক্সট; রিভিউয়ের সুবিধার জন্য ছবি ও টেবিলগুলো লেখার মাঝে ঢুকিয়ে দিতে পারেন)
4. **Highlights** (আলাদা ডক ফাইল)
5. **Graphical Abstract** (ক্যানভা থেকে ডাউনলোড করা ল্যান্ডস্কেপ ইমেজটি)
6. **High-Resolution Figures** (পেপারের সব ইমেজ আলাদাভাবে TIFF/PNG ফরম্যাটে ৩০০ DPI রেজোলিউশনে আপলোড করবেন)

সাবমিশন পোর্টালে কীভাবে ধাপে ধাপে কাজ করবেন তার সম্পূর্ণ গাইডলাইন [SUBMISSION_CHECKLIST_GUIDE.md](file:///home/alamin/Documents/DroughtClassificationTest/SUBMISSION_CHECKLIST_GUIDE.md) ফাইলে দেওয়া আছে। পেপার সাবমিশনের শুভকামনা! কোনো প্রয়োজনে আমাকে জানাতে দ্বিধা করবেন না।

---

## 🚀 Part 4: Step-by-Step Submission Guide

Follow these steps to submit your paper online:

1. **Access the Portal:**
   - Go to the journal homepage and click **"Submit Your Paper"**.
   - Log in or create an account on **Editorial Manager (EM)**.
2. **Start New Submission:**
   - Click **"Submit New Manuscript"**.
   - Select your article type (usually **"Research Paper"** or **"Original Research"**).
3. **Upload Files:**
   - Drag and drop your Title Page, Manuscript, Highlights, Graphical Abstract, Cover Letter, and individual Figure files.
   - Label each file correctly from the dropdown menu (e.g., "Manuscript", "Highlights", "Graphical Abstract", "Figure").
4. **Enter Metadata:**
   - Copy-paste your **Title**, **Abstract**, and **Keywords** from the manuscript.
   - Add all co-authors' names, email addresses, and institutional affiliations.
5. **Declarations & Questions:**
   - Confirm ethical clearances, GenAI usage policies (disclose if GenAI was used for language refining or coding assistance), and competing interests.
6. **Review PDF & Submit:**
   - The system will build a consolidated PDF of your submission.
   - Download the PDF, review it carefully to ensure all figures are clear, tables are formatted correctly, and text has no spelling errors.
   - Click **"Approve Submission"** to send it to the journal editor.
