from sqlalchemy import Column, String, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class FinishedGood(Base):
    __tablename__ = "finished_goods"

    id = Column(UUID(as_uuid=True), primary_key=True)

    style_number = Column(
        String,
        unique=True,
        nullable=False
    )

    style_name = Column(String)
    category = Column(String)
    fabric = Column(String)
    gsm = Column(Numeric)
    color = Column(String)
    print = Column(String)
    season = Column(String)
    brand = Column(String)

    supplier_id = Column(
        UUID(as_uuid=True),
        ForeignKey("suppliers.id")
    )

    cost = Column(Numeric(12, 2))
    selling_price = Column(Numeric(12, 2))
    image_url = Column(String)