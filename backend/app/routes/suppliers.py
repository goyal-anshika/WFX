from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.supplier import Supplier


router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)


@router.get("/")
def get_suppliers(db: Session = Depends(get_db)):
    return db.query(Supplier).all()


@router.get("/{supplier_id}")
def get_supplier(
    supplier_id: str,
    db: Session = Depends(get_db)
):
    supplier = (
        db.query(Supplier)
        .filter(Supplier.supplier_id == supplier_id)
        .first()
    )

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    return supplier