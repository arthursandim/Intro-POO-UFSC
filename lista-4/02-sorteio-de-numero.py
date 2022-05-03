from random import randrange
palpite = int(input('Digite um número: '))
sorteado = randrange(11)

while (sorteado != palpite):
    palpite = int(input('Errado. Digite novamente: '))
    
print (f'Acertou, o numero sorteado é {sorteado}')

