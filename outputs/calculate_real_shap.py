import joblib
import pandas as pd
import numpy as np
import os
import json
import shap
import time

models_dir = "/home/alamin/Documents/DroughtClassificationTest/models"
outputs_dir = "/home/alamin/Documents/DroughtClassificationTest/outputs"
output_json_path = os.path.join(outputs_dir, "precomputed_shap.json")

print("🔄 Starting authentic SHAP values calculation...")
start_time = time.time()

# 1. Load test data
test_data_path = os.path.join(outputs_dir, "shap_test_data.csv")
X_test = pd.read_csv(test_data_path)
print(f"Loaded test data with shape: {X_test.shape}")

# 2. Load models
rf = joblib.load(os.path.join(models_dir, "rf_model.joblib"))
xgb = joblib.load(os.path.join(models_dir, "xgb_model.joblib"))
cat = joblib.load(os.path.join(models_dir, "catboost_model.joblib"))
print("All 3 models loaded successfully.")

# 3. Compute RF SHAP
print("Calculating Random Forest SHAP values...")
t0 = time.time()
explainer_rf = shap.TreeExplainer(rf)
rf_shap = explainer_rf.shap_values(X_test)
if isinstance(rf_shap, list):
    rf_shap_pos = rf_shap[1]
elif len(rf_shap.shape) == 3:
    rf_shap_pos = rf_shap[:, :, 1]
else:
    rf_shap_pos = rf_shap
print(f"Random Forest SHAP calculated in {time.time() - t0:.1f}s. Shape: {rf_shap_pos.shape}")

# 4. Compute XGBoost SHAP
print("Calculating XGBoost SHAP values...")
t0 = time.time()
explainer_xgb = shap.TreeExplainer(xgb)
xgb_shap = explainer_xgb.shap_values(X_test)
if isinstance(xgb_shap, list):
    xgb_shap_pos = xgb_shap[1]
elif len(xgb_shap.shape) == 3:
    xgb_shap_pos = xgb_shap[:, :, 1]
else:
    xgb_shap_pos = xgb_shap
print(f"XGBoost SHAP calculated in {time.time() - t0:.1f}s. Shape: {xgb_shap_pos.shape}")

# 5. Compute CatBoost SHAP
print("Calculating CatBoost SHAP values...")
t0 = time.time()
explainer_cat = shap.TreeExplainer(cat)
cat_shap = explainer_cat.shap_values(X_test)
if isinstance(cat_shap, list):
    cat_shap_pos = cat_shap[1]
elif len(cat_shap.shape) == 3:
    cat_shap_pos = cat_shap[:, :, 1]
else:
    cat_shap_pos = cat_shap
print(f"CatBoost SHAP calculated in {time.time() - t0:.1f}s. Shape: {cat_shap_pos.shape}")

# 6. Ensemble SHAP values (Averaging)
ensemble_shap = (rf_shap_pos + xgb_shap_pos + cat_shap_pos) / 3.0
print(f"Ensemble SHAP shape: {ensemble_shap.shape}")

# 7. Save to JSON
print("Saving precomputed SHAP values to JSON...")
data_to_save = {
    "feature_names": X_test.columns.tolist(),
    "shap_values": ensemble_shap.tolist(),
    "test_data": X_test.values.tolist()
}

with open(output_json_path, "w", encoding="utf-8") as f:
    json.dump(data_to_save, f)

print(f"🎉 Success! Precomputed SHAP values saved to: {output_json_path}")
print(f"Total execution time: {time.time() - start_time:.1f}s")
