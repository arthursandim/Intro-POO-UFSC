#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602
numeros = list()

size = int(input('Digite a quantidade de itens que haverão na lista: '))
cont = 0
for i in range(0,size):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))
    if numeros.count(numeros[i])>1:
        cont += 1

if cont > 0:
    print(f'Existem números repetidos na sequência digitada.')
else:
    print('Não existem número repetidos na sequência digitada.')