from fastapi import FastAPI, WebSocket,Request
from fastapi.responses import JSONResponse

# Create application
app = FastAPI(title='WebSocket Example')




@app.get("/")
def read_root():
    return JSONResponse(content={"Hello":"How are you"})



@app.post("/")
async def read_root(request:Request):
    print(request.json())
    return 200

