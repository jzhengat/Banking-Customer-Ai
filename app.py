import streamlit as st

from agents.orchestrator import process_message

if st.button("Submit"):

    if not user_input:
        st.warning("Please enter a comment or query before submitting.")
        st.stop()

    result = process_message(user_input)

    st.write("Type:", result["type"])
    st.write("Sentiment:", result["sentiment"])
    st.success(result["response"])