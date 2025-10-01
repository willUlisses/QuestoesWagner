# Questão 3: Sistema de autenticação simples
# Usuários e senhas pré-definidos. Criar uma função para autenticar.

from autenticador import autenticar_usuario

usuarios = {
    "admin": "1234",
    "joao": "senha123",
    "maria": "abc@2024"
}

usuario = input("Usuário: ")
senha = input("Senha: ")

print(autenticar_usuario(usuarios, usuario, senha))



   

    