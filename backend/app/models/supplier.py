from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(UUID(as_uuid=True), primary_key=True)
    supplier_id = Column(String, unique=True, nullable=False)
    company_name = Column(String, nullable=False)
    country = Column(String)
    contact = Column(String)
    lead_time_days = Column(Integer)
    rating = Column(Numeric(3, 2))