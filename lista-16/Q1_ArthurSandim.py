#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

t=int(input('Digite a quantidade de casos-teste: '))
while not(1<=t<=5000):
    print('Inválido.')
    t=int(input('Digite a quantidade de casos-teste novamente: '))
cont=0
medias=list()
while cont<t: 
    p,n=[int(x) for x in input('Digite a quantidade de provas e de alunos matriculados: ').split()]
    while not(2<=p<=5 and 2<=n<=50):
        print('Inválido.')
        p,n=[int(x) for x in input('Digite a quantidade de provas e de alunos matriculados: ').split()]

    matriz=[[0]*p]*n

    for i in range(n):
        matriz[i]=[float(x) for x in input().split()]
        soma=0
        maior=0
        for element in matriz[i]:
            if element>maior:
                maior=element
            soma+=element
        media=soma/len(matriz[i])
        if media>=7.0:
            status='aprovado'
            media=maior
            medias.append(media)
        elif 4.0<=media<=7.0:
            status='prova final'
            medias.append(round(media))
        else:
            status='reprovado'
            medias.append(media)
    cont+=1

for i in range(len(medias)):
    print(f'{medias[i]:.2f}')