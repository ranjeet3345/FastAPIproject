from fastapi import FastAPI,Path,Query
from typing import Annotated
from pydantic import AfterValidator

app=FastAPI()

PRODUCTS=[
    {
        "id":1,
        "title":"Pizza plaza",
        "price":109,
        "desc":"THis is very tasty Pizza made in China"
    },
    {
        "id":2,
        "title":"Chicken curry",
        "price":179,
        "desc":"THis is very tasty Chicken made in China"
    },
    {
        "id":3,
        "title":"Mutton Biryani",
        "price":209,
        "desc":"THis is very tasty Mutton biryani  made in China"
    }
]

# #Basic query
# @app.get('/product/{product_id}')
# async def get_product(product_id:int):
#     for product in PRODUCTS:
#         if product["id"]==product_id:
#             return product
#         return {"error":"Product not found"}
    
## Numeric validation
# @app.get('/product/{product_id}')
# async def get_product(product_id: Annotated[int,Path(ge=1,le=3)]):
#     for product in PRODUCTS:
#         if product["id"]==product_id:
#             return product
#     return {"error":"Product not found"}



#Adding metadata
@app.get('/product/{product_id}')
async def get_product(product_id: Annotated[int,Path(title="product details",description="detailed list of product details")]):
    for product in PRODUCTS:
        if product["id"]==product_id:
            return product
    return {"error":"Product not found"}