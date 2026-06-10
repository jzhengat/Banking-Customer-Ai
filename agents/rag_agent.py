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
# Load existing vector DB
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

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a helpful banking assistant.

Answer ONLY using the context below.

If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}
"""

    return llm.invoke(prompt).content