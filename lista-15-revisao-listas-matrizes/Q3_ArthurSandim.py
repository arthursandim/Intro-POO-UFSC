#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

while True:
    print('Digite a quantidade de participantes e de problemas, separados por espaço: ')
    n,m=[int(x) for x in input().split()]

    if(n!=0 and m!=0) and not((3<=n and m<=100)):
        print('Inválido. Insira os valores novamente:')
        n,m=[int(x) for x in input().split()]
        
    if(n==0 and m==0):
        break

    matriz=[[0]*m]*n
    
    print('Digite os valores: ')
    for i in range(n):
        matriz[i]=[int(x) for x in input().split()]
        while len(matriz[i])!=m:
           print(f'Inválido. Insira os valores da {i+1}ª linha novamente:')
           matriz[i]=[int(x) for x in input().split()]
        
    acerTudo=False
    errTudo=False
    todAcert=False
    todErr=False
    carac=4

    for i in range(n):
        acertos=0
        quantosAcertaram=0
        quantosErraram=0
        for j in range(m):
            if matriz[i][j]==1:
                acertos+=1
                quantosAcertaram += 1
            elif matriz[i][j]==0:
                quantosErraram+=1
        if acertos==m:
            acerTudo=True
        elif acertos==0:
            errTudo=True
        if quantosAcertaram == n:
            todAcert = True
        if quantosErraram == n:
            todErr = True
    
    if acerTudo:
        carac -= 1
    if errTudo:
        carac -= 1
    if todErr:
        carac -= 1
    if todAcert:
        carac -= 1
    print(f'Características atingidas: {carac}')
    print('-'*45)