from langchain_ollama import OllamaLLM

from tools.medical_rag_tool import medical_rag_tool
from tools.drug_tool import drug_info_tool
from safety import detect_emergency


# -----------------------------
# Load MedGemma
# -----------------------------
llm = OllamaLLM(
    model="alibayram/medgemma:4b",
    temperature=0.2
)


# -----------------------------
# Router Logic
# -----------------------------
def route_query(query: str):

    q = query.lower()

    # 🚨 Emergency first
    if detect_emergency(q):
        return "EMERGENCY"

    # 💊 Drug detection
    drug_keywords = [
        "ibuprofen", "paracetamol", "metformin",
        "aspirin", "side effects", "dosage", "drug"
    ]

    if any(word in q for word in drug_keywords):
        return "DRUG"

    return "RAG"


# -----------------------------
# Main Run Function
# -----------------------------
def run_agent(query: str):

    route = route_query(query)

    # 🚨 Emergency
    if route == "EMERGENCY":
        return (
            "⚠️ This may indicate a medical emergency.\n\n"
            "Please seek immediate medical attention or call your local emergency number."
        )

    # 💊 Drug Tool
    if route == "DRUG":
        data = drug_info_tool(query)

        prompt = f"""
        Convert this drug data into a clear medical explanation:

        {data}
        """

    # 🧠 RAG Tool
    else:
        data = medical_rag_tool(query)

        prompt = f"""
        Convert this medical information into a clear explanation:

        {data}
        """

    # -----------------------------
    # LLM formats answer
    # -----------------------------
    answer = llm.invoke(prompt)

    disclaimer = (
        "\n\n⚠️ This information is for educational purposes only. "
        "Consult a qualified healthcare professional for medical advice."
    )

    return answer.strip() + disclaimer