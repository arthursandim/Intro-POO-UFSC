#Arthur Vinicius Gouvea Sandim
#21204602
#https://www.beecrowd.com.br/judge/pt/problems/view/2167

n = int(input('Digite o número de medidas realizadas: '))
while not(1<=n<=100):
    print('Inválido.')
    n = int(input('Digite o número de medidas realizadas: '))

medidas=[int(x) for x in input(f'Digite as {n} medidas: ').split()]
while True:
    cont=0
    for element in medidas:
        if not(len(medidas)==n) or not(0<=element<=10000):
            cont+=1
    if cont!=0:
        print('Inválido')
        medidas=[int(x) for x in input(f'Digite as {n} medidas: ').split()]
    else:
        break

queda=0

for i in range(len(medidas)):
    if i==0:
        queda = 0
    elif medidas[i]<medidas[i-1]:
        queda = i+1
        break
if queda==0:
    print('Não houve queda nas medidas.')
else:
    print(f'O motor caiu na {queda}ª medida')