from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

dict={}
app = FastAPI()



@app.get("/")
async def index_page():
    return FileResponse("index.html")

@app.post("/submit")
async def submit(studentName: str = Form(...), marks: int = Form(...)):
    dict[studentName]=marks
    return {"studentName": studentName, "marks": marks}
@app.get('/marks')
async def marks():
    return dict