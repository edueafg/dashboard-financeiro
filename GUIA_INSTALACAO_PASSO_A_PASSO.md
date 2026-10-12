# 📚 GUIA DE INSTALAÇÃO - Passo a Passo (INICIANTE)

## 🎯 O que vamos fazer?

1. ✅ Descompactar o ZIP
2. ✅ Instalar Python (se não tiver)
3. ✅ Configurar suas empresas
4. ✅ Testar no computador
5. ✅ Colocar na nuvem (online)

---

## 🖥️ PASSO 1: Preparar o Computador

### Windows 10/11

#### 1.1 Instalar Python

1. Acesse: https://www.python.org/downloads/
2. Clique em **"Download Python 3.11"** (versão recomendada)
3. Execute o arquivo `python-3.11.X.exe`
4. **IMPORTANTE:** Marque a opção **"Add Python to PATH"** ✅
5. Clique em **"Install Now"**
6. Aguarde terminar

#### 1.2 Verificar instalação
1. Abra o **Prompt de Comando** (procure por "cmd" no Windows)
2. Digite:
```
python --version
```
3. Deve aparecer algo como: `Python 3.11.X`

---

### Mac ou Linux

Abra Terminal e execute:
```bash
# Mac
brew install python3

# Ubuntu/Debian
sudo apt-get install python3 python3-pip
```

Verifique:
```bash
python3 --version
```

---

## 📁 PASSO 2: Descompactar o Projeto

1. **Baixe o arquivo** `dashboard-financeiro.zip`
2. **Clique com botão direito** nele
3. Escolha **"Extrair tudo..."** (Windows) ou **"Descompactar"** (Mac)
4. Abra a pasta extraída

Você deve ver:
```
dashboard-financeiro/
├── app.py
├── auth.py
├── config.py
├── database.py
├── requirements.txt
├── queries/
└── README.md
```

---

## ⚙️ PASSO 3: Instalar Dependências

### Windows

1. Abra **Prompt de Comando** (procure por "cmd")
2. Navegue até a pasta do projeto:
```
cd C:\Users\SEU_USUARIO\Desktop\dashboard-financeiro
```
(Ajuste o caminho conforme onde você extraiu)

3. Execute:
```
pip install -r requirements.txt
```

Vai aparecer várias linhas instalando bibliotecas. **Aguarde terminar** (pode levar 2-3 minutos).

### Mac/Linux

Abra Terminal e execute:
```bash
cd ~/Dashboard/dashboard-financeiro
pip3 install -r requirements.txt
```

---

## 🔑 PASSO 4: Configurar Suas Empresas

### 4.1 Abrir o arquivo `config.py`

1. Abra a pasta do projeto
2. Clique com botão **direito** em `config.py`
3. Escolha **"Abrir com..."** → **"Bloco de Notas"** (ou seu editor preferido)

### 4.2 Editar as conexões

Você vai ver algo assim:

```python
EMPRESAS = {
    1: {
        "nome": "Empresa A (Firebird)",
        "tipo_db": "firebird",
        "host": "localhost",
        "database": "/caminho/para/decalc.fdb",
        "user": "SYSDBA",
        "password": "masterkey",
        "port": 3050
    },
    ...
}
```

**Você precisa mudar:**
- `host` → IP do servidor (ex: 192.168.1.50)
- `database` → Caminho do arquivo .fdb
- `user` → Seu usuário Firebird
- `password` → Sua senha
- `port` → Porta (padrão 3050)

### Exemplo Real:

```python
EMPRESAS = {
    1: {
        "nome": "Gráfica SP - Firebird",
        "tipo_db": "firebird",
        "host": "192.168.1.50",
        "database": "/data/rp_decalc/db.fdb",
        "user": "SYSDBA",
        "password": "senha123",
        "port": 3050
    },
    2: {
        "nome": "Gráfica RJ - SQL Server",
        "tipo_db": "mssql",
        "host": "sql.empresa.com.br",
        "database": "decalc_rj",
        "user": "sa",
        "password": "senha456",
        "port": 1433
    },
}
```

**Salve o arquivo** (Ctrl+S)

---

## 🧪 PASSO 5: Testar Localmente

### Windows

1. Abra **Prompt de Comando** na pasta do projeto
2. Execute:
```
streamlit run app.py
```

3. Uma aba do navegador vai abrir automaticamente
4. Acesse: `http://localhost:8501`

### Mac/Linux

```bash
streamlit run app.py
```

---

## ✅ PASSO 6: Criar Primeiro Usuário

1. Na tela do app, clique em **"📝 Registrar"**
2. Preencha:
   - **Nome:** João Silva
   - **Email:** joao@empresa.com.br
   - **Senha:** teste123
   - **Empresa:** Selecione uma das suas 12
3. Clique em **"Registrar"**
4. Agora clique em **"🔐 Login"** e entre com esses dados

