from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

app=FastAPI()


fruits={
    "apple":"a juicy fruit",
    "banana":"a yellow delight"
}


##create Exception
class FruitException(Exception):
    def __init__(self,fruit_name:str):
        self.fruit_name=fruit_name


#Custom Exeption Handler
@app.exception_handler(FruitException)
async def Fruit_exception_handler(request:Request,exc:FruitException):
    return JSONResponse(
        status_code=418,
        content={"message":f"{exc.fruit_name} is not valid"}
    )


@app.get('/fruit/{fruit_name}')
async def read_fruit(fruit_name:str):
    if fruit_name not in fruits:
        raise FruitException(fruit_name=fruit_name) 
    return fruits[fruit_name]
