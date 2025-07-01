import streamlit as st

st.set_page_config(page_title="Tukuza Bible App", page_icon="📖")

st.title("📖 Welcome to the Tukuza Yesu Bible App")
st.write("This is a test to verify Streamlit is running correctly.")

# Test input
verse = st.text_input("Type a Bible verse:")

if st.button("Submit"):
    st.success(f"You entered: {verse}")
# Streamlit app entry point
