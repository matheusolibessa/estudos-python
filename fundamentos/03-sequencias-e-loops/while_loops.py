# While loops e menu com while True

# While loops:
n = 0

while n < 3:
    print(f'O valor de n é: {n}')
    n += 1

print('O loop acabou')

# While True:
while True:
    opt = input('Escolha uma opção (1, 2) | "q" para sair: ')
    if opt == 'q':
        break
    elif opt != '1' and opt != '2':
        print('Opção inválida!')
        continue
    print(f'Opção selecionada: {opt}')

print('Programa finalizado')
