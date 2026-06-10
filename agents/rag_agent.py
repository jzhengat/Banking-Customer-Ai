from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

llm = ChatOpenAI(model="gpt-4o-mini")

embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 3})


def answer_query(question):

    docs = retriever.get_relevant_documents(question)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    You are a banking assistant.

    Use the context to answer.

    Context:
    {context}

    Question:
    {question}
    """

    return llm.invoke(prompt).content