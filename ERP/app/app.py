#!/home/ERP/.virtualenvs/bin/python3

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from gerador import clientes
from gerador import vendas


app = FastAPI()


@app.get("/healthcheck")
async def check() -> dict:
    try:
        if not clientes():
             raise ValueError("Erro")
        if not vendas():
            raise ValueError("Erro")
        return JSONResponse(status_code=200, content="Tudo Ok com o servidor.")
    except Exception as _:
        return JSONResponse(status_code=500, content="Ocorreu um erro interno no servidor.")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app:app",
        host="0.0.0.0",
        port=8888,
        log_level="info",
        reload=True
    )