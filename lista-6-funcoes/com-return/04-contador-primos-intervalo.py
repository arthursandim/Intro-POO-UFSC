def ehPrimo(num):
    mult = 0
    for i in range(2,num):
        if (num % i == 0 or num == 1):
            mult += 1

    if(mult == 0 and num != 1):
        primo = True
    else:
        primo = False
    return primo

def contagemPrimos(n1,n2):
    cont = 0
    n3 = n1
    for i in range(n1, n2+1):
        if (ehPrimo(n3)):
            cont +=1
        n3 += 1
    return cont

numA = int(input('Digite o número: '))
numB = int(input('Digite outro número: ')) 

if (numA <= numB):
    print(f'Existem {contagemPrimos(numA,numB)} números primos dentro do intervalo digitado.')   

else:
    print(f'Existem {contagemPrimos(numB,numA)} números primos dentro do intervalo digitado.')