testes = int(input())
cont = 0
while (cont < testes):
    numA,numB = [int(x) for x in input().split()]
    soma = 0
    if (numA < numB):
        for i in range(numA+1, numB):
            if (i % 2 != 0):
                soma += i
    else:
        for i in range(numB+1, numA):
            if (i % 2 != 0):
                soma += i
    print (soma)
    cont += 1
