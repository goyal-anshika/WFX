import psycopg2

from app.config import DATABASE_URL
from app.services.embedding_service import generate_image_embedding


def search_similar_images(
    image_path: str,
    match_count: int = 10,
):

    # Generate CLIP embedding
    embedding = generate_image_embedding(image_path)

    # Convert embedding to PostgreSQL vector format
    embedding_string = "[" + ",".join(
        str(float(value)) for value in embedding
    ) + "]"

    connection = psycopg2.connect(DATABASE_URL)

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM match_finished_goods(
                %s::vector,
                %s::integer
            );
            """,
            (
                embedding_string,
                int(match_count),
            ),
        )

        rows = cursor.fetchall()

        columns = [
            "id",
            "style_number",
            "style_name",
            "category",
            "fabric",
            "color",
            "print",
            "season",
            "brand",
            "image_url",
            "selling_price",
            "similarity",
        ]

        results = [
            dict(zip(columns, row))
            for row in rows
        ]

        cursor.close()

        return results

    finally:
        connection.close()