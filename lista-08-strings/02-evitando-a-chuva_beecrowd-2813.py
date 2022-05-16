dias = int(input('Digite o número de dias previstos: '))
casa = 0
casaSobrando = 0
escrit = 0
escritSobrando = 0

if (dias<1 or dias>1000):
    dias = int(input('Número inválido. Digite o número de dias previstos: '))

for i in range(0,dias):
    idaTrab, voltaTrab = input().split()
    if(idaTrab.lower() == 'chuva' and casaSobrando == 0):
        casa += 1
        escritSobrando += 1
    elif(idaTrab.lower() == 'chuva' and casaSobrando > 0):
        escritSobrando += 1
        casaSobrando -= 1
    if(voltaTrab.lower() == 'chuva' and escritSobrando == 0):
        escrit += 1
        casaSobrando += 1
    elif(voltaTrab.lower() == 'chuva' and escritSobrando > 0):
        casaSobrando += 1
        escritSobrando -= 1
        
print(f'Casa: {casa}. Escritório: {escrit}')