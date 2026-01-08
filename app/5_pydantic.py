from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    id: int = Field(title="Product ID should be integer")
    name: str
    price: float
    stock: int

## Create product with validation and add a new calculated attribute
@app.post("/product")
def create_product(new_product: Product):
    product_dict = new_product.model_dump()
    price_with_tax = new_product.price + (new_product.price * 15 / 100)
    product_dict.update({"price_with_tax": price_with_tax})
    return product_dict