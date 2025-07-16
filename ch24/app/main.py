from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated,List

app=FastAPI()



class Product(BaseModel):
    id:int
    name:str
    price:float
    stock:int |None=None


##Without return Type
# @app.get('/products')
# async def get_products():
#     return [
#             { "status":"OK"},
#             { "status":"200"},
#             ]  


## REturn type Annotation
# @app.get('/products/')
# async def get_products()->Product:
#     return {
#             "id":1,
#             "name":"Ranjeet",
#             "price":90.03,
#              "stock":34
#     }

# @app.get('/products/')
# async def get_products()->Product:
#     return {
#             "id":1,
#             "name":"Ranjeet",
#             "price":90.03,
            
#     }


# @app.get('/products/')
# async def get_products()->Product:
#     return {
#             "id":1,
#             "name":"Ranjeet",
#             "price":90.03,
#              "stock":34,
#              "desc":"this is Ranjeet yadav desc"
#     }


##IMp

# @app.get('/products/')
# async def get_products()->List[Product]:
#     return [

#         {
#             "id":1,
#             "name":"MOtorola",
#             "price":90.03,
#              "stock":34
#     },

#     {
#             "id":2,
#             "name":"Nothing",
#             "price":1000.03,
#              "stock":90
#     }

#     ]



## 
# @app.post('/product/')
# async def create_product(product:Product)->Product:
#     return product




class BaseUser(BaseModel):
    username:str
    fullname:str

class UserIn(BaseUser):
    password:str


@app.post('/users/')
async def create_user(user:UserIn)->BaseUser:
    return user

