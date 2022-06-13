#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

n, m = [int(x) for x in input().split()]
while not (n >= 1 and m <= 100):
    n, m = [int(x) for x in input().split()]
pedras = [0 for i in range(n)]

for i in range (m):
    p, d = [int(x) for x in input().split()]
    while not (p >= 1 and d <= n):
        p, d = [int(x) for x in input().split()]        
    p -= 1
    pedras[p] = 1

    esquerda = p - d
    while esquerda >= 0:
        pedras[esquerda] = 1
        esquerda -= d


    direita = p + d
    while direita < n:
        pedras[direita] = 1
        direita += d

for i in pedras:
    print(i)