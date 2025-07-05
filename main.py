from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def index():
    return {'data':'blog_list'}




@app.get('/blog/{id}')
def showblog(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{"1","2"}}
    