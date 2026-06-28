# 

# Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI. 

# 

# 

Md. Alamin and SK Ikhtear Ahmed Choton

A Thesis in the Partial Fulfillment of the Requirements

for the Award of Bachelor of Computer Science and Engineering (BCSE)

![CSE logo](/home/z/my-project/download/thesis_media/media/image1.jpeg){width="0.6204188538932633in" height="0.612153324584427in"}![Image result for iubat logo](/home/z/my-project/download/thesis_media/media/image2.jpeg){width="0.6865518372703412in" height="0.6865518372703412in"}

Department of Computer Science and Engineering

IUBAT School of Computer Science and Engineering

IUBAT---International University of Business Agriculture and Technology

Spring 2026

# Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI. 

Md. Alamin and SK Ikhtear Ahmed Choton

A Thesis in the Partial Fulfillment of the Requirements for the Award of Bachelor of Computer Science and Engineering (BCSE)

The thesis has been examined and approved,

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Prof. Dr. Utpal Kanti Das

Dean and Chair

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Dr. Md. Rashedul Islam

Co-supervisor, Coordinator and Associate Professor

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Md. Alomgir Hossain

Supervisor and Associate Professor

Department of Computer Science and Engineering

IUBAT School of Computer Science and Engineering

IUBAT---International University of Business Agriculture and Technology

Spring 2026

## **Letter of Transmittal**

2 June 2026

The Chair

Thesis Defense Committee

Department of Computer Science and Engineering

IUBAT School of Computer Science and Engineering

IUBAT---International University of Business Agriculture and Technology

4 Embankment Drive Road, Sector 10, Uttara Model Town

Dhaka 1230, Bangladesh.

**Subject:** [Letter of Transmittal.]{.underline}

Dear Sir,

With due respect, we would like to inform you that it is a great pleasure and a great pleasure for us to submit this report entitled "Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI" to complete my thesis course.It was a great opportunity for me to work on this project to make my theoretical knowledge more realistic and I gained a lot of exposure to the business culture of a famous company. I now look forward to your kind commentary on this performance report. I will always be very grateful to you if you kindly go through this report and check me performance.

Yours Sincerely,

\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Md. Alamin SK Ikhtear Ahmed Choton

ID# 21303134 ID# 21303136

## **Student's Declaration**

We, Md. Alamin and SK Ikhtear Ahmed Choton, are the students of the BCSE-Bachelor of Computer Science and Engineering program, under the College of Engineering and Technology (CEAT) of the International University of Business Agriculture and Technology (IUBAT) announcing, this report entitled 'Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI' has been prepared for the completion of the requirement for the Bachelor of Computer Science and Engineering degree. The report and the project \"Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI\" was edited by us. All modules and procedures for this project are done after proper testing and online information.

It is not designed for other purposes, awards or presentations.

\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Md. Alamin SK Ikhtear Ahmed Choton

ID# 21303134 ID# 21303136

## **Supervisor's Certification**

This is to ensure that the Thesis report on "**Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI**" is compiled by Md. Alamin and SK Ikhtear Ahmed Choton, student of IUBAT-- International University of Business Agriculture and Technology, as part of the fulfillment of the required part of an effective defense course. The report has been prepared under my supervision and is a record of the work accomplished, successfully completed. To the best of my knowledge and as per her declaration, no portions of this report have been posted anywhere by any degree, diploma or certificate.

You are now allowed to submit a report. I wish her every success in her future endeavors.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Md. Alomgir Hossain

Supervisor and Associate Professor

Department of Computer Science and Engineering

IUBAT School of Computer Science and Engineering

IUBAT---International University of Business Agriculture and Technology

## **Abstract**

Bangladesh faces increasing drought vulnerability under climate change which is threatening agricultural and national food security. Existing drought indices lack rigorous temporal validation and multi-scale analysis for reliable early warning. Our study proposes an explainable three-model ensemble framework (XGBoost 40%, Random Forest 35% and CatBoost 25%) for drought classification using multi-scale SPEI across 35 meteorological stations from 1961 to 2023. The framework incorporates 76 engineered features capturing Bangladesh-specific patterns (such as monsoon phases, agricultural seasons and temporal lags) and employs five-fold walk-forward temporal cross-validation to prevent data leakage. The ensemble method achieves 97.27% ± 0.32% accuracy and 99.69% ± 0.14% AUC (2011--2023), outperforming individual models: XGBoost (97.46% accuracy, 99.78% AUC), CatBoost (97.34%, 99.77% AUC) and Random Forest (94.41%, 98.93% AUC). SHAP-based explainability reveals that multi-scale SPEI lag features and monsoon indicators dominate predictions while regional analysis highlights higher vulnerability in north-western Bangladesh. This framework provides the first 63-year temporally validated drought classification system for Bangladesh and achieving a superior performance compared to previous studies. The ensemble SHAP analysis enables explainable operational deployment for agricultural planning and early warning systems. It is providing a scientifically rigorous and operationally ready drought monitoring solution for Bangladesh\'s agricultural vulnerability.

Keywords: Drought classification, Machine learning, SPEI, SHAP explainability, Bangladesh, Temporal validation

## **Acknowledgments**

First and foremost, we express our deepest gratitude to Almighty Allah for granting us the strength, patience, and perseverance to successfully complete this thesis entitled \"Explainable Ensemble Learning for Drought Classification in Bangladesh Using Multi-Scale SPEI.\"

We would like to express our sincere gratitude to Dr. Md. Alomgir Hossain, Associate Professor, Department of CSE, IUBAT, for his invaluable guidance, continuous encouragement, constructive suggestions, and unwavering support throughout every stage of this research. His expertise, insightful feedback, and motivation have greatly contributed to the successful completion of this thesis.

We are also grateful to IUBAT and the Department of CSE for providing an excellent academic environment, necessary resources, and the opportunity to conduct this research. Our sincere appreciation also goes to the honorable Chair, respected faculty members, and the thesis defense committee for their valuable guidance and encouragement throughout our academic journey.

We would like to extend our heartfelt thanks to our parents, family members, friends, and classmates for their constant encouragement, patience, understanding, and moral support. Their motivation and belief in us inspired us to overcome numerous challenges during the course of this research.

Finally, we express our sincere appreciation to everyone who directly or indirectly contributed to the completion of this thesis. We apologize if we have unintentionally omitted the names of anyone whose support and contribution were invaluable. We remain deeply grateful to all who helped make this research possible.

**Table of Contents**

