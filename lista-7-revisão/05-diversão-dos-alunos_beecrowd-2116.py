def verificadorPrimo(num):
    multiplos = 0
    for i in range(2,num):
        if (num % i == 0 or num == 1):
            multiplos += 1
    if(multiplos == 0 and num != 1):
        return True
    else:
        return False

def atribuicao(num):
    if (verificadorPrimo(num)):
        return num        
    while(verificadorPrimo(num) == False):
        num = num - 1
        if (verificadorPrimo(num)):
            p = num
            return p

numA, numB = [int(x) for x in input().split()]
p1 = atribuicao(numA)   
p2 = atribuicao(numB)      
saida = p1 * p2

print(saida)