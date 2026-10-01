from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.sales_invoice import SalesInvoice


router = APIRouter(
    prefix="/sales-invoices",
    tags=["Sales Invoices"]
)


@router.get("/")
def get_sales_invoices(db: Session = Depends(get_db)):
    return db.query(SalesInvoice).all()


@router.get("/{invoice_number}")
def get_sales_invoice(
    invoice_number: str,
    db: Session = Depends(get_db)
):
    invoice = (
        db.query(SalesInvoice)
        .filter(SalesInvoice.invoice_number == invoice_number)
        .first()
    )

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Sales invoice not found"
        )

    return invoice