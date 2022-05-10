numA, numB = [int(x) for x in input().split()]

while (numA != numB):
    if (numA < numB):
        print('Crescente')
    elif(numB < numA):
        print('Descrescente')
    else:
        break
    numA, numB = [int(x) for x in input().split()]