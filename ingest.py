from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

DB_PATH = "chroma_db"
PDF_PATH = "data/banking_faq.pdf"

embeddings = OpenAIEmbeddings()

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
# STEP 3: Load or Create DB
# -----------------------------
db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

# Only add if empty
if db._collection.count() == 0:
    db.add_documents(chunks)
    print("Documents added to Chroma DB")
else:
    print("DB already exists, skipping ingestion")