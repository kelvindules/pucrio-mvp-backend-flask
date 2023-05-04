from sqlalchemy import Column, String, Integer, Float

from  model import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column("pk_product", Integer, primary_key=True)
    name = Column(String(140), unique=True)
    count = Column(Integer)
    price = Column(Float)

    def __init__(self, name:str, count:int, price:float):
        self.name = name
        self.count = count
        self.price = price
