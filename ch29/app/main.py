from fastapi import FastAPI,Form,File,UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic  import BaseModel,Field
import os
import uuid
import shutil



app=FastAPI()

# @app.get("/", response_class=HTMLResponse)
# async def main():
#     return """
#     <html>
#         <body>
#             <h2>Single File Upload (bytes)</h2>
#             <form action="/files/" enctype="multipart/form-data" method="post">
#                 <input name="file" type="file">
#                 <input type="submit" value="Upload">
#             </form>
#         </body>
#     </html>
#     """


# @app.post('/files/')
# async def create_file(file:Annotated[bytes | None,File()]=None):
#     if not file:
#         return {"msg":"File not present"}
#     else:
#         return {"file length": len(file) }
        
    
## To save in HardDiisk
# @app.post('/files/')
# async def create_file(file:Annotated[bytes | None,File()]=None):
#     if not file:
#         return {"msg":"File not present"}
    
#     filename=f"{uuid.uuid4()}.bin"
#     save_path=f"uploads/{filename}"

#     os.makedirs('uploads',exist_ok=True)

#     with open(save_path,"wb") as buffer:
#         buffer.write(file)

#     return {"file size" : len(file)}        
    
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Single File Upload (bytes)</h2>
            <form action="/files/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>

            <h2>Single File Upload (Upload files)</h2>
            <form action="/Uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """


@app.post('/Uploadfiles/')
async def create_upload_file(file:Annotated[UploadFile | None,File()]=None):
    if not file:
        return {"msg":"File not present"}
    
    
    save_path=f"uploads/{file.filename}"

    os.makedirs('uploads',exist_ok=True)

    with open(save_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {"filename":file.filename,"content_type":file.content_type}


    
