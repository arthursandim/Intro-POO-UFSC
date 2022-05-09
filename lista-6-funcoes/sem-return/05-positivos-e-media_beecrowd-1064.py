def digiteNovamente():
    contador = 0
    positivos = 0
    soma = 0
    media = 0
    while (contador < 6):
        numero = float(input())
        contador +=1
        if (numero > 0):
            soma += numero
            positivos += 1

    media = soma/positivos
    print (f'{positivos} valores positivos')
    print (f'{media:.1f}')


digiteNovamente()