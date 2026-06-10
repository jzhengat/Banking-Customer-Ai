import streamlit as st
from agents.orchestrator import process_message

# -----------------------------
# UI HEADER
# -----------------------------
st.title("Banking Support AI Assistant")

# -----------------------------
# INPUT BOX
# -----------------------------
user_input = st.text_area("Enter your query or comment here:")

# -----------------------------
# SUBMIT BUTTON
# -----------------------------
if st.button("Submit"):

    if not user_input:
        st.warning("Please enter a comment or query before submitting.")
        st.stop()

    result = process_message(user_input)

    st.subheader("Results")
    st.write("Type:", result["type"])
    st.write("Sentiment:", result["sentiment"])
    st.success(result["response"])