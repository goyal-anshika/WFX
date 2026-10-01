from app.services.llm_service import ask_llm


def generate_answer(question: str, sql: str, results: list) -> str:

    prompt = f"""
You are an ERP data assistant.

User question:
{question}

SQL used:
{sql}

Database results:
{results}

Answer the user's question using ONLY the provided database results.

Rules:
- Do not invent information.
- Be concise.
- If there are no results, say that no matching data was found.
"""

    return ask_llm(prompt).strip()