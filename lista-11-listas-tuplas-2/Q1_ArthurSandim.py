#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

N= int(input('Digite a quantidade de casos teste: '))
sorteado = 0

for i in range(0,N):
    
    menor = 0
    indice = 0
    QT,S=[int(x) for x in input('Digite a qtd de alunos e o número secreto: ').split()]
    while QT<4 or QT>10 or S<1 or S>100:
        print('Entrada inválida.')
        QT,S=[int(x) for x in input('Digite a qtd de alunos e o número secreto: ').split()]
    
    numAlu=[int(x) for x in input('Digite os nºs escolhidos pelos alunos: ').split()]
    while len(numAlu)!=QT:
        print('Entrada inválida.')
        numAlu=[int(x) for x in input('Digite os nºs escolhidos pelos alunos: ').split()]
    
    for num in numAlu:
        if numAlu.index(num)==0:
            menor=num
            indice=numAlu.index(num)
        elif num==S:
            indice=numAlu.index(num)
        elif abs(num-S)<abs(menor-S):
            menor=num
            indice=numAlu.index(num)


        sorteado=indice+1
            
        
    
    print(f'O aluno sorteado foi o {sorteado}º')
