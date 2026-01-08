from fastapi import FastAPI
from enum import Enum

app = FastAPI()

products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 10
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 20
    },
    {
        "id": 3,
        "name": "Product 1",
        "price": 30
    },
]

## All products
@app.get("/products")
def all_products():
    return products


## Single products with path parameter and parameter type
@app.get("/product/{product_id}")
def single_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    
    return "Not found!"


## Parameter with predefined value

class ProductCategory(str, Enum):
    book = "book"
    clothing = "clothing"
    electronics = "electronics"


@app.get("/category/{category_name}")
def product_category(category_name: ProductCategory):
    if category_name  == ProductCategory.book:
        return f"This is book category"
    elif category_name.value == "clothing":
        return f"This is clothing category"
    elif category_name == ProductCategory.electronics.value:
        return f"This is electronics category"

## Path converter (:path- it will take all paths of the url)
@app.get("/path_converter/{my_path:path}")
def path_converter(my_path):
    return f"All Path: {my_path}"