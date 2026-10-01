from app.services.image_search_service import search_similar_images


def main():

    image_path = "test_image.jpg"

    results = search_similar_images(
        image_path,
        match_count=5
    )

    print("\nSimilar products:\n")

    for result in results:

        print(
            result["style_number"],
            "|",
            result["style_name"],
            "|",
            result["similarity"]
        )


if __name__ == "__main__":
    main()