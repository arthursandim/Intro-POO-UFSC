#Arthur Vinicius Gouvea Sandim
#21204602
#https://www.beecrowd.com.br/judge/pt/problems/view/1261

def calculo(lista,dicio):
    soma = 0
    for element in lista:
        if element.lower() in dicio.keys():
            soma += dicio[element]
    return soma

n,m = [int(x) for x in input('Digite o tamanho do dicionário e a quantidade de casos teste: ').split()]
while not(n<=100 and m <= 1000):
    print('Valor inválido.')
    n,m = [int(x) for x in input('Digite o tamanho do dicionário e a quantidade de casos teste: ').split()]

palavras = dict()
for i in range(n):
    palavra = input('Digite a palavra e o salário vinculado a ela: ').lower().split()
    palavra[1] = int(palavra[1])
    while len(palavra[0]) > 16 or palavra[1] > 1000000:
        print('Inválido')
        palavra = input('Digite a palavra e o salário vinculado a ela: ').lower().split()
        palavra[1] = int(palavra[1])
    palavras[palavra[0]] = palavra[1]

for j in range(m):
    descricoes = list()
    print(f'Digite a {j+1}ª descrição: ')
    while True:
        desc = list()
        desc = input().lower().split()
        if desc == ['.']:
            break
        descricoes += desc[:]

    print(f'Salário: USD {calculo(descricoes, palavras)}')
