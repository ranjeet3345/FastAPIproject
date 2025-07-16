from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()

# ##Using Field level examples
# class Product(BaseModel):
#     name:str=Field(examples=["Moto e7"])
#     price:float=Field(examples=["45.56"])
#     stock:int|None=Field(default=None,examples=[43]) 



##Pydantic methid json_scheme
class Product(BaseModel):
    name:str
    price:float
    stock:int|None=None

    model_config={
        "json_schema_extra":{
            "examples":[
                {
                "name":"Moto e7",
                "price":"38.90"
            }
            ]
        }
    }





@app.post('/product')
async def create_product(product:Product):
    return product

