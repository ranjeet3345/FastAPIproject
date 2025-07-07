from fastapi import FastAPI

app=FastAPI()

#default query parameter
# @app.get('/product')
# async def product(category:str ,limit:int=10):
#     return {"status":"OK","category":category,"limit":limit}

#optional parameter
@app.get('/product')
async def product(limit:int,category:str|None=None):
    return {"status":"OK","category":category,"limit":limit}

#Path and Query Parameter
@app.get('product/{year}')
async def product(year:int,limit:int):
    return {"status":"OK","limit":limit}
