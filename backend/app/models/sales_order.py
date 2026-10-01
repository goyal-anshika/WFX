from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class SalesOrder(Base):
    __tablename__ = "sales_orders"

    id = Column(UUID(as_uuid=True), primary_key=True)

    order_number = Column(
        String,
        unique=True,
        nullable=False
    )

    buyer_id = Column(
        UUID(as_uuid=True),
        ForeignKey("buyers.id")
    )

    style_number = Column(
        String,
        ForeignKey("finished_goods.style_number"),
        nullable=False
    )

    quantity = Column(Integer, nullable=False)

    unit_price = Column(Numeric(12, 2))

    shipment_date = Column(Date)

    status = Column(String)