# Estrutura condicional if / elif / else

idade = int(input("Digite sua idade: "))

# if, elif e else
if idade < 18:
    print("Você tem menos de 18 anos!")
    print("Você não pode dirigir um carro")
elif idade == 18:
    print("Você tem exatamente 18 anos!")
else:
    print("Você tem mais de 18 anos!")
    print("Você pode dirigir um carro")
