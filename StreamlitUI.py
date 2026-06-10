import streamlit as st

from app import BankingSupportMultiAgent
from database import create_database

create_database()

agent_system = BankingSupportMultiAgent()

st.title("Banking Customer Support AI Agent")

user_message = st.text_area(
    "Enter Customer Message"
)

if st.button("Submit"):

    classification = (
        agent_system.classifier.classify(user_message)
    )

    response = (
        agent_system.route(user_message)
    )

    st.subheader("Classification")
    st.success(classification)

    st.subheader("Agent Response")
    st.info(response)

    