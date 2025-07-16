from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic  import BaseModel,Field



app=FastAPI()


@app.get('/',response_class=HTMLResponse)
async def get_form():
    return """"
      <html>
      
      <body>
        <h2>Login Form</h2>
         <form action="/login/" method="post">
    <label for="username">UserName:</label>
    <input type="text" id="username" name="username" placeholder="Enter your name" >
    <br>
     <label for="password">Password</label>
    <input type="text" id="password" name="password" placeholder="Enter your password">
     <br>
    
     <input type="submit" value="Submit">
    
  </form>
      
      </body>
      
      </html>
     
    """



class FormData(BaseModel):
    model_config={"extra":"forbid"}
    username:str=Field(min_length=7)
    password:str

# @app.post('/login/')
# async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
#     return {"username":username,"password":len(password)}




@app.post('/login/')
async def login(data:Annotated[FormData,Form()]):
    return data

