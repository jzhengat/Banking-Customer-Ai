# BUILD PHASE (one-time setup)

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

llm = ChatOpenAI(model="gpt-4o-mini")

embeddings = OpenAIEmbeddings()

DB_PATH = "chroma_db"
PDF_PATH = "data/banking_faq.pdf"


# -----------------------------
# STEP 1: Load PDF
# -----------------------------
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()


# -----------------------------
# STEP 2: Split into chunks
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)


# -----------------------------
# STEP 3: Create / Load Vector DB
# -----------------------------
db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

# Only add documents if DB is empty (prevents duplicates)
if len(db.get()['documents']) == 0:
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )


retriever = db.as_retriever(search_kwargs={"k": 3})


# -----------------------------
# STEP 4: QA Function
# -----------------------------
def answer_query(question):

    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a helpful banking assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

    return llm.invoke(prompt).content