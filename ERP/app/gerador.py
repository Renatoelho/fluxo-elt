
from gerador_dados import gerador_de_cliente_e_venda
from banco_de_dados import executa_query

def registra_cliente_e_venda() -> bool:
    try:
        cliente_e_venda = gerador_de_cliente_e_venda()
        cliente = cliente_e_venda[0]
        venda = cliente_e_venda[1]
        executa_query(cliente, venda)
        return True
    except Exception as _:
        return False

