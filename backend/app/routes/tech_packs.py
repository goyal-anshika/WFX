from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.tech_pack import TechPack


router = APIRouter(
    prefix="/tech-packs",
    tags=["Tech Packs"]
)


@router.get("/")
def get_tech_packs(db: Session = Depends(get_db)):
    return db.query(TechPack).all()


@router.get("/{tech_pack_id}")
def get_tech_pack(
    tech_pack_id: str,
    db: Session = Depends(get_db)
):
    tech_pack = (
        db.query(TechPack)
        .filter(TechPack.tech_pack_id == tech_pack_id)
        .first()
    )

    if not tech_pack:
        raise HTTPException(
            status_code=404,
            detail="Tech pack not found"
        )

    return tech_pack


@router.get("/style/{style_number}")
def get_tech_pack_by_style(
    style_number: str,
    db: Session = Depends(get_db)
):
    tech_pack = (
        db.query(TechPack)
        .filter(TechPack.style_number == style_number)
        .first()
    )

    if not tech_pack:
        raise HTTPException(
            status_code=404,
            detail="Tech pack not found for this style"
        )

    return tech_pack