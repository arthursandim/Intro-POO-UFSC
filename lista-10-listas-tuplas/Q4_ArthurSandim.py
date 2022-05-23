#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

listaX = list()
size = int(input('Digite o tamanho da lista: '))

for i in range(0,size):
    listaX.append(int(input(f'Digite o {i+1}º valor: ')))

numK = int(input('Digite o valor multiplicador: '))

listaResultante = list(range(size))

for i in range(0,size):
    listaResultante[i] = listaX[i] * numK

print (f'Lista original: {listaX}')
print (f'Multiplicador: {numK}')
print (f'Lista resultante do produto da lista original pelo multiplicador: {listaResultante}')