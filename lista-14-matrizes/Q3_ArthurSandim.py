#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

q = int(input('Numero de participantes: '))
cont1=0
cont0=0
while not (4 <= q <= 233000):
    print('Inválido. Digite novamente.')
    q = int(input('Numero de participantes: '))

v = [int(x) for x in input('1 OU 0: ').split()]

for element in v:
    if element == 1:
        cont1+=1
    elif element == 0:
        cont0+=1

if cont1>=cont0:
    print('N')
else:
    print('Y')