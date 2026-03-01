from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

DB_PATH = "vectorstore/db_faiss"

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vectorstore
vectorstore = FAISS.load_local(
    DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Local MedGemma
llm = Ollama(
    model="alibayram/medgemma:4b",
    temperature=0.2
)

def medical_rag_tool(query: str) -> str:
    """
    Clean structured medical answer from RAG.
    """

    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a medical information assistant.

Using ONLY the information provided below,
generate a clear, structured answer.

Do NOT include:
- citations
- book references
- page numbers
- raw textbook fragments

Structure the answer as:

Definition:
Causes:
Symptoms:
When to See a Doctor (if applicable):

Keep it under 250 words.
Use simple, clear language.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.strip()