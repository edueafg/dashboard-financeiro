"""
Configurações de conexão com Firebird e SQL Server
CUSTOMIZE AQUI com seus dados de conexão
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Mapeamento de empresas com suas conexões
EMPRESAS = {
    1: {
        "nome": "Empresa 1 - Novo Original (Firebird)",
        "tipo_db": "firebird",
        "host": "192.168.1.98",
        "database": r"F:\Base\NOVORIGINAL.FDB",
        "user": "SYSDBA",
        "password": "masterkey",
        "port": 3050
    },
    2: {
        "nome": "Empresa 2 (Firebird/SQL Server)",
        "tipo_db": "firebird",  # Mude para "mssql" se for SQL Server
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",  # Ou r"F:\Base\arquivo.FDB"
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    3: {
        "nome": "Empresa 3 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    4: {
        "nome": "Empresa 4 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    5: {
        "nome": "Empresa 5 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    6: {
        "nome": "Empresa 6 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    7: {
        "nome": "Empresa 7 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    8: {
        "nome": "Empresa 8 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    9: {
        "nome": "Empresa 9 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    10: {
        "nome": "Empresa 10 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    11: {
        "nome": "Empresa 11 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    12: {
        "nome": "Empresa 12 (Firebird/SQL Server)",
        "tipo_db": "firebird",
        "host": "SEU_IP_AQUI",
        "database": r"C:\Caminho\Base.FDB",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
}

# Configuração de dashboards disponíveis
DASHBOARDS = {
    "dre": {
        "titulo": "📊 DRE - Demonstração de Resultado",
        "descricao": "Receitas, Custos e Despesas do período",
        "arquivo_query": "queries/financeiro/dre_mensal.sql"
    },
    "contas_receber": {
        "titulo": "💰 Contas a Receber",
        "descricao": "Análise de clientes em atraso",
        "arquivo_query": "queries/financeiro/contas_receber.sql"
    },
    "contas_pagar": {
        "titulo": "💳 Contas a Pagar",
        "descricao": "Análise de fornecedores",
        "arquivo_query": "queries/financeiro/contas_pagar.sql"
    },
    "fluxo_caixa": {
        "titulo": "💵 Fluxo de Caixa",
        "descricao": "Previsão 30/60/90 dias",
        "arquivo_query": "queries/financeiro/fluxo_caixa.sql"
    }
}

# Cores padrão
COLORS = {
    "receita": "#2ecc71",      # Verde
    "despesa": "#e74c3c",       # Vermelho
    "lucro": "#3498db",         # Azul
    "atraso": "#f39c12",        # Laranja
}
