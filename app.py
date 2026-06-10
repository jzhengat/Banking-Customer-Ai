# streamlit main app; RUN PHASE (main application)

import streamlit as st

from agents.classifier_agent import classify_message
from agents.sentiment_agent import analyze_sentiment
from agents.rag_agent import answer_query
from agents.ticket_agent import handle_complaint

from database.db import init_db

init_db()

st.title("🏦 Banking Support AI (Multi-Agent + RAG)")

user_input = st.text_area("Enter your message")

if st.button("Submit"):

    if not user_input:
        st.warning("Please enter a message")
        st.stop()

    category = classify_message(user_input)
    sentiment = analyze_sentiment(user_input)

    st.write("**Category:**", category)
    st.write("**Sentiment:**", sentiment)

    # QUERY → RAG
    if "query" in category:
        response = answer_query(user_input)
        st.success(response)

    # NEGATIVE → TICKET
    elif "negative" in category:
        response = handle_complaint(user_input)
        st.error(response)

    # POSITIVE → THANK YOU
    else:
        st.success("Thank you for your feedback")