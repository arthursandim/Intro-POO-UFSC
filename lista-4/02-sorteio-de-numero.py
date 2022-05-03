from random import randrange

sorteado = randrange(11)
palpite = int(input('Digite um número: '))


print (sorteado)
while (sorteado != palpite):
    palpite = input ('Errado. Digite novamente: ')
    
print (f'Acertou, o numero sorteado é {sorteado}')

