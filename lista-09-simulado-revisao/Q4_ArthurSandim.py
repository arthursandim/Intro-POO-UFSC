#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

def escadaLigada(temp, tAnt, tot):
    if tot == 0:
        tot += 10
    elif temp-tAnt <= 10:
        tot += (temp - tAnt)
    else:
        tot += 10
    return tot

N = int(input('Número de pessoas: '))
tAnterior = 0
tTotal = 0

while(N<1 or N>1000):
        print('Entrada inválida, digite novamente.')
        N = int(input('Número de pessoas: '))
        print()
        
for i in range(0,N):
    segundos = int(input('Segundos: '))
    while (segundos<0 or segundos>10000):
        print('Entrada inválida, digite novamente.')
        segundos = int(input('Segundos: '))
    tTotal = escadaLigada(segundos, tAnterior, tTotal)
    tAnterior = segundos

print(f'O tempo total foi: {tTotal}')