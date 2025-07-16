from fastapi import FastAPI,Form,File,UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic  import BaseModel,Field
import os
import uuid
import shutil



app=FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
           
            <h2>Multiple Files Upload (Upload files)</h2>
            <form action="/Uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple >
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """


@app.post('/Uploadfiles/')
async def create_upload_file(files:Annotated[list[UploadFile],File()]):
    if not files:
        return {"msg":"File not present"}
    
    save_files=[]
    os.makedirs('uploads',exist_ok=True)
    for file in files:
        save_path=f"uploads/{file.filename}"
        with open(save_path,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)

        save_files.append({"filename":file.filename})
    
    
    

    return save_files


    
