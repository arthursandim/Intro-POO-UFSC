#Arthur Vinicius Gouvea Sandim
#21204602
#https://www.urionlinejudge.com.br/judge/pt/problems/view/2454

p,r = [int(x) for x in input('Digite os valores das portas P e R [0/1]: ').split()]
while not((p==0 or p==1) and (r==0 or r==1)):
    print('Inválido.')
    p,r = [int(x) for x in input('Digite os valores das portas P e R [0/1]: ').split()]

if(p==0 and r==0):
    print('Resultado: C')
elif(p==1 and r==0):
    print('Resultado: B')
else:
    print('Resultado: A')

