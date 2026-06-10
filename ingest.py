from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

DB_PATH = "chroma_db"
DATA_PATH = "data"

embeddings = OpenAIEmbeddings()

# -----------------------------
# STEP 1: Load ALL documents
# -----------------------------
docs = []

for file in os.listdir(DATA_PATH):

    file_path = os.path.join(DATA_PATH, file)

    if file.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        docs.extend(loader.load())

    elif file.endswith(".txt"):
        loader = TextLoader(file_path, encoding="utf-8")
        docs.extend(loader.load())

# -----------------------------
# STEP 2: Split text
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)

print("Total chunks:", len(chunks))

# -----------------------------
# STEP 3: Create / load DB
# -----------------------------
db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

# Always rebuild safely (avoids stale DB issues)
db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory=DB_PATH
)

db.persist()

print("Vector DB updated with PDFs + text files")