from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# -----------------------------
# LLM
# -----------------------------
llm = ChatOpenAI(model="gpt-4o-mini")

# -----------------------------
# Embeddings (must match ingest.py)
# -----------------------------
embeddings = OpenAIEmbeddings()

# -----------------------------
# Load vector DB
# -----------------------------
DB_PATH = "chroma_db"

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 3})


# -----------------------------
# RAG QUERY FUNCTION
# -----------------------------
def answer_query(question: str):

    docs = retriever.invoke(question)

    # -------------------------
    # SAFETY: handle empty DB
    # -------------------------
    if not docs:
        return llm.invoke(
            f"You are a banking assistant. Answer this question generally:\n\n{question}"
        ).content

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a helpful banking assistant.

Use ONLY the context below to answer the question.
If the answer is not clearly in the context, say you don't know.

Context:
{context}

Question:
{question}

Answer:
"""

    return llm.invoke(prompt).content