from app.database import SessionLocal
from sqlalchemy import text
from app.services.search_service import client


COLLECTION_NAME = "finished_goods"


COLLECTION_SCHEMA = {
    "name": COLLECTION_NAME,
    "fields": [
        {"name": "style_number", "type": "string"},
        {"name": "style_name", "type": "string", "optional": True},
        {"name": "category", "type": "string", "optional": True, "facet": True},
        {"name": "fabric", "type": "string", "optional": True, "facet": True},
        {"name": "gsm", "type": "float", "optional": True},
        {"name": "color", "type": "string", "optional": True, "facet": True},
        {"name": "print", "type": "string", "optional": True, "facet": True},
        {"name": "season", "type": "string", "optional": True, "facet": True},
        {"name": "brand", "type": "string", "optional": True, "facet": True},
        {"name": "supplier", "type": "string", "optional": True, "facet": True},
        {"name": "cost", "type": "float", "optional": True},
        {"name": "selling_price", "type": "float"},
    ],
    "default_sorting_field": "selling_price",
}


def create_collection():

    try:
        client.collections[COLLECTION_NAME].delete()
        print("Existing collection deleted.")
    except Exception:
        pass

    client.collections.create(COLLECTION_SCHEMA)

    print("Finished Goods collection created successfully.")

def get_finished_goods():

    db = SessionLocal()

    try:
        query = text("""
            SELECT
                fg.style_number,
                fg.style_name,
                fg.category,
                fg.fabric,
                fg.gsm,
                fg.color,
                fg.print,
                fg.season,
                fg.brand,
                s.company_name AS supplier,
                fg.cost,
                fg.selling_price
            FROM finished_goods fg
            LEFT JOIN suppliers s
                ON fg.supplier_id = s.id
        """)

        result = db.execute(query)

        return [dict(row) for row in result.mappings().all()]

    finally:
        db.close()

def index_finished_goods():

    products = get_finished_goods()

    documents = []

    for product in products:

        document = {
            "id": product["style_number"],
            "style_number": product["style_number"],
            "style_name": product["style_name"] or "",
            "category": product["category"] or "",
            "fabric": product["fabric"] or "",
            "gsm": float(product["gsm"]) if product["gsm"] is not None else 0,
            "color": product["color"] or "",
            "print": product["print"] or "",
            "season": product["season"] or "",
            "brand": product["brand"] or "",
            "supplier": product["supplier"] or "",
            "cost": float(product["cost"]) if product["cost"] is not None else 0,
            "selling_price": (
                float(product["selling_price"])
                if product["selling_price"] is not None
                else 0
            ),
        }

        documents.append(document)

    if documents:

        result = client.collections[
            COLLECTION_NAME
        ].documents.import_(
            documents,
            {"action": "upsert"}
        )

        print(f"Indexed {len(documents)} Finished Goods.")

        return result

    print("No Finished Goods found.")        