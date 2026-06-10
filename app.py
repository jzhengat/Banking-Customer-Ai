from agents.orchestrator import process_message

if st.button("Submit"):
    result = process_message(user_input)

    st.write("Type:", result["type"])
    st.write("Sentiment:", result["sentiment"])
    st.success(result["response"])