import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("cleaned_blood_data.csv")

# Drop rows with missing essential values
df = df.dropna(subset=["blood_type", "donation_date", "shelf_life_days", "collection_volume_ml"])

# Convert donation_date to datetime
df["donation_date"] = pd.to_datetime(df["donation_date"], errors="coerce")
df = df.dropna(subset=["donation_date"])

# Feature engineering: day of year from donation_date
df["day_of_year"] = df["donation_date"].dt.dayofyear

# Map blood types to integers
blood_type_map = {'A+': 0, 'A-': 1, 'B+': 2, 'B-': 3, 'AB+': 4, 'AB-': 5, 'O+': 6, 'O-': 7}
df["blood_type_encoded"] = df["blood_type"].map(blood_type_map)
df = df.dropna(subset=["blood_type_encoded"])

# Features and target
X = df[["blood_type_encoded", "day_of_year", "collection_volume_ml"]]
y = df["shelf_life_days"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "expiry_predictor.pkl")
print("✅ Model saved as expiry_predictor.pkl")
