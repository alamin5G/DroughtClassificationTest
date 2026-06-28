# 🛠️ Implementation Plan — ১৩টি Concept কীভাবে Codebase-এ বাস্তবায়িত হবে

> এই ডকুমেন্ট প্রতিটি concept-কে **কোন Phase, কোন function, কীভাবে, কোন output**-এ implement করা হবে তা ম্যাপ করে। কোডবেস: [`master_drought_v2.ipynb`](master_drought_v2.ipynb) (৮-Phase pipeline)।

**Legend:** 🌡️=Meteorological, 🌾=Agricultural, 💧=Hydrological

---

## 📊 এক নজরে ম্যাপিং টেবিল

| # | Concept | কোন Phase / Function | Implement কীভাবে | Output | Tag |
|---|---|---|---|---|---|
| 0 | **SPEI Scale Mapping** | Phase 3 (`phase_3_spei_calculation`), CONFIG line 371 | ইতিমধ্যেই ৮ scale হিসাব হয়; ৩–৬m=🌾, ৬–২৪m=💧 হিসেবে tag করো | `climate_data_with_spei_8scales.csv` | 🌡️🌾💧 |
| 1 | **EDA** | **নতুন Phase 0** (`phase_eda`) — Phase 1-এর আগে | `df.describe()`, missing-value check, histogram/boxplot, station/division-wise trend | `figs/eda_*.png` | 🌡️🌾💧 |
| 2 | **ADF Test** | **নতুন Phase 6b**-এর অংশ | `statsmodels.adfuller()` প্রতি স্টেশন × SPEI scale-এ | `outputs/adf_results.csv` (station×scale×p-value) | 🌾💧 |
| 3 | **SPEI Classification (label)** | Phase 5 (line 2175) — **বদলাও** | label বদলে `SPEI_3m < -0.5` (meteorological primary); সাথে `SPEI_6m`, `SPEI_12m` label extension | `enhanced_temporal_features.csv` | 🌡️🌾💧 |
| 4 | **Hyperparameter Tuning** | Phase 6 (line 2245) — **আপগ্রেড করো** | `GridSearchCV`/`Optuna` (বর্তমানে hardcoded param) | best params → `outputs/best_params.json` | 🌡️🌾💧 |
| 5 | **Train/Val/Test (CV)** | Phase 6 (`temporal_splits`, line 2357) — **persistence baseline যোগ করো** | বিদ্যমান ৫-fold walk-forward CV + naive baseline ("last month=this month") | `temporal_cv_results.json` + persistence accuracy | 🌡️🌾💧 |
| 6 | **NSE** | **নতুন Phase 10** (forecasting evaluation) | forecasting model-এর predicted SPEI vs observed SPEI → NSE সূত্র | `outputs/nse_results.csv` | 🌾💧 |
| 7 | **KGE** | **নতুন Phase 10** | NSE-এর সাথে KGE (r, α, β decomposition) প্রতি স্টেশনে | `outputs/kge_results.csv` | 🌾💧 |
| 8 | **Kruskal-Wallis** | **নতুন Phase 10** | `scipy.stats.kruskal` — Boro/Aus/Aman বা ৮ বিভাগে severity তুলনা | `outputs/kruskal_wallis.csv` (p-value) | 🌾💧 |
| 9 | **Taylor Diagram** | **Phase 7** — নতুন figure function `create_taylor_diagram()` | ৮ scale বা ৩৫ station এক polar plot-এ (r, σ, RMSE) | `figs/figure_taylor_diagram.png` | 🌾💧 |
| 10 | **ACF/PACF ("VOS")** | **নতুন Phase 6b** | `statsmodels.plot_acf/plot_pacf` প্রতি স্টেশন SPEI series-এ → p,d,q ঠিক করো | `figs/acf_pacf_*.png` | 🌾💧 |
| 11 | **ARIMA** | **নতুন Phase 6b** (short-term) + **6c** (10-year) | `statsmodels.ARIMA(order=(p,d,q))` → ১–১২ মাস + ১০-বছর forecast | `outputs/arima_forecast.json`, `figs/forecast_arima.png` | 💧 |
| 12 | **SARIMA** | **নতুন Phase 6b** | `statsmodels.SARIMAX(seasonal_order=(P,D,Q,12))` → মৌসুমি কৃষি-খরা forecast | `outputs/sarima_forecast.json`, `figs/forecast_sarima.png` | 🌾 |
| 13 | **LSTM** | **নতুন Phase 6b** | `tensorflow.keras` LSTM → non-linear sequence forecast | `outputs/lstm_forecast.json`, `figs/forecast_lstm.png` | 🌾💧 |

---

## 🏗️ নতুন Pipeline কাঠামো (৮ Phase → ১১ Phase)

```
Phase 0:  EDA (নতুন)                                    🌡️🌾💧
Phase 1:  Daily → Monthly (অপরিবর্তিত)
Phase 2:  PET Hargreaves (অপরিবর্তিত)
Phase 3:  8-scale SPEI (অপরিবর্তিত)
Phase 4:  Drought extraction (অপরিবর্তিত)
Phase 5:  Feature Eng — label বদলে SPEI_3m (primary)   🌡️ + ৬m/১২m extension labels 🌾💧
Phase 6a: Classification + persistence baseline (upgraded) 🌡️🌾💧
Phase 6b: Short-term Forecasting (ADF→ACF/PACF→ARIMA/SARIMA/LSTM, ১–১২ মাস) 🌾💧
Phase 6c: 10-year Climate Outlook (SARIMA/LSTM + uncertainty) 💧
Phase 7:  Figures (+ নতুন Taylor diagram)               🌾💧
Phase 8:  Tables (অপরিবর্তিত)
Phase 10: Hydrology Evaluation (NSE, KGE, Kruskal-Wallis) 🌾💧
```

