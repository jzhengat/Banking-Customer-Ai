from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")


def classify_message(message):
    prompt = f"""
    Classify the message into one of:
    - positive_feedback
    - negative_feedback
    - query

    Message: {message}

    Return only one label.
    """

    return llm.invoke(prompt).content.strip().lower()