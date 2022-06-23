#Arthur Vinicius Gouvea Sandim
#21204602
#https://www.beecrowd.com.br/repository/UOJ_1911.html

def verificarAssinatura(iterador, diferenca, contFalsas, dicio):
    for k in range(iterador):
        cont = 0
        name,sign = input('Digite o nome e a assinatura na aula: ').split()
        for j in dicio[name]:
            while len(dicio[name])!=len(sign):
                print('O tamanho dos nomes é incompatível')
                name,sign = input('Digite o nome e a assinatura na aula: ').split()
            if j != sign[cont]:
                diferenca += 1
            cont += 1
        if diferenca > 1:
            contFalsas += 1
        
        diferenca = 0
    return contFalsas

while True:
    n = int(input('Digite a quantidade de alunos na turma: '))
    if n==0:
        print('Fim do Programa.')
        break
    while not(1<=n<=50):
        print('Inválido.')
        n = int(input('Digite a quantidade de alunos na turma: '))
    
    alunosMatriculados = dict()
    for i in range(n):
        nome,assinatura = input('Digite o nome e a assinatura original: ').split()
        alunosMatriculados[nome] = assinatura
    
    m = int(input('Digite a quantidade de alunos presentes: '))
    while not(0<=m<=n):
        print('Inválido.')
        m = int(input('Digite a quantidade de alunos presentes: '))

    diff = 0
    assFalsas = 0

    total = verificarAssinatura(m, diff, assFalsas, alunosMatriculados)

    print(f'Assinaturas falsas: {total}')