numero = int(input("Digite o número: "))
multiplos=0
primo = False
for i in range(2,numero):
    if (numero % i == 0 or numero == 1):
        multiplos += 1

if(multiplos == 0 and numero != 1):
    primo = True
else:
    primo = False
    
if (primo):
    print ('É primo')
else:
    print('Não é primo')