---

## 🚀 PASSO 7: Colocar Online (Cloud)

### Opção A: Streamlit Cloud (GRÁTIS - Recomendado)

#### 7.1 Criar conta no GitHub

1. Acesse https://github.com
2. Clique em **"Sign up"**
3. Crie uma conta (use seu email pessoal)
4. Confirme email

#### 7.2 Fazer upload do projeto

1. No GitHub, clique em **"Create repository"**
2. Digite o nome: `dashboard-financeiro`
3. Deixe **"Public"** marcado
4. Clique em **"Create repository"**
5. Você vai ver instruções. Execute no Prompt de Comando:

```bash
cd C:\Users\SEU_USUARIO\Desktop\dashboard-financeiro

git init
git add .
git commit -m "Primeiro upload"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/dashboard-financeiro.git
git push -u origin main
```

(Vai pedir seu email/senha do GitHub)

#### 7.3 Deploy no Streamlit Cloud

1. Acesse https://share.streamlit.io/
2. Clique em **"Create app"**
3. Selecione:
   - Repository: `SEU_USUARIO/dashboard-financeiro`
   - Branch: `main`
   - Main file path: `app.py`
4. Clique em **"Deploy"**
5. Aguarde (2-3 minutos)

**Pronto!** Seu app está online! 🎉

A URL será algo como:
```
https://dashboard-financeiro.streamlit.app
```

---

## 🔐 PASSO 8: Configurar Senhas no Cloud

Seu `config.py` tem senhas. **NÃO colocamos no GitHub!**

### 8.1 Adicionar Secrets no Streamlit Cloud

1. Na página do seu app no Streamlit Cloud
2. Clique em **"Settings"** (engrenagem)
3. Clique em **"Secrets"**
4. Cole isso (customize com seus dados):

```
[database]
empresa_1_host = "192.168.1.50"
empresa_1_password = "sua_senha_firebird"
empresa_2_host = "sql.empresa.com.br"
empresa_2_password = "sua_senha_sql"
```

5. Clique em **"Save"**

---

## 📊 PASSO 9: Customizar as QUERIES

As queries SQL estão em:
```
queries/financeiro/
├── dre_mensal.sql
├── contas_receber.sql
├── contas_pagar.sql
└── fluxo_caixa.sql
```

Para customizar (ex: DRE):

1. Clique com direito em `dre_mensal.sql`
2. Abra com **Bloco de Notas**
3. Mude as tabelas para as suas:
   - `nf_saida` → `sua_tabela_de_vendas`
   - `contas_pagar` → `sua_tabela_de_despesas`
4. Salve
5. Commit e push no GitHub:

```bash
git add queries/
git commit -m "Atualizei as queries"
git push
```

---

## ❌ Problemas Comuns

### "Comando 'streamlit' não reconhecido"

```bash
pip install streamlit
```

### "Erro ao conectar ao Firebird"

- ✅ Verifique IP do servidor
- ✅ Confirme porta 3050 está aberta
- ✅ Teste a senha manualmente

### "Erro ao conectar ao SQL Server"

**Windows:**
```bash
pip install pyodbc
```

**Linux/Mac:**
```bash
sudo apt-get install unixodbc-dev
pip install pyodbc
```

### As queries retornam vazio

1. Teste a query diretamente no gerenciador Firebird/SQL
2. Confirme nomes das tabelas (case-sensitive!)
3. Confirme tem dados no período

---

## 📞 Checklist Final

- [ ] Python instalado
- [ ] Projeto descompactado
- [ ] Dependencies instaladas (`pip install -r requirements.txt`)
- [ ] `config.py` editado com suas 12 empresas
- [ ] Testou localmente (`streamlit run app.py`)
- [ ] Criou primeiro usuário
- [ ] Queries SQL customizadas
- [ ] GitHub repository criado
- [ ] Streamlit Cloud deployado
- [ ] Secrets configurados
- [ ] Compartilhou URL com seus usuários

---

## 🎉 Parabéns!

Seu dashboard está **ONLINE** e seus **20 usuários** conseguem acessar de qualquer navegador! 

**URL para compartilhar:**
```
https://dashboard-financeiro.streamlit.app
```

---

## 📧 Próximos Passos

Depois que funcionar, você pode pedir:

1. **Agendamento de relatórios** (enviar por email automaticamente)
2. **Novos dashboards** (vendas, produção, estoque)
3. **Gráficos melhorados** (com filtros, cores customizadas)
4. **Exportar para Excel/PDF**
5. **Integrar com seu CRM Firebase**

---

## 💬 Dúvidas?

**Me envie:**
- Screenshot do erro
- Qual step travou
- Qual banco de dados (Firebird/SQL Server)

Estarei aqui para ajudar! 🚀

---

**Desenvolvido com ❤️ para sua consultoria de RP Decalc**
