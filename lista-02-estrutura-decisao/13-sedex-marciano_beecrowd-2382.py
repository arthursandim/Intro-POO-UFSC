import math

largura, altura, profundidade, raioEsfera = [int(x) for x in input().split()]

diametroEsfera = raioEsfera * 2
diagonalCaixa = math.sqrt(largura ** 2 + altura ** 2 + profundidade ** 2)

if (diametroEsfera >= diagonalCaixa):
    print('S')
else:
    print('N')