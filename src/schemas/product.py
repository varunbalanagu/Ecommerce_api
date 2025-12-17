from pydantic import BaseModel
from decimal import Decimal

class ProductCreate(BaseModel):
    name: str
    price: Decimal
    stock_quantity: int
    category: str

class ProductResponse(ProductCreate):
    id: int
    version: int

    class Config:
        orm_mode = True