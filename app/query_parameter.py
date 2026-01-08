from fastapi import FastAPI

app = FastAPI()

## Single query parameter (If we not define path parameter, it will be decide as a query parameter in fastapi)
@app.get("/products")
def products(category: str):
    return f"This is {category} category"

## Multiple query parameter 
@app.get("/user")
def user(name: str, limit: int):
    return f"This is {name} and his limit {limit}"

## Default query parameter
@app.get("/student")
def student(name: str, age: int = 20):
    return f"This is {name} and his age is {age}"

## Optional query parameter (optional parameter should be last of the parameter, otherwise it will not work)
@app.get("/cars")
def cars(name: str, color: str | None = None):
    return {
        "name": name,
        "color": color
    }
    
## Path Parameter and Query parameter 
@app.get("/books/{book_id}")
def books(book_id: int, book: str):
    return {
        "book_id": book_id,
        "book": book
    }