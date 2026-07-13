from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def info(request: Request):
    return {
        "ip": request.client.host,
        "porta": request.client.port,
        "metodo": request.method,
        "url": str(request.url),
        "caminho": request.url.path,
        "headers": dict(request.headers),
        "cookies": request.cookies,
        "query": dict(request.query_params),
    }