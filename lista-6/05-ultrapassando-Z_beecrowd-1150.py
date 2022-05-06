def contagem(x,c,z):
    c = x
    aux = c
    vezes = 1
    while aux < z:
        c = c + 1
        aux = c + aux
        vezes +=1

    print(vezes)
    
numX = int(input())
numZ = int(input())
contador = 0
while numZ <= numX:
    numZ = int(input())
    
contagem(numX,contador,numZ)


    