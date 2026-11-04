# Desafio: sistema de login (versão com comparação e versão com booleanos)

# Desafio Controle de Fluxo!
# Comparação:
usuario_correto = "Pedro"
senha_correta = "senha secreta"

usuario = input("Nome de usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto:
    if senha == senha_correta:
        print(f"Acesso liberado, seja bem-vindo {usuario}!")
    else:
        print(f"Senha incorreta para o usuário {usuario}.")
else:
    print(f"Usuário {usuario} não cadastrado no sistema")

# Booleano:
usuario_correto = "Pedro"
senha_correta = "senha secreta"

usuario = input("Nome de usuário: ")
usuario_esta_correto = usuario == usuario_correto
senha_esta_correta = input("Senha: ") == senha_correta

if usuario_esta_correto and senha_esta_correta:
    print(f"Acesso liberado, seja bem-vindo {usuario}!")
if usuario_esta_correto and not senha_esta_correta:
    print(f"Senha incorreta para o usuário {usuario}.")
if not usuario_esta_correto:
    print(f"Usuário {usuario} não cadastrado no sistema")
