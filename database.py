"""
Gerenciador de conexões Firebird e SQL Server
Suporta fallback quando drivers não estão disponíveis (ex: Streamlit Cloud)
"""
import pandas as pd
from typing import Optional
import streamlit as st
from config import EMPRESAS
import os

# Imports opcionais - podem não estar disponíveis em ambiente cloud
try:
    import fdb
    HAS_FDB = True
except ImportError:
    HAS_FDB = False

try:
    import pyodbc
    HAS_PYODBC = True
except ImportError:
    HAS_PYODBC = False

# Detectar ambiente
IS_STREAMLIT_CLOUD = "STREAMLIT_SERVER_HEADLESS" in os.environ or not (HAS_FDB and HAS_PYODBC)

class DatabaseManager:
    def __init__(self, empresa_id: int):
        self.empresa_id = empresa_id
        self.config = EMPRESAS[empresa_id]
        self.tipo_db = self.config["tipo_db"]
        self.connection = None

    def connect(self) -> bool:
        """Conecta ao banco de dados"""
        try:
            # Verificar se drivers estão disponíveis
            if self.tipo_db == "firebird" and not HAS_FDB:
                st.error(
                    "❌ **Driver Firebird não disponível em Streamlit Cloud**\n\n"
                    "Para usar Firebird, você tem duas opções:\n"
                    "1. **Instalar localmente** no seu computador\n"
                    "2. **Usar um proxy de banco de dados** (próximo passo)"
                )
                return False
            
            if self.tipo_db == "mssql" and not HAS_PYODBC:
                st.error(
                    "❌ **Driver SQL Server não disponível em Streamlit Cloud**\n\n"
                    "Para usar SQL Server, você tem duas opções:\n"
                    "1. **Instalar localmente** no seu computador\n"
                    "2. **Usar um proxy de banco de dados** (próximo passo)"
                )
                return False
            
            if self.tipo_db == "firebird":
                self.connection = fdb.connect(
                    host=self.config["host"],
                    database=self.config["database"],
                    user=self.config["user"],
                    password=self.config["password"],
                    port=self.config["port"]
                )
            elif self.tipo_db == "mssql":
                conn_str = (
                    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                    f"SERVER={self.config['host']};"
                    f"DATABASE={self.config['database']};"
                    f"UID={self.config['user']};"
                    f"PWD={self.config['password']}"
                )
                self.connection = pyodbc.connect(conn_str)

            return True
        except Exception as e:
            st.error(f"Erro ao conectar: {str(e)}")
            return False

    def execute_query(self, query: str) -> Optional[pd.DataFrame]:
        """Executa uma query SQL e retorna DataFrame"""
        try:
            if not self.connection:
                if not self.connect():
                    return None

            df = pd.read_sql(query, self.connection)
            return df
        except Exception as e:
            st.error(f"Erro ao executar query: {str(e)}")
            return None

    def close(self):
        """Fecha a conexão"""
        if self.connection:
            try:
                self.connection.close()
            except:
                pass

def load_query_from_file(filepath: str) -> str:
    """Carrega query SQL de um arquivo"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

@st.cache_resource
def get_db_manager(empresa_id: int) -> DatabaseManager:
    """Retorna instance cached do DatabaseManager"""
    return DatabaseManager(empresa_id)
