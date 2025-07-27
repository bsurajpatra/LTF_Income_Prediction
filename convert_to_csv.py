import pandas as pd

file_path = "data/LTF Challenge data with dictionary.xlsx"

# Load sheets
train_df = pd.read_excel(file_path, sheet_name='TrainData')
test_df = pd.read_excel(file_path, sheet_name='TestData')

# Save as CSV
train_df.to_csv("data/train_data.csv", index=False)
test_df.to_csv("data/test_data.csv", index=False)

print("✅ CSV files created successfully.")
