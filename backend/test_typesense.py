from app.services.search_service import client


try:
    response = client.operations.is_healthy()

    print("Typesense connection successful.")
    print(response)

except Exception as e:
    print("Typesense connection failed.")
    print(e)