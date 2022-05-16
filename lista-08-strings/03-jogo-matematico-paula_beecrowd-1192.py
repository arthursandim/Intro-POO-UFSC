casos = int(input('Digite a quantidade de casos teste: '))
produto = 0
soma = 0
print()
print('------------------------')
print()
for i in range(1,casos + 1):
    print(f'Teste {i}')
    seq = input('Digite a sequencia: ')
    for i in seq:
        numA = int(seq[0])
        numB = int(seq[2])
        letra = seq[1]
    if(numA == numB or numB == numA):
        produto = numA * numB
        print(f'Resultado = {produto}')
    elif(letra == letra.lower()):
        soma = numA + numB
        print(f'Resultado = {soma}')
    elif(letra == letra.upper()):
        soma = numB - numA
        print(f'Resultado = {soma}')
    print()
    print('------------------------')
    print()