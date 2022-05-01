numA, numB = [int(x) for x in input('Digite os números separados por espaço: ').split()]
soma = 0

print ('Os elementos do intervalo são: ', end = '')
for i in range (numA + 1,numB):
    print (f'({i})', end='')
    soma = soma + i

print()    
print (f'A soma dos números do intervalo ]{numA},{numB}[ é {soma}')