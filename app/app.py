import streamlit as st

st.set_page_config(page_title="Pipeline Bible App", page_icon="📖")

st.title("📖 Welcome to the Pipeline Module")
st.write("If you see this message, your Streamlit app is working!")

verse = st.text_input("Type a Bible verse")

if st.button("Submit"):
    st.success(f"You typed: {verse}")
