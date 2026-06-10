from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")


def analyze_sentiment(message):
    prompt = f"""
    Detect sentiment:
    - positive
    - neutral
    - negative

    Message: {message}

    Return only one word.
    """

    return llm.invoke(prompt).content.strip().lower()