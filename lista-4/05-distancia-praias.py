totalPraias = int(input('Quantas praias deseja cadastrar: '))
praiaMaisDistante = ''
maiorDistancia = 0
contadorPraias = 0
distanciaMedia = 0
contador = 0

while True:
    contador += 1
    praia = input('Digite o nome da praia: ')
    distanciaCentro = int(input('Digite a distância, em Km, do centro de Floripa: '))
    distanciaMedia += distanciaCentro/contador
    if (distanciaCentro > maiorDistancia):
        praiaMaisDistante = praia
        maiorDistancia = distanciaCentro
    if (15 <= distanciaCentro <= 20):
        contadorPraias += 1
    if (contador >= totalPraias):
        break
    
print (f'A praia mais distante é {praiaMaisDistante}')
print (f'{contadorPraias} praia(s) estão em uma distância entre 15 e 20 km')
print (f'A distância média das praias digitadas é de {distanciaMedia:.1f} km')
