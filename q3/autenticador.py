def autenticar_usuario(usuarios, usuario, senha):
    
    if usuario in usuarios:
        if usuarios[usuario] == senha:
            return "Autenticação bem sucedida!"
        else:
            return "Usuário ou senha incorretos"