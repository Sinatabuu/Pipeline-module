import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load the dataset
data_path = os.path.join("data", "gifts_training_data.csv")
df = pd.read_csv(data_path)

# Separate features and label
X = df.drop(columns=["DominantGift"])
y = df["DominantGift"]

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
os.makedirs("models", exist_ok=True)
model_path = os.path.join("models", "gift_model.pkl")
joblib.dump(model, model_path)

# Test prediction
sample = X.iloc[0].values.reshape(1, -1)
predicted = model.predict(sample)[0]

print("✅ Model trained and saved to:", model_path)
print("🎯 Sample prediction:", predicted)
