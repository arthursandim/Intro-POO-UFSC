#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

linhas, capacidadeMaxima = [int(x) for x in input('Digite os parâmetros iniciais: ').split()]
while(linhas<1 or linhas>1000 or capacidadeMaxima<1 or capacidadeMaxima>1000):
    linhas, capacidadeMaxima = [int(x) for x in input('1 ou mais valores inválidos. Digite os parâmetros iniciais novamente: ').split()]
saida = 0
entrada = 0
soma = 0
acumulador = 0
maior = 0

for i in range (0,linhas):
    print('Entraram / Saíram')
    saida,entrada = [int(x) for x in input().split()]
    while(saida<0 or saida>1000 or entrada<0 or entrada>1000):
        print('Valor inválido, digite novamente.')
        saida,entrada = [int(x) for x in input().split()]
    soma = -(saida) + entrada
    acumulador += soma
    if (acumulador > maior):
        maior = acumulador


if (maior > capacidadeMaxima):
    print('S')
else:
    print('N')
