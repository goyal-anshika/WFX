from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class TechPack(Base):
    __tablename__ = "tech_packs"

    id = Column(UUID(as_uuid=True), primary_key=True)

    tech_pack_id = Column(
        String,
        unique=True,
        nullable=False
    )

    style_number = Column(
        String,
        ForeignKey("finished_goods.style_number"),
        nullable=False
    )

    fabric_details = Column(String)
    construction = Column(String)
    wash_instructions = Column(String)