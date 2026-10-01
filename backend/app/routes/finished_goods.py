from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.finished_good import FinishedGood


router = APIRouter(
    prefix="/finished-goods",
    tags=["Finished Goods"]
)


@router.get("/")
def get_finished_goods(db: Session = Depends(get_db)):
    return db.query(FinishedGood).all()


@router.get("/{style_number}")
def get_finished_good(
    style_number: str,
    db: Session = Depends(get_db)
):
    finished_good = (
        db.query(FinishedGood)
        .filter(FinishedGood.style_number == style_number)
        .first()
    )

    if not finished_good:
        raise HTTPException(
            status_code=404,
            detail="Finished good not found"
        )

    return finished_good