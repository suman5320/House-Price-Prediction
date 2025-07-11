# 🏡 House Price Predictor


This project predicts house prices using a machine learning model trained on selected features from a housing dataset. It includes an interactive **Jupyter Notebook for EDA and modeling**, and a **FastAPI backend** for making predictions via API.

---

## 🚀 Project Features

✅ Exploratory Data Analysis (EDA)  
✅ Feature selection & preprocessing using pipelines  
✅ XGBoost Regression model  
✅ Deployment-ready FastAPI endpoint  
✅ Accepts JSON input for real-time prediction

---

## 📁 Repository Structure


---

## 🔍 Dataset Info

> The dataset contains various numerical and categorical features related to residential homes.  
> This project focuses on a subset of the most influential features:
- `OverallQual` (Overall material and finish quality)
- `GrLivArea` (Above grade living area in square feet)
- `GarageCars` (Number of cars garage can hold)
- `TotalBsmtSF` (Total square feet of basement area)
- `FullBath` (Number of full bathrooms)
- `YearBuilt` (Year the house was built)

---

## 📊 Jupyter Notebook: Model Development

Open the notebook `house_price_predictor.ipynb` to:

- Perform EDA with visualizations
- Clean and transform the dataset
- Train a regression model using XGBoost
- Evaluate with R², MAE, and RMSE
- Save a pipeline with preprocessing + model

---

## 🔌 FastAPI: Model Deployment

The FastAPI app (`main.py`) loads the trained pipeline and exposes a prediction endpoint:

### 🔧 Endpoint

### 📥 Sample JSON Input:
```json
{
  "OverallQual": 7,
  "GrLivArea": 1710,
  "GarageCars": 2,
  "TotalBsmtSF": 856,
  "FullBath": 2,
  "YearBuilt": 2003
}
```
### 📤 Sample Response:
```json
{
  "predicted_price": 208383.12
}
```
▶️ Run Locally:
uvicorn main:app --reload
Then open in browser: http://127.0.0.1:8000/docs


