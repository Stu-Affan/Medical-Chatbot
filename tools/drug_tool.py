from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="alibayram/medgemma:4b",
    temperature=0.2
)

def drug_info_tool(query: str) -> str:
    prompt = f"""
You are a medical assistant.

Explain the following drug in a safe and factual way.

Include:
- What it is
- What it is used for
- Common side effects
- Important warnings

Be concise and medically accurate.

Drug: {query}
"""

    return llm.invoke(prompt)