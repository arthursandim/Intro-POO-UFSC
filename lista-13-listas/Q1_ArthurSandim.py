#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

n = int(input('Digite a quantidade de casos testes: '))
while not (1 <= n <= 20):
    n = int(input('Digite a quantidade de casos testes: '))

for i in range(n):
    soma = 0
    j = 1
    x = int(input('Digite o número a ser testado: '))
    divisores = list()
    while not (1 <= x <= 10**8):
        print('Entrada inválida. Digite novamente.')
        x = int(input('Digite o número a ser testado: '))
    while j < x:
        if x % j == 0:
            divisores.append(j)
        j += 1
    
    for element in divisores:
        soma += element

    if soma == x:
        print(f'{x} eh perfeito.')
    else:
        print(f'{x} nao eh perfeito')