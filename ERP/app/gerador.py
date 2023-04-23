
from pathlib import Path
from datetime import datetime

def clientes() -> bool:
    try:
        local = Path(__file__).parent
        datahora = datetime.now().strftime("%Y%m%d%H%M%S")
        with open(f"{local}/{datahora}.txt", "w+") as arquivo:
            arquivo.write(datahora)
        return True
    except Exception as _:
        return False

def vendas() -> bool:
    try:
        print("Vendas...")
        return True
    except Exception as _:
        return False

