#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

p, n = [int(x) for x in input().split()]
while not(1<=p<=5 and 2<=n<=100):
    p, n = [int(x) for x in input().split()]

canos = [int(x) for x in input().split()]
while len(canos)!=n:
    print('erro. digite novamente: ')
    canos = [int(x) for x in input().split()]

cont=0
for i in range(len(canos)):
    while canos[i]>10:
        print('erro. digite novamente: ')
        canos = [int(x) for x in input().split()]
    
    if i<n-1 and abs(canos[i]-canos[i+1])<=p:
        cont+=1
    elif i==n:
        cont+1

if cont==n-1:
    print("YOU WIN")
else:
    print("Game Over")
    