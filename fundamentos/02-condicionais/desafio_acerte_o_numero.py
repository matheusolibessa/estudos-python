# Desafio: acerte o número secreto em 3 tentativas (só com condicionais)

# Desafio - Acerte o número!
numero_secreto = 10
descobriu = False

if not descobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True

if not descobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True

if not descobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True

if descobriu:
    print('Parabéns, você ganhou!')
else:
    print(f'Que pena, você perdeu! O número secreto era {numero_secreto}')
