from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.sales_order import SalesOrder


router = APIRouter(
    prefix="/sales-orders",
    tags=["Sales Orders"]
)


@router.get("/")
def get_sales_orders(db: Session = Depends(get_db)):
    return db.query(SalesOrder).all()


@router.get("/{order_number}")
def get_sales_order(
    order_number: str,
    db: Session = Depends(get_db)
):
    sales_order = (
        db.query(SalesOrder)
        .filter(SalesOrder.order_number == order_number)
        .first()
    )

    if not sales_order:
        raise HTTPException(
            status_code=404,
            detail="Sales order not found"
        )

    return sales_order