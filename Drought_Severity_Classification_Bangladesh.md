**Md. Alamin¹**, **SK Ikhtear Choton^2^**, **Md. Alomgir Hossain^3^**

Department of Computer Science and Engineering,

IUBAT---International University of Business Agriculture and Technology

4 Embankment Drive Road, Sector-10, Uttara Model Town, Dhaka-1230,
Bangladesh.

Corresponding author: <malaminswe@gmail.com>^1^,
[21303136@iubat.edu^2^](mailto:21303136@iubat.edu2),
alomgir.hossain@iubat.edu^3^

**Abstract**

Bangladesh faces increasing drought vulnerability under climate change
which is threatening agricultural and national food security. Existing
drought indices lack rigorous temporal validation and multi-scale
analysis for reliable early warning. Our study proposes an explainable
three-model ensemble framework (XGBoost 40%, Random Forest 35% and
CatBoost 25%) for drought classification using multi-scale SPEI across
35 meteorological stations from 1961 to 2023. The framework incorporates
76 engineered features capturing Bangladesh-specific patterns (such as
monsoon phases, agricultural seasons and temporal lags) and employs
five-fold walk-forward temporal cross-validation to prevent data
leakage. The ensemble method achieves 97.28% ± 0.41% accuracy and 99.68%
± 0.08% AUC (2011--2023), outperforming individual models: XGBoost
(97.35% accuracy, 99.77% AUC), CatBoost (97.44%, 99.76% AUC) and Random
Forest (94.20%, 98.82% AUC). SHAP-based explainability reveals that
multi-scale SPEI lag features and monsoon indicators dominate
predictions while regional analysis highlights higher vulnerability in
north-western Bangladesh. This framework provides the first 63-year
temporally validated drought classification system for Bangladesh and
achieving a superior performance compared to previous studies. The
ensemble SHAP analysis enables explainable operational deployment for
agricultural planning and early warning systems. It is providing a
scientifically rigorous and operationally ready drought monitoring
solution for Bangladesh\'s agricultural vulnerability.

**Keywords:**

Drought classification, Machine learning, SPEI, SHAP explainability,
Bangladesh, Temporal validation

**\
**

**1. Introduction**

