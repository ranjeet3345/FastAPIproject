from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated,List,Any

app=FastAPI()



class Product(BaseModel):
    id:int
    name:str
    price:float
    stock:int |None=None


# #without Response model
# @app.get('/products/')
# async def get_products()->Product:
#     return {
#             "id":1,
#             "name":"Ranjeet",
#             "price":90.03,
#              "stock":34
#     }


#with Response model
# @app.get('/products/',response_model=Product)
# async def get_products():
#     return {
#             "id":1,
#             "name":"Ranjeet",
#             "price":90.03,
#              "stock":34
#     }


#with Response model
@app.get('/products/',response_model=List[Product])
async def get_products():
    return [{
            "id":1,
            "name":"Ranjeet",
            "price":90.03,
             "stock":34
    }
    ]


class BaseUser(BaseModel):
    username:str
    fullname:str

class UserIn(BaseUser):
    password:str


@app.post('/users/',response_model=BaseUser)
async def create_user(user:UserIn):
    return user

