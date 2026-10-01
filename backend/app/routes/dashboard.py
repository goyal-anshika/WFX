from fastapi import APIRouter

from app.database import engine
from sqlalchemy import text


router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def dashboard_stats():

    queries = {
        "finished_goods": "SELECT COUNT(*) FROM finished_goods",
        "suppliers": "SELECT COUNT(*) FROM suppliers",
        "buyers": "SELECT COUNT(*) FROM buyers",
        "sales_orders": "SELECT COUNT(*) FROM sales_orders",
        "sales_invoices": "SELECT COUNT(*) FROM sales_invoices",
    }

    result = {}

    with engine.connect() as connection:

        for key, query in queries.items():

            value = connection.execute(
                text(query)
            ).scalar()

            result[key] = value

    return result