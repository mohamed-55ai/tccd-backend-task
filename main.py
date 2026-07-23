from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db= SessionLocal()
    try:
        yield db 
    finally:
        db.close()


@app.post("/api/products",response_model=schemas.ProductResponse)
def create_product(product:schemas.ProductCreate, db: Session=Depends(get_db)):
    new_product=models.Product(name=product.name, price=product.price, category_id=product.category_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/api/products", response_model=list[schemas.ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


@app.get("/api/products/{id}", response_model=schemas.ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.patch("/api/products/{id}", response_model=schemas.ProductResponse)
def update_product(id: int, updated: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = updated.name
    product.price = updated.price
    product.category_id = updated.category_id

    db.commit()
    db.refresh(product)
    return product


@app.delete("/api/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
#######################################################################
@app.post("/api/categories", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    new_category = models.Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@app.get("/api/categories", response_model=list[schemas.CategoryResponse])
def get_all_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@app.get("/api/categories/{id}", response_model=schemas.CategoryResponse)
def get_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@app.patch("/api/categories/{id}", response_model=schemas.CategoryResponse)
def update_category(id: int, updated: schemas.CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.name = updated.name
    db.commit()
    db.refresh(category)
    return category


@app.delete("/api/categories/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    return {"message": "Category deleted successfully"}