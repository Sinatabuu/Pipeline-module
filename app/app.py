import streamlit as st
import openai
import os
import joblib

# ---------------------------
# App Config
# ---------------------------
st.set_page_config(page_title="Tukuza Yesu AI Toolkit", page_icon="📖", layout="centered")

# ---------------------------
# Sidebar Navigation
# ---------------------------
st.sidebar.title("Tukuza Yesu")
tool = st.sidebar.radio("🛠 Choose a Tool:", ["📖 BibleBot", "🔖 Verse Classifier", "🌅 Daily Verse"])

st.title("Tukuza Yesu AI Toolkit")

# ---------------------------
# 1. BibleBot
# ---------------------------
if tool == "📖 BibleBot":
    st.subheader("Ask the BibleBot 📜")
    st.caption("🙋 Ask a question related to the Bible or Christian life.")

    question = st.text_input("What would you like to know?")
    openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

    if st.button("Get Answer") and question.strip():
        with st.spinner("Searching Scripture..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful Christian assistant. Answer with love, wisdom, and Scripture references."},
                        {"role": "user", "content": question}
                    ],
                    temperature=0.6
                )
                answer = response.choices[0].message.content
                st.success(answer)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")

# ---------------------------
# 2. Verse Classifier
# ---------------------------
elif tool == "🔖 Verse Classifier":
    st.subheader("Classify a Bible Verse")

    model_path = os.path.join("models", "model.pkl")
    vectorizer_path = os.path.join("models", "vectorizer.pkl")

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    st.write("🧠 Model can detect these topics:", model.classes_)

    verse = st.text_area("Paste a Bible verse here:")
    if st.button("Classify"):
        if verse.strip() == "":
            st.warning("Please enter a verse.")
        else:
            X = vectorizer.transform([verse])
            prediction = model.predict(X)[0]
            st.success(f"🧠 Detected Topic: **{prediction}**")

# ---------------------------
# 3. Daily Verse
# ---------------------------
elif tool == "🌅 Daily Verse":
    st.subheader("🌞 Your Daily Verse")
    verse = "“This is the day that the Lord has made; let us rejoice and be glad in it.” – Psalm 118:24"
    st.success(verse)