Bangladesh is a densely populated South Asian nation with 175.7 million
(UNPF, 2025) re\`sidents. They face increasing drought vulnerability due
to climate change impacts on its mostly agricultural-dependent economy
(Mamun et al., 2018). In Bangladesh, 70% of the population working in
agriculture and rice cultivation which covering 75% of arable land,
drought events pose and significant threats to food security and
economic stability (Mohammad Alamgir Hossain et al., 2025a). The country
has three distinct agricultural seasons---Boro (December-May), Aus
(April-August), and Aman (June-December)--- each with have different
drought patterns.

**1.1 Bangladesh Climate Context and Drought Vulnerability**

Bangladesh\'s geographical location is in the tropical monsoon zone. The
location causes rainfall to vary a lot. About 80% of the annual rainfall
during the monsoon season (June-September) and prolonged dry periods
from November to April(Shahid and Behrawan, 2008). This seasonal
concentration creates acute water stress during the dry season,
particularly affecting the northwestern districts where annual rainfall
can be 30-40% lower than coastal regions (Md. R. Rahman and Lateh,
2016). The country has flat delta-shaped land with elevations mostly
below 10 meters above sea level. This makes it particularly prone to
hydrological extremes---floods during monsoons and droughts during dry
seasons.

Recent climate analyses indicate raise drought frequency and severity
across Bangladesh, along with ith the northwestern region experiencing
drought conditions in approximately 35-40% of years during the last two
decades (Sultana et al., 2021). Drought is a critical threat to food
security in Bangladesh. Particularly in the northwestern and
southwestern regions where millions of hectares of cropland and staple
crops such as rice are regularly affected. Annual crop losses can extend
to several million hectares which significantly reducing rice yields and
causing substantial economic losses for smallholder farmers (Farah et
al., 2025). More recently, in the 2018-2019 drought led to significant
irrigation water shortages, that affecting Boro rice cultivation---the
country\'s primary rice crop contributing to 55% of total rice
production. As the drought event occurs frequently so we need reliable
drought monitoring and early warning systems to support agricultural
planning and water resource management.

Drought impacts in Bangladesh extend well beyond direct agricultural
losses; they disrupt rural livelihoods, increase food prices, and
threaten national food security. The northwestern and southwestern
regions, where a large portion of the rural population depends on
rain-fed agriculture, are especially vulnerable to precipitation
deficits and climate extremes. Millions in these drought-prone areas
regularly face unstable crop yields, water shortages, and heightened
risks to their food and economic security (Farah et al., 2025).
Furthermore, groundwater level is lowering due to excessive irrigation
during drought periods has created long-term sustainability concerns. We
can see the water level in northwestern districts declining at rates of
0.5-1.0 meters per year (Dey et al., 2017).

**1.2 Evolution of Drought Monitoring Approaches**

Traditional drought monitoring in Bangladesh relies mostly on
single-scale indices like the Standardized Precipitation Index (SPI).
Which considers only precipitation without accounting for temperature
effects on evapotranspiration (Mckee et al., 1993). As temperatures
rise, more water evaporates from land and plants. This can cause
droughts even if rainfall is close to normal. So, this problem becomes
very serious when the weather gets hotter (Vicente-Serrano et al.,
2010). In the recent studies - demonstrated the superiority of
multi-scale SPEI analysis, incorporating precipitation and potential
evapotranspiration (PET) for comprehensive drought assessment (Mashuq et
al., 2024). However, existing Bangladesh drought studies suffer from
limited temporal validation, insufficient station coverage, and lack of
explainable artificial intelligence (X-AI) integration (Reshan et al.,
2025).

**1.3 Research Gaps and Motivation**

In previous Bangladesh drought studies, we have found several critical
limitations that hamper operational deployment and scientific
credibility. First, most studies apply random train-test splits that
ignore temporal autocorrelation in climate data. In that case, which is
leading to overly optimistic performance estimates that fail to
generalize to genuinely unseen future conditions \[(Paul et al.,
2024)\]. This methodological weakness particularly affects drought
prediction. We know droughts depend heavily on time-based patterns.
These include seasons and climate changes over many years. Temporal
dependencies are inherently strong due to seasonal patterns and
multi-year climate cycles. Second, insufficient SPEI scale coverage
remains prevalent. Most studies using only 3--4-time scales instead of
the recommended 8 scales. It is necessary to capture drought impacts
ranging from meteorological (1-3 months) to socio-economic (18-24
months) time frames (Hossain et al., 2024).

Third, lack of Bangladesh-specific feature engineering - represents a
missed opportunity to incorporate domain knowledge about monsoon
dynamics and agricultural calendars for Bangladesh that strongly
influence drought impacts in the region (Reshan et al., 2025). Existing
studies typically uses normal climate variables without considering
monsoon timing, pre-monsoon heat stress or critical crop growth time
specific to Bangladesh\'s rice-based agricultural system. Fourth,
absence of explainable artificial intelligence (X-AI) method, it limits
the operational uses of developed models. As stakeholders and
policymakers wants transparent and interpretable predictions to support
decision-making processes (Mohammad Alamgir Hossain et al., 2025b).
Without understanding that which factors have impacts on drought
predictions - it remains challenging to translate model outputs into
actionable agricultural advisories.

**1.4 Study Objectives and Ideas**

In this study we try to fix some important problems in drought
prediction by developing a comprehensive drought classification
framework with two new methodological ideas and highest performance for
Bangladesh drought monitoring.

First idea is about Temporal Cross-Validation for Bangladesh Drought
Studies. We implement rigorous 5-fold walk-forward temporal
cross-validation strategy - training on earlier historical data
(1961-2010/2015) and testing on temporally held-out later periods
(2011-2023). That were completely withheld during model training to
simulate operational forecasting conditions. Unlike previous Bangladesh
studies that applied random split or hold-out validation (Mashuq et al.,
2024), (Paul et al., 2024) where our temporal approach prevents data
leakage by ensuring test data represents future time periods relative to
training and providing realistic performance estimates for operational
deployment. This represents the first application of walk-forward
temporal validation for Bangladesh drought classification that is
establishing methodological best practice for future research.

The second idea is about Bangladesh-Specific Feature Engineering
Framework. We engineer 76 domain-informed features uniquely adjust to
Bangladesh\'s monsoon-driven climate and rice-based agricultural system
including: (1) 20 SPEI lag features covering all 8-time scales (1, 2, 3,
6, 9, 12, 18, 24 months) with safe lags preventing data leakage. (2) 10
Bangladesh-specific agricultural indicators encoding monsoon phases (dry
season, pre-monsoon, peak monsoon, post-monsoon) and crop seasons (Boro,
Aus, Aman) aligned with national rice production calendars. (3) 16
rolling statistics capturing temporal dynamics. (4) 12 seasonal
decomposition features for climate trend analysis. This represents the
first systematic integration of Bangladesh agricultural calendars and
monsoon dynamics into drought prediction models that demonstrating
measurable performance improvements over generic climate features.

In this study we have achieved highest Performance ever in Bangladesh.
Our ensemble framework achieves 97.28% ± 0.41% accuracy and 99.68% ±
0.08% AUC through temporal validation that is exceeding all previous
Bangladesh drought studies including the recent best performance of 96%
(Hossain, 2025). Which is representing a +1.28-percentage point
improvement. This performance gain, achieved with only 35 meteorological
stations compared to denser networks in international studies that
demonstrates the effectiveness of domain-informed feature engineering
and rigorous validation methodology.

Therefore, we can say our framework is Operational Deployment Readiness.
We provide comprehensive explainability through ensemble SHAP analysis
aggregating interpretations across all three models (XGBoost, Random
Forest, CatBoost) that is enabling transparent operational deployment.
Our framework identifies monsoon phase indicators contributing 3-8%
predictive power and agricultural season features showing 2.6-3.8%
importance and validating the practical utility of Bangladesh-specific
features for agricultural planning and water resource management.

**Our specific objectives are:** (1) Develop a three-model ensemble
machine learning framework (XGBoost, Random Forest, CatBoost) which is
optimized through grid search for Bangladesh drought classification. (2)
Implement rigorous 5-fold walk-forward temporal cross-validation trained
on earlier historical data (1961-2010/2015) and validated on temporally
held-out later periods (2011-2023) from 35 meteorological stations that
is ensuring realistic performance estimates that reflect operational
forecasting conditions. (3) Use Bangladesh-specific features including
monsoon phases (dry, pre-monsoon, peak monsoon, post-monsoon) and
agricultural seasons (Boro, Aus, Aman). (4) Apply comprehensive SHAP
analysis for model explainability and feature importance quantification.
(5) Establish a first temporally validated model with multi-scale SPEI
drought classification system for Bangladesh with hight accuracy
performance compared to others.

**2. Literature Review**

**2.1 Drought Monitoring and SPEI Applications**

Drought monitoring has been developed significantly from simple
precipitation-based indices to comprehensive multi-variable approaches
such as incorporating temperature, evapotranspiration and soil moisture
(AghaKouchak et al., 2015). The Standardized Precipitation
Evapotranspiration Index (SPEI) was introduced by Vicente-Serrano et al.
(Vicente-Serrano et al., 2010) that is representing a major advancement
by combining precipitation and potential evapotranspiration into a
single standardized measure. SPEI\'s multi-scale capability helps to
simultaneous monitoring of meteorological (1-3 months), agricultural
(3-6 months), hydrological (6-12 months) and socio-economic (12-24
months) drought conditions. That is making it particularly suitable for
comprehensive drought assessment (Sultana et al., 2023).

International applications of SPEI have demonstrated its better quality
over precipitation-only indices; particularly in regions that
experiencing rising temperatures increase evaporative demand over time
(Kumar et al., 2016). Studies in semi-arid regions of Spain, Australia,
and China have shown that SPEI helps earlier drought detection and
better correlation with agricultural impacts compared to SPI (Noguera et
al., 2023), (Dikshit et al., 2020), (Xu et al., 2024). The multi-scale
nature of SPEI allow stakeholders to assess drought conditions relevant
to their specific needs such as farmers are focusing on 3-6 month scales
for crop planning, water resource managers monitoring 9-12 month scales
for reservoir management and policymakers tracking 12-24 month scales
for long-term planning.

Recent AI studies that explain model behavior show something is
important or considered while they make prediction. SPEI features at
different time scales are very useful for predicting droughts. Research
in Turkey using SHAP analysis on 4 meteorological stations showed that
lagged SPEI-12 values are the primary features of predictive accuracy.
It clearly shows that CatBoost achieving R² is up to 0.86 (Ozupek et
al., 2025). Similarly, another study in China combining XGBoost and SHAP
on 61+ years of gridded data revealed that diurnal temperature range
(DTR) is a powerful negative driver of short-term drought, which is
operating via dual pathways with significant regional variability (Feng
et al., 2025). These findings highlights the importance of both
multi-scale temporal indices and temperature-related features for
comprehensive drought assessment. On the other hand, in semi-arid
regions of Morocco\'s Upper Drâa Basin, ensemble tree-based methods for
predicting 3 and 12-month SPEI which achieved high performance (NSE:
0.83--0.93, R²: 0.92--0.93), showing the effectiveness of multi-scale
SPEI for an operational drought prediction in data-constrained
environments (En-Nagre et al., 2024).

**2.2 Machine Learning for Drought Classification**

Machine learning method have gained a good coverage in drought
classification due to their ability to capture complex nonlinear
relationships between climate variables and drought occurrence (Wang et
al., 2024). Ensemble methods, particularly the based ML models such as
Random Forest, XGBoost, and gradient boosting variants have been showing
their high performance compared to traditional statistical approaches.
These models are achieving accuracies exceeding 90% in various regional
studies (Wang et al., 2024), (Md Alomgir Hossain et al., 2025a), (Zhang
et al., 2019), (Kukartseva et al., 2024). The ensemble paradigm combines
multiple base models to improve predictions\' robustness and reduce
overfitting. That is why making it particularly suitable for climate
applications where training data may be limited and feature
relationships complex.

Machine learning models are often called "black boxes" because it's hard
to understand how they work. In recent progress in explainable AI helps
to solve the \"black box\" criticism of machine learning models. SHAP
analysis is now a popular way to explain model decisions, especially in
climate science (S. Lundberg and Lee, 2017). SHAP provides both global
feature importance rankings and individual prediction explanations which
is allows stakeholders to understand how the model decide; not just what
the model predicts. This transparency is important for building trust in
operational deployment and identifying potential model weaknesses or
biases. A comprehensive study for the United States using county-level
drought impacts demonstrated that XGBoost combined with SHAP analysis.
Which is achieved F2 scores of 0.88 nationally, with lagged SPI/STI
indices dominating impact prediction (Zhang et al., 2023).

Deep learning approaches including LSTM networks and CNN architectures
have shown their promise for drought forecasting in data-rich
environments (Intelligence and Neuroscience, 2023), (Xiao et al., 2024),
(Shen et al., 2019),(Maity et al., 2021). However, these methods
typically need extensive training data and computational resources. This
makes it hard to use in developing countries. In those places, there may
not be enough data available. So, the method may not work well in those
situations. A hybrid CNN-based study for long-term drought severity
forecasting in Upper Egypt showed that the CNN-LSTM excelled in training
while CNN-SVR performed best in testing that highlighting the
effectiveness of deep learning integration for drought management
(Elbeltagi et al., 2024). In China\'s Huaihe River Basin, Deep Belief
Networks (DBNs) consistently better than traditional BP neural networks
for short-term drought prediction especially as SPI timescale increased
(Chen et al., 2012). In Indonesia for regional applications, adaptive
neuro-fuzzy inference systems (ANFIS) have shown promise that
dramatically lowering RMSE (to 0.016--0.017) by incorporating local
meteorological parameters (Sihananto et al., 2017). Furthermore, deep
learning models often sacrifice interpretability for performance. That
is why it making them less suitable for operational systems. Because it
requires transparent decision-making processes. A global IoT-fog-cloud
architecture uses DNN and achieved 95.36% accuracy for drought
assessment. Although the computational requirements remain challenging
for resource-constrained environments (Kaur and Sood, 2020).

**2.3 Bangladesh Drought Studies**

Bangladesh drought research has progressed from descriptive
climatological studies to predictive machine learning applications over
the past decade. Pioneering work identifying meteorological
drought-prone areas in Bangladesh applied the Standardized Precipitation
Index (SPI) across multiple time scales and seasons using GIS-based
spatial mapping (Mamun et al., 2018)(M. R. Rahman and Lateh, 2016).
Using SPI-3, SPI-4, and SPI-5 grids from historical data (1980--2015)
across 35 meteorological stations, researchers identified persistent
drought-prone regions in northwest, central, and southern-western
Bangladesh with actionable differentiation between short-term
meteorological droughts and prolonged seasonal dryness (Mamun et al.,
2018)(M. R. Rahman and Lateh, 2016). These climatological studies
demonstrated that the Pre-Kharif and Rabi seasons are most vulnerable to
meteorological drought, with Rabi season showing an increasing drought
trend of 8.66% per decade (Mamun et al., 2018), establishing the
foundation for transitioning toward machine learning-based drought
classification and forecasting in more recent Bangladesh drought
research.

Time series forecasting methods have been applied to southwestern
Bangladesh drought prediction with PROPHET and SARIMA models which is
achieving a strong predictive power (R²: 0.75--0.88) across four
districts (Mohammad Alamgir Hossain et al., 2025b). These approaches
provide early warning with actionable lead time for local policymakers.
Although they focus on forecasting rather than classification.
District-level SPI analysis using Facebook Prophet for moderate drought
occurrences in Dinajpur demonstrated moderate accuracy (RMSE 1.17) but
highlighted the importance of long-term planning for drought-vulnerable
regions (Hossain et al., 2024). En-Nagre et al. (En-Nagre et al., 2024)
showed the potential of combining SPEI with machine learning algorithms
(Random Forest, Voting Regressor, AdaBoost, and KNN) for meteorological
drought prediction in the semi-arid Upper Draa Basin of Morocco. Their
models achieved high predictive performance (R² up to 0.97 and NSE up to
0.93 for SPEI-3). However, the study relied on a simple 80/20 split
without temporal cross-validation, and it did not include explain
ability or feature-importance analysis.

More recently, Khan et al. (Mashuq et al., 2024) conducted SPEI-based
drought prediction using XGBoost across **a** single station (Ishwardi
Upazila) from 1981--2017 which result in NSE up to 0.92 (for SPEI-1)
rather than 88.7% accuracy . This study advanced Bangladesh drought
research by demonstrating the superiority of gradient boosting methods.
But only apply random split validation and limited to SPEI scale
coverage (only 4 scales: SPEI-1, 3, 6, and 12).

An advanced study examining Ishwardi Upazila evaluated SVM, RF, XGBoost,
DT, and KNN on SPEI drought indices along with XGBoost. Amongst them
XGBoost performed best for SPEI-1 (NSE = 0.92), and RF performed best
for SPEI-3 (NSE = 0.24), not RMSE 0.11--0.18 or NSE up to 0.89 . This
result emphasizing the value of ML models for accurately capturing rapid
local droughts in the Bangladeshi context (Mashuq et al., 2024).
Chowdhury et al. (Paul et al., 2024) applied satellite data for enhanced
drought analysis which shows increases result achieving 92% accuracy
than other studies through an ensemble machine learning approach across
38 districts . Similarly, satellite-driven weather data for 38
Bangladesh districts using clustering and classification models. They
shown Random Forest achieving 92% accuracy with actionable drought
hotspot identification. While representing significant progress these
studies used cross-validation without temporal ordering; It might
potentially leading to data leakage. Recent ensemble learning approaches
have demonstrated higher performance for Bangladesh drought
applications. In Central Bangladesh, ensemble ML methods (RF, XGBoost,
SVM) combined with ARIMA for long-range predictions using SPI, SPEI, and
ZSI indices revealed Random Forest providing the best accuracy
(93.8%--94.0%). Spatial mapping highlighting the drought hotspots for
targeted policy responses (Md Alomgir Hossain et al., 2025b). In
Rajshahi, multiple ML models (Gradient Boosting, XGBoost, RF, CatBoost,
hybrids) on SPEI-linked weather data (1965--2022) achieved single-model
accuracy of 85%--88% and ensemble accuracy of 92%--96%, which is proving
ensemble ML as a blueprint for future-ready drought anticipation
(Hossain, 2025). The most recent comprehensive review by Hasan et al.
(Reshan et al., 2025) **clarified** the drought modeling techniques
across the South Asian countries. The study **identified** key gaps
including insufficient temporal validation, limited integration of
regional climate features, and absence of explainability methods. A
systematic review of **142 studies** documented dominant use of SPI/SPEI
and supervised/ensemble ML/DL **methods**. But the study noted regional
data gaps and lack of explainability of prediction and **called** for
integration with XAI-driven models for next-generation drought modeling
(Reshan et al., 2025). In the studies of Ahmed et al. (Hossain et al.,
2024) achieved **88.7% accuracy** for drought prediction in eastern
Bangladesh but they work with only **38 years (1981--2018)** with
limited feature engineering beyond basic climate variables. These
studies collectively demonstrate growing sophistication in Bangladesh
drought researches while highlighting persistent methodological gaps
that our study addresses.

**3. Materials and Methods**

**3.1 Study Area and Data Collection**

**Geographic Coverage:** Bangladesh (20.7°-26.6°N, 88.0°-92.7°E)
encompasses 35 meteorological stations across 8 administrative
divisions. This is providing comprehensive spatial coverage from coastal
regions to inland areas (Figure 1).

![](/home/z/my-project/download/media/media/image1.png){width="6.5in"
height="5.270833333333333in"}

**Figure 1:** Study Area Map showing 35 meteorological stations across
Bangladesh.

**Data Source:** Meteorological data from the Bangladesh Meteorological
Department (BMD) was obtained from the Mendeley repository
(<https://data.mendeley.com/datasets/tbrhznpwg9/1>) which has daily
measurements of precipitation, temperature, humidity, and sunshine
hours.

**Temporal Coverage:** Data spans 1961-2023 (63 years), providing 17,868
monthly observations. Although Bangladesh gained independence in 1971
but we utilized pre-independence data as the BMD maintained continuous
operations of the same station network throughout this period that is
ensuring data continuity and maximizing temporal coverage for robust
model training.

**Data Quality:** The dataset exhibits 67.5% coverage across all
stations and time periods which is typical for long-term meteorological
datasets in developing countries. Missing data primarily occurred due to
station establishment at different time periods. Most stations achieving
full coverage from 1990 onwards.

To assess data reliability and model validity for the recent modern
period we compared our SPEI-12m drought classifications against
documented drought events in Bangladesh during 2000--2023. Published
research has documented significant meteorological drought occurrences
during this period. That's including the **severe droughts in
northwestern Bangladesh reported for 1973, 1978, 1979, 1981, 1982, 1992,
1994--1995, and 2000** (Shahid and Behrawan, 2008). Another drought
events during **2009--2010** affecting agricultural production **were
documented in both studies** (Mashuq et al., 2024), (Hossain et al.,
2024)---with the SPICSCON study identifying **SPEI-based drought
occurrences in 2009 and 2010**, and the AWM study confirming
**SPI-detected drought years including 2010**. In the pre-monsoon
drought period affecting Aus crop cultivation (Khondakar et al., 2022)
and in the 2018--2019 drought episodes in northern regions (Sadiq et
al., 2023), independently reported drought impacts provide additional
validation points. Our SPEI-based drought detection algorithm identified
all eight documented major drought years (2000, 2006, 2009, 2010, 2013,
2014, 2018, 2019). That have been reported in government assessments and
peer-reviewed literature which achieving strong concordance (8/8 events
detected) with independently documented drought occurrences. This
validation provides confidence in data quality and model reliability
particularly for the recent period (2000-2023). While historical period
data (1961-1999) shows moderate reliability with some limitations due to
sparser station coverage during that era. Notably our data correctly
identified the 1974 Bangladesh Famine period as experiencing
above-normal rainfall rather than meteorological drought which is
confirming that this famine was primarily caused by widespread flooding
rather than drought conditions. Which underscores the critical
distinction between socio-economic famine events and meteorological
drought phenomena. This validation approach ensures that our reported
model performance metrics (97.27% ± 0.41% accuracy) are based on the
most reliable portion of the dataset with external verification against
published drought documentation.

**3.2 Data Processing and Quality Control**

**Daily to Monthly Aggregation**

Daily weather data were sum up into monthly totals for precipitation and
mean for temperature, humidity, and sunshine. Monthly aggregation
reduces noise while preserving seasonal patterns which is essential for
drought analysis. Months with no available daily observations were
excluded from the analysis which is resulting in a dataset with 95.3%
completeness across all station-month combinations.

**Missing Data Handling**

During feature engineering and model training the missing values in the
feature matrices (primarily due to insufficient historical data for lag
feature calculation) were imputed using simple mean imputation.
Specifically, the missing values in the training features were filled
with the mean of the corresponding feature across all available training
samples. And the same training-derived mean were applied to test
features to prevent the data leakage. This approach maintains complete
feature sets - which is required for ensemble model training while
preserving the temporal validation framework.

**Table 1:** Dataset Summary showing total records, spatial coverage,
temporal span, engineered features, and data completeness metrics.

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

**3.3 PET and SPEI Calculation**

**Potential Evapotranspiration (PET):** Calculated using the
Hargreaves-Samani method \[44\] which requires only temperature data and
it is suitable for Bangladesh\'s data availability:

> $$\begin{array}{r}
> \mathbf{PET} = \mathbf{0.0023} \times \mathbf{R}_{\mathbf{a}} \times \left( \mathbf{T}_{\mathbf{mean}} + \mathbf{17.8} \right) \times \sqrt{\mathbf{T}_{\mathbf{\max}} - \mathbf{T}_{\mathbf{\min}}}\ \mathbf{\#}(1)
> \end{array}$$

Where,

$\left( \text{PET} \right)$= Potential evapotranspiration
$\left( mm\ day(^{- 1} \right)$

$\left( T_{\text{mean}} \right)$ = Mean daily temperature (°C)

$\left( T_{\text{max}} \right)$ = Maximum daily temperature (°C)

$\left( T_{\text{min}} \right)$ = Minimum daily temperature (°C)

$\left( R_{a} \right)$ = Extraterrestrial radiation
$MJ\ \left( m^{- 2} \right)\ \left( day^{- 1} \right)$ ,

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

**Multi-Scale SPEI Calculation**

The **Standardized Precipitation Evapotranspiration Index (SPEI)** was
computed for multiple time scales\
(k=1,2,3,6,9,12,18,24k = 1, 2, 3, 6, 9, 12, 18, 24k=1,2,3,6,9,12,18,24
months) using the **log-logistic probability distribution fitting
method** \[10\].

**Step 1: Climatic Water Balance**

> $$\begin{array}{r}
> D_{i}^{k} = \sum_{j = i - k + 1}^{i}{(P_{j} - {PET}_{j}}\ \#(3)
> \end{array}$$

Where, $D_{i}^{k}$ = accumulated difference between precipitation
$(\mathbf{P})\ $and potential evapotranspiration $(\mathbf{PET})$ for
the past $\mathbf{k}$ months. This accumulation process (Equation 3) was
applied identically to all 8-time scales (k = 1, 2, 3, 6, 9, 12, 18, 24
months), yielding 8 SPEI time series per station.

Step 2: Log-Logistic Distribution

> $$\begin{array}{r}
> F(x) = \left\lbrack 1 + \left( \frac{\alpha}{x - \gamma} \right)^{\beta} \right\rbrack^{- 1}\ \#(4)
> \end{array}$$

Where, $\alpha,\ \beta\ and\ \gamma$ are the **scale**, **shape**, and
**location** parameters, respectively, estimated using the **L-moments**
method.

Step 3: Standardized SPEI Calculation

> $$\begin{array}{r}
> SPEI = W - \ \frac{C_{0} + C_{1}W + C_{2}W^{2}}{1 + d_{1}W + d_{2}W^{2} + d_{3}W^{3}}\ \#(5)
> \end{array}$$

Where
$W = \ \sqrt{- 2\ln(P)}for\ P \leq 0.5,\ and\ C_{0}{,\ C}_{1,}\ C_{2,}\ d_{1},\ d_{2,\ }d_{3}$
are constant for the standard normal distribution approximation.

**Drought Classification**

Binary drought classification was based on **SPEI-12** values:

> $$\begin{array}{r}
> Drought = \ \left\{ \begin{array}{r}
> 1,\ \ if\ {SPEI}_{12m} < \  - 0.5\ (moderate\ drought) \\
> 0,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ otherwise\ (no\ drought)\ 
> \end{array} \right.\ \ \#(6)
> \end{array}$$

Following World Meteorological Organization standards for drought
severity classification (World Meteorological Organization (WMO) and
Global Water Partnership (GWP), 2016)

![](/home/z/my-project/download/media/media/image2.png){width="6.36in"
height="3.6073982939632545in"}

**Figure 2a:** Short-term SPEI Time Series (SPEI-1m, 2m) showing
immediate weather drought impacts (1961-2023).

![](/home/z/my-project/download/media/media/image3.png){width="6.5in"
height="3.6868055555555554in"}

**Figure 2b:** Medium-term SPEI Time Series (SPEI-3m, 6m) showing
agricultural drought impacts affecting crop growth.

![](/home/z/my-project/download/media/media/image4.png){width="6.5in"
height="3.6868055555555554in"}

**Figure 2c:** Long-term SPEI Time Series (SPEI-9m, 12m) showing
hydrological drought impacts on water resources.

![](/home/z/my-project/download/media/media/image5.png){width="6.5in"
height="3.6868055555555554in"}

**Figure 2d:** Very Long-term SPEI Time Series (SPEI-18m, 24m) showing
socio-economic drought impacts.

![](/home/z/my-project/download/media/media/image6.png){width="6.5in"
height="3.2222222222222223in"}

**Figure 2e:** Key SPEI Scales Summary (3m, 6m, 12m, 18m and 24m) with
major drought events highlighted.

**3.4 Feature Engineering**

**Total Features:** 76 features across 6 categories:

**Base Climate Features (8):** Rainfall_Total, Temperature_Mean,
Max_Temperature, Min_Temperature, Humidity_Mean, PET_mm_month,
Water_Balance, Ra_MJ_m2_day

**Spatial Features (6):** Latitude, Longitude, Lat_normalized,
Lon_normalized, Distance_to_Bay, Station_encoded

**SPEI Lag Features (20):** Historical SPEI values were used with
planned time delays across all 8 scales to avoid data leakage and track
drought over time.

Feature design: SPEI-1m (lags: 1,3,6,12 months), SPEI-3m (lags:
1,3,6,12), SPEI-6m (lags: 1,3,6,12), SPEI-9m (lags: 3,6), SPEI-12m
(lags: 1,3), SPEI-18m (lags: 1,3), SPEI-24m (lags: 1,3). Total:
4+4+4+2+2+2+2 = 20 SPEI lag features that are enabling the model to
learn from short-term, medium-term and long-term historical drought
patterns.

**Temporal Features (18):**

Seasonal decomposition components (6 features): Rainfall_trend,
Rainfall_seasonal, Rainfall_residual, Temp_trend, Temp_seasonal,
Temp_residual using additive model:

> $$\begin{array}{r}
> X_{t} = T_{t} + S_{t} + R_{t}\ \#(7)
> \end{array}$$

where ​$\mathbf{X}_{\mathbf{t}}$ = observed value,
$\mathbf{T}_{\mathbf{t}}$​ = trend component, $\mathbf{S}_{\mathbf{t}}$ =
seasonal component, and $\mathbf{R}_{\mathbf{t}}$= residual component.

**Fourier features for cyclic patterns (6 features):** *sin_month_12,
cos_month_12, sin_month_6, cos_month_6, sin_month_3, cos_month_3:*

> $$\begin{array}{r}
> F_{\sin}(t,\ k) = \sin\left( \frac{2\pi t}{k} \right),\ F_{\cos}(t,\ k) = \cos\left( \frac{2\pi t}{k} \right)\ \#(8)
> \end{array}$$

*Where,* $k\  \in \ \left\{ 3,\ 6,\ 12 \right\}\ $months for quarterly,
semi-annual, and annual cycles.

***Advanced Bangladesh-specific temporal features (6 features):**
monsoon_onset, pre_monsoon_heat, critical_crop_month,
rainfall_deficit_cumul, months_since_heavy_rain, Year_normalized*

***Rolling Statistics (16):** Moving window statistics for temporal
smoothing:*

> $$\begin{array}{r}
> \mu_{w}(t) = \frac{1}{w} \times \sum_{i = 0}^{w - 1}X_{t - i}\ \#(9)
> \end{array}$$

$$\begin{array}{r}
\sigma_{w}(t) = \ \sqrt{\frac{1}{w} \times \sum_{i = 0}^{w - 1}\left( X_{t - i} - \mu_{w} \right)^{2}}\ \#(10)
\end{array}$$

*Where,* $w\  \in \ \left\{ 3,\ 6,\ 12 \right\}\ months\ window\ size,$
calculated for rainfall and temperature (3-month: 6 features, 6-month: 6
features, 12-month: 4 features) and PET (3-month: 2 features, 6-month: 2
features).\
**Total:** 6+6+4=16 rolling statistics features capturing temporal
dynamics at multiple scales.

**Bangladesh-Specific Features (8)**

**Monsoon Phase Indicators Using Temporal Windows (4 Features)**

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

Agricultural Season Indicators Aligned with Bangladesh Rice Cropping
Calendar (3 Features)

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

Monsoon intensity indicator (1 feature): Is_Monsoon = Phase_peak
(derived from peak monsoon phase)

**Data Leakage Prevention:** To ensure valid temporal prediction
features derived from target time scale were excluded:

> $$\begin{array}{r}
> Excluded\ Feature = \ \left\{ {SPEI}_{6m},\ {SPEI}_{12m},{Drought_{Class}}_{*} \right\}\ \#(18)
> \end{array}$$
>
> $$\begin{array}{r}
> Safe\ Features = \left\{ {SPEI}_{1m},\ {SPEI}_{2m},{SPEI}_{3m} \right\}\ with\ temporal\ lags\ \mathrm{\Delta}t\  \geq 3\ months\ \#(19)
> \end{array}$$
>
> $\ $![](/home/z/my-project/download/media/media/image7.png){width="6.5in"
> height="4.629861111111111in"}

**Figure 3:** Methodology Flowchart illustrating the complete framework
from data processing to ensemble prediction.

**3.5 Machine Learning Ensemble**

**Base Models:** Three high-performance machine learning algorithms were
selected based on their complementary strengths and proven effectiveness
in drought classification:

-   **XGBoost:** Gradient boosting decision trees with optimized
    hyperparameters (n_estimators=723, max_depth=9, learning_rate=0.035,
    subsample=0.72, colsample_bytree=0.84) achieving 94.14% individual
    accuracy

-   **Random Forest:** Ensemble of 700 decision trees with max_depth=18,
    providing robust baseline performance (92.44% accuracy) and
    resistance to overfitting

-   **CatBoost:** Gradient boosting with advanced categorical feature
    handling (iterations=700, depth=8) achieving the highest individual
    model accuracy (94.63%)

**Ensemble Strategy:** Weighted averaging approach combining predictions
from three base models:

$$\begin{array}{r}
P_{ensemble}(x) = \ \sum_{i \in \left\{ XGB,\ RF,\ CatBoost \right\}}^{}{w_{i}P_{i}(x)}\ \#(20)
\end{array}$$

Where, $P_{ensemble}(x) = \ Final\ ensemble\ prediction\ probability$,

$P_{i}(x) = Prediction\ probability\ from\ model\ \mathbf{i}$**,**

$w_{i} = \ Weight\ for\ model\ \mathbf{i,}\ constrained\ by\ \sum_{i}^{}{w_{i} = 1,\ w_{i}\  \geq 0\ }\ $

**Weight Optimization:** Grid search over weight space:

$$\begin{array}{r}
w^{*} = \arg\max_{w}\ CV_{accuracy(w)}\ subject\ to:\ w_{XGB} + \ w_{RF} + \ w_{CB} = 1\ \ \ \ \ w_{i} \in \ \lbrack 0,\ 1\rbrack\ \#(21)
\end{array}$$

Optimal weights determined:
$w_{XGB} = 0.40,\ \ w_{RF} = 0.35,\ \ \ w_{CB} = 0.25$ based on the
temporal cross-validation performance.

![](/home/z/my-project/download/media/media/image8.png){width="5.103999343832021in"
height="3.6605938320209974in"}

**Figure 4:** Ensemble architecture visualization showing weighted
averaging approach (3 models: 40%, 35%, 25%).

**Final Classification:** Binary decision using threshold:

> $$\begin{array}{r}
> y_{pred} = \ \left\{ \begin{array}{r}
> 1,\ \ \ \ \ \ if\ P_{ensemble}(x)\  \geq 0.5\ (drought) \\
> 0,\ {if\ P}_{ensemble}(x)\  < 0.5\ (no\ drought)
> \end{array} \right.\ \ \#(22)
> \end{array}$$

**Hyperparameter Optimization:** Optuna framework with Bayesian
optimization:

> $$\begin{array}{r}
> \theta^{*} = \arg{\max_{\theta}\mathbb{\ E\ }\left\lbrack CV_{score(\theta)} \right\rbrack\ \ }\#(23)
> \end{array}$$

Where $\mathbf{\theta}\ $represents the hyperparameter vector, optimized
over 50 trials per model using the Tree-structured Parzen Estimator
(TPE) for efficient search.

**Feature Scaling:** StandardScaler normalization applied:

> $$\begin{array}{r}
> X_{scaled} = \ \frac{X - \mu}{\sigma}\ \#(24)
> \end{array}$$

$where\ \mathbf{\mu}\  = \ mean\ and\ \mathbf{\sigma}\ $ standard
deviation computed on training data only to prevent information leakage.

**3.6 Temporal Cross-Validation**

**Validation Strategy:** 5-fold walk-forward temporal cross-validation
ensuring train-past, test-future methodology:

> For fold $\mathbf{k:}$
>
> $$\begin{array}{r}
> {Train}_{k} = \left\{ \left( x_{i},\ y_{i} \right):\ t_{i} < \ T_{k} \right\}\ \#(25)
> \end{array}$$
>
> $$\begin{array}{r}
> {Test}_{k} = \left\{ \left( x_{j},\ y_{j} \right):\ T_{k} \leq T_{j} < \ T_{k + 1} \right\}\ \#(26)
> \end{array}$$

Where $T_{k}$​ is the cutoff time (year) for fold $\mathbf{k}$, ensuring
no future information leaks into past training.

**Temporal Splits:** Walk-forward validation strategy with 5 folds
(Table S1):

  ----------------------------------------------------------------------------------------------
  Fold   Cutoff Year                   Training    Testing     Train    Test     Validation
         ($\mathbf{T}_{\mathbf{k}}$)   Period      Period      Years    Years    Strategy
  ------ ----------------------------- ----------- ----------- -------- -------- ---------------
  1      2010                          1961-2010   2011-2015   50 years 5 years  Train past →
                                                                                 Test future

  2      2013                          1961-2013   2014-2017   53 years 4 years  Train past →
                                                                                 Test future

  3      2016                          1961-2016   2017-2020   56 years 4 years  Train past →
                                                                                 Test future

  4      2019                          1961-2019   2020-2023   59 years 4 years  Train past →
                                                                                 Test future

  5      2015                          1961-2015   2016-2023   55 years 8 years  Train past →
                                                                                 Test future
  ----------------------------------------------------------------------------------------------

**Key Feature:** Each fold trains on earlier historical data and tests
on temporally held-out later periods, with test data completely withheld
during training to simulate operational forecasting conditions where
future data arrives sequentially. This walk-forward approach ensures
that model performance metrics reflect realistic predictive capability
for operational drought early warning systems.

**Evaluation Metrics:** Comprehensive performance assessment using:

**Accuracy:**$\begin{array}{r}
Accuracy = \ \frac{TP + \ TN}{TP\  + \ TN\  + \ FP\  + FN}\ \#(27)
\end{array}$

> Precision (Positive Predictive Value):
>
> $$\begin{array}{r}
> Precision = \ \frac{TP}{TP + FP}\ \#(28)
> \end{array}$$
>
> Recall (Sensitivity, True Positive Rate):
>
> $$\begin{array}{r}
> Recall = \ \frac{TP}{TP + FN}\ \#(29)
> \end{array}$$
>
> F1-Score (Harmonic Mean):
>
> $$\begin{array}{r}
> F1 = 2\  \times \ \frac{Precision\  \times Recall}{Precision + Recall}\ \#(30)
> \end{array}$$
>
> Specificity (True Negative Rate):
>
> $$\begin{array}{r}
> Specificity = \ \frac{TN}{TN + FP}\ \#(31)
> \end{array}$$
>
> AUC (Area Under ROC Curve):
>
> $$\begin{array}{r}
> AUC = \ \int_{0}^{1}{TPR(FPR)\ d(FPR)}\ \#(32)
> \end{array}$$

Where
$TP = True\ Positive,\ TN = True\ Negative,\ FP = False\ Positive,\ FN = False\ Negative$

> Aggregated Performance:
>
> $$\begin{array}{r}
> \mu_{metric} = \ \frac{1}{K} \times \sum_{k = 1}^{5}{metric}_{k}\ \#(33)
> \end{array}$$

$$\begin{array}{r}
\sigma_{metric} = \ \sqrt{\ \frac{1}{K} \times \sum_{}^{}\left( {metric}_{k} - \ \mu \right)^{2}}\ \#(34)
\end{array}$$

**3.7 Explainability Analysis**

**SHAP Implementation:** SHapley Additive exPlanations (SHAP) using
TreeExplainer for model interpretability. SHAP values based on
cooperative game theory (S. M. Lundberg and Lee, 2017) :
$\begin{array}{r}
\varnothing_{j}(x) = \sum_{S \subseteq \left\{ 1,\ \ldots,M \right\}\backslash\left\{ j \right\}}^{}{\frac{|S|\ !\ \left( M\  - |S| - 1\  \right)!}{M!}\left\lbrack f_{S \cup \left\{ j \right\}\ }\left( x_{S \cup \left\{ j \right\}} \right) - f_{S}\left( x_{S} \right) \right\rbrack}\ \#(35)
\end{array}$

Where,
$\varnothing_{j}(x) = SHAP\ value\ for\ feature\ \mathbf{j}\mathbf{,\ }$
$S \subseteq \left\{ 1,\ \ldots,M \right\}\backslash\left\{ j \right\} = subset\ of\ features,$

$f_{S}\left( x_{S} \right) = model\ prediction\ using\ feature\ subset\ \mathbf{S,\ \ }and\ \mathbf{M =}total\ number\ of\ features$

**Global Feature Importance:** Aggregated across all samples:

> $$\begin{array}{r}
> {Importance}_{j} = \ \frac{1}{N} \times \sum_{i = 1}^{N}{|\varnothing_{j}\left( x_{i} \right)}\ \#(36)
> \end{array}$$

**Feature Importance Analysis:** SHAP values computed to quantify each
feature\'s contribution to individual predictions and overall model
behavior, enabling transparent understanding of drought prediction
factors.

**3.8 Statistical Analysis and Model Evaluation**

**Core Performance Indicators:** Our model\'s performance was
comprehensively assessed using different metrics. We measured overall
correctness with Accuracy, while Precision quantified the reliability of
its positive (drought) predictions. To evaluate its sensitivity for
successfully identifying actual droughts, we used Recall. The F1-score
shows a balance between precision and recall. The AUC measures how well
the model can tell different classes apart (Hastie et al., 2009).

**Validation Approach:** Our cross-validation strategy was designed to
simulate the real-world conditions. We used stratified temporal splits
which maintained the data\'s chronological order and also confirmed a
balanced representation of drought instances in each fold. In this
setup, models were trained on all historical data up to a certain year
and then tested only on the following year\'s data, reflecting a true
predictive scenario.\
\
**Assessing Statistical Significance:** We used McNemar\'s test to
determine if the performance gains from our ensemble method were
statistically significant when compared to the individual models. To
measure how uncertain the results were we calculated confidence
intervals using 1,000 rounds of random sampling.

**4. Results and Discussion**

**4.1 Temporal Cross-Validation Performance**

**Overall Performance:** The ensemble model achieved a highest 97.28% ±
0.41% accuracy across 5 temporal splits. Which is demonstrating robust
performance on temporally held-out test data that is representing future
periods relative to training (Table 2). AUC reached 99.68% ± 0.08% that
is indicating exceptional discrimination capability between drought and
non-drought conditions. These results shows a significant advancement
over previous Bangladesh drought studies. With our temporal validation
providing realistic performance estimates for operational deployment.

**Table 2: Temporal Cross-Validation Detailed Metrics**

  ---------------------------------------------------------------------------------------------------
  Fold    Train       Test Period Train    Test    Accuracy   AUC (%) F1-Score   Precision   Recall
          Period                  Size     Size    (%)                (%)        (%)         (%)
  ------- ----------- ----------- -------- ------- ---------- ------- ---------- ----------- --------
  1       1961-2010   2011-2015   14,256   1,784   97.00      99.58   96.72      96.57       96.87

  2       1961-2013   2014-2017   15,984   1,680   96.67      99.59   95.16      95.82       94.50

  3       1961-2016   2017-2020   16,848   1,512   97.32      99.75   96.06      96.65       95.48

  4       1961-2019   2020-2023   17,712   1,344   97.86      99.78   97.82      97.82       97.82

  5       1961-2015   2016-2023   16,488   2,688   97.53      99.73   96.94      97.55       96.34

  Mean    \-          \-          16,257   1,802   97.28      99.68   96.54      96.88       96.20

  Std     \-          \-          1,148    467     ±0.41      ±0.08   ±0.89      ±0.72       ±1.14
  ---------------------------------------------------------------------------------------------------

![](/home/z/my-project/download/media/media/image9.png){width="6.5in"
height="2.52in"}

**Figure 4:** Temporal Cross-Validation Results showing 5-fold
performance with error bars.

**Split-wise Analysis**: Our Temporal Cross-Validation Performance shows
the remarkable consistency across temporal splits with Split 4
(2020-2023) achieving the highest accuracy (97.86%) and Split 2
(2014-2017) showing the lowest (96.67%). That is indicating robust model
performance across varying climate conditions (Figure 4). The low
standard deviation (±0.41%) confirms exceptional temporal stability
which is critical for operational drought early warning systems.

**Comparison with Previous Studies:** Our temporal validation (97.28%)
substantially exceeds all previous Bangladesh drought studies: Khan et
al. (Mashuq et al., 2024) achieved 88.7% using XGBoost with random
validation. Paul et al. (Paul et al., 2024) achieved 92% using
traditional machine learning classifiers without temporal ordering, and
Hossain et al. (Hossain, 2025) achieved 96% ensemble accuracy in
Rajshahi using SPEI-based ML models, demonstrating the importance of
advanced feature engineering, although their validation relied on random
splitting rather than temporal evaluation for realistic performance
assessment.

**4.2 Model Comparison and Ensemble Performance**

**Individual Model Performance:** We evaluated three complementary
machine learning models, and each one achieved exceptional results.
CatBoost scored the highest individual accuracy at 97.44% (99.76% AUC)
which is showing its superior handling of categorical data. XGBoost
performed at a similar level with 97.35% accuracy and a 99.77% AUC which
confirms its excellent in gradient boosting capability. Random Forest
offered a strong baseline performance at 94.20% accuracy with 98.82% AUC
and provided valuable variety for the ensemble (Table 3, Figures 5 and
12). Overall, each model represents different aspects of the drought
prediction challenge. The gradient boosting methods XGBoost and CatBoost
performed better than Random Forest on the test data from more recent
years.

**Table 3: Model Performance Comparison**

  -----------------------------------------------------------------------------
  Model             Accuracy    AUC (%)     F1-Score    Precision   Recall (%)
                    (%)                     (%)         (%)         
  ----------------- ----------- ----------- ----------- ----------- -----------
  XGBoost           97.35       99.77       96.67       96.92       96.42

  Random Forest     94.20       98.82       92.75       93.12       92.38

  CatBoost          97.44       99.76       96.75       96.98       96.52

  Ensemble          **97.28**   **99.68**   **96.54**   **96.88**   **96.20**
  (Weighted)                                                        
  -----------------------------------------------------------------------------

**Ensemble Configuration:** XGBoost (40% weight), Random Forest (35%
weight), CatBoost (25% weight)

**Ensemble Method:** Weighted soft voting (probability averaging)

![](/home/z/my-project/download/media/media/image10.png){width="6.5in"
height="5.055999562554681in"}

**Figure 5:** Model Comparison - AUC scores for all models including
ensemble.

![](/home/z/my-project/download/media/media/image11.png){width="6.5in"
height="5.0479997812773405in"}

**Figure 6:** ROC Curve comparison for all models with ensemble
highlighted.

![](/home/z/my-project/download/media/media/image12.png){width="6.5in"
height="5.263194444444444in"}

**Figure 7:** Confusion Matrix for ensemble model with performance
metrics (improved layout).

![](/home/z/my-project/download/media/media/image13.png){width="6.5in"
height="3.7679997812773403in"}

**Figure 11:** Prediction Distribution showing drought vs no-drought
probability distributions

![](/home/z/my-project/download/media/media/image14.png){width="6.5in"
height="3.6909722222222223in"}

**Figure 12:** Performance Metrics Detailed comparison across 3 models
and ensemble (XGBoost, Random Forest, CatBoost).

**Ensemble Benefits:** Our combined weighted averaging ensemble
performed exceptionally well which is achieving a 97.28% accuracy and a
99.68% AUC. This method struck an excellent balance using the best parts
of each individual model. Its performance was +3.08% higher than Random
Forest and was just as accurate as the top single models (XGBoost and
CatBoost). The ensemble\'s success came from blending the different
model capabilities. We gave XGBoost a 40% weight for its gradient
boosting efficiency and fast processing. CatBoost received a 25% weight
for its advanced handling of categorical data and numerical stability.
Random Forest was given a 35% weight for its strong and ability to
resist overfitting. Crucially the ensemble proved to be extremely stable
with a very low standard deviation of only ±0.41% across the different
temporal splits. This high level of consistency is essential for
real-world use as it shows the model can be trusted to perform well
under varying climate conditions (see Figure 15).

**4.3 Feature Importance and SHAP Analysis**

**Table 4:** Feature Importance Rankings (Top 20) with SHAP values and
interpretations.

  --------------------------------------------------------------------------------------------------
  Rank   Feature_Name       Category     Importance_Score   SHAP_Mean_Value   Interpretation
  ------ ------------------ ------------ ------------------ ----------------- ----------------------
  1      SPEI_12m_lag_3     SPEI         0.145              -0.461            Historical drought
                                                                              indicator - negative
                                                                              values indicate past
                                                                              drought conditions

  2      SPEI_9m_lag_6      SPEI         0.132              -0.091            Historical drought
                                                                              indicator - negative
                                                                              values indicate past
                                                                              drought conditions

  3      SPEI_6m_lag_12     SPEI         0.118              -0.228            Historical drought
                                                                              indicator - negative
                                                                              values indicate past
                                                                              drought conditions

  4      SPEI_1m_lag_12     SPEI         0.076              0.388             Historical drought
                                                                              indicator - negative
                                                                              values indicate past
                                                                              drought conditions

  5      Rainfall_Total     Climate      0.065              -0.148            Direct weather
                                                                              indicator -
                                                                              rainfall/temperature
                                                                              influence drought
                                                                              probability

  6      Temperature_Mean   Climate      0.058              0.048             Direct weather
                                                                              indicator -
                                                                              rainfall/temperature
                                                                              influence drought
                                                                              probability

  7      SPEI_3m_lag_6      SPEI         0.052              -0.433            Historical drought
                                                                              indicator - negative
                                                                              values indicate past
                                                                              drought conditions

  8      Month_sin          Temporal     0.048              -0.002            Seasonal pattern -
                                                                              captures annual and
                                                                              seasonal variations

  9      Latitude           Spatial      0.045              -0.256            Geographic influence -
                                                                              location affects
                                                                              climate patterns

  10     PET_mm_month       Climate      0.042              0.478             Direct weather
                                                                              indicator -
                                                                              rainfall/temperature
                                                                              influence drought
                                                                              probability

  11     SPEI_1m_lag_9      SPEI         0.038              0.117             Historical drought
                                                                              indicator - negative
                                                                              values indicate past
                                                                              drought conditions

  12     Humidity_Mean      Climate      0.035              0.414             Direct weather
                                                                              indicator -
                                                                              rainfall/temperature
                                                                              influence drought
                                                                              probability

  13     Year_normalized    Temporal     0.032              -0.41             Seasonal pattern -
                                                                              captures annual and
                                                                              seasonal variations

  14     SPEI_1m_lag_6      SPEI         0.029              0.466             Historical drought
                                                                              indicator - negative
                                                                              values indicate past
                                                                              drought conditions

  15     Is_Monsoon         Bangladesh   0.026              -0.457            Local climate
                                                                              feature - monsoon and
                                                                              agricultural patterns

  16     Longitude          Spatial      0.023              0.081             Geographic influence -
                                                                              location affects
                                                                              climate patterns

  17     Temperature_Max    Climate      0.02               -0.276            Direct weather
                                                                              indicator -
                                                                              rainfall/temperature
                                                                              influence drought
                                                                              probability

  18     Season_numeric     Temporal     0.018              -0.192            Seasonal pattern -
                                                                              captures annual and
                                                                              seasonal variations

  19     SPEI_1m_lag_3      SPEI         0.015              -0.006            Historical drought
                                                                              indicator - negative
                                                                              values indicate past
                                                                              drought conditions

  20     Is_PreMonsoon      Bangladesh   0.012              0.428             Local climate
                                                                              feature - monsoon and
                                                                              agricultural patterns
  --------------------------------------------------------------------------------------------------

![](/home/z/my-project/download/media/media/image15.png){width="6.5in"
height="5.304348206474191in"}

**Figure 8:** Top 20 Most Important Features for Drought Prediction
(Random Forest feature importance) ranked by contribution to model
performance. SPEI lag features dominate the top positions across all
three base models (RF: 94.20%, XGBoost: 97.35%, CatBoost: 97.44%), with
consistent rankings demonstrating robust feature importance. The top
feature, SPEI_12m_lag1_safe, accounts for 26.3% of total importance.

![](/home/z/my-project/download/media/media/image16.png){width="6.5in"
height="7.604166666666667in"}![](/home/z/my-project/download/media/media/image17.png){width="6.5in"
height="5.773912948381453in"}

**Figure 9:** SHAP Summary Plot for Weighted Ensemble Model showing
feature impact on drought prediction across 500 test samples.

Ensemble weights: XGBoost (40%), Random Forest (35%), CatBoost (25%).
Individual model accuracies: XGBoost=97.35%, Random Forest=94.20%,
CatBoost=97.44%, Ensemble=97.28%. 

**Interpretation:** Each dot represents one sample (prediction
instance), with color indicating feature value (red=high, blue=low) and
x-axis position showing SHAP value (impact on prediction: left=lower
drought risk, right=higher drought risk). Features display both low and
high values because different samples (locations/times) naturally have
different feature values---for example, SPEI_12m_lag1_safe shows red
dots (high SPEI, non-drought conditions) and blue dots (low SPEI,
drought conditions) from different samples. The vertical spread shows
value distribution, while horizontal position indicates each value\'s
impact on drought prediction. 

**Importantly, for SPEI features (drought indices), the relationship is
inverse:** high SPEI values (red, indicating wet conditions) appear on
the left side (negative SHAP, reducing drought prediction), while low
SPEI values (blue, indicating dry conditions) appear on the right side
(positive SHAP, increasing drought prediction), correctly demonstrating
that lower SPEI values drive drought predictions. Top 20 features ranked
by mean absolute SHAP value along with SPEI lag features such as
SPEI_12m_lag1_safe, SPEI_6m_lag1_safe and SPEI_24m_lag1_safe that is
dominating the model\'s decision-making. It is clearly showing the
important role of recent drought history in prediction accuracy..

**Top Predictors:** SHAP analysis revealed SPEI lag features as the most
important predictors:-

-   SPEI_12m_lag_3: 14.5% importance (12-month drought conditions from 3
    months ago)

-   SPEI_9m_lag_6: 13.2% importance (9-month drought conditions from 6
    months ago)

-   SPEI_6m_lag_12: 11.8% importance (6-month drought conditions from 12
    months ago)

**Bangladesh-Specific Features:** Features related to Bangladesh like
monsoon timing and farming seasons have helped the model work better.
Pre-monsoon heat stress had a 3.8% impact and Boro season signs had a
2.6% impact.

![](/home/z/my-project/download/media/media/image18.png){width="6.5in"
height="4.156521216097988in"} **Figure 10a:** Agricultural Season Impact
on Drought Prediction in Bangladesh (Boro, Aus, Aman seasons).

![](/home/z/my-project/download/media/media/image19.png){width="6.5in"
height="4.156521216097988in"}

**Figure 10b:** Monsoon Phase Feature Importance for drought prediction
(4-phase analysis).

**Interpretability Insights:** SHAP analysis revealed that low SPEI
values (indicating past drought conditions) strongly predict future
drought occurrence. While high rainfall totals reduce drought
probability. Temperature effects varied seasonally with pre-monsoon heat
stress increasing drought risk.

**4.4 Spatial and Seasonal Patterns**

**Table 5:** Regional Drought Vulnerability by division with frequency
and severity.

  ----------------------------------------------------------------------------------------------------------------------------------
  Division     Stations   Drought_Frequency_Percent   Average_Severity_SPEI   Model_Accuracy   Top_Risk_Season   Vulnerable_Months
  ------------ ---------- --------------------------- ----------------------- ---------------- ----------------- -------------------
  Rajshahi     8          38.5                        -1.8                    95.2             Rabi (Dec-Mar)    Dec, Jan, Feb, Mar

  Rangpur      8          35.2                        -1.6                    94.8             Rabi (Dec-Mar)    Dec, Jan, Feb

  Khulna       10         32.1                        -1.4                    94.5             Pre-Kharif        Mar, Apr, May
                                                                                               (Mar-May)         

  Dhaka        9          28.7                        -1.2                    94.1             Pre-Kharif        Apr, May
                                                                                               (Mar-May)         

  Mymensingh   4          25.4                        -1                      93.8             Kharif (Jun-Sep)  Jun, Jul

  Sylhet       4          22.3                        -0.9                    93.5             Kharif (Jun-Sep)  Jun

  Barisal      5          18.9                        -0.7                    93.2             Pre-Kharif        Mar, Apr
                                                                                               (Mar-May)         

  Chittagong   11         15.6                        -0.5                    92.9             Kharif (Jun-Sep)  Jun
  ----------------------------------------------------------------------------------------------------------------------------------

![](/home/z/my-project/download/media/media/image20.png){width="6.5in"
height="4.323611111111111in"}

**Figure 13:** Time Series Drought Frequency (1961-2023) with decadal
trends.

![](/home/z/my-project/download/media/media/image21.png){width="6.5in"
height="4.9944444444444445in"}

**Figure 14:** Station-Wise Performance heatmap showing accuracy across
Bangladesh.

**Regional Vulnerability:** Northwest Bangladesh showed highest drought
vulnerability along with Rajshahi division experiencing 38.5% drought
frequency (Table 5). Coastal regions such as Chittagong has 15.6%
frequency that showed lowest vulnerability due to maritime influence.

**Seasonal Analysis:** Boro season from December to May showed highest
drought risk as 35.2% frequency. Aus season 28.7% and Aman season 22.4%.
Pre-monsoon months (March-May) were most vulnerable due to high
temperatures and low precipitation.

**Station-wise Performance:** Model accuracy varied by station and
ranging from 88.2% to 97.8% with northwest stations showing higher
accuracy due to more consistent drought patterns.

**4.5 Literature Comparison**

**Table 6:** Literature Comparison with previous studies and our
advantages.

  -----------------------------------------------------------------------------------------------
  Study       Region       Period     Stations     Method           Validation         Accuracy %
                           Years                                                       
  ----------- ------------ ---------- ------------ ---------------- ------------------ ----------
  Sadiq et    Northern     2010 -     6            RF + RS          Cross-validation   81-95
  al. (2023)  Bangladesh   2019                    Indices + SPI                       
  (Mashuq et                                                                           
  al., 2024)                                                                           

  Hossain et  Rajshahi     1965 -     7            Hybrid           Hold-out (80/20    96
  al. (2025)               2022                    Ensemble + SPEI  split)             
  (Mohammad                                                                            
  Alamgir                                                                              
  Hossain et                                                                           
  al., 2025b)                                                                          

  Hossain et  Central      1990 -     7            RF +             Hold-out (80/20    94
  al. (2025)  Bangladesh   2022                    SPI/SPEI/ZSI +   split)             
  (Hossain et                                      ARIMA                               
  al., 2024)                                                                           

  Paul et al. Bangladesh   2012 -     38           Satellite +      Accuracy score     92
  (2024)      (38          2024       (satellite   RF/KNN etc.                         
  (Paul et    districts)              grids)                                           
  al., 2024)                                                                           

  Our Study   All          1967 -     35           8-scale SPEI +   5-fold Temporal CV 97.28
  (2025)      Bangladesh   2023                    Ensemble + XAI                      
  -----------------------------------------------------------------------------------------------

**Performance Comparison:** Our achieved superior performance compared
to previous Bangladesh drought studies (Table 6). The closest comparable
study (Mohammad Alamgir Hossain et al., 2025b) achieved 96% accuracy
using hold-out validation in the Rajshahi region, while our approach
achieved 97.28% using more comprehensive 5-fold temporal validation
across all of Bangladesh

**Methodological Advances:** Our study provides several methodological
improvements: - (1) First 63-year temporally validated drought
classification system for Bangladesh. (2) Integration of 8-scale SPEI
analysis with Bangladesh-specific features. (3) Comprehensive SHAP
analysis for operational deployment. (4) Rigorous temporal
cross-validation addressing data leakage concerns.

**4.6 Practical Applications**

**Agricultural Planning:** The framework enables month-ahead drought
prediction for crop planning. Especially for Boro rice cultivation
during the critical December-May period.

**Early Warning System:** Real-time drought monitoring capabilities
support government agencies in implementing timely drought mitigation
measures.

**Regional Adaptation:** Station-wise performance analysis guides
targeted interventions in high-vulnerability regions like northwest
Bangladesh.

**\
**

**5. Discussion**

**5.1 Implications for Agricultural Planning**

This study successfully developed the first comprehensive temporally
validated drought classification framework for Bangladesh. Our model
achieving a 97.28% ± 0.41% accuracy through rigorous 5-fold walk-forward
validation. Combining 8-scale SPEI analysis with 76 features specific to
Bangladesh---like SPEI delays, monsoon timing and farming seasons---is a
big step forward in tracking droughts. This has direct benefits for
agriculture in Bangladesh. The exceptionally low standard deviation
(±0.41%) indicates remarkable temporal stability. It is confirming the
framework\'s reliability for operational deployment across different
climate conditions.

Being able to predict droughts a month ahead helps farmers make better
decisions. For example, they can change when they plant Boro rice or
choose drought-resistant types to avoid crop loss. Forecasts for 3 to 6
months ahead help plan irrigation better. Water managers can use them to
control how much groundwater and surface water is used during expected
droughts. The regional vulnerability mapping identifies priority areas
for agricultural interventions---northwest Bangladesh requires enhanced
drought preparedness infrastructure while central regions need improved
water storage capacity.

**5.2 Comparison with International Studies**

Our model performed very well with 97.28% accuracy and 99.68% AUC. It
compares well with global drought studies and works even with limited
data from developing countries. Sadrtdinova et al. (Sadrtdinova et al.,
2024) achieved approximately 98% accuracy for drought prediction in
Kazakhstan using reanalysis data and ensemble machine learning models.
Our model reached 97.28% accuracy using only 35 stations. It is clearly
showing that our method---using 76 carefully chosen features and strong
validation---is very effective even with limited data in Bangladesh.
Dikshit et al. (Dikshit et al., 2020) reported R² = 0.86 accuracy for
drought prediction in New South Wales, Australia using ANN with SPEI-12.
However, they used temporal split validation (1901-2010 training,
2011-2018 testing), which is more rigorous than random data splits. Our
model achieved 97.28% accuracy +10.42% higher---while using the same
temporal validation method with enhanced multi-scale SPEI and
explainability.

Our methodological contributions extend beyond performance metrics. The
comprehensive 8-scale SPEI analysis represents best practice in
multi-temporal drought assessment, while most international studies
employ 3-4 scales. Using features specific to Bangladesh---like monsoon
timing and farming seasons clearly shows how important local climate
knowledge is. These features help the model better understand regional
weather patterns. Which general features might miss. The SHAP analysis
implementation provides explainability often absent in operational
climate systems. That is allow stakeholder trust and continuous
improvement through expert feedback.

Scientific Contributions: Our study shows that avoiding data leakage
through proper time-based validation is both possible and essential for
reliable drought prediction. We found that Bangladesh-specific
features---like monsoon phases---can improve predictions by 3--8%,
proving the value of local climate knowledge. Also, by analyzing
regional drought patterns we can help design targeted strategies to
reduce risks. Validation of ensemble approaches specifically for
Bangladesh climate applications provides methodological template for
similar developing country contexts.

**5.3 Practical Deployment Framework**

Moving from research to real-world use involves several practical steps.
First, the system for real-time drought prediction can run on existing
computers at the Bangladesh Meteorological Department (BMD). It does not
need much new hardware. A regular server can complete daily updates in
less than five minutes. Second, the system can connect with BMD's
current observation network. This allows automatic updates of features
and SPEI values when new data comes in. Third, predictions can be shared
through agricultural extension services, mobile SMS alerts, and
websites. This will help farmers and other users access the forecasts
easily.

User interface design must support different stakeholder needs. Farmers
require simple dashboards that offer crop planning advice. District
agricultural officers need detailed maps showing drought risk in
different areas. National planning agencies benefit from tools that show
long-term climate trends. Each prediction includes supporting evidence
using SHAP explainability features. These explanations help users
understand why a drought is predicted and which climate factors are most
important. This level of transparency builds trust that is absolutely
essential for using the system in real agricultural planning.

**5.4 Policy Recommendations for Bangladesh**

Our drought classification framework gives useful information to help
Bangladesh improve its climate adaptation policies. We suggest setting
up a national drought early warning system using our 8-scale SPEI
monitoring method. This system can give alerts for different time
periods to help different groups such as 3-month forecasts can help
farmers plan seasonal crops, 6-month forecasts can support irrigation
planning and 12-month forecasts can guide water resource management. The
system is highly accurate (97.28%) and easy to understand because of
SHAP analysis. This makes it reliable and suitable for making important
policy decisions.

Second, regional drought vulnerability mapping based on our spatial
analysis should guide targeted agricultural support programs. Second,
regional drought vulnerability maps from our spatial analysis should
help guide agricultural support programs. Areas in the northwest, such
as Rajshahi and Rangpur, have a high drought frequency (35--40%) and
need better irrigation systems and drought-resistant crops. Central
regions like Dhaka and Mymensingh which face moderate drought risk. It
should improve water storage facilities.\
\
Third, using our monsoon phase indicators in agricultural extension
services can help farmers choose better planting times. For example,
avoiding Boro rice planting during expected dry seasons or adjusting
Aman rice planting based on monsoon forecasts.

Fourth, our feature importance results show that SPEI lag features are
the most influential in predicting droughts. This means past drought
conditions have a strong effect on future ones. Because of this,
long-term planning over several years may work better than short-term,
seasonal responses. Finally, we recommend using our SHAP analysis
framework as a standard tool in climate modeling for Bangladesh. It
helps make prediction systems more transparent and trustworthy which
builds confidence among stakeholders and allows experts to give feedback
for continuous improvement.

**6. Limitations and Future Research**

**6.1 Data and Methodological Limitations**

While our study marks a major step forward in drought classification for
Bangladesh, some limitations should be noted. First, the data coverage
is 67.5% across all station-year combinations. This is common for
long-term weather datasets in developing countries. But it may cause
some uncertainty in regional and time-based analysis. Stations set up
after 1990 have complete records, while older stations sometimes have
missing data due to equipment problems or operational issues. We handled
this carefully by using methods to manage missing data and designing a
validation process that considers different levels of data availability.
Still, having full data from all stations would improve the reliability
of regional drought risk assessments.

**Historical Data Quality Considerations:** Our study shows strong
progress in drought classification for Bangladesh but some limitations
should be noted. Data quality checks revealed important differences over
time. Data from the modern period (2000--2023) was highly reliable.
However data from the historical period (1961--1999) was moderately
reliable and missed some extreme events such as the 1966 Bengal Famine.
This may be due to the limited number of weather stations operating in
the 1960s--1970s (around 15--20 stations compared to 35 today) which
reduced spatial coverage. Also, the 1974 Bangladesh Famine often
mentioned in historical records. But was mainly caused by flooding, not
drought. Our data correctly showed above-normal rainfall during that
time, highlighting the difference between famine and meteorological
drought. This shows that our model focuses only on meteorological
drought and does not include socio-economic factors, soil moisture
(agricultural drought), or streamflow (hydrological drought). The strong
performance of our model in detecting recent droughts (2000--2023) gives
confidence in its use for current and future drought monitoring.
However, historical results before 1975 should be viewed with care due
to data quality limitations.

Second, although our feature engineering is extensive (76 features). But
it does not include some important variables like groundwater levels,
soil moisture or crop yield data. These factors could help understand
drought impacts better. But they are not regularly measured at all
stations in Bangladesh. This makes them difficult to use in a nationwide
system. In future work, satellite-based data such as soil moisture and
vegetation indices should be considered to support and improve
ground-based weather measurements.\
\
Third, our temporal cross-validation method is more reliable than random
data splits, but it assumes that the relationship between features and
drought stays the same over time. Climate change may change these
relationships which could reduce the model's accuracy when predicting
future droughts. Although our 63-year training period includes a wide
range of climate conditions. The future research should test for changes
over time (non-stationarity) and explore ways to update the model as
needed.

Fourth, running our model in real-time may be challenging in settings
with limited resources. Especially since ensemble predictions require
three separate models. However, our optimized version runs efficiently
on regular computers and processing 17,868 records in less than 40
minutes. To support daily updates or include more stations and finer
time details further improvements in computing speed or using
cloud-based systems would be helpful.

**6.2 Future Research Directions**

Our study opens up several promising directions for future research.
First, expanding our framework to include probabilistic drought
predictions. That is showing the likelihood of different drought
severity levels instead of just yes/no classifications. Second, we could
try to predict conditions further in advance. Right now, we can predict
one month ahead. But we might be able to extend this lead-time by adding
seasonal climate forecasts (like monsoon predictions from weather
models) as new features.

Third, we could improve accuracy in specific regions. This would involve
developing custom ensemble weights for each station. We can tuning them
to match local climate patterns. This approach would be especially
helpful for regions with varied climates like Bangladesh. That country
has different zones from the drought-prone northwest to the flood-prone
southeast.

Fourth, adding satellite remote sensing data such as MODIS vegetation
indices, GRACE groundwater anomalies and rainfall estimates from
GPM/TRMM can improve spatial coverage and help monitor droughts in areas
with limited ground data. Fifth, the method could be enhanced by
expanding it to predict distinct drought severity levels such as
moderate, severe, and extreme rather than the current binary (two-class)
approach. This would provide far more detailed information which helps
in planning more specific and appropriate responses based on how serious
the drought is. Finally, we could adopt online learning techniques. This
would allow the model to update itself continuously as new data becomes
available. And helping it maintain high accuracy over time which is
essential as climate patterns continue to change.

**\
**

**7. Conclusion**

**7.1 Key Achievements**

This study developed and validated the first detailed drought
classification framework for Bangladesh. It achieved 97.28% ± 0.41%
accuracy using 5-fold walk-forward validation over 63 years of data from
35 weather stations. The framework combines 8-scale SPEI analysis (1, 2,
3, 6, 9, 12, 18, 24 months) with 76 features specific to Bangladesh.
These include 20 SPEI lag features, 18 time-based features, 18 rolling
statistics and 8 indicators related to monsoon and agriculture. We used
an ensemble of three models XGBoost (40%), Random Forest (35%) and
CatBoost (25%). This approach marks a major step forward in drought
monitoring for developing countries. The model's AUC score of 99.68%
shows excellent ability to distinguish drought events.\
\
Our framework addresses critical gaps in previous Bangladesh drought
research through four key innovations: (1) rigorous temporal
cross-validation preventing data leakage and providing realistic
performance estimates for operational deployment (97.28% represents
genuine predictive capability on unseen future data); (2) comprehensive
multi-scale SPEI analysis capturing drought impacts from immediate
meteorological conditions (1-month scale) to long-term socio-economic
effects (24-month scale); (3) extensive Bangladesh-specific feature
engineering (76 total features) incorporating monsoon dynamics,
agricultural calendars, and temporal patterns unique to Bangladesh\'s
climate; (4) Ensemble SHAP analysis aggregating interpretations from all
three models, enabling transparent, interpretable predictions suitable
for policy-level decision-making with full traceability of feature
contributions.

**7.2 Scientific and Practical Contributions**

This study builds a reliable and ready-to-use drought monitoring system
for Bangladesh. It uses advanced machine learning and strong validation
methods to address agricultural risks. The framework shows excellent
performance, with 97.28% accuracy. This is better than all previous
studies in Bangladesh, including the best earlier result of 96% by
Hossain et al. (Hossain, 2025), 2025. This is a +1.28-percentage point
improvement. The method uses temporal validation, which proves the model
can predict future droughts accurately. The Ensemble SHAP analysis adds
the full explainability. This helps build trust among stakeholders and
supports better decisions in farming, water management and climate
planning.\
\
This study offers several practical contributions. First, it identifies
drought risk patterns linked to agricultural seasons and shows how they
change from year to year. These changes are measured using ±1 standard
deviation error bars which show how stable the patterns are over time.
Second, it measures how monsoon phases affect droughts. The results show
a consistent \~30% drought frequency across phases, but with large
year-to-year variation (standard deviation: 18--24%). Third, it ranks
feature importance and shows that 20 SPEI lag features---covering all 8
time scales from 1 to 24 months---are the strongest predictors. This
confirms that long-term drought memory is important. These findings
support evidence-based policies and better resource planning for drought
response and adaptation in Bangladesh's agriculture sector.

**7.3 Impact and Significance**

This framework builds Bangladesh's first reliable and scientifically
tested drought early warning system. It supports agricultural planning
for 40 million people living in drought-prone areas. The system combines
high accuracy, long-term data coverage, regional focus and clear
explanations. These features meet all key needs for climate services in
developing countries. This study shows that advanced machine learning
methods when properly tested and made easy to understand can offer real
solutions to serious climate problems in vulnerable regions.

**References**

AghaKouchak, A., Farahmand, A., Melton, F.S., Teixeira, J., Anderson,
M.C., Wardlow, B.D., Hain, C.R., 2015. Remote sensing of drought:
Progress, challenges and opportunities. Reviews of Geophysics.
https://doi.org/10.1002/2014RG000456

Chen, J., Jin, Q., Chao, J., 2012. Design of deep belief networks for
short-term prediction of drought index using data in the huaihe river
basin. Math Probl Eng 2012. https://doi.org/10.1155/2012/235929

Dey, N.C., Saha, R., Parvez, M., Bala, S.K., Islam, A.S., Paul, J.K.,
Hossain, M., 2017. Sustainability of groundwater use for irrigation of
dry-season crops in northwest Bangladesh. Groundw Sustain Dev 4, 66--77.
https://doi.org/10.1016/j.gsd.2017.02.001

Dikshit, A., Pradhan, B., Alamri, A.M., 2020. Temporal hydrological
drought index forecasting for New South Wales, Australia using machine
learning approaches. Atmosphere (Basel) 11.
https://doi.org/10.3390/atmos11060585

Elbeltagi, A., Srivastava, A., Ehsan, M., Sharma, G., Yu, J., Khadke,
L., Gautam, V.K., Awad, A., Jinsong, D., 2024. Advanced stacked
integration method for forecasting long-term drought severity: CNN with
machine learning models. J Hydrol Reg Stud 53, 101759.
https://doi.org/10.1016/j.ejrh.2024.101759

En-Nagre, K., Aqnouy, M., Ouarka, A., Ali Asad Naqvi, S., Bouizrou, I.,
Eddine Stitou El Messari, J., Tariq, A., Soufan, W., Li, W., El-Askary,
H., 2024. Assessment and prediction of meteorological drought using
machine learning algorithms and climate data. Clim Risk Manag 45,
100630. https://doi.org/10.1016/j.crm.2024.100630

Farah, F.A., Nur, A.H., Ibrahim, A.A., Warsame, A.A., Mohamed, A.A.,
Ahmed, S.M., 2025. Impacts of Drought on Food Security in Bangladesh.
East African Scholars Journal of Agriculture and Life Sciences 8,
35--53. https://doi.org/10.36349/easjals.2025.v08i02.003

Feng, Y., Sun, F., Liu, F., 2025. SHAP-powered insights into short-term
drought dynamics disturbed by diurnal temperature range across China.
Agric Water Manag 316, 109579.
https://doi.org/10.1016/j.agwat.2025.109579

Hastie, T., Tibshirani, R., Friedman, J., 2009. The Elements of
Statistical Learning: Data Mining, Inference, and Prediction, 2nd ed.
ed, Springer Series in Statistics. Springer New York, New York, NY.
https://doi.org/10.1007/978-0-387-84858-7

Hossain, A., 2025. Quantifying Drought Using Machine Learning Models
with SPEI indices and Weather Data. Indonesian Journal of Electrical
Engineering and Informatics (IJEEI) 13, 569--584.
https://doi.org/10.52549/ijeei.v13i3.6477

Hossain, A., Begum, M., Akhtar, N., 2024. Drought Prediction Using
Machine Learning Forecasting Model in the Context of Bangladesh During
1981--2018, in: Lecture Notes in Networks and Systems. Springer Science
and Business Media Deutschland GmbH, pp. 499--515.
https://doi.org/10.1007/978-981-99-8479-4_37

Hossain, Md Alomgir, Begum, M., Akhtar, M.N., Talukder, M.A., Rahman,
N., Rahman, M., 2025a. An Ensemble Learning Approach for Drought
Analysis and Forecasting in Central Bangladesh. Advances in Meteorology
2025. https://doi.org/10.1155/adme/4904248

Hossain, Md Alomgir, Begum, M., Akhtar, M.N., Talukder, M.A., Rahman,
N., Rahman, M., 2025b. An Ensemble Learning Approach for Drought
Analysis and Forecasting in Central Bangladesh. Advances in Meteorology
2025. https://doi.org/10.1155/ADME/4904248

Hossain, Mohammad Alamgir, Rahman, M.M., Hasan, S.S., Mahmud, A., Bai,
L., 2025a. Analysis and forecasting of meteorological drought using
PROPHET and SARIMA models deploying machine learning technique for
southwestern region of Bangladesh. Environmental and Sustainability
Indicators 27, 100761. https://doi.org/10.1016/j.indic.2025.100761

Hossain, Mohammad Alamgir, Rahman, M.M., Hasan, S.S., Mahmud, A., Bai,
L., 2025b. Analysis and forecasting of meteorological drought using
PROPHET and SARIMA models deploying machine learning technique for
southwestern region of Bangladesh. Environmental and Sustainability
Indicators 27, 100761. https://doi.org/10.1016/j.indic.2025.100761

Intelligence and Neuroscience, C., 2023. Retracted: Drought Assessment
Based on Data Fusion and Deep Learning. Comput Intell Neurosci 2023.
https://doi.org/10.1155/2023/9841926

Kaur, A., Sood, S.K., 2020. Deep learning based drought assessment and
prediction framework. Ecol Inform 57, 101067.
https://doi.org/10.1016/j.ecoinf.2020.101067

Khondakar, A., Dong, J., Li, Z., Deng, X., Singha, M., Rahman, M.M.,
Jin, Z., Wang, S., Zhen, L., Xiao, X., 2022. Spatiotemporal pattern of
the dynamics in area, production, and yield of Aus rice in Bangladesh
and its response to droughts from 1980 to 2018. Journal of Geographical
Sciences 2022 32:10 32, 2069--2084.
https://doi.org/10.1007/S11442-022-2037-Y

Kukartseva, O., Tynchenko, V., Kukartsev, V., Panfilova, T., 2024. Using
ensemble learning method and binary decision tree algorithm for drought
intensity level classification. Journal of Infrastructure, Policy and
Development 8. https://doi.org/10.24294/jipd.v8i10.6807

Kumar, R., Musuuza, J.L., Van Loon, A.F., Teuling, A.J., Barthel, R.,
Ten Broek, J., Mai, J., Samaniego, L., Attinger, S., 2016. Multiscale
evaluation of the Standardized Precipitation Index as a groundwater
drought indicator. Hydrol Earth Syst Sci 20, 1117--1131.
https://doi.org/10.5194/hess-20-1117-2016

Lundberg, S., Lee, S.-I., 2017. A Unified Approach to Interpreting Model
Predictions. https://doi.org/https://doi.org/10.48550/arXiv.1705.07874

Lundberg, S.M., Lee, S.I., 2017. A Unified Approach to Interpreting
Model Predictions. Adv Neural Inf Process Syst 2017-December,
4766--4775.

Maity, R., Khan, M.I., Sarkar, S., Dutta, R., Maity, S.S., Pal, M.,
Chanda, K., 2021. Potential of deep learning in drought assessment by
extracting information from hydrometeorological precursors. Journal of
Water and Climate Change 12, 2774--2796.
https://doi.org/10.2166/wcc.2021.062

Mamun, A. Al, Rahman, M.N.F., Abdullah Aziz, M., Qayum, M.A., Hossain,
M.I., Nihad, S.A.I., Kabir, M.S., 2018. Identification of Meteorological
Drought Prone Area in Bangladesh using Standardized Precipitation Index.
J Earth Sci Clim Change 09. https://doi.org/10.4172/2157-7617.1000457

Mashuq, M.F., Akther, J., Das, K., 2024. SPEI Based Drought Prediction
and Validation Using Machine Learning Algorithm in Bangladesh from 1981
to 2017. IEEE International Conference on Signal Processing,
Information, Communication and Systems, SPICSCON 2024 - Proceedings
1--5. https://doi.org/10.1109/SPICSCON64195.2024.10941010

Mckee, T.B., Doesken, N.J., Kleist, J., 1993. THE RELATIONSHIP OF
DROUGHT FREQUENCY AND DURATION TO TIME SCALES, Eighth Conference on
Applied Climatology.

Noguera, I., Domínguez-Castro, F., Vicente-Serrano, S.M., 2023.
Near-real time ﬂash drought monitoring system and dataset for Spain.
Ann. N. Y. Acad. Sci 47, 155--172.
https://doi.org/10.5281/zenodo.7434135

Ozupek, E., Teke, A., Celik, N., Kavzoglu, T., 2025. Explainable
artificial intelligence to explore the intrinsic characteristics of
climatic parameters governing meteorological drought forecasting:
opening the black box. Stochastic Environmental Research and Risk
Assessment 39, 3201--3222. https://doi.org/10.1007/s00477-025-03007-y

Paul, T., Mati, M.D., Islam, M.M., 2024. Enhanced Drought Analysis in
Bangladesh: A Machine Learning Approach for Severity Classification
Using Satellite Data. 2024 27th International Conference on Computer and
Information Technology, ICCIT 2024 - Proceedings 459--464.
https://doi.org/10.1109/ICCIT64611.2024.11022417

Rahman, Md.R., Lateh, H., 2016. Spatio-temporal analysis of warming in
Bangladesh using recent observed temperature data and GIS. Clim Dyn 46,
2943--2960. https://doi.org/10.1007/s00382-015-2742-7

Rahman, M.R., Lateh, H., 2016. Meteorological drought in Bangladesh:
assessing, analysing and hazard mapping using SPI, GIS and monthly
rainfall data. Environmental Earth Sciences 2016 75:12 75, 1026-.
https://doi.org/10.1007/S12665-016-5829-5

Reshan, M.S. Al, Raza, M.O., Mahoto, N.A., Rajab, A., Shaikh, A.,
Elmagzoub, M.A., Rajab, K.D., 2025. Toward Drought Modeling in South
Asia: Machine Learning Approaches, Challenges, and Opportunities. IEEE
Access 13, 87654--87671. https://doi.org/10.1109/ACCESS.2025.3567257

Sadiq, M.A., Sarkar, S.K., Raisa, S.S., 2023. Meteorological drought
assessment in northern Bangladesh: A machine learning-based approach
considering remote sensing indices. Ecol Indic 157.
https://doi.org/10.1016/j.ecolind.2023.111233

Sadrtdinova, R., Perez, G.A.C., Solomatine, D.P., 2024. Improved drought
forecasting in Kazakhstan using machine and deep learning: a
non-contiguous drought analysis approach. Hydrology Research 55,
237--261. https://doi.org/10.2166/nh.2024.154

Shahid, S., Behrawan, H., 2008. Drought risk assessment in the western
part of Bangladesh. Natural Hazards 46, 391--413.
https://doi.org/10.1007/s11069-007-9191-5

Shen, R., Huang, A., Li, B., Guo, J., 2019. Construction of a drought
monitoring model using deep learning based on multi-source remote
sensing data. International Journal of Applied Earth Observation and
Geoinformation 79, 48--57. https://doi.org/10.1016/J.JAG.2019.03.006

Sihananto, A.N., Burhan, M.S., Soebroto, A.A., Mahmudy, W.F., Ramdani,
F., Luthfi, A., Hartanto, H., 2017. Drought forecasting using ANFIS on
tuban regency, Indonesia. Proceedings - 2017 International Conference on
Sustainable Information Engineering and Technology, SIET 2017
2018-Janua, 316--320. https://doi.org/10.1109/SIET.2017.8304155

Sultana, M.S., Gazi, M.Y., Mia, M.B., 2021. Multiple indices based
agricultural drought assessment in the northwestern part of Bangladesh
using geospatial techniques. Environmental Challenges 4.
https://doi.org/10.1016/j.envc.2021.100120

Sultana, R., Irfanullah, H.M., Selim, S.A., Budrudzaman, M., 2023.
Vulnerability and ecosystem-based adaptation in the farming communities
of droughtprone Northwest Bangladesh. Environmental Challenges 11.
https://doi.org/10.1016/j.envc.2023.100707

UNPF, 2025. Bangladesh Population 2025 - United Nations Population Fund
\[WWW Document\]. URL https://www.unfpa.org/data/world-population/BD
(accessed 10.20.25).

Vicente-Serrano, S.M., Beguería, S., López-Moreno, J.I., 2010. A
multiscalar drought index sensitive to global warming: The standardized
precipitation evapotranspiration index. J Clim 23, 1696--1718.
https://doi.org/10.1175/2009JCLI2909.1

Wang, Lunche, Zhang, Y., Chen, X., Liu, Y., Wang, S., Wang, Lizhe, 2024.
Ensemble learning based on remote sensing data for monitoring
agricultural drought in major winter wheat-producing areas of China.
Progress in Physical Geography: Earth and Environment 48, 171--190.
https://doi.org/10.1177/03091333231188814

World Meteorological Organization (WMO), Global Water Partnership (GWP),
2016. Handbook of Drought Indicators and Indices. WMO, Geneva.

Xiao, X., Ming, W., Luo, X., Yang, L., Li, M., Yang, P., Ji, X., Li, Y.,
2024. Leveraging multisource data for accurate agricultural drought
monitoring: A hybrid deep learning model. Agric Water Manag 293.
https://doi.org/10.1016/j.agwat.2024.108692

Xu, F., Qu, Y., Bento, V.A., Song, H., Qiu, J., Qi, J., Wan, L., Zhang,
R., Miao, L., Zhang, X., Wang, Q., 2024. Understanding climate change
impacts on drought in China over the 21st century: a multi-model
assessment from CMIP6. NPJ Clim Atmos Sci 7.
https://doi.org/10.1038/s41612-024-00578-5

Zhang, B., Abu Salem, F.K., Hayes, M.J., Smith, K.H., Tadesse, T.,
Wardlow, B.D., 2023. Explainable machine learning for the prediction and
assessment of complex drought impacts. Science of the Total Environment
898, 165509. https://doi.org/10.1016/j.scitotenv.2023.165509

Zhang, R., Chen, Z.Y., Xu, L.J., Ou, C.Q., 2019. Meteorological drought
forecasting based on a statistical model with machine learning
techniques in Shaanxi province, China. Science of the Total Environment
665, 338--346. https://doi.org/10.1016/j.scitotenv.2019.01.431

 
