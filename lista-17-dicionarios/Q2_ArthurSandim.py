#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602
#Questão - https://www.beecrowd.com.br/judge/pt/problems/view/2482

def criarLista(cabec,index1,index2):
    iter = int(input(cabec))
    dicio = dict()
    lista = list()
    for i in range(iter):
        dicio[index1] = str(input(f'Digite o(a) {index1}: '))
        dicio[index2] = str(input(f'Digite o(a) {index2}: ')) 
        lista.append(dicio.copy())
    return lista


idiomas = criarLista('Digite a quantidade de idiomas: ', 'idioma', 'mensagem')
criancas = criarLista('Digite a quantidade de crianças que irão receber as cartas: ', 'nome', 'idioma')

for k in range(len(criancas)):
    for l in range(len(idiomas)):
        if criancas[k]['idioma'] == idiomas[l]['idioma']:
            print()
            print(criancas[k]['nome'])
            print(idiomas[l]['mensagem'])
