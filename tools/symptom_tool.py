from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="alibayram/medgemma:4b",
    temperature=0.2
)

def symptom_analysis_tool(query: str) -> str:

    prompt = f"""
You are a clinical medical assistant.

A patient is describing symptoms.

Your task is to:

1. Identify possible causes
2. Suggest safe home remedies (if applicable)
3. Suggest common OTC support (if appropriate)
4. Tell when to see a doctor

Be practical, concise and safety-focused.
DO NOT give diagnosis.
DO NOT prescribe medication.

Symptoms: {query}

Respond ONLY in this format:

Possible Causes:
• ...

Potential Remedies:
• ...

OTC Support (if appropriate):
• ...

When to See a Doctor:
• ...
"""

    return llm.invoke(prompt)