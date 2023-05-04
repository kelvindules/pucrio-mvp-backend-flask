from pydantic import BaseModel
from typing import Optional, List
from model.product import Product

class ProductCreateUpdateSchema(BaseModel):
    name: str
    count: int
    price: float

class ProductSearchSchema(BaseModel):
    name: str = "Teste"

class ProductListSchema(BaseModel):
    products:List[ProductCreateUpdateSchema]

class ProductViewSchema(BaseModel):
    id: int = 1
    name: str = "Banana Prata"
    count: Optional[int] = 12
    price: float = 12.50

class ProductDeleteSchema(BaseModel):
    name: str

def render_product(product: Product):
    return {
        "id": product.id,
        "name": product.name,
        "count": product.count,
        "price": product.price
    }

def render_products(products: List[Product]):
    result = []
    for product in products:
        result.append({
            "name": product.name,
            "count": product.count,
            "price": product.price,
        })

    return {"products": result}