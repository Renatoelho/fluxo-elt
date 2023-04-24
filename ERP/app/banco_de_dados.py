
import pandas as pd

from os import getenv
from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy import create_engine


load_dotenv()

query_para_criar_tabela_clientes = """
CREATE TABLE IF NOT EXISTS clientes (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  sobrenome VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  telefone VARCHAR(20) NOT NULL,
  data_nascimento DATE NOT NULL,
  cidade VARCHAR(50) NOT NULL,
  estado VARCHAR(50) NOT NULL,
  pais VARCHAR(50) NOT NULL,
  codigo_pais VARCHAR(10) NOT NULL,
  datahora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
"""

query_para_criar_tabela_vendas = """
CREATE TABLE IF NOT EXISTS vendas (
  id INT NOT NULL AUTO_INCREMENT,
  produto VARCHAR(50) NOT NULL,
  data_compra DATE NOT NULL,
  tipo_cartao VARCHAR(60) NOT NULL,
  numero_cartao VARCHAR(20) NOT NULL,
  quantidade INT NOT NULL,
  valor VARCHAR(20) NOT NULL,
  datahora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
"""


URL_CONEXAO: str = (
    f"mysql+pymysql://{getenv('MYSQL_USER')}:"
    f"{getenv('MYSQL_PASS')}@"
    f"{getenv('MYSQL_HOST')}:"
    f"{getenv('MYSQL_PORT')}/"
    f"{getenv('MYSQL_DB')}"
)

engine = create_engine(url=URL_CONEXAO, echo=False)

def _executa_query(query: str) -> bool:
    try:
        query = text(f"{query}")
        with engine.connect() as conn:
            _ = conn.execute(query)
        return True
    except Exception as _:
        return False

def executa_query(lista_cliente: list, lista_venda: list) -> bool:
    try:
        _executa_query(query_para_criar_tabela_clientes)
        colunas_clientes = ["nome","sobrenome","email","telefone","data_nascimento","cidade","estado","pais","codigo_pais"]
        df_cliente = pd.DataFrame([lista_cliente], columns=colunas_clientes)
        df_cliente.to_sql(con=engine, name="clientes", if_exists="append", index=False)

        _executa_query(query_para_criar_tabela_vendas)
        colunas_vendas = ["produto","data_compra","tipo_cartao","numero_cartao","quantidade","valor"]
        df_vendas = pd.DataFrame([lista_venda], columns=colunas_vendas)
        df_vendas.to_sql(con=engine, name="vendas", if_exists="append", index=False)

        return True
    except Exception as _:
        return False
