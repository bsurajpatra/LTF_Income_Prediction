import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import LabelEncoder
import joblib

# Load and clean training data
df = pd.read_csv("data/train_data.csv")
df = df.drop(columns=['FarmerID'])
df = df.dropna(subset=['Target_Variable/Total Income'])

# Encode categorical features
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna('Unknown')
    df[col] = LabelEncoder().fit_transform(df[col])

# Split into features and target
X = df.drop(columns=['Target_Variable/Total Income'])
y = df['Target_Variable/Total Income']

# Train/test split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Validation
y_pred = model.predict(X_val)
mape = mean_absolute_percentage_error(y_val, y_pred)
print(f"✅ Validation MAPE: {mape:.4f}")

# Save model
joblib.dump(model, "model.pkl")
