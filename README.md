# 🌾 L&T Finance Challenge – Farmer Income Prediction (2025)

## 🔍 Problem Statement

L&T Finance (LTF) is striving to enhance financial inclusion for India's unbanked farming population by enabling access to fair credit. One of the key requirements for this is **accurately predicting the annual income** of farmers using both traditional and alternate data sources.

This project builds a machine learning model that predicts `Target_Variable/Total Income` based on farmer demography, landholding, local climate, and socio-economic indicators.

---

## 📁 Project Structure

ltf_income_prediction/
├── data/
│   ├── LTF Challenge data with dictionary.xlsx   # Provided dataset
│   └── Predicted_Farmer_Income_Sample_.xlsx     # Submission format sample
├── convert_to_csv.py                            # Script to extract Excel sheets as CSV
├── train_model.py                               # ML model training and MAPE evaluation
├── predict_income.py                            # Predicts income for test dataset
├── ltf_income_predictions.csv                   # Final prediction output
├── requirements.txt                             # Python dependencies
├── README.md                                    # Project documentation

---

## ⚙️ Approach

1. **Data Preparation**  
   - Converted Excel sheets (`TrainData` and `TestData`) to CSV using `pandas`.
   - Dropped irrelevant columns like `FarmerID` during training.
   - Encoded categorical features using `LabelEncoder`.

2. **Model Selection**  
   - Started with **RandomForestRegressor** (sklearn) for its simplicity and robustness.
   - Evaluated performance using **Mean Absolute Percentage Error (MAPE)**.

3. **Training & Validation**  
   - Split training data into train-validation sets.
   - Achieved a baseline MAPE of **0.2336** on validation data.

4. **Prediction**  
   - Trained model was saved using `joblib`.
   - Predictions were made on `TestData`, and results were exported in the submission format.

---

## 📈 Result

- Validation MAPE: **0.2336**
- Predictions saved in: `ltf_income_predictions.csv`
- Submission format matches the sample provided by L&T Finance.

---

## 🧪 Dependencies

Install the required packages:


pip install -r requirements.txt

---


## 🚀 How to Run

# 1. Convert Excel sheets to CSV
python3 convert_to_csv.py

# 2. Train the model
python3 train_model.py

# 3. Generate predictions for submission
python3 predict_income.py

## 🧠 Future Improvements

    Incorporate external datasets (weather, crop pricing)

    Switch to XGBoost or CatBoost for higher performance

    Improve feature engineering and missing value handling

    Use SHAP or feature importance for model explainability

## 👨‍💻 Author

B. Suraj Patra
GitHub | Email

