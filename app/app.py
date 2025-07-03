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
elif tool == "📖 BibleBot":
    import openai
    import os

    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY"))

    st.subheader("Ask the BibleBot 📜")
    st.caption("🙋 Ask anything related to the Bible or Christian life.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    question = st.chat_input("🖋️ Ask your Bible question...")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        try:
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            with st.chat_message("assistant"):
                reply = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": reply})
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
