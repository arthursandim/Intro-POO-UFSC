teste = 1
while True:
    V = int(input('Digite o valor: B$ '))
    if (V == 0):
            break
    if (V < 0):
            V = int(input('Valor inválido. Digite o valor: B$ '))
    print(f'Teste {teste}')
    teste += 1
    I = 0
    J = 0
    K = 0
    L = 0
    while (V > 0):
        if (V >= 50):
            I = V // 50
            V -= I * 50
        elif (V >= 10):
            J = V // 10
            V -= J * 10
        elif (V >= 5):
            K = V // 5
            V -= K * 5
        elif (V >= 1):
            L = V // 1
            V -= L * 1
        else:
            break
    print (I, J, K, L)
    print()
