quantCompetidores, quantFolhas, folhasCompetidores = [int(x) for x in input().split()]

if (quantCompetidores * folhasCompetidores <= quantFolhas):
    print('S')
else:
    print ('N')