# ✅ Primeira Empresa Configurada!

Opa! Coloquei seus dados aqui:

```python
1: {
    "nome": "Empresa 1 - Novo Original (Firebird)",
    "tipo_db": "firebird",
    "host": "192.168.1.98",
    "database": r"F:\Base\NOVORIGINAL.FDB",
    "user": "SYSDBA",
    "password": "masterkey",
    "port": 3050
}
```

---

## 🎯 Próximos Passos Agora:

### 1️⃣ **Baixe o ZIP atualizado**
O arquivo `dashboard-financeiro.zip` agora tem seus dados!

### 2️⃣ **Descompacte**
Extraia em uma pasta no seu computador

### 3️⃣ **Teste a conexão**
```bash
pip install -r requirements.txt
streamlit run app.py
```

1. Na tela, clique em **"Registrar"**
2. Crie um usuário:
   - Nome: Eduardo (seu nome)
   - Email: seu@email.com
   - Senha: teste123
   - Empresa: **"Empresa 1 - Novo Original"**
3. Clique **"Registrar"**
4. Clique **"Login"** com esses dados

**Se carregar os dashboards = sucesso! 🎉**

---

## 📝 Adicionar as Outras 11 Empresas

Abra o arquivo `config.py` com Bloco de Notas e edite a seção **EMPRESAS**:

Para cada empresa, preencha assim:

```python
2: {
    "nome": "Empresa 2 - (Nome Real)",
    "tipo_db": "firebird",  # ou "mssql"
    "host": "IP_AQUI",
    "database": r"F:\Caminho\arquivo.FDB",
    "user": "SYSDBA",
    "password": "senha_aqui",
    "port": 3050
},
```

---

## 📋 Template para as 11 Restantes

**Me envie isso preenchido:**

```
EMPRESA 2:
- Nome: 
- IP: 
- Banco: 
- Senha: 

EMPRESA 3:
- Nome: 
- IP: 
- Banco: 
- Senha: 

... (até EMPRESA 12)
```

Depois eu preencho tudo no `config.py` para você! 😊

---

## 🚀 Customizar as Queries (IMPORTANTE)

Os dashboards usam queries SQL genéricas. Você precisa adaptar para suas tabelas:

**Edite os arquivos:**
- `queries/financeiro/dre_mensal.sql`
- `queries/financeiro/contas_receber.sql`
- `queries/financeiro/contas_pagar.sql`
- `queries/financeiro/fluxo_caixa.sql`

**Mude as tabelas para as suas do RP Decalc:**

Exemplo: Se sua tabela de notas é `NF_SAIDA`, deixe assim:
```sql
FROM nf_saida
WHERE ...
```

---

## ✅ Checklist:

- [ ] Testei com a Empresa 1 (Novo Original)
- [ ] Consegui fazer login
- [ ] Os dashboards carregaram
- [ ] Coletei dados das outras 11 empresas (IP, banco, senha)
- [ ] Enviei para você customizar o config.py
- [ ] Adaptei as queries para minhas tabelas

---

## 📞 Me Chame Quando:

1. ✅ Testar a primeira empresa
2. 📝 Enviar dados das outras 11
3. 🔧 Customizar as queries SQL
4. 🚀 Fazer deploy na nuvem

---

**Vamos lá! A primeira empresa já tá pronta! 💪**
