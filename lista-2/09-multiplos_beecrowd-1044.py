valorA, valorB = [int(x) for x in input().split()]

if (valorA % valorB == 0 or valorB % valorA == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')