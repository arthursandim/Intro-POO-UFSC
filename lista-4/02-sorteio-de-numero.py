from random import randrange

sorteado = randrange(11)
palpite = int(input('Digite um número: '))


while (sorteado != palpite):
    palpite = int(input('Errado. Digite novamente: '))
    
print (f'Acertou, o numero sorteado é {sorteado}')

