from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.buyer import Buyer


router = APIRouter(
    prefix="/buyers",
    tags=["Buyers"]
)


@router.get("/")
def get_buyers(db: Session = Depends(get_db)):
    return db.query(Buyer).all()


@router.get("/{buyer_id}")
def get_buyer(
    buyer_id: str,
    db: Session = Depends(get_db)
):
    buyer = (
        db.query(Buyer)
        .filter(Buyer.buyer_id == buyer_id)
        .first()
    )

    if not buyer:
        raise HTTPException(
            status_code=404,
            detail="Buyer not found"
        )

    return buyer