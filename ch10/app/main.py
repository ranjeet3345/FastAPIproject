from fastapi import FastAPI

app=FastAPI()

PRODUCTS=[
    {
        "id":1,
        "title":"Pizza",
        "price":109,
        "desc":"THis is very tasty Pizza made in China"
    },
    {
        "id":2,
        "title":"Chicken",
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

@app.get('/product')
async def all_products():
    return PRODUCTS


@app.get('/product/{product_id}')
async def single_product(product_id : int):
    for product in PRODUCTS:
        if product["id"]==product_id:
            return product


@app.post('/product')
async def create_product(new_product:dict):
    PRODUCTS.append(new_product)
    return {"status":"created","new_product":new_product}



#complete update
@app.put('/product/{product_id}')
def update_product(product_id:int,new_updated_product:dict):
    for index,product in enumerate(PRODUCTS):
        if product["id"]==product_id:
            PRODUCTS[index]=new_updated_product
            return {"status":"product_updated"}
        



#partial update
@app.patch('/product/{product_id}')
def partial_product(product_id:int,new_updated_product:dict):
    for product in PRODUCTS:
        if product["id"]==product_id:
            product.update(new_updated_product)
            return {"status":"product deleted "}
        

@app.delete('/product/{product_id}')
def delete_product(product_id:int,new_updated_product:dict):
    for index,product in enumerate(PRODUCTS):
        if product["id"]==product_id:
            PRODUCTS.pop(index)
            return {"status":"product_updated"}
        
