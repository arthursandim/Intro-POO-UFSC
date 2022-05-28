#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

def campoMin(lista,n):
    c=0
    while c<n:
        if len(lista)==1:
            print(lista[c])
        elif c==0:
            print(lista[c]+lista[c+1])
        elif c>0 and c<n-1:
            print(lista[c]+lista[c-1]+lista[c+1])
        else:
            print(lista[c]+lista[c-1])
        c+=1


N = int(input('Digite a quantidade de célula do tabuleiro: '))
while N<1 or N>50:
    N = int(input('Inválido. Digite novamente: '))

tab = list()

for i in range(N):
    tab.append(int(input()))
print('Resultado do jogo:')
campoMin(tab,N)
 

  