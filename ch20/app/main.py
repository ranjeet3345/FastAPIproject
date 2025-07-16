from fastapi import FastAPI,Cookie
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()

@app.get('/product/recommendations')
async def get_recommendations(session_id : Annotated[str|None,Cookie()]=None):
    if session_id:
        return {
            "message":f"recommendation for {session_id}",
            "session_id":session_id
        }
    return {
            "message":"No Sssion ID",
            
        }


