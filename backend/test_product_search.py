from app.services.search_service import search_products


result = search_products("dress")


print("FOUND:", result["found"])

for product in result["hits"]:

    print(
        product["document"]["style_number"],
        "-",
        product["document"]["style_name"]
    )