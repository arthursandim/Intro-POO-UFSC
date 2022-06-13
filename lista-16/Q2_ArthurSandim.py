#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

n=int(input('Digite a quantidade de casas, na rua: '))
while not(2<=n<=10**5):
    n=int(input('Inválido. Digite a quantidade de casas, novamente: '))

cont=1
casas=list()
while cont<=n:
    casas.append(int(input('Digite o número da casa: ')))
    cont+=1

k=int(input('Digite a soma do número das casas: '))

casasSelecionadas=list()

for i in range(len(casas)):
    for j in range(len(casas)):
        if i!=j and casas[i]+casas[j]==k:
            casasSelecionadas.append(casas[i])
            casasSelecionadas.append(casas[j])
        elif i==j:
            break

casasSelecionadas.sort()

for element in casasSelecionadas:
    print(f'{element}', end=' ')
