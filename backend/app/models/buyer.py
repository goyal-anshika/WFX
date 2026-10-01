from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(UUID(as_uuid=True), primary_key=True)
    buyer_id = Column(String, unique=True, nullable=False)
    company_name = Column(String, nullable=False)
    country = Column(String)
    buyer_category = Column(String)