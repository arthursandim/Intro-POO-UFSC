#Arthur Vinicius Gouvea Sandim
#21204602
#https://www.beecrowd.com.br/repository/UOJ_2091.html

def validaLista(mensagem,n):
        lista=[int(x) for x in input(mensagem).split()]
        while True:
            cont=0
            for element in lista:
                if not(len(lista)==n) or not(0<=element<=10**12):
                    cont+=1
            if cont==0:
                return lista
            if cont!=0:
                print('Inválido')
                lista=[int(x) for x in input(mensagem).split()]
            else:
                break

while True:
    n = int(input('Digite a quantidade de números: '))
    if n==0:
        break
    while not(1<=n<=10**5):
        print('Inválido.')
        n = int(input('Digite a quantidade de números: '))
    
    numeros=validaLista((f'Digite os {n} números: '),n)

    for elemento in numeros:
        for j in range(numeros.index(elemento)+1,len(numeros)):
            if j >= len(numeros):
                break
            if elemento==numeros[j]:
                numeros.pop(numeros.index(numeros[j]))
                numeros.pop(numeros.index(elemento))
    print(f'Número solitário: {numeros[0]}')