from math import sqrt
while True:
    try:
        D, VF, VG = [int(x) for x in input('Digite os valores determinados: ').split()]
        while (D < 1 or VF < 1 or VG < 1 or D > 100 or VF > 100 or VG > 100):
            D, VF, VG = [int(x) for x in input('Um dos valores foi inválido. Digite os valores novamente: ').split()]    
        VG = (sqrt(12**2 + D**2))/VG
        VF = 12/VF
        if VG > VF:
            print('N')
        else:
            print('S')
    except EOFError:
        break