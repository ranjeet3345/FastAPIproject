from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()

##Pydantic field
##Nested Body
# class Category(BaseModel):
#     name:str=Field(
#         title="Product name",
#         description="the name of the product category",
#         max_length=20,
#         min_length=3,
#         pattern="^[A-Za-z0-9]+$"
#     )
#     description:str|None=Field(
#         default=None,
#         title="Product name",
#         description="the name of the product category",
#         max_length=200,
       
#     )


# class Product(BaseModel):
#     name:str=Field(
#         title="Product name",
#         description="the name of the product category",
#         max_length=20,
#         min_length=3,
#         pattern="^[A-Za-z0-9]+$"
#     )
#     price:float=Field(
#         title="Product name",
#         description="the name of the product",
#         ge=10,

#     )
#     stock:int|None=Field(
#         default=None,
#         ge=0,
#     )
#     category : Category| None=Field(
#         default=None,
#         title="Product Category link",
#         description="the name of the category to whic product belongs !!",
#     )
    


# @app.post('/product')
# async def create_product(product:Product):
#     return product



class Category(BaseModel):
    name:str=Field(
        title="Product name",
        description="the name of the product category",
        max_length=20,
        min_length=3,
        pattern="^[A-Za-z0-9]+$"
    )
    description:str|None=Field(
        default=None,
        title="Product name",
        description="the name of the product category",
        max_length=200,
       
    )


class Product(BaseModel):
    name:str=Field(
        title="Product name",
        description="the name of the product category",
        max_length=20,
        min_length=3,
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
    category : list[Category]| None=Field(
        default=None,
        title="Product Category link",
        description="the name of the category to whic product belongs !!",
    )
    


@app.post('/product')
async def create_product(product:Product):
    return product

