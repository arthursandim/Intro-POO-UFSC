numero = int(input("Digite o número: "))
multiplos=0

for i in range(2,numero):
    if (numero % i == 0):
        multiplos += 1

if(multiplos == 0):
    print('É primo')
else:
    print('Não é primo.')