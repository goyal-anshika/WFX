from openai import OpenAI

from app.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
)


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content