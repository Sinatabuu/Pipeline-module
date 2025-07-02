import streamlit as st
import joblib
import os

st.title("📖 Bible Verse Classifier")

# Correct file paths
model_path = os.path.join("models", "model.pkl")
vectorizer_path = os.path.join("models", "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Input
verse = st.text_area("Paste a Bible verse:")
if st.button("Classify"):
    if verse.strip() == "":
        st.warning("Please enter a verse.")
    else:
        X = vectorizer.transform([verse])
        prediction = model.predict(X)[0]
        st.success(f"🔖 Predicted Topic: **{prediction}**")
