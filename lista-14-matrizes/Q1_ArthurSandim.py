#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

import random
random.seed(1)

matriz = []
soma = 0.0
indice = int(input())
opp = input()

for i in range(12):
    linha = []
    for j in range(12):
        numero = random.randint(0,100)
        linha.append(numero)
    matriz.append(linha)

for a in range(12):
    for b in range(12):
        if a == indice:
            soma+=matriz[a][b]

if opp == "S":      
    print(f"{soma:.1f}")      
elif opp == "M":
    print(f"{soma/12:.1f2}")