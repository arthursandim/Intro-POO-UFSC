qtdPessoas = int(input('Digite a quantidade de pessoas: '))
soma = 0
media = 0

for i in range(1, qtdPessoas + 1):
    idade = int(input(f'Idade da pessoa número {i}: '))
    soma = soma + idade
    
media = soma / qtdPessoas
print (f'A média de idades é de: {media} anos')

if (0 <= media <= 25):
    print ('A turma é jovem.')
elif (26 <= media <= 60):
    print ('A turma é adulta.')
else:
    print ('A turma é idosa.')
    
    