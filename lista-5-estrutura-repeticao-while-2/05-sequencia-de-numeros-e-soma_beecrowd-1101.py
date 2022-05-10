numA, numB = [int(x) for x in input().split()]

while (numB != 0 and numA != 0):
    soma = 0
    if (numA < numB):
        for i in range (numA,numB+1):
            soma = soma + i
    else:
        for i in range (numB,numA+1):
            print (f'{i}', end=' ')
            soma = soma + i
    print (f'Sum={soma}')
    numA, numB = [int(x) for x in input().split()]