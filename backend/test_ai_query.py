from app.services.ai_query_service import process_question


question = "Which buyer has the highest number of sales orders?"


response = process_question(question)


print("\nQUESTION:")
print(response["question"])

print("\nGENERATED SQL:")
print(response["sql"])

print("\nRESULTS:")
print(response["results"])

print("\nAI ANSWER:")
print(response["answer"])
