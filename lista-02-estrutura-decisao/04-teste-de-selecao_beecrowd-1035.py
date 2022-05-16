valorA, valorB, valorC, valorD = [int(x) for x in input().split()]
if (valorB > valorC and valorD > valorA and valorC + valorD > valorA + valorB and valorC > 0 and valorD > 0 and valorA%2 == 0):
    print ('Valores aceitos')
else:
    print ('Valores não aceitos')