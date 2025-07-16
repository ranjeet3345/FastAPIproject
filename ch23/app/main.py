from fastapi import FastAPI,Header
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()

# ##Pydantic Model

# class ProductHeader(BaseModel):
#     authorization:str
#     accept_language:str|None=None
#     x_tracking_id:list[str]=[]

# @app.get('/products')
# async def get_products(headers:Annotated[ ProductHeader ,Header()]):
#     return {
#         "headers":headers
#     } 


## Forbidden extra 
##Pydantic Model

class ProductHeader(BaseModel):
    model_config={"extra":"forbid"}
    authorization:str
    accept_language:str|None=None
    x_tracking_id:list[str]=[]

@app.get('/products')
async def get_products(headers:Annotated[ ProductHeader ,Header()]):
    return {
        "headers":headers
    }

