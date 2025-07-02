import streamlit as st

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
    question = st.text_input("What would you like to know?")
    if st.button("Get Answer"):
        # TEMPORARY RESPONSE — replace with chatbot model later
        st.success("🙌 The Bible says: 'Fear not, for I am with you' – Isaiah 41:10")

# ---------------------------
# 2. Verse Classifier
# ---------------------------
elif tool == "🔖 Verse Classifier":
    st.subheader("Classify a Bible Verse")
    verse = st.text_area("Paste a Bible verse here:")
    if st.button("Classify"):
        # TEMPORARY LOGIC — replace with ML model later
        st.info("🧠 Detected Topic: *Encouragement*")

# ---------------------------
# 3. Daily Verse
# ---------------------------
elif tool == "🌅 Daily Verse":
    st.subheader("🌞 Your Daily Verse")

    # Placeholder — can be loaded from file or API later
    verse = "“This is the day that the Lord has made; let us rejoice and be glad in it.” – Psalm 118:24"
    st.success(verse)
