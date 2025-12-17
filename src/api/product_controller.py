from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from src.database import get_db
from src.schemas.product import ProductCreate, ProductResponse
from src.repositories import product_repository

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def add_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    """Creates a new product in the catalog."""
    return product_repository.create_product(db, product_data)

@router.get("/", response_model=List[ProductResponse])
def list_products(
    category: Optional[str] = Query(None), 
    db: Session = Depends(get_db)
):
    """Lists all available products."""
    return product_repository.get_all_products(db, category)