---

## 🔧 প্রতিটি Concept-এর Implementation Detail

### 1. EDA (নতুন Phase 0)
```python
def phase_eda():
    df = pd.read_csv('data/processed/climate_data_with_spei_8scales.csv')
    # Distribution, missing values, outliers
    df.describe(); df.isnull().sum()
    # Per-division & per-season trends
    sns.boxplot(data=df, x='Station', y='Rainfall_Total')
    # 1961-2023 temperature trend (climate change signal)
```
→ Output: `figs/eda_distribution.png`, `figs/eda_trend.png`, `figs/eda_division_boxplot.png`

### 2. ADF Test (Phase 6b)
```python
from statsmodels.tsa.stattools import adfuller
for station in stations:
    for scale in [1,3,6,12]:
        p_val = adfuller(df_spei[f'SPEI_{scale}m'])[1]   # p < 0.05 → stationary
        # যদি non-stationary → differencing (d) দরকার ARIMA-তে
```
→ Output: `outputs/adf_results.csv` — কোন scale-এ কত differencing লাগবে তার ছক।

### 3. SPEI Classification (Phase 5, line 2175 বদলাও)
```python
# আগে: Is_Drought_Binary = (SPEI_12m < -0.5)   ← hydrological
# নতুন PRIMARY:
df['Drought_Meteo'] = (df['SPEI_3m'] < -0.5).astype(int)     # 🌡️ primary
df['Drought_Agri']  = (df['SPEI_6m'] < -0.5).astype(int)     # 🌾 extension
df['Drought_Hydro'] = (df['SPEI_12m'] < -0.5).astype(int)    # 💧 extension (আগের ৯৭% কাজ)
```

### 4. Hyperparameter Tuning (Phase 6 আপগ্রেড)
```python
from sklearn.model_selection import GridSearchCV
param_grid = {'n_estimators':[500,700,900], 'max_depth':[7,9,12]}
gs = GridSearchCV(XGBClassifier(), param_grid, cv=3)   # Optuna দিয়েও করা যায়
```

### 5. Persistence Baseline (Phase 6a যোগ করো) ⭐ সবচেয়ে গুরুত্বপূর্ণ
```python
# Naive baseline: "গত মাসের খরা = এই মাসের খরা"
persistence_pred = df.groupby('Station')['Drought_Meteo'].shift(1)
persistence_acc = accuracy_score(y_true, persistence_pred)
# তারপর দেখাও তোমার মডেল persistence_acc-এর চেয়ে কত বেশি → leakage critique বন্ধ
```

### 6–7. NSE & KGE (Phase 10, forecasting evaluation)
```python
# Forecasting model-এর predicted SPEI vs observed SPEI
NSE = 1 - np.sum((obs-sim)**2) / np.sum((obs-obs.mean())**2)
r = np.corrcoef(obs, sim)[0,1]; alpha = sim.std()/obs.std(); beta = sim.mean()/obs.mean()
KGE = 1 - np.sqrt((r-1)**2 + (alpha-1)**2 + (beta-1)**2)
```

### 8. Kruskal-Wallis (Phase 10)
```python
from scipy.stats import kruskal
# Boro/Aus/Aman মৌসুমে drought severity আলাদা কি না
H, p = kruskal(boro_severity, aus_severity, aman_severity)   # p<0.05 → আলাদা
```

### 9. Taylor Diagram (Phase 7, নতুন figure)
```python
def create_taylor_diagram():
    # ৮ SPEI scale বা ৩৫ station এক polar plot-এ
    # radial = std, angular = correlation, distance = RMSE
```
→ Output: `figs/figure_taylor_diagram.png` (reviewer-এর প্রিয়)

### 10. ACF/PACF (Phase 6b)
```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(df_spei['SPEI_3m'], lags=40)    # PACF cut → p; ACF cut → q
```

### 11–13. ARIMA / SARIMA / LSTM (Phase 6b + 6c)
```python
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
arima = ARIMA(spei_series, order=(p,d,q)).fit()
sarima = SARIMAX(spei_series, order=(p,d,q), seasonal_order=(P,D,Q,12)).fit()
# LSTM (tensorflow.keras)
model = Sequential([LSTM(50, input_shape=(12,1)), Dense(1)])
```
→ Output: short-term (১–১২ মাস) + ১০-বছর outlook forecast figures + JSON

---

## ✅ Implementation Priority Order (ধাপে ধাপে)

1. **Phase 5 label বদল (SPEI-3m)** + **persistence baseline** — সবচেয়ে ছোট, সবচেয়ে গুরুত্বপূর্ণ ⭐
2. **Phase 6a retrain** (meteorological primary classification)
3. **Phase 0 EDA** + **Phase 10 Kruskal-Wallis** — দ্রুত, বিশ্লেষণ গভীর করে
4. **Phase 6b forecasting** (ADF→ACF/PACF→ARIMA/SARIMA/LSTM) — সবচেয়ে বড় কাজ, main value
5. **Phase 10 NSE/KGE** + **Phase 7 Taylor diagram** — evaluation ও visualization
6. **Phase 6c 10-year outlook** — শেষে, uncertainty band সহ

---
