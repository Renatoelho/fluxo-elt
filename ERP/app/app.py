#!/home/ERP/.virtualenvs/bin/python3

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from gerador import registra_cliente_e_venda


app = FastAPI()


@app.get("/healthcheck")
def check() -> dict:
    try:
        if not registra_cliente_e_venda():
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