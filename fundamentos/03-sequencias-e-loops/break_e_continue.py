# Controle de loops com break e continue

# Break e Continue:
# Break:
n = 0

while n < 10:
    print(f'O valor de n é: {n}')
    n += 1
    if n == 5:
        break

print('O loop acabou')

# Continue:
for n in range(-5, 6):
    print(n)
    if n == 0:
        continue
    resultado = 1 / n
    print(f'O resultado é: {resultado}')

print('O loop acabou')
