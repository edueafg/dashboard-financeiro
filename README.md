# 📊 Dashboard Financeiro RP Decalc

Sistema de dashboards financeiros multi-tenant para RP Decalc com autenticação email/senha.

**Suporta:** Firebird + SQL Server | **Usuários:** 20 | **Empresas:** 12

---

## 🎯 Características

✅ Autenticação segura (email/senha com bcrypt)
✅ Multi-tenant (12 empresas, cada usuário vê seus dados)
✅ 4 Dashboards financeiros prontos
✅ Deploy em nuvem (Streamlit Cloud, Heroku, etc)
✅ Queries SQL customizáveis
✅ Conexão com Firebird e SQL Server

---

## 📦 Instalação Local

### 1. Clone/Baixe os arquivos
```bash
git clone seu-repo
cd dashboard-financeiro
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as conexões em `config.py`
```python
EMPRESAS = {
    1: {
        "nome": "Sua Empresa A",
        "tipo_db": "firebird",
        "host": "192.168.1.100",
        "database": "/caminho/decalc.fdb",
        "user": "SYSDBA",
        "password": "sua_senha",
        "port": 3050
    },
    2: {
        "nome": "Sua Empresa B",
        "tipo_db": "mssql",
        "host": "sql-server.local",
        "database": "rp_decalc_b",
        "user": "sa",
        "password": "sua_senha",
        "port": 1433
    },
    # Adicione até 12 empresas
}
```

### 4. Customize as queries SQL
Edite os arquivos em `queries/financeiro/`:
- `dre_mensal.sql`
- `contas_receber.sql`
- `contas_pagar.sql`
- `fluxo_caixa.sql`

Use suas tabelas reais do RP Decalc.

### 5. Rode localmente
```bash
streamlit run app.py
```

Acesse: `http://localhost:8501`

---

## 🚀 Deploy em Produção

### Opção 1: Streamlit Cloud (Recomendado - GRÁTIS)

1. **Crie repositório no GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/seu-usuario/dashboard-financeiro.git
git push -u origin main
```

2. **Acesse** https://share.streamlit.io/
   - Clique em "Create app"
   - Selecione seu repositório
   - Branch: `main`
   - Main file path: `app.py`
   - Deploy!

3. **Configure Secrets** (dados sensíveis):
   - Vá em Settings → Secrets
   - Adicione suas conexões:
```
[database]
firebird_host = "seu-host"
firebird_password = "sua-senha"
mssql_host = "seu-host"
mssql_password = "sua-senha"
```

### Opção 2: Heroku

1. **Crie conta em** https://heroku.com

2. **Crie arquivo `Procfile`:**
```
web: streamlit run app.py --logger.level=error
```

3. **Deploy:**
```bash
heroku login
heroku create seu-app-name
git push heroku main
```

### Opção 3: Seu Servidor (Windows/Linux)

1. **Instale Python 3.9+**

2. **Configure como serviço:**
   - Windows: Use Task Scheduler
   - Linux: Use systemd ou supervisor

3. **Execute:**
```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

---

## 👥 Gerenciamento de Usuários

### Registrar novo usuário

1. Acesse a aplicação
2. Clique em "Registrar"
3. Preencha dados (email, senha, nome, empresa)
4. Clique em "Registrar"

**Usuários são salvos em `users.json` (localmente)**

Para produção, considere usar:
- Firebase Authentication
- Auth0
- Banco de dados próprio

---

## 📊 Estrutura dos Dashboards

### 1. DRE Mensal
- Receitas
- Custos
- Despesas
- Lucro líquido

### 2. Contas a Receber
- Clientes com atraso
- Valor em aberto
- Dias de atraso
- Status

### 3. Contas a Pagar
- Fornecedores
- Títulos vencidos
- Próximos 30 dias
- Status

### 4. Fluxo de Caixa
- Previsão 0-30 dias
- Previsão 30-60 dias
- Previsão 60-90 dias
- Saldo líquido

---

## 🔧 Customização

### Adicionar novo dashboard

1. **Crie a query SQL** em `queries/financeiro/seu_dashboard.sql`

2. **Edite `config.py`:**
```python
DASHBOARDS = {
    "seu_dashboard": {
        "titulo": "📌 Seu Dashboard",
        "descricao": "Descrição aqui",
        "arquivo_query": "queries/financeiro/seu_dashboard.sql"
    }
}
```

3. **Crie função de render** em `app.py`:
```python
def render_seu_dashboard(df: pd.DataFrame):
    # Sua lógica aqui
    st.dataframe(df, use_container_width=True)
```

4. **Atualize `render_dashboard()`:**
```python
elif dashboard_type == "seu_dashboard":
    render_seu_dashboard(df)
```

---

## 🔐 Segurança

- ✅ Senhas com hash bcrypt (nunca armazenadas em texto)
- ✅ Conexões criptografadas (use HTTPS em produção)
- ✅ Autenticação por empresa (cada usuário vê só seus dados)
- ⚠️ Armazene `users.json` em local seguro
- ⚠️ Use environment variables para senhas em produção

---

## 📝 Troubleshooting

### Erro: "Não consegue conectar ao banco Firebird"
- Verifique IP/host em `config.py`
- Confirme porta 3050 está aberta
- Teste conexão com gerenciador Firebird

### Erro: "ODBC Driver not found"
**Linux:**
```bash
sudo apt-get install unixodbc-dev
sudo apt-get install odbc-firebird
```

**Windows:**
- Download ODBC Driver em https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server

### Query retorna vazio
- Verifique nomes das tabelas no RP Decalc
- Teste a query direto no gerenciador
- Confirme dados existem no período

---

## 📞 Próximos Passos

1. **Agendamento de relatórios** (enviar por email)
2. **Exportação para Excel/PDF**
3. **Gráficos mais avançados**
4. **Integração com Firebase** (autenticação centralizada)
5. **Página de administrador** (gerenciar usuários)
6. **API REST** (integrar com outros sistemas)

---

## 📧 Contato

Dúvidas? Abra uma issue ou envie um email.

---

**Desenvolvido com ❤️ para consultoria de RP Decalc**
