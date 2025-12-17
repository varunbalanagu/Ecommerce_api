from sqlalchemy.orm import Session
from src.models.product import Product
from src.schemas.product import ProductCreate

def create_product(db: Session, product_data: ProductCreate):
    """Saves a new product to the database."""
    db_product = Product(
        name=product_data.name,
        price=product_data.price,
        stock_quantity=product_data.stock_quantity,
        category=product_data.category,
        version=1  # Initial version for optimistic locking
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_products(db: Session, category: str = None):
    """Retrieves all products, with optional category filtering."""
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    return query.all()