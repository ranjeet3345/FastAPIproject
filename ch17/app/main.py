from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()

##Pydantic field
class Product(BaseModel):
    name:str=Field(
        title="Product name",
        description="the name of the product",
        max_length=20,
        min_length=5,
        pattern="^[A-Za-z0-9]+$"
    )
    price:float=Field(
        title="Product name",
        description="the name of the product",
        ge=10,

    )
    stock:int|None=Field(
        default=None,
        ge=0,
    )


@app.post('/product')
async def create_product(product:Product):
    return {"product":product}

