from src.database import engine, Base 
import src.models.user, src.models.product, src.models.order 
Base.metadata.create_all(bind=engine) 
print("Database tables created!") 
