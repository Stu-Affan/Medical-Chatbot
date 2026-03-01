from tools.medical_rag_tool import medical_rag_tool
from tools.drug_tool import drug_info_tool
from tools.hospital_finder import find_nearby_hospitals
from safety import is_emergency
from tools.symptom_tool import symptom_analysis_tool


# -----------------------------
# Greeting Detection
# -----------------------------
def is_greeting(query: str) -> bool:
    greetings = [
        "hi", "hello", "hey",
        "good morning", "good afternoon", "good evening"
    ]
    return query.lower().strip() in greetings


# -----------------------------
# Symptom Detection
# -----------------------------
def is_symptom_query(query: str) -> bool:
    symptom_words = [
        "pain", "itch", "fever", "headache", "dizziness",
        "vomiting", "nausea", "cough", "throat",
        "burning", "swelling", "weakness", "fatigue"
    ]
    return any(word in query.lower() for word in symptom_words)


# -----------------------------
# Hospital Detection
# -----------------------------
def is_hospital_query(query: str) -> bool:
    hospital_keywords = [
        "hospital", "clinic",
        "nearby hospital",
        "hospital near me",
        "find hospital",
        "nearest hospital",
        "show hospitals"
    ]
    return any(word in query.lower() for word in hospital_keywords)


# -----------------------------
# Drug Detection
# -----------------------------
def is_drug_query(query: str) -> bool:
    drug_keywords = [
        "tablet", "capsule", "side effect", "dosage",
        "ibuprofen", "paracetamol", "advil",
        "medicine", "drug"
    ]
    return any(word in query.lower() for word in drug_keywords)


# -----------------------------
# Router
# -----------------------------
def route_query(query: str, location=None) -> str:

    query_lower = query.lower()

    # ⭐ If location exists but no text → hospital intent
    if location and not query_lower.strip():
        return find_nearby_hospitals(location)
    # 1️⃣ Greeting
    if is_greeting(query_lower):
        return (
            "Hello 👋 I'm your medical assistant.\n\n"
            "You can ask me about:\n"
            "• Symptoms\n"
            "• Diseases\n"
            "• Medicines\n"
            "• Nearby hospitals\n\n"
            "How can I help you today?"
        )

    # 2️⃣ Emergency (highest priority)
    if is_emergency(query_lower):
        hospitals = find_nearby_hospitals(location)
        return f"""
⚠️ This may indicate a medical emergency.

Please seek immediate medical attention.

Nearby Hospitals:
{hospitals}
"""

    # 3️⃣ Hospital query (WITH LOCATION)
    if is_hospital_query(query_lower):
        return find_nearby_hospitals(location)

    # 4️⃣ Symptom Analysis
    if is_symptom_query(query_lower):
        return symptom_analysis_tool(query)

    # 5️⃣ Drug
    if is_drug_query(query_lower):
        return drug_info_tool(query)

    # 6️⃣ Default
    return medical_rag_tool(query)