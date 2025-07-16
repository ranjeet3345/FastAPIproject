from fastapi import FastAPI,Cookie
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()


##Pydantic model
# class ProductCookies(BaseModel):
#     session_id:str
#     preferred_category:str|None=None
#     tracking_id:str|None=None


# app.get('/product/recommendations')
# async def get_recommendations(cookies : Annotated[ProductCookies |None,Cookie()]=None):
#     response={"session_id":cookies.session_id}
#     if cookies.preferred_category:
#         response["message"]=f"Recommendation for {cookies.preferred_category} products"
#     else:
#         response["message"]=f"DEfault Recommendation for session"

#     return response



# ##Forbidden extra cookies
# class ProductCookies(BaseModel):
#     model_config={"extra":"forbid"}
#     session_id:str
#     preferred_category:str|None=None
#     tracking_id:str|None=None


# app.get('/product/recommendations')
# async def get_recommendations(cookies : Annotated[ProductCookies |None,Cookie()]=None):
#     response={"session_id":cookies.session_id}
#     if cookies.preferred_category:
#         response["message"]=f"Recommendation for {cookies.preferred_category} products"
#     else:
#         response["message"]=f"DEfault Recommendation for session"

#     return response



##Body parameter
class ProductCookies(BaseModel):
    session_id:str=Field(ge=0,)
    preferred_category:str|None=None
    tracking_id:str|None=None


app.get('/product/recommendations')
async def get_recommendations(cookies : Annotated[ProductCookies |None,Cookie()]=None):
    response={"session_id":cookies.session_id}
    if cookies.preferred_category:
        response["message"]=f"Recommendation for {cookies.preferred_category} products"
    else:
        response["message"]=f"DEfault Recommendation for session"

    return response
