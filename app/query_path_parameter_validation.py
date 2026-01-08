from fastapi import FastAPI, Query, Path
from typing import Annotated


app = FastAPI()


shipment = {
    12701: {
        "weight": 0.6,
        "content": "glassware",
        "status": "place"
    },
    12702: {
        "weight": 2.3,
        "content": "books",
        "status": "in_transit"
    },
    12703: {
        "weight": 5.0,
        "content": "electronics",
        "status": "delivered"
    },
    12704: {
        "weight": 0.2,
        "content": "documents",
        "status": "awaiting_pickup"
    },
    12705: {
        "weight": 12.5,
        "content": "furniture",
        "status": "pending"
    },
    12706: {
        "weight": 1.1,
        "content": "clothing",
        "status": "returned"
    },
    12707: {
        "weight": 0.9,
        "content": "cosmetics",
        "status": "lost"
    },
}

## Using Annotated
@app.get("/products/{product_id}")
def products(product_id: Annotated[str, Path(title="Product ID should be string", max_length=10)], search: Annotated[str | None, Query(max_length=5)] = None):
    return {
        "product_id": product_id,
        "search": search
    }