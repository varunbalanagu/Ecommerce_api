from sqlalchemy import Column, Integer, String, Numeric
from src.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    category = Column(String, index=True)
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    
    # CRITICAL: Used to prevent overselling via concurrency control
    version = Column(Integer, nullable=False, default=1)