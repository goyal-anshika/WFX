from sqlalchemy import Column, String, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class SalesInvoice(Base):
    __tablename__ = "sales_invoices"

    id = Column(UUID(as_uuid=True), primary_key=True)

    invoice_number = Column(
        String,
        unique=True,
        nullable=False
    )

    sales_order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("sales_orders.id")
    )

    amount = Column(
        Numeric(14, 2),
        nullable=False
    )

    currency = Column(
        String,
        default="USD"
    )

    payment_status = Column(String)