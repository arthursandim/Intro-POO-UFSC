from random import randrange
palpite = int(input('Digite um número: '))
sorteado = randrange(11)

print (sorteado)
while (sorteado != palpite):
    palpite = input ('Errado. Digite novamente: ')
    
print (f'Acertou, o numero sorteado é {sorteado}')

