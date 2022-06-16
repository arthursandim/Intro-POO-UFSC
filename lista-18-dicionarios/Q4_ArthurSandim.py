#Arthur Vinicius Gouvea Sandim
#21204602
#https://www.beecrowd.com.br/judge/pt/problems/view/1953


while True:
    listaAlunos = list()
    epr = 0
    ehd = 0
    intrusos = 0
    n = int(input('Digite a quantidade de alunos: '))
    while not(1<=n<10**4):
        print('Inválido.')
        n = int(input('Digite a quantidade de alunos novamente: '))

    for i in range(n):
        aluno = dict()
        aluno[str(input('Digite a disciplina: ').upper())] = str(input('Digite a matrícula: '))
        listaAlunos.append(aluno.copy())

    for j in range(len(listaAlunos)):
        for k in listaAlunos[j].keys():
            if k == 'EPR':
                epr+=1
            elif k == 'EHD':
                ehd+=1
            else:
                intrusos+=1
    print(f'EHD: {ehd}')
    print(f'EPR: {epr}')
    print(f'Intrusos: {intrusos}')
    continuar = str(input('Deseja continuar [S/N]?: ').upper())
    if continuar == 'N':
        break