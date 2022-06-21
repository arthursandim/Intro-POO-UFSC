#Arthur Vinicius Gouvea Sandim
#21204602
#https://www.beecrowd.com.br/judge/pt/problems/view/2322

n = int(input('Digite a quantidade de peças: '))

pecas = [int (x) for x in input('Digite o número das peças: ').split()]
while True:
    cont = 0
    for element in pecas:
        if not(len(pecas)==n-1) or not(1<=element<=n):
            cont+=1
    if cont != 0:
        print('Inválido')
        pecas = [int (x) for x in input('Digite o número das peças: ').split()]
    else:
        break

pecaFaltante = 0
for i in range(n):
    if i not in pecas:
        pecaFaltante = i

print(f'A peça faltante: {pecaFaltante}')

