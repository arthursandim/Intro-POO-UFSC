teste = 1
while True:
    N = int(input('Digite o número: '))
    if (N == 0):
        break
    if (N < 0):
        N = int(input('Entrada inválida. Digite novamente: '))
    diferenca = 0
    print(f'Teste {teste}')
    teste += 1
    for i in range(1,N+1):
        J,Z = [int(x) for x in input().split()]
        diferenca += J - Z 
        print(diferenca)
    print()