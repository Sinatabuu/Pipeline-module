import streamlit as st
import joblib
import os


base_dir = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(base_dir, "models", "gift_model.pkl")

print("🔍 Trying to load model from:", model_path)

# Load model
model = joblib.load(model_path)

# Real spiritual gift questions
questions = [
    "I enjoy explaining Bible truths in a clear, structured way.",
    "I naturally take the lead when organizing ministry activities.",
    "I feel driven to share the gospel with strangers.",
    "I often sense spiritual warnings or encouragements for others.",
    "I easily feel compassion for people who are suffering.",
    "I enjoy giving resources to help others, even when it costs me.",
    "I’m happiest when working behind the scenes to help others.",
    "People often ask for my advice in complex spiritual matters.",
    "I enjoy studying and understanding deep biblical concepts.",
    "I trust God even in situations where others worry.",
    "I can often sense when something is spiritually wrong or deceptive.",
    "I enjoy hosting people and making them feel welcome.",
    "I often feel led to pray for others, even for long periods.",
    "I’m concerned about the spiritual growth of those around me.",
    "I naturally uplift others who are discouraged or unsure.",
    "I’ve prayed for people and seen them emotionally or physically healed.",
    "I enjoy pioneering new ministries or reaching unreached people.",
    "I enjoy managing projects and keeping people on track.",
    "I have spoken in a spiritual language not understood by others.",
    "I can understand and explain messages spoken in tongues.",
    "I stand firm in my faith even in hostile or public settings.",
    "I prepare lessons that help people grow in their faith.",
    "I look for ways to bring spiritual truth into everyday conversations.",
    "I cry or feel deeply moved when others are in pain.",
    "I often give above my tithe when I see a need.",
    "I influence others toward a vision in ministry.",
    "I can distinguish between truth and error without visible signs.",
    "I’ve had dreams, impressions, or messages that turned out accurate.",
    "I take personal responsibility for the spiritual welfare of others.",
    "I write or speak encouraging words that impact others deeply."
]

# Streamlit UI
st.title("🧪 Spiritual Gifts Assessment")
st.caption("Answer each question on a scale from 1 (Strongly Disagree) to 5 (Strongly Agree).")

with st.form("gift_assessment_form"):
    responses = []
    for i, q in enumerate(questions):
        score = st.slider(f"{i+1}. {q}", 1, 5, 3)
        responses.append(score)

    submitted = st.form_submit_button("🎯 Discover My Spiritual Gift")

# --- Fivefold Mapping Logic ---
gift_to_fivefold = {
    "Teaching": "Teacher",
    "Prophecy": "Prophet",
    "Evangelism": "Evangelist",
    "Service": "Pastor",
    "Giving": "Pastor",
    "Mercy": "Pastor",
    "Leadership": "Apostle"
}

# --- Prediction & Display ---
if submitted:
    try:
        prediction = model.predict([responses])[0]
        role = gift_to_fivefold.get(prediction, "Undetermined")

        # Results Section
        st.success(f"🧠 Your dominant spiritual gift is: **{prediction}**")

        if role != "Undetermined":
            st.info(f"👑 This aligns with the **Fivefold ministry role** of: **{role}**")
            st.markdown("✝️ *'So Christ himself gave the apostles, the prophets, the evangelists, the pastors and teachers...' – Ephesians 4:11*")
        else:
            st.warning("This gift does not directly map to one of the fivefold ministry roles.")

        # Store result summary
        summary = f"""Spiritual Gift Assessment Result
-----------------------------
Dominant Gift: {prediction}
Fivefold Role: {role}

Thank you for taking the Spiritual Gifts Assessment!
"""

    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")

# --- Fivefold Mapping ---
gift_to_fivefold = {
    "Teaching": "Teacher",
    "Prophecy": "Prophet",
    "Evangelism": "Evangelist",
    "Service": "Pastor",
    "Giving": "Pastor",
    "Mercy": "Pastor",
    "Leadership": "Apostle"
}

# --- Prediction & Display ---
if submitted:
    try:
        prediction = model.predict([responses])[0]
        role = gift_to_fivefold.get(prediction, "Undetermined")

        st.success(f"🧠 Based on your answers, your dominant spiritual gift is **{prediction}**.")

        st.markdown(f"👑 This aligns with the **Fivefold ministry role** of: **{role}**")

        st.markdown("✝️ *'So Christ himself gave the apostles, the prophets, the evangelists, the pastors and teachers...' – Ephesians 4:11*")

    except Exception as e:
        st.error(f"⚠️ Something went wrong: {e}")

# Prediction
if submitted:
    try:
        prediction = model.predict([responses])[0]
        st.success(f"🧠 Based on your answers, your dominant spiritual gift is **{prediction}**.")
    except Exception as e:
        st.error(f"⚠️ Something went wrong: {e}")
# Additional information