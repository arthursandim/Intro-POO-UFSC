teste = 1
resultado = 0
while True:
    N = int(input('Digite um número: '))
    if (N == - 1):
        break
    if (N > 15):
        N = int(input('Valor inválido. Digite um número: '))
    print(f'Teste {teste}')
    teste += 1
    if (N == 0):
        resultado = 4
    elif (N == 1):
        resultado = 9
    else:
        resultado = (1+2**N)*(1+2**N)
    print (resultado)
    print()
        