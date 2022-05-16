notas = [float(x) for x in input().split()]
n1 = notas[0]
n2 = notas[1]
n3 = notas[2]
n4 = notas[3]
n5 = notas[4]
while len(notas) > 5 or n1<5 or n2<5 or n3<5 or n4<5 or n5<5 or n1>10 or n2>10 or n3>10 or n4>10 or n5>10 :
    notas = [float(x) for x in input().split()]
    n1 = notas[0]
    n2 = notas[1]
    n3 = notas[2]
    n4 = notas[3]
    n5 = notas[4]

maior = 0
menor = 0

for i in range(0,5):
    if (notas[i] > maior):
        maior = notas[i]
        menor = maior

for i in range(0,5):
    if (notas[i] < menor):
        menor = notas[i]

notaFinal = (n1 + n2 + n3 + n4 + n5) - maior - menor

print(f'{notaFinal:.1f}')