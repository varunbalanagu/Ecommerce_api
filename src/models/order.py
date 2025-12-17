from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.sql import func
from src.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="PENDING") # PENDING, COMPLETED, FAILED
    total_price = Column(Numeric(10, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())