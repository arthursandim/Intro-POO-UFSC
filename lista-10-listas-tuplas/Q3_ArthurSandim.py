#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602


from random import sample

tupla = (sample(range(100),10))
maior = menor = 0
for i in range (0,len(tupla)):
    if (i == 0):
        maior = menor = tupla[i]
    elif (tupla[i] > maior):
        maior = tupla[i]
        posMaior = i
    elif (tupla[i] < menor):
        menor = tupla[i]
        posMenor = i
        
print (f'A tupla sorteada foi: {tupla}')
print (f'O menor valor da tupla é {menor} e está na posição {posMenor}')
print (f'O maior valor da tupla é {maior} e está na posição {posMaior}')