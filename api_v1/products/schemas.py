from pydantic import BaseModel, ConfigDict

#базовый класс
class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    
    
#объект чтобы создавать данные
class ProductCreate(ProductBase):
    pass
    
    
class ProductUpdate(ProductCreate):
    pass
    
    
class ProductUpdatePartial(ProductCreate):
    name: str | None = None
    description: str | None = None
    price: int | None = None
    
    
#объект чтобы возвращать данные    
class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    
    