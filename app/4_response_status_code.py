from fastapi import FastAPI, status

app = FastAPI()

## response status code
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created"}
