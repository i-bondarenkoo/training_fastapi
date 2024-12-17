from .base import Base
from sqlalchemy.orm import Mapped



class Product(Base):
    
    # модель таблицы 
    name: Mapped [str]
    description: Mapped [str]
    price: Mapped [int]