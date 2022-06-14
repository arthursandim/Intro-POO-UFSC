#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602
#Questão - https://www.beecrowd.com.br/judge/pt/problems/view/1281

def soma(lista,prod,qtt):
    somm = 0
    for i in range(len(lista)):
        if prod in lista[i].values():
            somm += lista[i]['preco']*qtt
    return somm

n = int(input('Digite a quantidade de idas a feira: '))
fruta = dict()
frutas = list()

for i in range(n):
    somma=0
    print('-'*50)
    print(f'{i+1}ª ida à feira.')
    print()
    
    m = int(input('Digite a quantidade frutas disponíveis no mercado: '))
    for j in range(m):
        fruta['fruta'] = str(input('Digite a fruta disponível: ')).lower()
        fruta['preco'] = float(input('Digite o valor: '))
        frutas.append(fruta.copy())
    
    print()
    
    p = int(input('Quantos tipos diferentes de produtos você deseja comprar: '))
    while not(1<=p<=m):
        p = int(input('Valor Inválido. Digite novamente quantos tipos diferentes de produtos você deseja comprar: '))
    
    for k in range(p):
        frutaC = str(input('Digite a fruta comprada: ')).lower()
        qtdC = int(input(f'Quantidade de {frutaC} comprada: '))
        somma+=soma(frutas, frutaC, qtdC)
    
    print()
    
    print(f'Total da compra: R$ {somma:.2f}')
    
    print()
    
    frutas.clear()