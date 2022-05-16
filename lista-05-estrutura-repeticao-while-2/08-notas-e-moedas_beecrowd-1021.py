N = float(input('Digite o valor: R$ '))

while (N < 0 or N > 1000000.00):
    print ('Entrada inválida. Digite novamente')
    N = float(input('Digite o valor: '))
    
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
moeda1 = 0
moeda50 = 0
moeda25 = 0
moeda10 = 0
moeda5 = 0
moeda001 = 0


while (N > 0):
    if (N >= 100):
        nota100 = N // 100
        N -= nota100 * 100
    elif (N >= 50):
        nota50 = N // 50
        N -= nota50 * 50
    elif (N >= 20):
        nota20 = N // 20
        N -= nota20 * 20
    elif (N >= 10):
        nota10 = N // 10
        N -= nota10 * 10
    elif (N >= 5):
        nota5 = N // 5
        N -= nota5 * 5
    elif (N >= 2):
        nota2 = N // 2
        N -= nota2 * 2
    elif (N >= 1):
        moeda1 = N // 1
        N -= moeda1 * 1
    elif (N >= 0.5):
        moeda50 = N // 0.5
        N -= moeda50 * 0.5
    elif (N >= 0.25):
        moeda25 = N // 0.25
        N -= moeda25 * 0.25
    elif (N >= 0.1):
        moeda10 = N // 0.1
        N -= moeda10 * 0.1
    elif (N >= 0.05):
        moeda5 = N // 0.05
        N -= moeda5 * 0.05
    elif (N >= 0.01):
        moeda001 = N // 0.01
        N -= moeda001 * 0.01
    else:
        break
        
print('NOTAS:')
print(f'{nota100:.0f} nota(s) de R$ 100.00')
print(f'{nota50:.0f} nota(s) de R$ 50.00')
print(f'{nota20:.0f} nota(s) de R$ 20.00')
print(f'{nota10:.0f} nota(s) de R$ 10.00')
print(f'{nota5:.0f} nota(s) de R$ 5.00')
print(f'{nota2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda1:.0f} moeda(s) de R$ 1.00')
print(f'{moeda50:.0f} moeda(s) de R$ 0.50')
print(f'{moeda25:.0f} moeda(s) de R$ 0.25')
print(f'{moeda10:.0f} moeda(s) de R$ 0.10')
print(f'{moeda5:.0f} moeda(s) de R$ 0.05')
print(f'{moeda001:.0f} moeda(s) de R$ 0.01')  
  
