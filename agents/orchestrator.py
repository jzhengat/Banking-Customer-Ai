from agents.classifier_agent import classify_message
from agents.sentiment_agent import analyze_sentiment
from agents.ticket_agent import handle_complaint
from agents.rag_agent import answer_query

def process_message(user_input):

    category = classify_message(user_input)
    sentiment = analyze_sentiment(user_input)

    if "query" in category:
        return {
            "type": "query",
            "response": answer_query(user_input),
            "sentiment": sentiment
        }

    elif "negative" in category:
        return {
            "type": "ticket",
            "response": handle_complaint(user_input),
            "sentiment": sentiment
        }

    else:
        return {
            "type": "feedback",
            "response": "Thank you for your feedback!",
            "sentiment": sentiment
        }