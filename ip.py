from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def inicio(request: Request):
    ip = request.client.host
    return {"ip": ip}