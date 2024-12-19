from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from starlette.responses import RedirectResponse
from io import BytesIO

from agent import Agent
from file_handler import FileHandler


agent = Agent()

app = FastAPI(
    title="lambda",
    version="0.1.0",
    redoc_url=None,
)

@app.get("/ping")
def ping():
    return {"message": "hello"}


@app.post("/generate_text")
def generate_v1(file: UploadFile):
    file_extension = file.filename.split(".")[-1]
    content = file.file.read()
    if file_extension == "pdf":
        info = FileHandler.extract_text_from_pdf(content)
    elif file_extension == "docx":
        info = FileHandler.extract_text_from_word(content)
    else:
        return HTTPException(status_code=400, detail="File extension is not possible ATM.")
    if len(info) == 0:
        return HTTPException(status_code=400, detail="File is empty.")
    
    resolution = agent.generate(info)
    return resolution


@app.post("/generate_pdf")
def generate_v2(file: UploadFile):
    file_extension = file.filename.split(".")[-1]

    content = file.file.read()
    if file_extension == "pdf":
        info = FileHandler.extract_text_from_pdf(content)
    elif file_extension == "docx":
        info = FileHandler.extract_text_from_word(content)
    else:
        return HTTPException(status_code=400, detail="File extension is not possible ATM.")
    if len(info) == 0:
        return HTTPException(status_code=400, detail="File is empty.")
    
    resolution = agent.generate(info)
    
    pdf_buffer = FileHandler.create_pdf(resolution)
    headers = {'Content-Disposition': f'inline; filename="{file.filename}"',"content-type": "application/octet-stream"}
    return StreamingResponse(BytesIO(pdf_buffer), headers=headers, media_type='application/pdf')


@app.get("/", include_in_schema=False)
def main():
    return RedirectResponse(url="/docs/")