#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602


futebol=set(input('Alunos de Futebol: ').split())
basquete=set(input('Alunos de Basquete: ').split())
natacao=set(input('Alunos de Natação: ').split())
volei=set(input('Alunos de Vôlei: ').split())

print()
print(f'Alunos de Futebol: {futebol}')
print(f'Alunos de Basquete: {basquete}')
print(f'Alunos de Natação: {natacao}')
print(f'Alunos de Vôlei: {volei}')
print()

print('Deseja cadastrar novos alunos? [S/N]')
addNovos=input()

while addNovos.upper()=='S':
    novosModal=input('Em qual modalidade: ')
    if novosModal!='':
        print('Digite somente um aluno por vez.')
    if novosModal.lower()=='futebol':
        futebol.add(input('Futebol: '))
    elif novosModal.lower()=='basquete':
        basquete.add(input('Basquete: '))
    elif novosModal.lower()=='natacao':
        natacao.add(input('Natação: '))
    elif novosModal.lower()=='volei':
        volei.add(input('Volei: '))
    print('Deseja cadastrar novos alunos? [S/N]')
    addNovos=input()

print()
print(f'Alunos de Futebol: {futebol}')
print(f'Alunos de Basquete: {basquete}')
print(f'Alunos de Natação: {natacao}')
print(f'Alunos de Vôlei: {volei}')
print()

alunosDesc=list()

def inserirAlunos(lista,modal1,modal2):
    if modal1.intersection(modal2):
        return lista.append(modal1.intersection(modal2))

inserirAlunos(alunosDesc,futebol,basquete)
inserirAlunos(alunosDesc,futebol,natacao)
inserirAlunos(alunosDesc,futebol,volei)
inserirAlunos(alunosDesc,basquete,volei)
inserirAlunos(alunosDesc,basquete,natacao)
inserirAlunos(alunosDesc,natacao,volei)

print(f'Alunos com desconto: {alunosDesc}')
print(f'Total de alunos da escola: {len(futebol.union(basquete).union(natacao).union(volei))}')
print(f'Total de alunos de futebol: {len(futebol)}')
print(f'Total de alunos de Basquete: {len(basquete)}')
print(f'Total de alunos de Natação: {len(natacao)}')
print(f'Total de alunos de Volei: {len(volei)}')
        