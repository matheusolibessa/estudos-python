# For loops: range() e iteração sobre listas e tuplas

# For Loops:
for n in range(2):
    print('Olá!')

#Iterando sobre sequências:
valores = [10, 20, 30, 3, -2, 17]

for valor in valores:
    print(f'O valor é: {valor}')

print('Acabou o loop!')

# Exemplo 2:
clientes = [
    ('Ana', 'xxx', 'xxx@email.com'),
    ('João', 'yyy', 'yyy@email.com')
]

for nome, cpf, email in clientes:
    print(f'Cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n\n')
