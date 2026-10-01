import requests

from io import BytesIO
from PIL import Image

from app.services.embedding_service import generate_image_embedding


IMAGE_URL = (
    "https://raw.githubusercontent.com/"
    "alexeygrigorev/clothing-dataset/master/images/"
    "1b9a7610-e6d9-4bb8-ace9-ed4870ae0d5b.jpg"
)


def main():

    print("Downloading test image...")

    response = requests.get(
        IMAGE_URL,
        timeout=30
    )

    response.raise_for_status()

    image = Image.open(
        BytesIO(response.content)
    ).convert("RGB")

    print("Image downloaded.")

    embedding = generate_image_embedding(
        image
    )

    print("Embedding generated.")

    print(
        "Embedding dimensions:",
        len(embedding)
    )

    print(
        "First 10 values:",
        embedding[:10]
    )


if __name__ == "__main__":
    main()