"""
Dashboard Financeiro - RP Decalc
Autenticação multi-tenant para 12 empresas
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from auth import login_user, register_user, get_user_by_email
from database import DatabaseManager, load_query_from_file
from config import EMPRESAS, DASHBOARDS, COLORS

# Config da página
st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3498db;
    }
</style>
""", unsafe_allow_html=True)

# Inicializa session state
if "user" not in st.session_state:
    st.session_state.user = None
if "empresa_id" not in st.session_state:
    st.session_state.empresa_id = None

def page_login():
    """Página de login/registro"""
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("# 📊 Dashboard Financeiro")
        st.markdown("**RP Decalc** - Multi-empresa")
        st.divider()

        tab1, tab2 = st.tabs(["🔐 Login", "📝 Registrar"])

        with tab1:
            st.subheader("Fazer Login")
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Senha", type="password", key="login_password")

            if st.button("Entrar", use_container_width=True, type="primary"):
                if email and password:
                    sucesso, user_data = login_user(email, password)
                    if sucesso:
                        st.session_state.user = user_data
                        st.session_state.empresa_id = user_data["empresa_id"]
                        st.success(f"Bem-vindo, {user_data['name']}!")
                        st.rerun()
                    else:
                        st.error("Email ou senha incorretos")
                else:
                    st.warning("Preencha email e senha")

        with tab2:
            st.subheader("Criar Nova Conta")
            name = st.text_input("Nome completo", key="register_name")
            email = st.text_input("Email", key="register_email")
            password = st.text_input("Senha (mín. 6 caracteres)", type="password", key="register_password")

            # Seletor de empresa
            empresa_options = {v["nome"]: k for k, v in EMPRESAS.items()}
            empresa_selected = st.selectbox(
                "Selecione sua empresa",
                options=list(empresa_options.keys()),
                key="register_empresa"
            )

            if st.button("Registrar", use_container_width=True, type="primary"):
                if name and email and password and empresa_selected:
                    empresa_id = empresa_options[empresa_selected]
                    sucesso, msg = register_user(email, password, name, empresa_id)
                    if sucesso:
                        st.success(msg)
                        st.info("Agora faça login com seus dados")
                    else:
                        st.error(msg)
                else:
                    st.warning("Preencha todos os campos")

def page_dashboard():
    """Página principal com dashboards"""

    # Header com info do usuário
    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        st.markdown(f"### 👋 Olá, {st.session_state.user['name']}!")

    with col3:
        if st.button("🚪 Sair"):
            st.session_state.user = None
            st.session_state.empresa_id = None
            st.rerun()

    st.divider()

    # Info da empresa selecionada
    empresa = EMPRESAS[st.session_state.empresa_id]
    st.info(f"📍 Empresa: **{empresa['nome']}** | Tipo DB: `{empresa['tipo_db'].upper()}`")

    st.divider()

    # Menu de dashboards
    st.subheader("📊 Dashboards Disponíveis")

    dashboard_selected = st.selectbox(
        "Escolha um dashboard:",
        options=list(DASHBOARDS.keys()),
        format_func=lambda x: DASHBOARDS[x]["titulo"]
    )

    st.divider()

    # Carrega e exibe dashboard
    if dashboard_selected:
        dashboard = DASHBOARDS[dashboard_selected]
        st.subheader(dashboard["titulo"])
        st.caption(dashboard["descricao"])

        # Conecta ao banco e executa query
        try:
            db = DatabaseManager(st.session_state.empresa_id)
            if db.connect():
                query = load_query_from_file(dashboard["arquivo_query"])

                if query:
                    df = db.execute_query(query)
                    if df is not None and not df.empty:
                        render_dashboard(dashboard_selected, df)
                    else:
                        st.warning("Nenhum dado retornado. Verifique a query.")
                else:
                    st.warning(f"Arquivo de query não encontrado: {dashboard['arquivo_query']}")

                db.close()
            else:
                st.error("Não foi possível conectar ao banco de dados")
        except Exception as e:
            st.error(f"Erro: {str(e)}")

def render_dashboard(dashboard_type: str, df: pd.DataFrame):
    """Renderiza o dashboard baseado no tipo"""

    if dashboard_type == "dre":
        render_dre(df)
    elif dashboard_type == "contas_receber":
        render_contas_receber(df)
    elif dashboard_type == "contas_pagar":
        render_contas_pagar(df)
    elif dashboard_type == "fluxo_caixa":
        render_fluxo_caixa(df)
    else:
        st.dataframe(df, use_container_width=True)

def render_dre(df: pd.DataFrame):
    """Renderiza DRE"""
    col1, col2, col3 = st.columns(3)

    try:
        # Exemplo: assumindo colunas: mes, receita, custo, despesa
        if not df.empty and len(df) > 0:
            total_receita = df.get('receita', df.iloc[:, 0] if len(df.columns) > 0 else 0).sum()

            with col1:
                st.metric("💰 Receita Total", f"R$ {total_receita:,.2f}")

            st.dataframe(df, use_container_width=True)

            # Gráfico exemplo
            if 'mes' in df.columns and 'receita' in df.columns:
                fig = px.bar(df, x='mes', y='receita', title="Receita por Mês")
                st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.warning(f"Erro ao renderizar: {str(e)}")
        st.dataframe(df, use_container_width=True)

def render_contas_receber(df: pd.DataFrame):
    """Renderiza Contas a Receber"""
    col1, col2 = st.columns(2)

    try:
        if not df.empty:
            with col1:
                st.metric("📊 Total em Aberto", f"R$ {df.get('valor', [0]).sum():,.2f}")

            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.warning(f"Erro ao renderizar: {str(e)}")
        st.dataframe(df, use_container_width=True)

def render_contas_pagar(df: pd.DataFrame):
    """Renderiza Contas a Pagar"""
    try:
        if not df.empty:
            st.metric("💳 Total a Pagar", f"R$ {df.get('valor', [0]).sum():,.2f}")
            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.warning(f"Erro ao renderizar: {str(e)}")
        st.dataframe(df, use_container_width=True)

def render_fluxo_caixa(df: pd.DataFrame):
    """Renderiza Fluxo de Caixa"""
    try:
        if not df.empty:
            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.warning(f"Erro ao renderizar: {str(e)}")
        st.dataframe(df, use_container_width=True)

# Main
def main():
    if st.session_state.user is None:
        page_login()
    else:
        page_dashboard()

if __name__ == "__main__":
    main()
