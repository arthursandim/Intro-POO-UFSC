def paresImpares (num):
    if (num % 2 == 0):
        return ('Par')
    else:
        return ('Ímpar')

contadorPares = 0
contadorImpares = 0

for i in range (0, 10):
    numero = int(input('Digite um número inteiro: '))
    parOuImpar = paresImpares(numero)
    if (parOuImpar == 'Par'):
        contadorPares += 1
    if (parOuImpar == 'Ímpar'):
        contadorImpares += 1
        
print (f'Foram digitados {contadorPares} números pares e {contadorImpares} números ímpares.')
    