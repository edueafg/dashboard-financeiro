# ⚙️ Guia de Configuração Inicial

## 1️⃣ Primeiro: Editar `config.py`

Localize a seção `EMPRESAS` e configure seus bancos de dados:

```python
EMPRESAS = {
    1: {
        "nome": "Empresa A (Seu Nome)",
        "tipo_db": "firebird",  # ou "mssql"
        "host": "IP_DO_SERVIDOR",
        "database": "/caminho/para/decalc.fdb",
        "user": "SYSDBA",
        "password": "sua_senha_aqui",
        "port": 3050
    },
    # Repita para cada empresa (máx 12)
}
```

**Exemplo prático:**
```python
EMPRESAS = {
    1: {
        "nome": "Gráfica SP - Firebird",
        "tipo_db": "firebird",
        "host": "192.168.1.50",
        "database": "/data/rp_decalc/db.fdb",
        "user": "SYSDBA",
        "password": "master123",
        "port": 3050
    },
    2: {
        "nome": "Gráfica RJ - SQL Server",
        "tipo_db": "mssql",
        "host": "sql.empresa.com.br",
        "database": "decalc_rj",
        "user": "sa",
        "password": "senha_sql",
        "port": 1433
    },
}
```

---

## 2️⃣ Segundo: Editar as QUERIES SQL

Vá em `queries/financeiro/` e customize as 4 queries com **suas tabelas reais**:

### Descobrir nomes das tabelas:
1. Abra gerenciador SQL (DBweaver, DBeaver, IBExpert)
2. Conecte ao RP Decalc
3. Veja lista de tabelas disponíveis
4. Copie nomes exatos

**Tabelas comuns do RP Decalc:**
- `NF_SAIDA` - Notas Fiscais de Saída
- `NF_ENTRADA` - Notas Fiscais de Entrada
- `CLIENTES` - Cadastro de clientes
- `FORNECEDORES` - Cadastro de fornecedores
- `PRODUTOS` - Cadastro de produtos
- `PEDIDOS` - Pedidos de venda
- `OP_PRODUCAO` - Ordens de produção
- `CONTAS_RECEBER` - Financeiro a receber
- `CONTAS_PAGAR` - Financeiro a pagar

**Dica:** Use `SELECT * FROM seu_banco.tabelas;` para listar

---

## 3️⃣ Terceiro: Testar Localmente

```bash
# Instale dependências
pip install -r requirements.txt

# Execute
streamlit run app.py

# Acesse http://localhost:8501
```

**Testar login:**
- Clique em "Registrar"
- Crie usuário de teste
- Selecione uma empresa
- Entre

---

## 4️⃣ Quarto: Customizar Dashboards

### Adicionar nova coluna ao DRE:
Edite `queries/financeiro/dre_mensal.sql`:

```sql
-- Exemplo: Adicionar "Margem Líquida"
SELECT 
    MONTH(data) as mes,
    SUM(valor_receita) as receita,
    SUM(valor_custo) as custo,
    SUM(valor_despesa) as despesa,
    ((SUM(valor_receita) - SUM(valor_custo) - SUM(valor_despesa)) / SUM(valor_receita) * 100) as margem_pct
FROM ...
```

### Adicionar novo dashboard:
1. Crie arquivo SQL em `queries/financeiro/novo_dashboard.sql`
2. Edite `config.py`:
```python
DASHBOARDS = {
    "novo": {
        "titulo": "📊 Novo Dashboard",
        "descricao": "Descrição",
        "arquivo_query": "queries/financeiro/novo_dashboard.sql"
    }
}
```
3. Edite `app.py`, adicione função:
```python
def render_novo_dashboard(df):
    st.metric("Métrica", df['valor'].sum())
    st.dataframe(df, use_container_width=True)
```

---

## 5️⃣ Configurações de Usuários (Email/Senha)

Atualmente os usuários são salvos em `users.json`.

**Para produção, recomendo:**
- Usar **Firebase Auth** (mais seguro, integrado com seu CRM)
- Ou banco de dados próprio (PostgreSQL/MySQL)

**Ativar Firebase (próximo passo):**
```
- Editar auth.py
- Usar firebase_admin em vez de json
- Sincronizar com seu CRM existente
```

---

## 🎯 Checklist de Configuração

- [ ] `config.py` editado com 12 empresas
- [ ] Testar conexão Firebird
- [ ] Testar conexão SQL Server
- [ ] Queries SQL customizadas com suas tabelas
- [ ] Teste local funcionando
- [ ] Deploy em nuvem (Streamlit Cloud)
- [ ] Criar primeiros usuários de teste
- [ ] Validar dashboards financeiros

---

## 🚀 Deploy em 5 Minutos (Streamlit Cloud)

1. Crie repo no GitHub com os arquivos
2. Acesse https://share.streamlit.io/
3. Selecione seu repo
4. Clique "Deploy"
5. Acesse seu URL (Ex: dashboard-financeiro.streamlit.app)

**Pronto! Seus usuários acessam online!**

---

## ❓ Próximas Customizações

Depois que estiver funcionando, você pode pedir:
- Agendamento automático de relatórios (email)
- Gráficos mais avançados
- Filtros por período/cliente
- Exportação para Excel
- Integração com seu CRM (Firebase)
- Página admin para gerenciar usuários

---

**Precisa de ajuda? Me chame! 🚀**
