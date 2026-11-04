# Desafio: apuração de eleição com contagem de votos e percentuais

# Desafio eleição:
# 1 - José | 2 - João | 3 - Maria | 4 - Ana | 5 - Nulo | 6 - Branco | 0 - Sair

jose = 0
joao = 0
maria = 0
ana = 0
nulos = 0
brancos = 0

voto = int(input("Digite o voto (0 para sair): "))

while voto != 0:
    if voto == 1:
        jose = jose + 1
    elif voto == 2:
        joao = joao + 1
    elif voto == 3:
        maria = maria + 1
    elif voto == 4:
        ana = ana + 1
    elif voto == 5:
        nulos = nulos + 1
    elif voto == 6:
        brancos = brancos + 1
    voto = int(input("Digite o voto (0 para sair): "))

total = jose + joao + maria + ana + nulos + brancos

print("José:", jose)
print("João:", joao)
print("Maria:", maria)
print("Ana:", ana)
print("Nulos:", nulos)
print("Brancos:", brancos)

if total > 0:
    print("Percentual de nulos:", nulos * 100 / total, "%")
    print("Percentual de brancos:", brancos * 100 / total, "%")

vencedor = "José"
maior = jose
if joao > maior:
    vencedor = "João"
    maior = joao
if maria > maior:
    vencedor = "Maria"
    maior = maria
if ana > maior:
    vencedor = "Ana"
    maior = ana

print("Vencedor:", vencedor)
