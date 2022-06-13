#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

n,w=[int(x) for x in input('Ditie o número de titãs conhecidos e a altura da muralha: ').split()]
while not(1<=n<=100 and 1<=w<=1000):
    print('Inválido')
    n,w=[int(x) for x in input('Ditie o número de titãs conhecidos e a altura da muralha: ').split()]

cont=0
maisAltos=list()
while cont<n:
    nome=input('Digite o nome do titã: ')
    while not(1<=len(nome)<=100):
        print('Inválido')
        nome=input('Digite o nome do titã: ')
    altura=int(input('Digite a altura do titã: '))
    while not(1<=altura<=1000):
        print('Inválido')
        altura=int(input('Digite a altura do titã: '))   
    if altura>w:
        maisAltos.append(nome)

    cont+=1
for element in maisAltos:
    print(f'{element}', end=' ')