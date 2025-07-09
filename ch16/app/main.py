from fastapi import FastAPI,Body
from pydantic import BaseModel
from typing import Annotated

app=FastAPI()


class Product(BaseModel):
    name:str
    price:float
    stock:int|None=None

class Seller(BaseModel):
    username:str
    full_name:str|None=None


# @app.post('/product')
# async def create_product(product:Product,seller:Seller):
#     return {"product":product,"seller":seller}



## Make Body OPtional 
# @app.post('/product')
# async def create_product(product:Product,seller:Seller|None=None):
#     return {"product":product,"seller":seller}


##Singular Value in Body
# @app.post('/product')
# async def create_product(
#     product:Product,
#     seller:Seller,
#     sec_key:Annotated[str,Body()]
#     ):

#     print(sec_key)
#     return {"product":product,"seller":seller,"sec_key":sec_key}



##Enbed a single Body parameter
##without Embed
# @app.post('/product')
# async def create_product(product:Product):
#     return product


##with embed
@app.post('/product')
async def create_product(product:Annotated[Product,Body(embed=True)]):
    return product

