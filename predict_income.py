import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# Load test data
test_df = pd.read_csv("data/test_data.csv")
farmer_ids = test_df['FarmerID']
X_test = test_df.drop(columns=['FarmerID'], errors='ignore')

# Also drop target column if it exists (safety check)
if 'Target_Variable/Total Income' in X_test.columns:
    X_test = X_test.drop(columns=['Target_Variable/Total Income'])


# Encode categoricals
for col in X_test.select_dtypes(include=['object']).columns:
    X_test[col] = X_test[col].fillna('Unknown')
    X_test[col] = LabelEncoder().fit_transform(X_test[col])

# Load model
model = joblib.load("model.pkl")

# Predict
predictions = model.predict(X_test)

# Create submission file
submission = pd.DataFrame({
    "FarmerID": farmer_ids,
    "Target_Variable/Total Income": predictions.astype(int)
})
submission.to_csv("ltf_income_predictions.csv", index=False)

print("✅ Predictions saved to ltf_income_predictions.csv")
