r = ['A','B','C','D','E','*']
while True:
    n = int(input('Digite a quantidade de casos testes: '))
    while not (1 <= n <= 255):
        n = int(input('Digite a quantidade de casos testes: '))
    if n == 0:
        break
    for i in range(n):
        p = -1
        print('Digite a sequência: ')
        l = [int(x) for x in input().split()]
        for c in range(len(l)):
            while not (0 <= l[c] <=255):
                print('Inválido. Digite a sequência: ')
                l = [int(x) for x in input().split()]
        for j in range(len(l)):
            if l[j] <= 127:
                if p != -1:
                    p = 5
                    break
                p = j
        print(f'Resposta: {r[p]}')