**Letter of Transmittal** [iii](#letter-of-transmittal)

**Student's Declaration** [iv](#students-declaration)

**Supervisor's Certification** [v](#supervisors-certification)

**Abstract** [vi](#abstract)

**Acknowledgments** [vii](#acknowledgments)

**List of Figures** [xi](#list-of-figures)

**List of Tables** [xii](#list-of-tables)

**Chapter 1. Introduction** [1](#chapter-1.-introduction)

1.1 Background [1](#background)

1.2 Overview [2](#overview)

1.3 Motivation [3](#motivation)

1.4 Problem Statement [4](#problem-statement)

1.5 Objectives [4](#objectives)

1.6 Research Questions [5](#research-questions)

1.7 Scope and Limitations [5](#scope-and-limitations)

1.8 Significance of the Research [6](#significance-of-the-research)

1.9 Thesis Outline [7](#thesis-outline)

**Chapter 2. Literature Review** [8](#chapter-2.-literature-review)

2.1 Machine Learning for Drought Classification [11](#machine-learning-for-drought-classification)

2.2 Bangladesh Drought Studies [13](#bangladesh-drought-studies)

**Chapter 3. Research Methodology** [16](#chapter-3.-research-methodology)

3.1 Study Area and Data Collection [16](#study-area-and-data-collection)

3.2 Data Processing and Quality Control [19](#data-processing-and-quality-control)

3.3 PET and SPEI Calculation [20](#pet-and-spei-calculation)

3.4 Feature Engineering [24](#feature-engineering)

3.5 Machine Learning Ensemble [28](#machine-learning-ensemble)

3.6 Temporal Cross-Validation [30](#temporal-cross-validation)

3.7 Explainability Analysis [32](#explainability-analysis)

3.8 Statistical Analysis and Model Evaluation [33](#statistical-analysis-and-model-evaluation)

**Chapter 4. Results and Discussion** [34](#chapter-4.-results-and-discussion)

4.1 Temporal Cross-Validation Performance [34](#temporal-cross-validation-performance)

4.2 Model Comparison and Ensemble Performance [36](#model-comparison-and-ensemble-performance)

4.3 Feature Importance and SHAP Analysis [41](#feature-importance-and-shap-analysis)

4.4 Spatial and Seasonal Patterns [48](#spatial-and-seasonal-patterns)

4.5 Result Comparison [51](#result-comparison)

4.6 Practical Applications [52](#practical-applications)

4.7 Achievement of Research Objectives [52](#achievement-of-research-objectives)

4.8 Study Limitations [53](#study-limitations)

**Chapter 5. Conclusion** [54](#chapter-5.-conclusion)

5.1 Restating the Research Problem and Objectives [54](#restating-the-research-problem-and-objectives)

5.2 Summarizing Key Findings [54](#summarizing-key-findings)

5.3 Highlighting Contributions [55](#highlighting-contributions)

5.4 Discussing Limitations [56](#discussing-limitations)

5.5 Suggesting Future Work [58](#suggesting-future-work)

**References** [60](#references)

## **List of Figures**

**Figure 1:** Study Area Map showing 35 meteorological stations across Bangladesh. [17](#_Toc233543480)

**Figure 2a:** Short-term SPEI Time Series (SPEI-1m) showing immediate weather drought impacts (1961-2023). [22](#_Toc233543481)

**Figure 2d:** Long-term SPEI Time Series (SPEI-12m) showing hydrological drought impacts. [24](#_Toc233543482)

**Figure 2e:** Very Long-term SPEI Time Series (SPEI-12m) showing socio-economic drought impacts. [24](#_Toc233543483)

**Figure 3:** Methodology Flowchart illustrating the complete framework from data processing to ensemble prediction and explainability. [27](#_Toc233543484)

**Figure 4:** Ensemble architecture visualization showing weighted averaging. [29](#_Toc233543485)

**Figure 5:** Temporal Cross-Validation Results showing 5-fold performance with error bars. [35](#_Toc233543486)

**Figure 6:** Model Comparison - AUC scores for all models including ensemble. [38](#_Toc233543487)

**Figure 7:** ROC Curve comparison for all models with ensemble highlighted. [39](#_Toc233543488)

**Figure 8:** Confusion Matrix for ensemble model with performance metrics. [39](#_Toc233543489)

**Figure 9:** Prediction Distribution showing drought vs no-drought probability distributions [40](#_Toc233543490)

**Figure 10:** Performance Metrics Detailed comparison across 3 models and ensemble (XGBoost, Random Forest, CatBoost). [40](#_Toc233543491)

**Figure 11:** Top 20 Most Important Features for Drought Prediction [44](#_Toc233543492)

**Figure 12:** SHAP Summary Plot for Weighted Ensemble Model showing feature impact on drought prediction across 500 test samples. [45](#_Toc233543493)

**Figure 13a:** Agricultural Season Impact on Drought Prediction in Bangladesh (Boro, Aus, Aman seasons). [47](#_Toc233543494)

**Figure 13b:** Monsoon Phase Feature Importance for drought prediction (4-phase analysis). [48](#_Toc233543495)

**Figure 14:** Station-Wise model reliability score heatmap showing across Bangladesh. [49](#_Toc233543496)

## **List of Tables**

Table 2.1 Comparison of Existing Bangladesh Drought Prediction Studies [9](#_Toc233543510)

Table 3.1 Dataset Summary showing total records, spatial coverage, temporal span, engineered features, and data completeness metrics. [19](#_Toc233543511)

Table 3.2 Configuration of the 5-fold walk-forward temporal cross-validation splits. [30](#_Toc233543512)

Table 4.1 Temporal Cross-Validation Detailed Metrics [34](#_Toc233543513)

Table 4.2 Model Performance Comparison [37](#_Toc233543514)

Table 4.3 Feature Importance Rankings (Top 20) with SHAP values and interpretations. [41](#_Toc233543515)

Table 4.4 Regional Drought Vulnerability by division with frequency and severity. [48](#_Toc233543516)

Table 4.5 Comparison with Existing Bangladesh Drought Studies. [51](#_Toc233543517)

## **Chapter 1. Introduction**

Bangladesh is a densely populated South Asian nation with 175.7 million \[1\] residents. They face increasing drought vulnerability due to climate change impacts on its mostly agricultural-dependent economy \[2\]. In Bangladesh, 70% of the population working in agriculture and rice cultivation which covering 75% of arable land, drought events pose and significant threats to food security and economic stability \[3\]. The country has three distinct agricultural seasons---Boro (December-May), Aus (April-August), and Aman (June-December)--- each with have different drought patterns.

#### 1.1 Background

Bangladesh\'s geographical location is in the tropical monsoon zone. The location causes rainfall to vary a lot. About 80% of the annual rainfall during the monsoon season (June-September) and prolonged dry periods from November to April\[4\]. This seasonal concentration creates acute water stress during the dry season, particularly affecting the northwestern districts where annual rainfall can be 30-40% lower than coastal regions \[5\]. The country has flat delta-shaped land with elevations mostly below 10 meters above sea level. This makes it particularly prone to hydrological extremes---floods during monsoons and droughts during dry seasons.

Recent climate analyses indicate raise drought frequency and severity across Bangladesh, along with ith the northwestern region experiencing drought conditions in approximately 35-40% of years during the last two decades \[6\]. Drought is a critical threat to food security in Bangladesh. Particularly in the northwestern and southwestern regions where millions of hectares of cropland and staple crops such as rice are regularly affected. Annual crop losses can extend to several million hectares which significantly reducing rice yields and causing substantial economic losses for smallholder farmers \[7\]. More recently, in the 2018-2019 drought led to significant irrigation water shortages, that affecting Boro rice cultivation---the country\'s primary rice crop contributing to 55% of total rice production. As the drought event occurs frequently so we need reliable drought monitoring and early warning systems to support agricultural planning and water resource management.

Drought impacts in Bangladesh extend well beyond direct agricultural losses; they disrupt rural livelihoods, increase food prices, and threaten national food security. The northwestern and southwestern regions, where a large portion of the rural population depends on rain-fed agriculture, are especially vulnerable to precipitation deficits and climate extremes. Millions in these drought-prone areas regularly face unstable crop yields, water shortages, and heightened risks to their food and economic security \[7\]. Furthermore, groundwater level is lowering due to excessive irrigation during drought periods has created long-term sustainability concerns. We can see the water level in northwestern districts declining at rates of 0.5-1.0 meters per year \[8\].

#### 1.2 Overview

Traditional drought monitoring in Bangladesh relies mostly on single-scale indices like the Standardized Precipitation Index (SPI). Which considers only precipitation without accounting for temperature effects on evapotranspiration \[9\]. As temperatures rise, more water evaporates from land and plants. This can cause droughts even if rainfall is close to normal. So, this problem becomes very serious when the weather gets hotter \[10\]. In the recent studies - demonstrated the superiority of multi-scale SPEI analysis, incorporating precipitation and potential evapotranspiration (PET) for comprehensive drought assessment \[11\]. However, existing Bangladesh drought studies suffer from limited temporal validation, insufficient station coverage, and lack of explainable artificial intelligence (X-AI) integration \[12\].

#### 1.3 Motivation

In previous Bangladesh drought studies, we have found several critical limitations that hamper operational deployment and scientific credibility. First, most studies apply random train-test splits that ignore temporal autocorrelation in climate data. In that case, which is leading to overly optimistic performance estimates that fail to generalize to genuinely unseen future conditions \[\[13\]\]. This methodological weakness particularly affects drought prediction. We know droughts depend heavily on time-based patterns. These include seasons and climate changes over many years. Temporal dependencies are inherently strong due to seasonal patterns and multi-year climate cycles. Second, insufficient SPEI scale coverage remains prevalent. Most studies using only 3--4-time scales instead of the recommended 8 scales. It is necessary to capture drought impacts ranging from meteorological (1-3 months) to socio-economic (18-24 months) time frames \[14\].

Third, lack of Bangladesh-specific feature engineering - represents a missed opportunity to incorporate domain knowledge about monsoon dynamics and agricultural calendars for Bangladesh that strongly influence drought impacts in the region \[12\]. Existing studies typically uses normal climate variables without considering monsoon timing, pre-monsoon heat stress or critical crop growth time specific to Bangladesh\'s rice-based agricultural system. Fourth, absence of explainable artificial intelligence (X-AI) method, it limits the operational uses of developed models. As stakeholders and policymakers wants transparent and interpretable predictions to support decision-making processes \[15\]. Without understanding that which factors have impacts on drought predictions - it remains challenging to translate model outputs into actionable agricultural advisories.

#### 1.4 Problem Statement

Most Bangladesh drought studies use random train-test splits, resulting in temporal data leakage and overly optimistic performance estimates. Existing studies employ only 3--4 SPEI time scales instead of comprehensive multi-scale analysis. Bangladesh-specific monsoon and agricultural characteristics are rarely incorporated into feature engineering. Existing machine learning models lack explainable AI techniques, limiting their practical use for policymakers and agricultural planning. Therefore, there is a need for an explainable, temporally validated, and Bangladesh-specific drought classification framework.

#### 1.5 Objectives

Develop an explainable ensemble machine learning framework for accurate meteorological drought classification in Bangladesh using multi-scale SPEI and temporal validation.

I.  Develop a three-model ensemble framework using XGBoost, Random Forest and CatBoost.

II. Implement five-fold walk-forward temporal cross-validation using historical climate data.

III. Construct Bangladesh-specific feature engineering based on monsoon phases and agricultural seasons.

IV. Apply SHAP for explainable drought prediction.

V.  Compare the proposed framework with previous Bangladesh drought studies.

#### 1.6 Research Questions

RQ1. Can an ensemble machine learning framework improve drought classification accuracy using multi-scale SPEI?

RQ2. Does walk-forward temporal cross-validation provide more reliable model evaluation than conventional validation approaches?

RQ3. How do Bangladesh-specific monsoon and agricultural features influence drought classification performance?

RQ4. Which climatic variables contribute most to drought prediction according to SHAP explainability?

RQ5. How does the proposed framework compare with existing Bangladesh drought studies?

#### 1.7 Scope and Limitations

This study focuses on meteorological drought assessment in Bangladesh using data collected from 35 meteorological stations over the period 1961--2023. The analysis is based on multi-scale Standardized Precipitation Evapotranspiration Index (SPEI) to capture drought variability across different temporal scales. Machine learning models, including XGBoost, Random Forest, and CatBoost, are employed to develop a robust classification framework. Model evaluation is conducted using five-fold walk-forward temporal cross-validation to ensure realistic performance assessment. Additionally, SHAP (SHapley Additive exPlanations) is utilized to provide interpretability and explainability of the model predictions.

This study is limited to meteorological drought and does not consider hydrological or agricultural drought conditions. The analysis does not incorporate satellite imagery or soil moisture data, which may provide additional insights into drought dynamics. The proposed framework relies solely on historical meteorological observations, which may not fully capture future climate variability. Furthermore, real-time operational deployment of the model is beyond the scope of this research.

#### 1.8 Significance of the Research

This study contributes to both academic research and practical applications in the field of drought prediction and climate analysis in Bangladesh.

This research introduces a walk-forward temporal validation approach for drought classification in Bangladesh, addressing the limitations of conventional random data splitting methods. It also incorporates Bangladesh-specific feature engineering based on monsoon patterns and agricultural seasons, which enhances the contextual relevance of the model. Furthermore, the study demonstrates the effectiveness of explainable ensemble machine learning techniques using SHAP, contributing to the growing field of explainable artificial intelligence in environmental studies.

The proposed framework has significant practical implications for agricultural planning and irrigation management by providing more reliable drought predictions. It can improve drought early warning systems, enabling timely decision-making for farmers and stakeholders. Additionally, the findings of this study can assist policymakers in developing effective climate adaptation strategies and managing water resources more efficiently.

This study develops an explainable ensemble machine learning framework for drought classification using multi-scale SPEI and Bangladesh-specific climate features. It provides a comprehensive evaluation of model performance under temporal validation, ensuring more realistic and reliable results. The integration of explainability through SHAP further enhances the transparency and usability of the proposed model.

#### 1.9 Thesis Outline

Chapter 1 introduces the research background, motivation, objectives, research questions, scope, significance, and overall organization of the thesis.

Chapter 2 reviews the existing literature on drought monitoring, SPEI, machine learning, explainable artificial intelligence, and previous Bangladesh drought studies.

Chapter 3 describes the research methodology, including data collection, preprocessing, SPEI calculation, feature engineering, machine learning models, temporal cross-validation, ensemble learning, SHAP analysis, and evaluation metrics.

Chapter 4 presents the experimental results, comparative analysis, model evaluation, explainability analysis, and discussion of the findings.

Chapter 5 summarizes the research, highlights the major contributions, discusses limitations, and provides recommendations for future research.

.

## **Chapter 2. Literature Review**

Drought monitoring has been developed significantly from simple precipitation-based indices to comprehensive multi-variable approaches such as incorporating temperature, evapotranspiration and soil moisture \[16\]. The Standardized Precipitation Evapotranspiration Index (SPEI) was introduced by Vicente-Serrano et al. \[10\] that is representing a major advancement by combining precipitation and potential evapotranspiration into a single standardized measure. SPEI\'s multi-scale capability helps to simultaneous monitoring of meteorological (1-3 months), agricultural (3-6 months), hydrological (6-12 months) and socio-economic (12-24 months) drought conditions. That is making it particularly suitable for comprehensive drought assessment \[17\].

International applications of SPEI have demonstrated its better quality over precipitation-only indices; particularly in regions that experiencing rising temperatures increase evaporative demand over time \[18\]. Studies in semi-arid regions of Spain, Australia, and China have shown that SPEI helps earlier drought detection and better correlation with agricultural impacts compared to SPI \[19\], \[20\], \[21\]. The multi-scale nature of SPEI allow stakeholders to assess drought conditions relevant to their specific needs such as farmers are focusing on 3-6 month scales for crop planning, water resource managers monitoring 9-12 month scales for reservoir management and policymakers tracking 12-24 month scales for long-term planning.

Recent AI studies that explain model behavior show something is important or considered while they make prediction. SPEI features at different time scales are very useful for predicting droughts. Research in Turkey using SHAP analysis on 4 meteorological stations showed that lagged SPEI-12 values are the primary features of predictive accuracy. It clearly shows that CatBoost achieving R² is up to 0.86 \[22\]. Similarly, another study in China combining XGBoost and SHAP on 61+ years of gridded data revealed that diurnal temperature range (DTR) is a powerful negative driver of short-term drought, which is operating via dual pathways with significant regional variability \[23\]. These findings highlights the importance of both multi-scale temporal indices and temperature-related features for comprehensive drought assessment. On the other hand, in semi-arid regions of Morocco\'s Upper Drâa Basin, ensemble tree-based methods for predicting 3 and 12-month SPEI which achieved high performance (NSE: 0.83--0.93, R²: 0.92--0.93), showing the effectiveness of multi-scale SPEI for an operational drought prediction in data-constrained environments \[24\].

[]{#_Toc233543510 .anchor}Table 2.1 Comparison of Existing Bangladesh Drought Prediction Studies

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Study                            Summary                                                                                                                                                                                                                                                                         Major Limitation
  -------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------
  Rahman and Lateh (2016) \[40\]   Region: Bangladesh; Period: 1980--2015; Data: 35 meteorological stations; Method: SPI, GIS and rainfall analysis; Validation: Statistical analysis; Performance: Drought hazard mapping.                                                                                        Conventional drought assessment without machine learning or explainable analysis.

  Mashuq et al. (2024) \[11\]      Region: Ishwardi, Bangladesh; Period: 1981--2017; Data: Single station; Method: XGBoost using multi-scale SPEI; Validation: Random train-test split; Performance: NSE = 0.92 (SPEI-1).                                                                                          Limited to one station, only four SPEI scales, and no temporal validation.

  Paul et al. (2024) \[13\]        Region: Bangladesh; Data: Satellite data (38 districts); Method: Ensemble machine learning; Validation: Cross-validation; Performance: 92% Accuracy.                                                                                                                            No temporal ordering and possible data leakage.

  Hossain et al. (2024) \[14\]     Region: Bangladesh; Period: 1981--2018; Data: SPI-based climate data; Method: Machine learning forecasting; Validation: Hold-out validation; Performance: RMSE = 1.17.                                                                                                          Forecast-oriented study with limited validation strategy.

  Hossain et al. (2025) \[15\]     Region: Southwestern Bangladesh; Data: Four districts; Method: PROPHET + SARIMA; Validation: Time-series forecasting; Performance: R² = 0.75--0.88.                                                                                                                             Forecasting only; not a drought classification framework.

  Hossain et al. (2025) \[41\]     Region: Central Bangladesh; Method: Ensemble ML (RF, XGBoost, SVM); Validation: Random validation; Performance: 93.8--94.0% Accuracy.                                                                                                                                           No explainable AI and no temporal validation.

  Proposed Study                   Region: Bangladesh; Period: 1961--2023; Data: 35 meteorological stations; Method: Weighted Ensemble (XGBoost + Random Forest + CatBoost) with multi-scale SPEI and SHAP; Validation: 5-fold walk-forward temporal cross-validation; Performance: 97.27% Accuracy, 99.69% AUC.   Addresses previous limitations through temporal validation, Bangladesh-specific feature engineering, explainable AI (SHAP), and ensemble learning.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### 2.1 Machine Learning for Drought Classification 

Machine learning method have gained a good coverage in drought classification due to their ability to capture complex nonlinear relationships between climate variables and drought occurrence \[25\]. Ensemble methods, particularly the based ML models such as Random Forest, XGBoost, and gradient boosting variants have been showing their high performance compared to traditional statistical approaches. These models are achieving accuracies exceeding 90% in various regional studies \[25\], \[26\], \[27\], \[28\]. The ensemble paradigm combines multiple base models to improve predictions\' robustness and reduce overfitting. That is why making it particularly suitable for climate applications where training data may be limited and feature relationships complex.

Machine learning models are often called "black boxes" because it's hard to understand how they work. In recent progress in explainable AI helps to solve the \"black box\" criticism of machine learning models. SHAP analysis is now a popular way to explain model decisions, especially in climate science \[29\]. SHAP provides both global feature importance rankings and individual prediction explanations which is allows stakeholders to understand how the model decide; not just what the model predicts. This transparency is important for building trust in operational deployment and identifying potential model weaknesses or biases. A comprehensive study for the United States using county-level drought impacts demonstrated that XGBoost combined with SHAP analysis. Which is achieved F2 scores of 0.88 nationally, with lagged SPI/STI indices dominating impact prediction \[30\].

Deep learning approaches including LSTM networks and CNN architectures have shown their promise for drought forecasting in data-rich environments \[31\], \[32\], \[33\],\[34\]. However, these methods typically need extensive training data and computational resources. This makes it hard to use in developing countries. In those places, there may not be enough data available. So, the method may not work well in those situations. A hybrid CNN-based study for long-term drought severity forecasting in Upper Egypt showed that the CNN-LSTM excelled in training while CNN-SVR performed best in testing that highlighting the effectiveness of deep learning integration for drought management \[35\]. In China\'s Huaihe River Basin, Deep Belief Networks (DBNs) consistently better than traditional BP neural networks for short-term drought prediction especially as SPI timescale increased \[36\]. In Indonesia for regional applications, adaptive neuro-fuzzy inference systems (ANFIS) have shown promise that dramatically lowering RMSE (to 0.016--0.017) by incorporating local meteorological parameters \[37\]. Furthermore, deep learning models often sacrifice interpretability for performance. That is why it making them less suitable for operational systems. Because it requires transparent decision-making processes. A global IoT-fog-cloud architecture uses DNN and achieved 95.36% accuracy for drought assessment. Although the computational requirements remain challenging for resource-constrained environments \[38\].

#### 2.2 Bangladesh Drought Studies 

Bangladesh drought research has progressed from descriptive climatological studies to predictive machine learning applications over the past decade. Pioneering work identifying meteorological drought-prone areas in Bangladesh applied the Standardized Precipitation Index (SPI) across multiple time scales and seasons using GIS-based spatial mapping \[2\]\[39\]. Using SPI-3, SPI-4, and SPI-5 grids from historical data (1980--2015) across 35 meteorological stations, researchers identified persistent drought-prone regions in northwest, central, and southern-western Bangladesh with actionable differentiation between short-term meteorological droughts and prolonged seasonal dryness \[2\]\[39\]. These climatological studies demonstrated that the Pre-Kharif and Rabi seasons are most vulnerable to meteorological drought, with Rabi season showing an increasing drought trend of 8.66% per decade \[2\], establishing the foundation for transitioning toward machine learning-based drought classification and forecasting in more recent Bangladesh drought research.

Time series forecasting methods have been applied to southwestern Bangladesh drought prediction with PROPHET and SARIMA models which is achieving a strong predictive power (R²: 0.75--0.88) across four districts \[15\]. These approaches provide early warning with actionable lead time for local policymakers. Although they focus on forecasting rather than classification. District-level SPI analysis using Facebook Prophet for moderate drought occurrences in Dinajpur demonstrated moderate accuracy (RMSE 1.17) but highlighted the importance of long-term planning for drought-vulnerable regions \[14\]. En-Nagre et al. \[24\] showed the potential of combining SPEI with machine learning algorithms (Random Forest, Voting Regressor, AdaBoost, and KNN) for meteorological drought prediction in the semi-arid Upper Draa Basin of Morocco. Their models achieved high predictive performance (R² up to 0.97 and NSE up to 0.93 for SPEI-3). However, the study relied on a simple 80/20 split without temporal cross-validation, and it did not include explain ability or feature-importance analysis.

More recently, Khan et al. \[11\] conducted SPEI-based drought prediction using XGBoost across **a** single station (Ishwardi Upazila) from 1981--2017 which result in NSE up to 0.92 (for SPEI-1) rather than 88.7% accuracy . This study advanced Bangladesh drought research by demonstrating the superiority of gradient boosting methods. But only apply random split validation and limited to SPEI scale coverage (only 4 scales: SPEI-1, 3, 6, and 12).

An advanced study examining Ishwardi Upazila evaluated SVM, RF, XGBoost, DT, and KNN on SPEI drought indices along with XGBoost. Amongst them XGBoost performed best for SPEI-1 (NSE = 0.92), and RF performed best for SPEI-3 (NSE = 0.24), not RMSE 0.11--0.18 or NSE up to 0.89 . This result emphasizing the value of ML models for accurately capturing rapid local droughts in the Bangladeshi context \[11\]. Chowdhury et al. \[13\] applied satellite data for enhanced drought analysis which shows increases result achieving 92% accuracy than other studies through an ensemble machine learning approach across 38 districts . Similarly, satellite-driven weather data for 38 Bangladesh districts using clustering and classification models. They shown Random Forest achieving 92% accuracy with actionable drought hotspot identification. While representing significant progress these studies used cross-validation without temporal ordering; It might potentially leading to data leakage. Recent ensemble learning approaches have demonstrated higher performance for Bangladesh drought applications. In Central Bangladesh, ensemble ML methods (RF, XGBoost, SVM) combined with ARIMA for long-range predictions using SPI, SPEI, and ZSI indices revealed Random Forest providing the best accuracy (93.8%--94.0%). Spatial mapping highlighting the drought hotspots for targeted policy responses \[40\]. In Rajshahi, multiple ML models (Gradient Boosting, XGBoost, RF, CatBoost, hybrids) on SPEI-linked weather data (1965--2022) achieved single-model accuracy of 85%--88% and ensemble accuracy of 92%--96%, which is proving ensemble ML as a blueprint for future-ready drought anticipation \[41\]. The most recent comprehensive review by Hasan et al. \[12\] clarified the drought modeling techniques across the South Asian countries. The study identified key gaps including insufficient temporal validation, limited integration of regional climate features, and absence of explainability methods. A systematic review of 142 studies documented dominant use of SPI/SPEI and supervised/ensemble ML/DL methods. But the study noted regional data gaps and lack of explainability of prediction and called for integration with XAI-driven models for next-generation drought modeling \[12\]. In the studies of Ahmed et al. \[14\] achieved 88.7% accuracy for drought prediction in eastern Bangladesh but they work with only 38 years (1981--2018) with limited feature engineering beyond basic climate variables. These studies collectively demonstrate growing sophistication in Bangladesh drought researches while highlighting persistent methodological gaps that our study addresses.

## **Chapter 3. Research Methodology**

This chapter describes the research methodology adopted in this study. It presents the study area, data collection process, data preprocessing, feature engineering, proposed ensemble learning framework, temporal cross-validation strategy, SHAP-based explainability, and evaluation metrics used to assess the performance of the proposed model.

#### 3.1 Study Area and Data Collection

Geographic Coverage: Bangladesh (20.7°-26.6°N, 88.0°-92.7°E) encompasses 35 meteorological stations across 8 administrative divisions. This is providing comprehensive spatial coverage from coastal regions to inland areas (Figure 1).

![](/home/z/my-project/download/thesis_media/media/image3.png){width="6.25in" height="5.2340277777777775in"}

[]{#_Toc233543480 .anchor}**Figure 1:** Study Area Map showing 35 meteorological stations across Bangladesh.

**Data Source:** Meteorological data from the Bangladesh Meteorological Department (BMD) was obtained from the Mendeley repository (<https://data.mendeley.com/datasets/tbrhznpwg9/1>) which has daily measurements of precipitation, temperature, humidity, and sunshine hours.

**Temporal Coverage:** Data spans 1961-2023 (63 years), providing 17,868 monthly observations. Although Bangladesh gained independence in 1971 but we utilized pre-independence data as the BMD maintained continuous operations of the same station network throughout this period that is ensuring data continuity and maximizing temporal coverage for robust model training.

**Data Quality:** The dataset exhibits 67.5% coverage across all stations and time periods which is typical for long-term meteorological datasets in developing countries. Missing data primarily occurred due to station establishment at different time periods. Most stations achieving full coverage from 1990 onwards.

To assess data reliability and model validity for the recent modern period we compared our SPEI-12m drought classifications against documented drought events in Bangladesh during 2000--2023. Published research has documented significant meteorological drought occurrences during this period. That's including the severe droughts in northwestern Bangladesh reported for 1973, 1978, 1979, 1981, 1982, 1992, 1994--1995, and 2000 \[4\]. Another drought events during 2009--2010 affecting agricultural production were documented in both studies \[11\], \[14\]---with the SPICSCON study identifying SPEI-based drought occurrences in 2009 and 2010, and the AWM study confirming SPI-detected drought years including 2010. In the pre-monsoon drought period affecting Aus crop cultivation \[42\] and in the 2018--2019 drought episodes in northern regions \[43\], independently reported drought impacts provide additional validation points. Our SPEI-based drought detection algorithm identified all eight documented major drought years (2000, 2006, 2009, 2010, 2013, 2014, 2018, 2019). That have been reported in government assessments and peer-reviewed literature which achieving strong concordance (8/8 events detected) with independently documented drought occurrences. This validation provides confidence in data quality and model reliability particularly for the recent period (2000-2023). While historical period data (1961-1999) shows moderate reliability with some limitations due to sparser station coverage during that era.

Notably our data correctly identified the 1974 Bangladesh Famine period as experiencing above-normal rainfall rather than meteorological drought which is confirming that this famine was primarily caused by widespread flooding rather than drought conditions. Which underscores the critical distinction between socio-economic famine events and meteorological drought phenomena. This validation approach ensures that our reported model performance metrics (97.27% ± 0.32% accuracy) are based on the most reliable portion of the dataset with external verification against published drought documentation.

#### 3.2 Data Processing and Quality Control

**Daily to Monthly Aggregation:** Daily weather data were sum up into monthly totals for precipitation and mean for temperature, humidity, and sunshine. Monthly aggregation reduces noise while preserving seasonal patterns which is essential for drought analysis. Months with no available daily observations were excluded from the analysis which is resulting in a dataset with 95.3% completeness across all station-month combinations.

Missing Data Handling: During feature engineering and model training the missing values in the feature matrices (primarily due to insufficient historical data for lag feature calculation) were imputed using simple mean imputation. Specifically, the missing values in the training features were filled with the mean of the corresponding feature across all available training samples. And the same training-derived mean were applied to test features to prevent the data leakage. This approach maintains complete feature sets - which is required for ensemble model training while preserving the temporal validation framework.

[]{#_Toc233543511 .anchor}Table 3.1 Dataset Summary showing total records, spatial coverage, temporal span, engineered features, and data completeness metrics.

  -----------------------------------------------------------------------
  Metric                             Value
  ---------------------------------- ------------------------------------
  Total Records                      17,868

  Stations                           35

  Years Coverage                     1961-2023

  Total Features                     76

  SPEI Lag Features                  20 (All 8 SPEI scales)

  Data Completeness                  95.30%
  -----------------------------------------------------------------------

#### 3.3 PET and SPEI Calculation

Potential Evapotranspiration (PET): Calculated using the Hargreaves-Samani method \[44\], \[45, p. 56\] following FAO-56 standard, which requires only temperature data and is suitable for Bangladesh\'s data availability:

> $$\begin{array}{r}
> PET = 0.0023 \times 0.408\  \times \ R_{a} \times \left( T_{mean} + 17.8 \right) \times \sqrt{T_{\max} - T_{\min}}\ \mathbf{\#}(1)
> \end{array}$$

Where,

$\left( \text{PET} \right)$= Potential evapotranspiration $\left( mm\ day(^{- 1} \right)$

$\left( T_{\text{mean}} \right)$ = Mean daily temperature (°C)

$\left( T_{\text{max}} \right)$ = Maximum daily temperature (°C)

$\left( T_{\text{min}} \right)$ = Minimum daily temperature (°C)

$\left( R_{a} \right)$ = Extraterrestrial radiation $MJ\ \left( m^{- 2} \right)\ \left( day^{- 1} \right)$ ,

calculated as:

> $$\begin{array}{r}
> R_{a} = \frac{24\  \times \ 60}{\pi} \times G_{sc} \times d_{r} \times \left\lbrack \omega_{s}\sin(\varphi)\sin{(\delta) + \cos{(\varphi)\cos{(\delta)\sin\left( \omega_{s} \right)}}} \right\rbrack\ \#(2)
> \end{array}$$

Where,

$G_{sc}$= Solar constant (0.0820 MJ $m^{- 2}\min^{- 1}$)

$d_{r}$= Inverse relative distance Earth--Sun

$\omega_{s}$= Sunset hour angle (radians)

$\varphi$= Latitude (radians)

$\delta$= Solar declination (radians)

Multi-Scale SPEI Calculation: The Standardized Precipitation Evapotranspiration Index (SPEI) was computed for multiple time scales\
(k=1,2,3,6,9,12,18,24k = 1, 2, 3, 6, 9, 12, 18, 24k=1,2,3,6,9,12,18,24 months) using the log-logistic probability distribution fitting method (Vicente-Serrano et al., 2010).

Step 1: Climatic Water Balance

> $$\begin{array}{r}
> D_{i}^{k} = \sum_{j = i - k + 1}^{i}{(P_{j} - {PET}_{j}}\ \#(3)
> \end{array}$$

Where, $D_{i}^{k}$ = accumulated difference between precipitation $(\mathbf{P})\ $and potential evapotranspiration $(\mathbf{PET})$ for the past $\mathbf{k}$ months. This accumulation process (Equation 3) was applied identically to all 8-time scales (k = 1, 2, 3, 6, 9, 12, 18, 24 months), yielding 8 SPEI time series per station.

Step 2: Log-Logistic Distribution

> $$\begin{array}{r}
> F(x) = \left\lbrack 1 + \left( \frac{\alpha}{x - \gamma} \right)^{\beta} \right\rbrack^{- 1}\ \#(4)
> \end{array}$$

Where, $\alpha,\ \beta\ and\ \gamma$ are the **scale**, **shape**, and **location** parameters, respectively, estimated using the **L-moments** method.

Step 3: Standardized SPEI Calculation

> $$\begin{array}{r}
> SPEI = W - \ \frac{C_{0} + C_{1}W + C_{2}W^{2}}{1 + d_{1}W + d_{2}W^{2} + d_{3}W^{3}}\ \#(5)
> \end{array}$$

Where $W = \ \sqrt{- 2\ln(P)}for\ P \leq 0.5,\ and\ C_{0}{,\ C}_{1,}\ C_{2,}\ d_{1},\ d_{2,\ }d_{3}$ are constant for the standard normal distribution approximation.

Drought Classification: Binary drought classification was based on SPEI-12 values:

> $$\begin{array}{r}
> Drought = \ \left\{ \begin{array}{r}
> 1,\ \ if\ {SPEI}_{12m} < \  - 0.5\ (moderate\ drought) \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise\ (no\ drought)\ 
> \end{array} \right.\ \ \#(6)
> \end{array}$$

Following World Meteorological Organization standards for drought severity classification \[46\]

![](/home/z/my-project/download/thesis_media/media/image4.png){width="6.25in" height="3.0930555555555554in"}

[]{#_Toc233543481 .anchor}**Figure 2a:** Short-term SPEI Time Series (SPEI-1m) showing immediate weather drought impacts (1961-2023).

![](/home/z/my-project/download/thesis_media/media/image5.png){width="6.25in" height="3.0930555555555554in"}**Figure 2b:** Medium-term SPEI Time Series (SPEI-3m) showing agricultural drought impacts affecting crop growth.

![](/home/z/my-project/download/thesis_media/media/image6.png){width="6.25in" height="3.0930555555555554in"}**Figure 2c:** Medium-term SPEI Time Series (SPEI-6m) showing agricultural drought impacts on water resources.

![](/home/z/my-project/download/thesis_media/media/image7.png){width="6.25in" height="3.0930555555555554in"}

[]{#_Toc233543482 .anchor}**Figure 2d:** Long-term SPEI Time Series (SPEI-12m) showing hydrological drought impacts.

![](/home/z/my-project/download/thesis_media/media/image8.png){width="6.25in" height="3.0930555555555554in"}

[]{#_Toc233543483 .anchor}**Figure 2e:** Very Long-term SPEI Time Series (SPEI-12m) showing socio-economic drought impacts.

#### 3.4 Feature Engineering

Total Features: 76 features across 6 categories

Base Climate Features (8): Rainfall_Total, Temperature_Mean, Max_Temperature, Min_Temperature, Humidity_Mean, PET_mm_month, Water_Balance, Ra_MJ_m2_day

Spatial Features (6): Latitude, Longitude, Lat_normalized, Lon_normalized, Distance_to_Bay, Station_encoded

SPEI Lag Features (20): Historical SPEI values were used with planned time delays across all 8 scales to avoid data leakage and track drought over time.

Feature design: SPEI-1m (lags: 1,3,6,12 months), SPEI-3m (lags: 1,3,6,12), SPEI-6m (lags: 1,3,6,12), SPEI-9m (lags: 3,6), SPEI-12m (lags: 1,3), SPEI-18m (lags: 1,3), SPEI-24m (lags: 1,3). Total: 4+4+4+2+2+2+2 = 20 SPEI lag features that are enabling the model to learn from short-term, medium-term and long-term historical drought patterns.

Temporal Features (18): Seasonal decomposition components (6 features): Rainfall_trend, Rainfall_seasonal, Rainfall_residual, Temp_trend, Temp_seasonal, Temp_residual using additive model:

> $$\begin{array}{r}
> X_{t} = T_{t} + S_{t} + R_{t}\ \#(7)
> \end{array}$$

where ​$\mathbf{X}_{\mathbf{t}}$ = observed value, $\mathbf{T}_{\mathbf{t}}$​ = trend component, $\mathbf{S}_{\mathbf{t}}$ = seasonal component, and $\mathbf{R}_{\mathbf{t}}$= residual component.

Fourier features for cyclic patterns (6 features): sin_month_12, cos_month_12, sin_month_6, cos_month_6, sin_month_3, cos_month_3:

> $$\begin{array}{r}
> F_{\sin}(t,\ k) = \sin\left( \frac{2\pi t}{k} \right),\ F_{\cos}(t,\ k) = \cos\left( \frac{2\pi t}{k} \right)\ \#(8)
> \end{array}$$

*Where,* $k\  \in \ \left\{ 3,\ 6,\ 12 \right\}\ $months for quarterly, semi-annual, and annual cycles.

Advanced Bangladesh-specific temporal features (6 features): monsoon_onset, pre_monsoon_heat, critical_crop_month, rainfall_deficit_cumul, months_since_heavy_rain, Year_normalized

Rolling Statistics (16): Moving window statistics for temporal smoothing:

> $$\begin{array}{r}
> \mu_{w}(t) = \frac{1}{w} \times \sum_{i = 0}^{w - 1}X_{t - i}\ \#(9)
> \end{array}$$

$$\begin{array}{r}
\sigma_{w}(t) = \ \sqrt{\frac{1}{w} \times \sum_{i = 0}^{w - 1}\left( X_{t - i} - \mu_{w} \right)^{2}}\ \#(10)
\end{array}$$

*Where,* $w\  \in \ \left\{ 3,\ 6,\ 12 \right\}\ months\ window\ size,$ calculated for rainfall and temperature (3-month: 6 features, 6-month: 6 features, 12-month: 4 features) and PET (3-month: 2 features, 6-month: 2 features).

**Total:** 6+6+4=16 rolling statistics features capturing temporal dynamics at multiple scales.

Bangladesh-Specific Features (8): Monsoon Phase Indicators Using Temporal Windows (4 Features)

> $$\begin{array}{r}
> {Phase}_{dry} = \left\{ \begin{array}{r}
> 1,\ \ \ if\ month\  \in \left\{ 12,\ 1,\ 2 \right\} \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise\ 
> \end{array} \right.\ \ \#(11)
> \end{array}$$
>
> $$\begin{array}{r}
> {Phase}_{pre} = \ \left\{ \begin{array}{r}
> 1,\ \ \ if\ month\  \in \left\{ 3,\ 4,\ 5 \right\} \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise
> \end{array} \right.\ \ \#(12)
> \end{array}$$
>
> $$\begin{array}{r}
> {Phase}_{peak} = \ \left\{ \begin{array}{r}
> 1,\ \ \ if\ month\  \in \left\{ 6,\ 7,\ 8,\ 9 \right\} \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise
> \end{array} \right.\ \ \#(13)
> \end{array}$$
>
> $$\begin{array}{r}
> {Phase}_{post} = \ \left\{ \begin{array}{r}
> 1,\ \ \ if\ month\  \in \left\{ 10,\ 11 \right\} \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise
> \end{array} \right.\ \ \#(14)
> \end{array}$$

Agricultural Season Indicators Aligned with Bangladesh Rice Cropping Calendar (3 Features)

> $$\begin{array}{r}
> {Season}_{Boro} = \ \left\{ \begin{array}{r}
> 1,\ \ \ if\ month\  \in \left\{ 12,\ 1,\ 2,\ 3,\ 4,\ 5 \right\} \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise
> \end{array} \right.\ \ \#(15)
> \end{array}$$
>
> $$\begin{array}{r}
> {Season}_{Aus} = \ \left\{ \begin{array}{r}
> 1,\ \ \ if\ month\  \in \left\{ 4,5,\ 6,\ 7,\ 8 \right\} \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise
> \end{array} \right.\ \ \#(16)
> \end{array}$$
>
> $$\begin{array}{r}
> {Season}_{Boro} = \ \left\{ \begin{array}{r}
> 1,\ \ \ if\ month\  \in \left\{ 6,\ 7,\ 8,\ 9,\ 10,\ 11 \right\} \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise
> \end{array} \right.\ \ \#(17)
> \end{array}$$

Monsoon intensity indicator (1 feature): Is_Monsoon = Phase_peak (derived from peak monsoon phase)

Data Leakage Prevention: To ensure valid temporal prediction features derived from target time scale were excluded:

> $$\begin{array}{r}
> Excluded\ Feature = \ \left\{ {SPEI}_{6m},\ {SPEI}_{12m},{Drought_{Class}}_{*} \right\}\ \#(18)
> \end{array}$$
>
> $$\begin{array}{r}
> Safe\ Features = \left\{ {SPEI}_{1m},\ {SPEI}_{2m},{SPEI}_{3m} \right\}\ with\ temporal\ lags\ \mathrm{\Delta}t\  \geq 3\ months\ \#(19)
> \end{array}$$
>
> $\ $![](/home/z/my-project/download/thesis_media/media/image9.png){width="6.01415135608049in" height="4.058883420822397in"}

[]{#_Toc233543484 .anchor}**Figure 3:** Methodology Flowchart illustrating the complete framework from data processing to ensemble prediction and explainability.

#### 3.5 Machine Learning Ensemble

Base Models: Three high-performance machine learning algorithms were selected based on their complementary strengths and proven effectiveness in drought classification:

-   **XGBoost:** Gradient boosting decision trees with optimized hyperparameters (n_estimators=723, max_depth=9, learning_rate=0.035, subsample=0.72, colsample_bytree=0.84) achieving 97.46% individual accuracy

-   **Random Forest:** Ensemble of 700 decision trees with max_depth=18, providing robust baseline performance (94.41% accuracy) and resistance to overfitting

-   **CatBoost:** Gradient boosting with advanced categorical feature handling (iterations=700, depth=8) achieving the highest individual model accuracy (97.34%)

**Ensemble Strategy:** Weighted averaging approach combining predictions from three base models:

$$\begin{array}{r}
P_{ensemble}(x) = \ \sum_{i \in \left\{ XGB,\ RF,\ CatBoost \right\}}^{}{w_{i}P_{i}(x)}\ \#(20)
\end{array}$$

Where, $P_{ensemble}(x) = \ Final\ ensemble\ prediction\ probability$,

$P_{i}(x) = Prediction\ probability\ from\ model\ \mathbf{i}$**,**

$w_{i} = \ Weight\ for\ model\ \mathbf{i,}\ constrained\ by\ \sum_{i}^{}{w_{i} = 1,\ w_{i}\  \geq 0\ }\ $

Weight Optimization: Grid search over weight space:

$$\begin{array}{r}
w^{*} = \arg\max_{w}\ CV_{accuracy(w)}\ subject\ to:\ w_{XGB} + \ w_{RF} + \ w_{CB} = 1\ \ \ \ \ w_{i} \in \ \lbrack 0,\ 1\rbrack\ \#(21)
\end{array}$$

Optimal weights determined: $w_{XGB} = 0.40,\ \ w_{RF} = 0.35,\ \ \ w_{CB} = 0.25$ based on the temporal cross-validation performance.

![](/home/z/my-project/download/thesis_media/media/image10.png){width="5.386805555555555in" height="2.188888888888889in"}

[]{#_Toc233543485 .anchor}**Figure 4:** Ensemble architecture visualization showing weighted averaging.

Final Classification: Binary decision using threshold:

> $$\begin{array}{r}
> y_{pred} = \ \left\{ \begin{array}{r}
> 1,\ \ \ \ \ \ if\ P_{ensemble}(x)\  \geq 0.5\ (drought) \\
> 0,\ {if\ P}_{ensemble}(x)\  < 0.5\ (no\ drought)
> \end{array} \right.\ \ \#(22)
> \end{array}$$

Hyperparameter Optimization: Optuna framework with Bayesian optimization:

> $$\begin{array}{r}
> \theta^{*} = \arg{\max_{\theta}\mathbb{\ E\ }\left\lbrack CV_{score(\theta)} \right\rbrack\ \ }\#(23)
> \end{array}$$

Where $\mathbf{\theta}\ $represents the hyperparameter vector, optimized over 50 trials per model using the Tree-structured Parzen Estimator (TPE) for efficient search.

**Feature Scaling:** StandardScaler normalization applied:

> $$\begin{array}{r}
> X_{scaled} = \ \frac{X - \mu}{\sigma}\ \#(24)
> \end{array}$$

$where\ \mathbf{\mu}\  = \ mean\ and\ \mathbf{\sigma}\ $ standard deviation computed on training data only to prevent information leakage.

#### 3.6 Temporal Cross-Validation

Validation Strategy: 5-fold walk-forward temporal cross-validation ensuring train-past, test-future methodology:

For fold $\mathbf{k:}$

> $$\begin{array}{r}
> {Train}_{k} = \left\{ \left( x_{i},\ y_{i} \right):\ t_{i} < \ T_{k} \right\}\ \#(25)
> \end{array}$$
>
> $$\begin{array}{r}
> {Test}_{k} = \left\{ \left( x_{j},\ y_{j} \right):\ T_{k} \leq T_{j} < \ T_{k + 1} \right\}\ \#(26)
> \end{array}$$

Where $T_{k}$​ is the cutoff time (year) for fold $\mathbf{k}$, ensuring no future information leaks into past training.

[]{#_Toc233543512 .anchor}Table 3.2 Configuration of the 5-fold walk-forward temporal cross-validation splits.

  -----------------------------------------------------------------------------------------------------------------------------------------
  Fold   Cutoff Year ($\mathbf{T}_{\mathbf{k}}$)   Training Period   Testing Period   Train Years   Test Years   Validation Strategy
  ------ ----------------------------------------- ----------------- ---------------- ------------- ------------ --------------------------
  1      2010                                      1961-2010         2011-2015        50 years      5 years      Train past → Test future

  2      2013                                      1961-2013         2014-2017        53 years      4 years      Train past → Test future

  3      2016                                      1961-2016         2017-2020        56 years      4 years      Train past → Test future

  4      2019                                      1961-2019         2020-2023        59 years      4 years      Train past → Test future

  5      2015                                      1961-2015         2016-2023        55 years      8 years      Train past → Test future
  -----------------------------------------------------------------------------------------------------------------------------------------

Key Feature: Each fold trains on earlier historical data and tests on temporally held-out later periods, with test data completely withheld during training to simulate operational forecasting conditions where future data arrives sequentially. This walk-forward approach ensures that model performance metrics reflect realistic predictive capability for operational drought early warning systems.

Evaluation Metrics: Comprehensive performance assessment using:

**Accuracy:**$\begin{array}{r}
Accuracy = \ \frac{TP + \ TN}{TP\  + \ TN\  + \ FP\  + FN}\ \#(27)
\end{array}$

Precision (Positive Predictive Value):

> $$\begin{array}{r}
> Precision = \ \frac{TP}{TP + FP}\ \#(28)
> \end{array}$$

Recall (Sensitivity, True Positive Rate):

> $$\begin{array}{r}
> Recall = \ \frac{TP}{TP + FN}\ \#(29)
> \end{array}$$

F1-Score (Harmonic Mean):

> $$\begin{array}{r}
> F1 = 2\  \times \ \frac{Precision\  \times Recall}{Precision + Recall}\ \#(30)
> \end{array}$$

Specificity (True Negative Rate):

> $$\begin{array}{r}
> Specificity = \ \frac{TN}{TN + FP}\ \#(31)
> \end{array}$$
>
> AUC (Area Under ROC Curve):
>
> $$\begin{array}{r}
> AUC = \ \int_{0}^{1}{TPR(FPR)\ d(FPR)}\ \#(32)
> \end{array}$$

Where $TP = True\ Positive,\ TN = True\ Negative,\ FP = False\ Positive,\ FN = False\ Negative$

Aggregated Performance:

> $$\begin{array}{r}
> \mu_{metric} = \ \frac{1}{K} \times \sum_{k = 1}^{5}{metric}_{k}\ \#(33)
> \end{array}$$

$$\begin{array}{r}
\sigma_{metric} = \ \sqrt{\frac{1}{K} \times \sum_{}^{}\left( {metric}_{k} - \ \mu \right)^{2}}\ \#(34)
\end{array}$$

#### 3.7 Explainability Analysis

SHAP Implementation: SHapley Additive exPlanations (SHAP) using TreeExplainer for model interpretability. SHAP values based on cooperative game theory \[47\] : $\begin{array}{r}
\varnothing_{j}(x) = \sum_{S \subseteq \left\{ 1,\ \ldots,M \right\}\backslash\left\{ j \right\}}^{}{\frac{|S|\ !\ \left( M\  - |S| - 1\  \right)!}{M!}\left\lbrack f_{S \cup \left\{ j \right\}\ }\left( x_{S \cup \left\{ j \right\}} \right) - f_{S}\left( x_{S} \right) \right\rbrack}\ \#(35)
\end{array}$

Where, $\varnothing_{j}(x) = SHAP\ value\ for\ feature\ \mathbf{j}\mathbf{,\ }$ $S \subseteq \left\{ 1,\ \ldots,M \right\}\backslash\left\{ j \right\} = subset\ of\ features,$

$f_{S}\left( x_{S} \right) = model\ prediction\ using\ feature\ subset\ \mathbf{S,\ \ }and\ \mathbf{M =}total\ number\ of\ features$

Global Feature Importance: Aggregated across all samples:

> $$\begin{array}{r}
> {Importance}_{j} = \ \frac{1}{N} \times \sum_{i = 1}^{N}{|\varnothing_{j}\left( x_{i} \right)}\ \#(36)
> \end{array}$$

Feature Importance Analysis: SHAP values computed to quantify each feature\'s contribution to individual predictions and overall model behavior, enabling transparent understanding of drought prediction factors.

#### 3.8 Statistical Analysis and Model Evaluation

Core Performance Indicators: Our model\'s performance was comprehensively assessed using different metrics. We measured overall correctness with Accuracy, while Precision quantified the reliability of its positive (drought) predictions. To evaluate its sensitivity for successfully identifying actual droughts, we used Recall. The F1-score shows a balance between precision and recall. The AUC measures how well the model can tell different classes apart \[48\].

Validation Approach: Our cross-validation strategy was designed to simulate the real-world conditions. We used stratified temporal splits which maintained the data\'s chronological order and also confirmed a balanced representation of drought instances in each fold. In this setup, models were trained on all historical data up to a certain year and then tested only on the following year\'s data, reflecting a true predictive scenario.

Assessing Statistical Significance: We used McNemar\'s test to determine if the performance gains from our ensemble method were statistically significant when compared to the individual models. To measure how uncertain the results where we calculated confidence intervals using 1,000 rounds of random sampling.

## **Chapter 4. Results and Discussion**

This chapter presents the experimental results obtained from the proposed explainable ensemble learning framework for drought classification in Bangladesh. The performance of the proposed models is evaluated using five-fold walk-forward temporal cross-validation and compared with existing approaches. Furthermore, feature importance, SHAP-based explainability, spatial and seasonal drought patterns, result comparison, and practical applications are discussed to demonstrate the effectiveness and applicability of the proposed framework.

#### 4.1 Temporal Cross-Validation Performance

Overall Performance: The ensemble model achieved a highest 97.27% ± 0.32% accuracy across 5 temporal splits. Which is demonstrating robust performance on temporally held-out test data that is representing future periods relative to training (Table 2). AUC reached 99.69% ± 0.14% that is indicating exceptional discrimination capability between drought and non-drought conditions. These results shows a significant advancement over previous Bangladesh drought studies. With our temporal validation providing realistic performance estimates for operational deployment.

[]{#_Toc233543513 .anchor}Table 4.1 Temporal Cross-Validation Detailed Metrics

  ---------------------------------------------------------------------------------------------------------------------------------
  Fold   Train Period   Test Period   Train Size   Test Size   Accuracy (%)   AUC (%)   F1-Score (%)   Precision (%)   Recall (%)
  ------ -------------- ------------- ------------ ----------- -------------- --------- -------------- --------------- ------------
  1      1961-2010      2011-2015     14,256       1,784       96.76          99.45     96.16          96.27           96.05

  2      1961-2013      2014-2017     15,984       1,680       97.20          99.68     95.23          96.11           94.37

  3      1961-2016      2017-2020     16,848       1,512       97.56          99.77     95.72          97.87           93.67

  4      1961-2019      2020-2023     17,712       1,344       97.38          99.79     97.05          97.84           96.28

  5      1961-2015      2016-2023     16,488       2,688       97.47          99.78     96.45          97.88           95.06

  Mean   \-             \-            16,257       1,802       97.27          99.69     96.12          97.19           95.09

  Std    \-             \-            1,148        467         ±0.32          ±0.14     ±0.70          ±0.92           ±1.10
  ---------------------------------------------------------------------------------------------------------------------------------

![](/home/z/my-project/download/thesis_media/media/image11.png){width="6.25in" height="2.7305555555555556in"}

[]{#_Toc233543486 .anchor}**Figure 5:** Temporal Cross-Validation Results showing 5-fold performance with error bars.

Split-wise Analysis: Our Temporal Cross-Validation Performance shows the remarkable consistency across temporal splits with Split 3 (2017-2020) achieving the highest accuracy (97.56%) and Split 1 (2011-2015) showing the lowest (96.76%). That is indicating robust model performance across varying climate conditions (Figure 4). The low standard deviation (±0.32%) confirms exceptional temporal stability which is critical for operational drought early warning systems.

Comparison with Previous Studies: Our temporal validation (97.27%) substantially exceeds all previous Bangladesh drought studies: Khan et al. \[11\] achieved 88.7% using XGBoost with random validation. Paul et al. \[13\] achieved 92% using traditional machine learning classifiers without temporal ordering, and Hossain et al. \[41\] achieved 96% ensemble accuracy in Rajshahi using SPEI-based ML models, demonstrating the importance of advanced feature engineering, although their validation relied on random splitting rather than temporal evaluation for realistic performance assessment.

#### 4.2 Model Comparison and Ensemble Performance

Individual Model Performance: We evaluated three complementary machine learning models, and each one achieved exceptional results. XGBoost scored the highest individual accuracy at 97.46% (99.78% AUC) which confirms its excellent in gradient boosting capability. CatBoost performed at a similar level with 97.34% accuracy and a 99.77% AUC which is showing its superior handling of categorical data. Random Forest offered a strong baseline performance at 94.41% accuracy with 98.93% AUC and provided valuable variety for the ensemble (Table 3, Figures 5 and 10). Overall, each model represents different aspects of the drought prediction challenge. The gradient boosting methods XGBoost and CatBoost performed better than Random Forest on the test data from more recent years.

[]{#_Toc233543514 .anchor}Table 4.2 Model Performance Comparison

  ------------------------------------------------------------------------------------------
  Model                 Accuracy (%)   AUC (%)   F1-Score (%)   Precision (%)   Recall (%)
  --------------------- -------------- --------- -------------- --------------- ------------
  XGBoost               97.46          99.78     96.43          97.02           95.86

  Random Forest         94.41          98.93     92.05          93.69           90.47

  CatBoost              97.34          99.77     96.23          97.40           95.10

  Ensemble (Weighted)   97.27          99.69     96.12          97.19           95.09
  ------------------------------------------------------------------------------------------

Ensemble Configuration: XGBoost (40% weight), Random Forest (35% weight), CatBoost (25% weight)

Ensemble Method: Weighted soft voting (probability averaging)

![](/home/z/my-project/download/thesis_media/media/image12.png){width="6.25in" height="4.6715277777777775in"}

[]{#_Toc233543487 .anchor}**Figure 6:** Model Comparison - AUC scores for all models including ensemble.

![](/home/z/my-project/download/thesis_media/media/image13.png){width="5.091075021872266in" height="4.122641076115485in"}

[]{#_Toc233543488 .anchor}**Figure 7:** ROC Curve comparison for all models with ensemble highlighted.

![](/home/z/my-project/download/thesis_media/media/image14.png){width="5.643234908136483in" height="3.726415135608049in"}

[]{#_Toc233543489 .anchor}**Figure 8:** Confusion Matrix for ensemble model with performance metrics.

![](/home/z/my-project/download/thesis_media/media/image15.png){width="5.3139249781277345in" height="3.4245286526684167in"}

[]{#_Toc233543490 .anchor}**Figure 9:** Prediction Distribution showing drought vs no-drought probability distributions

![](/home/z/my-project/download/thesis_media/media/image16.png){width="5.882075678040245in" height="3.901123140857393in"}

[]{#_Toc233543491 .anchor}**Figure 10:** Performance Metrics Detailed comparison across 3 models and ensemble (XGBoost, Random Forest, CatBoost).

Ensemble Benefits: Our combined weighted averaging ensemble performed exceptionally well which is achieving a 97.27% accuracy and a 99.69% AUC. This method struck an excellent balance using the best parts of each individual model. Its performance was +2.86% higher than Random Forest and was just as accurate as the top single models (XGBoost and CatBoost). The ensemble\'s success came from blending the different model capabilities. We gave XGBoost a 40% weight for its gradient boosting efficiency and fast processing. CatBoost received a 25% weight for its advanced handling of categorical data and numerical stability. Random Forest was given a 35% weight for its strong and ability to resist overfitting. Crucially the ensemble proved to be extremely stable with a very low standard deviation of only ±0.32% across the different temporal splits. This high level of consistency is essential for real-world use as it shows the model can be trusted to perform well under varying climate conditions (see Figure 10).

#### 4.3 Feature Importance and SHAP Analysis

[]{#_Toc233543515 .anchor}Table 4.3 Feature Importance Rankings (Top 20) with SHAP values and interpretations.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------
  Rank   Feature Name       Category     Importance Score   SHAP Mean Value   Interpretation
  ------ ------------------ ------------ ------------------ ----------------- ---------------------------------------------------------------------------------
  1      SPEI_12m_lag_3     SPEI         0.145              -0.461            Historical drought indicator - negative values indicate past drought conditions

  2      SPEI_9m_lag_6      SPEI         0.132              -0.091            Historical drought indicator - negative values indicate past drought conditions

  3      SPEI_6m_lag_12     SPEI         0.118              -0.228            Historical drought indicator - negative values indicate past drought conditions

  4      SPEI_1m_lag_12     SPEI         0.076              0.388             Historical drought indicator - negative values indicate past drought conditions

  5      Rainfall_Total     Climate      0.065              -0.148            Direct weather indicator - rainfall/temperature influence drought probability

  6      Temperature_Mean   Climate      0.058              0.048             Direct weather indicator - rainfall/temperature influence drought probability

  7      SPEI_3m_lag_6      SPEI         0.052              -0.433            Historical drought indicator - negative values indicate past drought conditions

  8      Month_sin          Temporal     0.048              -0.002            Seasonal pattern - captures annual and seasonal variations

  9      Latitude           Spatial      0.045              -0.256            Geographic influence - location affects climate patterns

  10     PET_mm_month       Climate      0.042              0.478             Direct weather indicator - rainfall/temperature influence drought probability

  11     SPEI_1m_lag_9      SPEI         0.038              0.117             Historical drought indicator - negative values indicate past drought conditions

  12     Humidity_Mean      Climate      0.035              0.414             Direct weather indicator - rainfall/temperature influence drought probability

  13     Year_normalized    Temporal     0.032              -0.41             Seasonal pattern - captures annual and seasonal variations

  14     SPEI_1m_lag_6      SPEI         0.029              0.466             Historical drought indicator - negative values indicate past drought conditions

  15     Is_Monsoon         Bangladesh   0.026              -0.457            Local climate feature - monsoon and agricultural patterns

  16     Longitude          Spatial      0.023              0.081             Geographic influence - location affects climate patterns

  17     Temperature_Max    Climate      0.02               -0.276            Direct weather indicator - rainfall/temperature influence drought probability

  18     Season_numeric     Temporal     0.018              -0.192            Seasonal pattern - captures annual and seasonal variations

  19     SPEI_1m_lag_3      SPEI         0.015              -0.006            Historical drought indicator - negative values indicate past drought conditions

  20     Is_PreMonsoon      Bangladesh   0.012              0.428             Local climate feature - monsoon and agricultural patterns
  -------------------------------------------------------------------------------------------------------------------------------------------------------------

![](/home/z/my-project/download/thesis_media/media/image17.png){width="6.511135170603675in" height="5.415094050743657in"}

[]{#_Toc233543492 .anchor}**Figure 11:** Top 20 Most Important Features for Drought Prediction

Random Forest feature importance ranked by contribution to model performance. SPEI lag features dominate the top positions across all three base models (RF: 94.41%, XGBoost: 97.46%, CatBoost: 97.34%), with consistent rankings demonstrating robust feature importance. The top feature, SPEI_12m_lag1_safe, accounts for 26.09% of total importance.

![](/home/z/my-project/download/thesis_media/media/image18.png){width="6.25in" height="6.803472222222222in"}

[]{#_Toc233543493 .anchor}**Figure 12:** SHAP Summary Plot for Weighted Ensemble Model showing feature impact on drought prediction across 500 test samples.

Ensemble weights: XGBoost (40%), Random Forest (35%), CatBoost (25%). Individual model accuracies: XGBoost=97.46%, Random Forest=94.41%, CatBoost=97.34%, Ensemble=97.27%. 

Interpretation: Each dot represents one sample (prediction instance), with color indicating feature value (red=high, blue=low) and x-axis position showing SHAP value (impact on prediction: left=lower drought risk, right=higher drought risk). Features display both low and high values because different samples (locations/times) naturally have different feature values---for example, SPEI_12m_lag1_safe shows red dots (high SPEI, non-drought conditions) and blue dots (low SPEI, drought conditions) from different samples. The vertical spread shows value distribution, while horizontal position indicates each value\'s impact on drought prediction. 

Importantly, for SPEI features (drought indices), the relationship is inverse: high SPEI values (red, indicating wet conditions) appear on the left side (negative SHAP, reducing drought prediction), while low SPEI values (blue, indicating dry conditions) appear on the right side (positive SHAP, increasing drought prediction), correctly demonstrating that lower SPEI values drive drought predictions. The top 20 features ranked by mean absolute SHAP value, along with SPEI lag features such as SPEI_12m_lag1_safe, SPEI_1m_lag12_safe, and SPEI_9m_lag3_safe, dominate the model\'s decision-making. This clearly illustrates the critical role of historical drought memory in achieving high prediction accuracy.

Top Predictors: SHAP analysis revealed SPEI lag features as the most important predictors -

-   SPEI_12m_lag1_safe: 26.09% importance (12-month drought conditions from 1 month ago)

-   SPEI_12m_lag3_safe: 10.86% importance (12-month drought conditions from 3 months ago)

-   SPEI_9m_lag3_safe: 5.48% importance (9-month drought conditions from 3 months ago)

Bangladesh-Specific Features: Local climate indicators uniquely tailored to Bangladesh's monsoon dynamics and agricultural calendar also contribute to the model's performance. The peak monsoon phase indicator (phase_peak_monsoon) contributed 1.93% predictive power, pre-monsoon heat stress (pre_monsoon_heat) had a 0.44% importance, and Boro season crop calendar (crop_Boro) had a 0.12% importance.

![](/home/z/my-project/download/thesis_media/media/image19.png){width="6.25in" height="4.11875in"}

 []{#_Toc233543494 .anchor}**Figure 13a:** Agricultural Season Impact on Drought Prediction in Bangladesh (Boro, Aus, Aman seasons).

![](/home/z/my-project/download/thesis_media/media/image20.png){width="6.25in" height="4.11875in"}

[]{#_Toc233543495 .anchor}**Figure 13b:** Monsoon Phase Feature Importance for drought prediction (4-phase analysis).

Interpretability Insights: SHAP analysis revealed that low SPEI values (indicating past drought conditions) strongly predict future drought occurrence, whereas high rainfall totals reduce drought probability. Temperature effects varied seasonally, with pre-monsoon heat stress significantly increasing drought risk.

#### 4.4 Spatial and Seasonal Patterns

[]{#_Toc233543516 .anchor}Table 4.4 Regional Drought Vulnerability by division with frequency and severity.

  --------------------------------------------------------------------------------------------------------------------------------
  Division     Stations   Drought Frequency   Average Severity SPEI   Model Accuracy   Top Risk Season         Vulnerable Months
  ------------ ---------- ------------------- ----------------------- ---------------- ----------------------- -------------------
  Sylhet       2          **33.2%**           **-1.10**               98.88%           Post-Kharif (Oct-Nov)   Oct, Feb, Jan

  Khulna       5          **30.4%**           **-1.24**               98.44%           Rabi (Dec-Feb)          Dec, Nov, Jan

  Barisal      4          **30.3%**           **-1.29**               98.66%           Post-Kharif (Oct-Nov)   Oct, Jan, Mar

  Dhaka        4          **29.3%**           **-1.25**               98.69%           Pre-Kharif (Mar-May)    May, Apr, Feb

  Mymensingh   1          **27.8%**           **-1.21**               98.70%           Kharif (Jun-Sep)        Sep, May, Jul

  Rajshahi     3          **27.8%**           **-1.32**               98.83%           Pre-Kharif (Mar-May)    May, Aug, Feb

  Chittagong   13         **27.6%**           **-1.24**               98.63%           Post-Kharif (Oct-Nov)   Aug, Oct, Nov

  Rangpur      3          **26.7%**           **-1.25**               98.38%           Rabi (Dec-Feb)          Jul, Jun, Jan
  --------------------------------------------------------------------------------------------------------------------------------

![](/home/z/my-project/download/thesis_media/media/image21.png){width="6.25in" height="4.771527777777778in"}

[]{#_Toc233543496 .anchor}**Figure 14:** Station-Wise model reliability score heatmap showing across Bangladesh.

Regional Vulnerability: Northwest Bangladesh showed the highest drought severity, with Rajshahi division experiencing an average SPEI severity of -1.32 and 27.8% drought frequency (Table 5). While the northeastern region (Sylhet) exhibited the highest historical frequency of dry months at 33.2%, these events were less severe (average SPEI of -1.10). The lowest overall drought frequency was observed in Rangpur division at 26.7%, closely followed by Chittagong at 27.6% (Table 5).

Seasonal Analysis: Across all 35 meteorological stations, the Aman season (June-December) showed a drought frequency of 28.45%, closely followed by the Boro season (December-May) at 28.31% and the Aus season (April-August) at 27.85%. However, regional analyses indicate that specific divisions face distinct seasonal vulnerabilities, such as Dhaka and Rajshahi exhibiting highest risks during the Pre-Kharif (March-May) pre-monsoon months due to high temperatures and delayed rainfall (Table 5).

Station-wise Performance: The Model Reliability Score varied across weather stations, ranging from 97.78% (Ambaganctg) to 99.28% (e.g., Dhaka, Bogra, Sylhet) (Table 4). Higher scores are observed at stations with long-term, complete records (756 months), demonstrating the model\'s high reliability when ample training data is available.

#### 4.5 Result Comparison

[]{#_Toc233543517 .anchor}Table 4.5 Comparison with Existing Bangladesh Drought Studies.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Study                          Region                      Period Years   Stations               Method                          Validation               Accuracy %
  ------------------------------ --------------------------- -------------- ---------------------- ------------------------------- ------------------------ ------------
  Sadiq et al. (2023) \[11\]     Northern Bangladesh         2010 - 2019    6                      RF + RS Indices + SPI           Cross-validation         81-95

  Hossain et al. (2025) \[15\]   Rajshahi                    1965 - 2022    7                      Hybrid Ensemble + SPEI          Hold-out (80/20 split)   96

  Hossain et al. (2025) \[14\]   Central Bangladesh          1990 - 2022    7                      RF + SPI/SPEI/ZSI + ARIMA       Hold-out (80/20 split)   94

  Paul et al. (2024) \[13\]      Bangladesh (38 districts)   2012 - 2024    38 (satellite grids)   Satellite + RF/KNN etc.         Accuracy score           92

  Our Study (2026)               All Bangladesh              1961 - 2023    35                     8-scale SPEI + Ensemble + XAI   5-fold Temporal CV       97.27
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Performance Comparison: Our achieved superior performance compared to previous Bangladesh drought studies (Table 6). The closest comparable study \[15\] achieved 96% accuracy using hold-out validation in the Rajshahi region, while our approach achieved 97.27% using more comprehensive 5-fold temporal validation across all of Bangladesh

Methodological Advances: Our study provides several methodological improvements: - (1) First 63-year temporally validated drought classification system for Bangladesh. (2) Integration of 8-scale SPEI analysis with Bangladesh-specific features. (3) Comprehensive SHAP analysis for operational deployment. (4) Rigorous temporal cross-validation addressing data leakage concerns.

#### 4.6 Practical Applications

Agricultural Planning: The framework enables month-ahead drought prediction for crop planning. Especially for Boro rice cultivation during the critical December-May period.

Early Warning System: Real-time drought monitoring capabilities support government agencies in implementing timely drought mitigation measures.

Regional Adaptation: Station-wise performance analysis guides targeted interventions in high-vulnerability regions like northwest Bangladesh.

#### 4.7 Achievement of Research Objectives

This study successfully achieved the research objectives presented in Chapter 1. The proposed weighted ensemble learning framework, consisting of XGBoost, Random Forest, and CatBoost, demonstrated high performance for meteorological drought classification in Bangladesh. The implementation of five-fold walk-forward temporal cross-validation provided reliable model evaluation under realistic forecasting conditions while minimizing the risk of temporal data leakage. Bangladesh-specific feature engineering, including multi-scale SPEI indices, monsoon phases, and agricultural season indicators, improved the predictive capability of the proposed framework. Furthermore, SHAP-based explainable artificial intelligence successfully identified the most influential features contributing to drought prediction, making the proposed framework transparent and suitable for operational decision support. Overall, the obtained accuracy of **97.27%** and **99.69% AUC** confirms that the proposed methodology successfully addressed the research objectives and achieved improved performance compared with previous Bangladesh drought studies.

#### 4.8 Study Limitations

Although the proposed framework achieved excellent performance, several limitations should be acknowledged. First, this study focuses only on meteorological drought using SPEI and does not consider agricultural or hydrological drought indices. Second, the proposed framework relies on historical meteorological observations collected from 35 Bangladesh Meteorological Department stations, and therefore areas with sparse station coverage may contain higher uncertainty. Third, satellite observations, soil moisture measurements, groundwater information, and remote sensing products were not incorporated into the current framework. Finally, the developed model was evaluated using historical climate data and temporal cross-validation; therefore, real-time deployment and future climate change scenario analysis remain beyond the scope of this study. These limitations provide opportunities for future research to develop more comprehensive drought prediction systems by integrating additional environmental datasets and operational forecasting capabilities.

## **Chapter 5. Conclusion**

This chapter summarizes the overall outcomes of the research and reflects on the extent to which the research objectives have been achieved. It presents the major findings of the proposed drought classification framework, highlights the scientific and practical contributions of the study, discusses its limitations, and outlines potential directions for future research. The chapter provides a concise conclusion to the thesis while emphasizing the significance of the proposed framework for drought monitoring and decision-making in Bangladesh.

#### 5.1 Restating the Research Problem and Objectives

This study addressed the challenge of developing an accurate, explainable, and temporally validated drought classification framework for Bangladesh. It achieved 97.27% ± 0.32% accuracy using 5-fold walk-forward validation over 63 years of data from 35 weather stations. The framework combines 8-scale SPEI analysis (1, 2, 3, 6, 9, 12, 18, 24 months) with 76 features specific to Bangladesh. These include 20 SPEI lag features, 18 time-based features, 18 rolling statistics and 8 indicators related to monsoon and agriculture. We used an ensemble of three models XGBoost (40%), Random Forest (35%) and CatBoost (25%). This approach marks a major step forward in drought monitoring for developing countries. The model's AUC score of 99.69% shows excellent ability to distinguish drought events.

#### 5.2 Summarizing Key Findings

Our framework addresses critical gaps in previous Bangladesh drought research through four key innovations: (1) rigorous temporal cross-validation preventing data leakage and providing realistic performance estimates for operational deployment (97.27% represents genuine predictive capability on unseen future data); (2) comprehensive multi-scale SPEI analysis capturing drought impacts from immediate meteorological conditions (1-month scale) to long-term socio-economic effects (24-month scale); (3) extensive Bangladesh-specific feature engineering (76 total features) incorporating monsoon dynamics, agricultural calendars, and temporal patterns unique to Bangladesh\'s climate; (4) Ensemble SHAP analysis aggregating interpretations from all three models, enabling transparent, interpretable predictions suitable for policy-level decision-making with full traceability of feature contributions.

This study builds a reliable and ready-to-use drought monitoring system for Bangladesh. It uses advanced machine learning and strong validation methods to address agricultural risks. The framework shows excellent performance, with 97.27% accuracy. This is better than all previous studies in Bangladesh, including the best earlier result of 96% by Hossain et al. \[41\], 2025. This is a +1.28-percentage point improvement. The method uses temporal validation, which proves the model can predict future droughts accurately. The Ensemble SHAP analysis adds the full explainability. This helps build trust among stakeholders and supports better decisions in farming, water management and climate planning.

#### 5.3 Highlighting Contributions

This study offers several practical contributions. First, it identifies drought risk patterns linked to agricultural seasons and shows how they change from year to year. These changes are measured using ±1 standard deviation error bars which show how stable the patterns are over time. Second, it measures how monsoon phases affect droughts. The results show a consistent \~30% drought frequency across phases, but with large year-to-year variation (standard deviation: 18--24%). Third, it ranks feature importance and shows that 20 SPEI lag features---covering all 8 time scales from 1 to 24 months---are the strongest predictors. This confirms that long-term drought memory is important. These findings support evidence-based policies and better resource planning for drought response and adaptation in Bangladesh's agriculture sector.

This framework builds Bangladesh's first reliable and scientifically tested drought early warning system. It supports agricultural planning for 40 million people living in drought-prone areas. The system combines high accuracy, long-term data coverage, regional focus and clear explanations. These features meet all key needs for climate services in developing countries. This study shows that advanced machine learning methods when properly tested and made easy to understand can offer real solutions to serious climate problems in vulnerable regions

#### 5.4 Discussing Limitations

While our study marks a major step forward in drought classification for Bangladesh, some limitations should be noted. First, the data coverage is 67.5% across all station-year combinations. This is common for long-term weather datasets in developing countries. But it may cause some uncertainty in regional and time-based analysis. Stations set up after 1990 have complete records, while older stations sometimes have missing data due to equipment problems or operational issues. We handled this carefully by using methods to manage missing data and designing a validation process that considers different levels of data availability. Still, having full data from all stations would improve the reliability of regional drought risk assessments.

**Historical Data Quality Considerations:** Our study shows strong progress in drought classification for Bangladesh but some limitations should be noted. Data quality checks revealed important differences over time. Data from the modern period (2000--2023) was highly reliable. However data from the historical period (1961--1999) was moderately reliable and missed some extreme events such as the 1966 Bengal Famine. This may be due to the limited number of weather stations operating in the 1960s--1970s (around 15--20 stations compared to 35 today) which reduced spatial coverage. Also, the 1974 Bangladesh Famine often mentioned in historical records. But was mainly caused by flooding, not drought. Our data correctly showed above-normal rainfall during that time, highlighting the difference between famine and meteorological drought. This shows that our model focuses only on meteorological drought and does not include socio-economic factors, soil moisture (agricultural drought), or streamflow (hydrological drought). The strong performance of our model in detecting recent droughts (2000--2023) gives confidence in its use for current and future drought monitoring. However, historical results before 1975 should be viewed with care due to data quality limitations.

Second, although our feature engineering is extensive (76 features). But it does not include some important variables like groundwater levels, soil moisture or crop yield data. These factors could help understand drought impacts better. But they are not regularly measured at all stations in Bangladesh. This makes them difficult to use in a nationwide system. In future work, satellite-based data such as soil moisture and vegetation indices should be considered to support and improve ground-based weather measurements.\
\
Third, our temporal cross-validation method is more reliable than random data splits, but it assumes that the relationship between features and drought stays the same over time. Climate change may change these relationships which could reduce the model's accuracy when predicting future droughts. Although our 63-year training period includes a wide range of climate conditions. The future research should test for changes over time (non-stationarity) and explore ways to update the model as needed.

Fourth, running our model in real-time may be challenging in settings with limited resources. Especially since ensemble predictions require three separate models. However, our optimized version runs efficiently on regular computers and processing 17,868 records in less than 40 minutes. To support daily updates or include more stations and finer time details further improvements in computing speed or using cloud-based systems would be helpful.

#### 5.5 Suggesting Future Work

Our study opens up several promising directions for future research. First, expanding our framework to include probabilistic drought predictions. That is showing the likelihood of different drought severity levels instead of just yes/no classifications. Second, we could try to predict conditions further in advance. Right now, we can predict one month ahead. But we might be able to extend this lead-time by adding seasonal climate forecasts (like monsoon predictions from weather models) as new features.

Third, we could improve accuracy in specific regions. This would involve developing custom ensemble weights for each station. We can tuning them to match local climate patterns. This approach would be especially helpful for regions with varied climates like Bangladesh. That country has different zones from the drought-prone northwest to the flood-prone southeast.

Fourth, adding satellite remote sensing data such as MODIS vegetation indices, GRACE groundwater anomalies and rainfall estimates from GPM/TRMM can improve spatial coverage and help monitor droughts in areas with limited ground data. Fifth, the method could be enhanced by expanding it to predict distinct drought severity levels such as moderate, severe, and extreme rather than the current binary (two-class) approach. This would provide far more detailed information which helps in planning more specific and appropriate responses based on how serious the drought is. Finally, we could adopt online learning techniques. This would allow the model to update itself continuously as new data becomes available. And helping it maintain high accuracy over time which is essential as climate patterns continue to change.

## **References**

\[1\] UNPF, "Bangladesh Population 2025 - United Nations Population Fund." Accessed: Oct. 20, 2025. \[Online\]. Available: https://www.unfpa.org/data/world-population/BD

\[2\] A. Al Mamun *et al.*, "Identification of Meteorological Drought Prone Area in Bangladesh using Standardized Precipitation Index," *J. Earth Sci. Clim. Change*, vol. 09, no. 03, 2018, doi: 10.4172/2157-7617.1000457.

\[3\] M. A. Hossain, M. M. Rahman, S. S. Hasan, A. Mahmud, and L. Bai, "Analysis and forecasting of meteorological drought using PROPHET and SARIMA models deploying machine learning technique for southwestern region of Bangladesh," *Environmental and Sustainability Indicators*, vol. 27, no. April, p. 100761, 2025, doi: 10.1016/j.indic.2025.100761.

\[4\] S. Shahid and H. Behrawan, "Drought risk assessment in the western part of Bangladesh," *Natural Hazards*, vol. 46, no. 3, pp. 391--413, Sep. 2008, doi: 10.1007/s11069-007-9191-5.

\[5\] Md. R. Rahman and H. Lateh, "Spatio-temporal analysis of warming in Bangladesh using recent observed temperature data and GIS," *Clim. Dyn.*, vol. 46, no. 9--10, pp. 2943--2960, May 2016, doi: 10.1007/s00382-015-2742-7.

\[6\] M. S. Sultana, M. Y. Gazi, and M. B. Mia, "Multiple indices based agricultural drought assessment in the northwestern part of Bangladesh using geospatial techniques," *Environmental Challenges*, vol. 4, Aug. 2021, doi: 10.1016/j.envc.2021.100120.

\[7\] F. A. Farah, A. H. Nur, A. A. Ibrahim, A. A. Warsame, A. A. Mohamed, and S. M. Ahmed, "Impacts of Drought on Food Security in Bangladesh," *East African Scholars Journal of Agriculture and Life Sciences*, vol. 8, no. 02, pp. 35--53, Mar. 2025, doi: 10.36349/easjals.2025.v08i02.003.

\[8\] N. C. Dey *et al.*, "Sustainability of groundwater use for irrigation of dry-season crops in northwest Bangladesh," *Groundw. Sustain. Dev.*, vol. 4, pp. 66--77, Mar. 2017, doi: 10.1016/j.gsd.2017.02.001.

\[9\] T. B. Mckee, N. J. Doesken, and J. Kleist, "THE RELATIONSHIP OF DROUGHT FREQUENCY AND DURATION TO TIME SCALES," 1993.

\[10\] S. M. Vicente-Serrano, S. Beguería, and J. I. López-Moreno, "A multiscalar drought index sensitive to global warming: The standardized precipitation evapotranspiration index," *J. Clim.*, vol. 23, no. 7, pp. 1696--1718, Apr. 2010, doi: 10.1175/2009JCLI2909.1.

\[11\] M. F. Mashuq, J. Akther, and K. Das, "SPEI Based Drought Prediction and Validation Using Machine Learning Algorithm in Bangladesh from 1981 to 2017," *IEEE International Conference on Signal Processing, Information, Communication and Systems, SPICSCON 2024 - Proceedings*, no. November, pp. 1--5, 2024, doi: 10.1109/SPICSCON64195.2024.10941010.

\[12\] M. S. Al Reshan *et al.*, "Toward Drought Modeling in South Asia: Machine Learning Approaches, Challenges, and Opportunities," *IEEE Access*, vol. 13, no. March, pp. 87654--87671, 2025, doi: 10.1109/ACCESS.2025.3567257.

\[13\] T. Paul, M. D. Mati, and M. M. Islam, "Enhanced Drought Analysis in Bangladesh: A Machine Learning Approach for Severity Classification Using Satellite Data," *2024 27th International Conference on Computer and Information Technology, ICCIT 2024 - Proceedings*, no. December, pp. 459--464, 2024, doi: 10.1109/ICCIT64611.2024.11022417.

\[14\] A. Hossain, M. Begum, and N. Akhtar, "Drought Prediction Using Machine Learning Forecasting Model in the Context of Bangladesh During 1981--2018," in *Lecture Notes in Networks and Systems*, Springer Science and Business Media Deutschland GmbH, 2024, pp. 499--515. doi: 10.1007/978-981-99-8479-4_37.

\[15\] M. A. Hossain, M. M. Rahman, S. S. Hasan, A. Mahmud, and L. Bai, "Analysis and forecasting of meteorological drought using PROPHET and SARIMA models deploying machine learning technique for southwestern region of Bangladesh," *Environmental and Sustainability Indicators*, vol. 27, no. April, p. 100761, 2025, doi: 10.1016/j.indic.2025.100761.

\[16\] A. AghaKouchak *et al.*, "Remote sensing of drought: Progress, challenges and opportunities," Jun. 01, 2015, *Blackwell Publishing Ltd*. doi: 10.1002/2014RG000456.

\[17\] R. Sultana, H. M. Irfanullah, S. A. Selim, and M. Budrudzaman, "Vulnerability and ecosystem-based adaptation in the farming communities of droughtprone Northwest Bangladesh," *Environmental Challenges*, vol. 11, Apr. 2023, doi: 10.1016/j.envc.2023.100707.

\[18\] R. Kumar *et al.*, "Multiscale evaluation of the Standardized Precipitation Index as a groundwater drought indicator," *Hydrol. Earth Syst. Sci.*, vol. 20, no. 3, pp. 1117--1131, Mar. 2016, doi: 10.5194/hess-20-1117-2016.

\[19\] I. Noguera, F. Domínguez-Castro, and S. M. Vicente-Serrano, "Near-real time ﬂash drought monitoring system and dataset for Spain," *Ann. N. Y. Acad. Sci*, vol. 47, pp. 155--172, 2023, doi: 10.5281/zenodo.7434135.

\[20\] A. Dikshit, B. Pradhan, and A. M. Alamri, "Temporal hydrological drought index forecasting for New South Wales, Australia using machine learning approaches," *Atmosphere (Basel).*, vol. 11, no. 6, Jun. 2020, doi: 10.3390/atmos11060585.

\[21\] F. Xu *et al.*, "Understanding climate change impacts on drought in China over the 21st century: a multi-model assessment from CMIP6," *NPJ Clim. Atmos. Sci.*, vol. 7, no. 1, Dec. 2024, doi: 10.1038/s41612-024-00578-5.

\[22\] E. Ozupek, A. Teke, N. Celik, and T. Kavzoglu, "Explainable artificial intelligence to explore the intrinsic characteristics of climatic parameters governing meteorological drought forecasting: opening the black box," *Stochastic Environmental Research and Risk Assessment*, vol. 39, no. 8, pp. 3201--3222, 2025, doi: 10.1007/s00477-025-03007-y.

\[23\] Y. Feng, F. Sun, and F. Liu, "SHAP-powered insights into short-term drought dynamics disturbed by diurnal temperature range across China," *Agric. Water Manag.*, vol. 316, no. December 2024, p. 109579, Jul. 2025, doi: 10.1016/j.agwat.2025.109579.

\[24\] K. En-Nagre *et al.*, "Assessment and prediction of meteorological drought using machine learning algorithms and climate data," *Clim. Risk Manag.*, vol. 45, no. June, p. 100630, 2024, doi: 10.1016/j.crm.2024.100630.

\[25\] L. Wang, Y. Zhang, X. Chen, Y. Liu, S. Wang, and L. Wang, "Ensemble learning based on remote sensing data for monitoring agricultural drought in major winter wheat-producing areas of China," *Progress in Physical Geography: Earth and Environment*, vol. 48, no. 2, pp. 171--190, Apr. 2024, doi: 10.1177/03091333231188814.

\[26\] M. A. Hossain, M. Begum, M. N. Akhtar, M. A. Talukder, N. Rahman, and M. Rahman, "An Ensemble Learning Approach for Drought Analysis and Forecasting in Central Bangladesh," *Advances in Meteorology*, vol. 2025, no. 1, 2025, doi: 10.1155/adme/4904248.

\[27\] R. Zhang, Z. Y. Chen, L. J. Xu, and C. Q. Ou, "Meteorological drought forecasting based on a statistical model with machine learning techniques in Shaanxi province, China," *Science of the Total Environment*, vol. 665, pp. 338--346, May 2019, doi: 10.1016/j.scitotenv.2019.01.431.

\[28\] O. Kukartseva, V. Tynchenko, V. Kukartsev, and T. Panfilova, "Using ensemble learning method and binary decision tree algorithm for drought intensity level classification," *Journal of Infrastructure, Policy and Development*, vol. 8, no. 10, 2024, doi: 10.24294/jipd.v8i10.6807.

\[29\] S. Lundberg and S.-I. Lee, "A Unified Approach to Interpreting Model Predictions," Nov. 2017, doi: https://doi.org/10.48550/arXiv.1705.07874.

\[30\] B. Zhang, F. K. Abu Salem, M. J. Hayes, K. H. Smith, T. Tadesse, and B. D. Wardlow, "Explainable machine learning for the prediction and assessment of complex drought impacts," *Science of the Total Environment*, vol. 898, no. July, p. 165509, 2023, doi: 10.1016/j.scitotenv.2023.165509.

\[31\] C. Intelligence and Neuroscience, "Retracted: Drought Assessment Based on Data Fusion and Deep Learning," *Comput. Intell. Neurosci.*, vol. 2023, no. 1, Jan. 2023, doi: 10.1155/2023/9841926.

\[32\] X. Xiao *et al.*, "Leveraging multisource data for accurate agricultural drought monitoring: A hybrid deep learning model," *Agric. Water Manag.*, vol. 293, Mar. 2024, doi: 10.1016/j.agwat.2024.108692.

\[33\] R. Shen, A. Huang, B. Li, and J. Guo, "Construction of a drought monitoring model using deep learning based on multi-source remote sensing data," *International Journal of Applied Earth Observation and Geoinformation*, vol. 79, pp. 48--57, Jul. 2019, doi: 10.1016/J.JAG.2019.03.006.

\[34\] R. Maity *et al.*, "Potential of deep learning in drought assessment by extracting information from hydrometeorological precursors," *Journal of Water and Climate Change*, vol. 12, no. 6, pp. 2774--2796, Sep. 2021, doi: 10.2166/wcc.2021.062.

\[35\] A. Elbeltagi *et al.*, "Advanced stacked integration method for forecasting long-term drought severity: CNN with machine learning models," *J. Hydrol. Reg. Stud.*, vol. 53, p. 101759, 2024, doi: 10.1016/j.ejrh.2024.101759.

\[36\] J. Chen, Q. Jin, and J. Chao, "Design of deep belief networks for short-term prediction of drought index using data in the huaihe river basin," *Math. Probl. Eng.*, vol. 2012, 2012, doi: 10.1155/2012/235929.

\[37\] A. N. Sihananto *et al.*, "Drought forecasting using ANFIS on tuban regency, Indonesia," *Proceedings - 2017 International Conference on Sustainable Information Engineering and Technology, SIET 2017*, vol. 2018-Janua, pp. 316--320, 2017, doi: 10.1109/SIET.2017.8304155.

\[38\] A. Kaur and S. K. Sood, "Deep learning based drought assessment and prediction framework," *Ecol. Inform.*, vol. 57, no. February, p. 101067, 2020, doi: 10.1016/j.ecoinf.2020.101067.

\[39\] M. R. Rahman and H. Lateh, "Meteorological drought in Bangladesh: assessing, analysing and hazard mapping using SPI, GIS and monthly rainfall data," *Environmental Earth Sciences 2016 75:12*, vol. 75, no. 12, pp. 1026-, Jun. 2016, doi: 10.1007/S12665-016-5829-5.

\[40\] M. A. Hossain, M. Begum, M. N. Akhtar, M. A. Talukder, N. Rahman, and M. Rahman, "An Ensemble Learning Approach for Drought Analysis and Forecasting in Central Bangladesh," *Advances in Meteorology*, vol. 2025, no. 1, 2025, doi: 10.1155/ADME/4904248.

\[41\] A. Hossain, "Quantifying Drought Using Machine Learning Models with SPEI indices and Weather Data," *Indonesian Journal of Electrical Engineering and Informatics (IJEEI)*, vol. 13, no. 3, pp. 569--584, 2025, doi: 10.52549/ijeei.v13i3.6477.

\[42\] A. Khondakar *et al.*, "Spatiotemporal pattern of the dynamics in area, production, and yield of Aus rice in Bangladesh and its response to droughts from 1980 to 2018," *Journal of Geographical Sciences 2022 32:10*, vol. 32, no. 10, pp. 2069--2084, Oct. 2022, doi: 10.1007/S11442-022-2037-Y.

\[43\] M. A. Sadiq, S. K. Sarkar, and S. S. Raisa, "Meteorological drought assessment in northern Bangladesh: A machine learning-based approach considering remote sensing indices," *Ecol. Indic.*, vol. 157, Dec. 2023, doi: 10.1016/j.ecolind.2023.111233.

\[44\] George H. Hargreaves and Zohrab A. Samani, "Reference Crop Evapotranspiration from Temperature," *Appl. Eng. Agric.*, vol. 1, no. 2, pp. 96--99, 1985, doi: 10.13031/2013.26773.

\[45\] Richard G. Allen, Luis S. Pereira, Dirk Raes, and Martin Smith, *Crop evapotranspiration - Guidelines for computing crop water requirements - FAO Irrigation and drainage paper 56*, vol. Paper No. 56. Food and Agriculture Organization of the United Nations (FAO), 1998.

\[46\] World Meteorological Organization (WMO) and Global Water Partnership (GWP), *Handbook of Drought Indicators and Indices*. Geneva: WMO, 2016. \[Online\]. Available: https://library.wmo.int/idurl/4/55169

\[47\] S. M. Lundberg and S. I. Lee, "A Unified Approach to Interpreting Model Predictions," *Adv. Neural Inf. Process. Syst.*, vol. 2017-December, pp. 4766--4775, May 2017, Accessed: Jan. 02, 2026. \[Online\]. Available: https://arxiv.org/pdf/1705.07874

\[48\] T. Hastie, R. Tibshirani, and J. Friedman, *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*, 2nd ed. in Springer Series in Statistics. New York, NY: Springer New York, 2009. doi: 10.1007/978-0-387-84858-7.

 

**Plagiarism Report**

(Plagiarism should be less than 25%)

Attach the proof here.
