# Entrada e saída de dados: input(), print(), f-strings, len() e int()

# Pega inputs do usuário
nome = input("Qual o seu nome?\nDigite aqui: ")
idade = input("Qual a sua idade?\nDigite aqui: ")

print("-" * 40)

# Exibe resultados do código
print(f"Olá, {nome}!")
print(f"Seu nome tem {len(nome)} letras.")
print(f"Daqui 5 anos, você terá {int(idade) + 5} anos.")

print("-" * 40)
