import sys
import time
from io import BytesIO

import requests
import psycopg2
from PIL import Image

from app.services.embedding_service import generate_image_embedding
from app.config import DATABASE_URL


BATCH_SIZE = 20


def main():

    print("Connecting to Supabase PostgreSQL...")

    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    print("Database connection successful.")

    cursor.execute("""
        SELECT
            id,
            style_number,
            image_url
        FROM public.finished_goods
        WHERE image_url IS NOT NULL
          AND image_embedding IS NULL
        ORDER BY style_number;
    """)

    products = cursor.fetchall()

    print(f"Products requiring embeddings: {len(products)}")

    if not products:
        print("No products require embeddings.")
        cursor.close()
        conn.close()
        return

    successful = 0
    failed = 0

    for index, (product_id, style_number, image_url) in enumerate(products, start=1):

        try:

            print(
                f"[{index}/{len(products)}] "
                f"Processing {style_number}..."
            )

            response = requests.get(
                image_url,
                timeout=30
            )

            response.raise_for_status()

            image = Image.open(
                BytesIO(response.content)
            ).convert("RGB")

            embedding = generate_image_embedding(image)

            cursor.execute(
                """
                UPDATE public.finished_goods
                SET image_embedding = %s
                WHERE id = %s
                """,
                (
                    embedding,
                    product_id
                )
            )

            successful += 1

            if successful % BATCH_SIZE == 0:

                conn.commit()

                print(
                    f"Committed {successful} embeddings."
                )

        except Exception as e:

            failed += 1

            print(
                f"FAILED: {style_number}"
            )

            print(
                f"Reason: {e}"
            )

    conn.commit()

    print()
    print("=" * 60)
    print("EMBEDDING GENERATION COMPLETE")
    print("=" * 60)

    print(f"Successful: {successful}")
    print(f"Failed:     {failed}")

    cursor.close()
    conn.close()

    print("Database connection closed.")


if __name__ == "__main__":
    main()