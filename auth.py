"""
Módulo de autenticação - Email/Senha com hash seguro
"""
import bcrypt
import json
import os
from pathlib import Path

# Arquivo onde salva os usuários (em produção, usar banco de dados)
USERS_FILE = "users.json"

def hash_password(password: str) -> str:
    """Hash seguro da senha"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    """Verifica se a senha está correta"""
    return bcrypt.checkpw(password.encode(), hashed.encode())

def load_users() -> dict:
    """Carrega usuários do arquivo JSON"""
    if Path(USERS_FILE).exists():
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users: dict):
    """Salva usuários no arquivo JSON"""
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

def register_user(email: str, password: str, name: str, empresa_id: int) -> tuple[bool, str]:
    """
    Registra novo usuário
    Returns: (sucesso, mensagem)
    """
    users = load_users()

    if email in users:
        return False, "Email já registrado"

    if len(password) < 6:
        return False, "Senha deve ter no mínimo 6 caracteres"

    users[email] = {
        "name": name,
        "password": hash_password(password),
        "empresa_id": empresa_id,
        "created_at": str(os.popen("date").read().strip())
    }

    save_users(users)
    return True, "Usuário registrado com sucesso!"

def login_user(email: str, password: str) -> tuple[bool, dict | None]:
    """
    Faz login do usuário
    Returns: (sucesso, dados_usuario)
    """
    users = load_users()

    if email not in users:
        return False, None

    user = users[email]
    if not verify_password(password, user["password"]):
        return False, None

    return True, {
        "email": email,
        "name": user["name"],
        "empresa_id": user["empresa_id"]
    }

def get_user_by_email(email: str) -> dict | None:
    """Obtém dados do usuário"""
    users = load_users()
    if email in users:
        user = users[email]
        return {
            "email": email,
            "name": user["name"],
            "empresa_id": user["empresa_id"]
        }
    return None
