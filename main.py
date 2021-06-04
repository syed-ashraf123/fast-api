from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

app=FastAPI()

@app.get("/home")
def home():
    return JSONResponse(content={"NAME":True})

@app.post("/post")
async def post(request:Request):
    print(await request.json())
    return(200)