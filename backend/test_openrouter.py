from app.services.llm_service import ask_llm


def main():
    prompt = "Say hello and tell me that the WFX AI connection is working."

    response = ask_llm(prompt)

    print("\nLLM RESPONSE:")
    print(response)


if __name__ == "__main__":
    main()