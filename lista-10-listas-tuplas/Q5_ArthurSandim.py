#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

from random import sample

listaX = list(sample(range(100),20))

print (f'A lista original: {listaX}')

listaY = listaX[::-1]

listaX = listaY

print (f'A lista invertida: {listaX}')
