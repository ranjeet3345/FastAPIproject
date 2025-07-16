from fastapi import FastAPI,Header
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()

##header parameter

# @app.get('/products')
# async def get_products(user_agent:Annotated[str|None,Header()]=None):
#     return user_agent


# # curl -H "User-Agent:Mozilla/5.0" http://127.0.0.1:8000/products


##Handling duplicate Headers
@app.get('/products')
async def get_products(x_product_token:Annotated[ list[str] ,Header()]=None):
    return {
        "x_product_token":x_product_token or []
    } 

##  dministrator@administrator-Latitude-7410:~$ curl -H "X-PRODUCT-TOKEN:token1" -H "X-PRODUCT-TOKEN:token2" http://127.0.0.1:8000/products
## output : {"x_product_token":["token1","token2"]}a