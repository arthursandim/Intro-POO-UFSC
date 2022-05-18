#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

while True:
    andre, pedro, camila, manoel, iara = [int(x) for x in input('Entrada: ').split()]
    andre *= 300
    pedro *= 1500
    camila *= 600
    manoel *= 1000
    iara *= 150
    dFrancisca = 225
    print (f'Saída: {andre + pedro + camila + manoel + iara + dFrancisca}')
    print()
    continuar = input('Deseja continuar executando? [S/N] ')
    if (continuar.upper() == 'N'):
        break