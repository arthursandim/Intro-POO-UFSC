#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

n, r = [int(x) for x in input('Numero de Voluntarios e total de voltuntarios retornantes: ').split()]
while not(1<=r<=n<=10**4):
    print('Inválido.')
    n, r = [int(x) for x in input('Numero de Voluntarios e total de voltuntarios retornantes: ').split()]

volunt = set(range(1,n+1))

retornantes = set(int(x) for x in input('Voluntários retornantes: ').split())
naoRertonaram = set(volunt.difference(retornantes))

if naoRertonaram==set():
    print("*")
else:
    print(f'Voluntários que não retornaram: {naoRertonaram}')