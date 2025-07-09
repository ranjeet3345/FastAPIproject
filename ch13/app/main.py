from fastapi import FastAPI,status,Query
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

#Basic query
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(search:str|None=None):
#     if search:
#         search_lower=search.lower()
#         filtered_products=[]
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
        
#         return filtered_products
#     return PRODUCTS


# #
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(search:str|None=Query(default=None,min_length=5)):
#     if search:
#         search_lower=search.lower()
#         filtered_products=[]
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
        
#         return filtered_products
#     return PRODUCTS


# #search with Annotated
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(
#                     search:
#                        Annotated[
#                         str|None,
#                         Query(default=None,max_length=5)
#                         ]=None):
#     if search:
#         search_lower=search.lower()
#         filtered_products=[]
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
        
#         return filtered_products
#     return PRODUCTS

# #requird parameter
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(
#                     search:
#                        Annotated[
#                         str,
#                         Query(min_length=5)
#                         ]):
#     if search:
#         search_lower=search.lower()
#         filtered_products=[]
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
        
#         return filtered_products
#     return PRODUCTS


#Regular Expression
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(
#                     search:
#                        Annotated[
#                         str|None,
#                         Query(min_length=3,pattern="^[a-z]+$")
#                         ]=None):
#     if search:
#         search_lower=search.lower()
#         filtered_products=[]
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
        
#         return filtered_products
#     return PRODUCTS


#Multiple search item
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(
#     search:
#     Annotated[
#         list[str] | None,
#         Query()
#         ]=None):
    
#     if search:
#         filtered_products=[]
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)

#         return filtered_products
#     return PRODUCTS            
        


#alias parametr
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(
#     search:
#     Annotated[
#         list[str] | None,
#         Query(alias='q')
#         ]=None):
    
#     if search:
#         filtered_products=[]
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)

#         return filtered_products
#     return PRODUCTS            
        


# #metadata adding 
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(
#     search:
#     Annotated[
#         list[str] | None,
#         Query(alias='q',title="search product",description="search by product title")
#         ]=None):
    
#     if search:
#         filtered_products=[]
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)

#         return filtered_products
#     return PRODUCTS            
        


#metadata adding 
# @app.get('/product',status_code=status.HTTP_200_OK)
# async def get_products(
#     search:
#     Annotated[
#         list[str] | None,
#         Query(deprecated=True)
#         ]=None):
    
#     if search:
#         filtered_products=[]
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)

#         return filtered_products
#     return PRODUCTS            
 

## Custom Validation
def check_valid_id(id:str):
    if not id.startswith("prod-"):
        raise ValueError("ID must start with 'prod-' ")
    return id

@app.get('/product')
async def get_products(
        id:Annotated[str|None,AfterValidator(check_valid_id)]=None
        ):
    if id:
        return {"id":id,"msg":"Valid ID"}
    return {"message":"No ID provided!!"}