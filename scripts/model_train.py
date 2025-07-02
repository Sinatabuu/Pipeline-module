# Script to train ML model
# train_model.py

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Load dataset
df = pd.read_csv("data/verse_training_data.csv")
X = df["verse"]
y = df["topic"]

# Define the pipeline
pipeline = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("model", MultinomialNB())
])

# Train the model
pipeline.fit(X, y)

# Save the model and vectorizer separately
model_dir = "models"
os.makedirs(model_dir, exist_ok=True)

joblib.dump(pipeline.named_steps["model"], os.path.join(model_dir, "model.pkl"))
joblib.dump(pipeline.named_steps["vectorizer"], os.path.join(model_dir, "vectorizer.pkl"))

print("✅ Model and vectorizer saved!")
