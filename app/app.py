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
tool = st.sidebar.radio("🛠 Choose a Tool:", [
    "📖 BibleBot", 
    "🔖 Verse Classifier", 
    "🌅 Daily Verse", 
    "🧪 Spiritual Gifts Assessment"
])

st.title("Tukuza Yesu AI Toolkit")

# ---------------------------
# 1. BibleBot
# ---------------------------
if tool == "📖 BibleBot":
    
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

# ---------------------------
# 4. Spiritual Gifts Assessment
# ---------------------------
elif tool == "🧪 Spiritual Gifts Assessment":
    import joblib
    import os

    # Load model
    model_path = os.path.join("models", "gift_model.pkl")
    model = joblib.load(model_path)

    # Questions
    questions = [ ... ]  # ⬅️ use full list of 30 real questions here

    gift_to_fivefold = {
        "Teaching": "Teacher",
        "Prophecy": "Prophet",
        "Evangelism": "Evangelist",
        "Service": "Pastor",
        "Giving": "Pastor",
        "Mercy": "Pastor",
        "Leadership": "Apostle"
    }

    st.subheader("🧪 Spiritual Gifts Assessment")
    st.caption("Answer each question on a scale from 1 (Strongly Disagree) to 5 (Strongly Agree).")

    with st.form("gift_assessment_form"):
        responses = [st.slider(f"{i+1}. {q}", 1, 5, 3) for i, q in enumerate(questions)]
        submitted = st.form_submit_button("🎯 Discover My Spiritual Gift")

    if submitted:
        prediction = model.predict([responses])[0]
        role = gift_to_fivefold.get(prediction, "Undetermined")

        st.success(f"🧠 Your dominant spiritual gift is: **{prediction}**")
        st.info(f"👑 Fivefold Ministry Role: **{role}**")
        st.markdown("✝️ *'So Christ himself gave the apostles, the prophets, the evangelists, the pastors and teachers...' – Eph 4:11*")

        # Download button
        summary_text = f"""
==============================
🎁 Spiritual Gifts Assessment
==============================
Dominant Gift: {prediction}
Fivefold Role: {role}
Thank you for using the Tukuza Yesu Toolkit!
"""
        st.download_button("📥 Download My Result", data=summary_text, file_name="gift_result.txt", mime="text/plain")
