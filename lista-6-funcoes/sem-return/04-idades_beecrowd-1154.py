def mediaIdade(idade):
    contador = 0
    soma = 0
    while (idade > 0):
        contador += 1
        soma += idade
        mediaIdade = soma / contador
        idade = int(input())
    print (f'{mediaIdade:.2f}')
        
idade = int(input())
mediaIdade(idade)