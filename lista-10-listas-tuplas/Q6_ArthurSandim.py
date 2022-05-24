#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

while True:
    nome=input('Atleta: ')
    if nome=='O':
        break
    melhor=pior=0
    soma=0
    saltos = list()
    for i in range(5):
        saltos.append(float(input(f'{i+1}º salto: ')))
        if i==0:
            melhor=pior=saltos[i]
        elif saltos[i]>melhor:
            melhor=saltos[i]
        elif saltos[i]<pior:
            pior=saltos[i]
        soma+=saltos[i]
    media=(soma-melhor-pior)/3
    print()
    print('-'*45)
    print()
    print(f'Melhor salto: {melhor:.1f} m')
    print(f'Pior salto: {pior:.1f} m')
    print(f'Média dos demais saltos: {media:.1f} m')
    print('-'*45)
    print(f'Resultado final:')
    print(f'{nome}: {media:.1f} m')
    print()
    print('-'*45)
    print()