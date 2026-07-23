from pydantic import BaseModel 

class ProductCreate(BaseModel):
    name: str
    price: float
    category_id: int
    
class ProductResponse(BaseModel):
    id:int
    name:str
    price:float
    category_id:int
    class config:
        from_attributes= True

class CategoryCreate(BaseModel):
    name:str

class CategoryResponse(BaseModel):
    id:int
    name:str
    class config:
        from_attributes=True
