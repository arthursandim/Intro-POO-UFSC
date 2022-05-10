numero = int(input())
while numero != 0:
    contador = 1
    while (contador < numero + 1):
        if (contador == numero):
            print(numero)
            contador += 1
        else:
            print (contador, end=' ')
            contador += 1
    print()
    numero = int(input())