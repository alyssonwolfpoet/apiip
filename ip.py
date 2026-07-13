from fastapi import FastAPI, Request

app = FastAPI()


def obter_ip(request: Request) -> tuple[str, str]:
    # Cloudflare
    ip = request.headers.get("cf-connecting-ip")
    if ip:
        return ip, "Cloudflare"

    # Proxy reverso (Nginx, Render, etc.)
    ip = request.headers.get("x-forwarded-for")
    if ip:
        return ip.split(",")[0].strip(), "X-Forwarded-For"

    # Conexão direta
    if request.client:
        return request.client.host, "Request Client"

    return "Desconhecido", "Nenhuma origem"


@app.get("/")
async def inicio(request: Request):
    ip, origem = obter_ip(request)

    return {
        "ip_publico": ip,
        "origem_ip": origem,
        "porta": request.client.port if request.client else None,
        "metodo": request.method,
        "url": str(request.url),
        "path": request.url.path,
        "user_agent": request.headers.get("user-agent"),
        "host": request.headers.get("host"),
    }