EMERGENCY_KEYWORDS = [
    "chest pain",
    "stroke",
    "overdose",
    "can't breathe",
    "cannot breathe",
    "heart attack",
    "severe bleeding",
    "unconscious",
    "suicide",
    "seizure"
]

def is_emergency(query: str) -> bool:
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in EMERGENCY_KEYWORDS)