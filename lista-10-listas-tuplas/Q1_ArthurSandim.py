#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

notas = [int(x) for x in input('Digite as 3 notas do aluno: ').split()]
maior = 0
menor = 0

for i in range (1,len(notas)+1):
    if i<=10 and (notas[i-1]<0 or notas[i-1]>10):
        print(f'A {i}ª foi nota digitada errada.')
        notas[i-1] = int(input(f'Digite novamente a {i}ª nota do aluno:'))

soma = 0  
for c in range(0,len(notas)):
    if c == 0:
        maior = menor = notas[c]
    elif notas[c] > maior:
        maior = notas[c]
    elif notas[c] < menor:
        menor = notas[c]
    soma += notas[c]

diffNotas = maior - menor
media = soma / len(notas)

print(f'Média do aluno: {media:.1f}')
print(f'Maior nota: {maior:.1f}')
print(f'Menor nota: {menor:.1f}')
print(f'Diferença entre maior e menor notas): {diffNotas:.1f}')
    