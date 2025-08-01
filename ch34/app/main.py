from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

app=FastAPI()

items={
    "apple":"a juicy fruit",
    "banana":"a yellow delight"
}



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,exc:RequestValidationError):
    return PlainTextResponse(str(exc),status_code=404)


@app.get('/items/{item_id}')
async def read_item(item_id:int):
    return item_id
    
