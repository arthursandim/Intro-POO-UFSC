#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

from random import randint
from random import seed
seed(1)
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(randint(0,100))
    matriz.append(linha)

print(matriz)

operacao = str(input()).upper()
while not (operacao == 'S' or operacao == 'M'):
    print('Operação inválida!')
    operacao = str(input()).upper()

soma = 0

for linha in range(0,len(matriz)):
    for coluna in range(0,linha):
        soma = soma + matriz[linha][coluna]

if operacao == 'S':
    print('Soma:', soma)
else:
    print(f'Média: {soma/72:.1f}')