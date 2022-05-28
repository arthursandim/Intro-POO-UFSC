#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

N = list()
N.append(int(input('Digite o primeiro item da lista: ')))
while N[0]>50:
    print('Valor inválido.')
    N[0]=(int(input('Digite o primeiro item da lista: ')))    

i = 0

while i<10:
    print(f'N[{i}] = {N[i]}')
    N.append(N[i]*2)
    i+=1