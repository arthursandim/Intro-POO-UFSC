numero = int(input())
alc = 0
gas = 0
die = 0

while (numero > 0):
    if (numero == 1):
        alc += 1
        numero = int(input())
    elif (numero == 2):
        gas += 1
        numero = int(input())
    elif (numero == 3):
        die += 1
        numero = int(input())
    elif (numero > 4):
        numero = int(input())
    else:
        break
    
print('MUITO OBRIGADO')
print(f'Alcool: {alc}')
print(f'Gasolina: {gas}')
print(f'Diesel: {die}')