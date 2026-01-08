from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    title: str
    price: int | None = None

## Return Type
@app.get("/product")
def product()-> Product:
    return {
        "id": 1,
        "title": "Product 1",
        "stock": 10
    }

''' Here, extra stock will not be given any error and also not be added '''

class User(BaseModel):
    id: int
    name: str

## Return type using response model
@app.get("/users", response_model=User)
def get_all_users():
    return {
        "id": 1,
        "name": "Tanjim"
    }