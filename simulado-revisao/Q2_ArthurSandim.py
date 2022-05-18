#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

def dadosPesquisa():
    cont = 0
    montanteIdade = 0
    mediaIdade = 0
    sexoMenorSal = ''
    idadeMenorSal = 0
    mulherMaior2k = 0
    maiorIdade = 0
    menorSal = 9999999999999999
    menorSalSexo = ''
    maisVelho = ''
    while True:
        nom = input('Digite o nome: ')
        idd = int(input('Digite a idade: '))
        sex = input('Digite o sexo [M/F]: ').upper()
        sal = float(input('Digite o salário: R$ '))
        cont += 1
        montanteIdade += idd
        if(idd > maiorIdade):
            maiorIdade = idd
            maisVelho = nom
        if(sal < menorSal):
            menorSal = sal
            idadeMenorSal = idd
            sexoMenorSal = sex
        if(sex == 'F' and sal > 2000.00):
            mulherMaior2k +=1
            
        print()
        continuar = input('Deseja continuar cadastrando? [S/N] ').upper()
        print()
        if(continuar == 'N'):
            media = montanteIdade/cont
            print(f'Média de idade do grupo: {media:.0f} anos')
            print(f'Quantidade de mulheres que recebem mais de R$ 2000,00: {mulherMaior2k}')
            print(f'Sexo da pessoa com menor salário: {sexoMenorSal}')
            print(f'Idade da pessoa com menor salário: {idadeMenorSal}')
            print(f'O nome do morador mais velho: {maisVelho}')
            break

    
dadosPesquisa()
print()
print('---------------------------')
print('Fim da execução do programa')    