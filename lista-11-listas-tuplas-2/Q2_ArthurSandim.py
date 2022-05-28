#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

def plugLinha(l1,l2):
    cont=0
    while True:
        if cont>=5:
            break
        if l1[cont]!=l2[cont]:
            cont+=1
        else:
            break
        
    if cont==5:
        return True
    else:
        return False
    
def restricao(lists):
    for element in lists:
        if element!=0 and element!=1:
            return True
    
lista1=[int(x) for x in input('Digita o primeiro: ').split()]
while restricao(lista1) or len(lista1)!=5:
    lista1=[int(x) for x in input('Inválido, digita de novo: ').split()]

lista2=[int(x) for x in input('Digita o segundo: ').split()]
while restricao(lista2) or len(lista2)!=5:
    lista2=[int(x) for x in input('Inválido, digita de novo: ').split()]
    
if plugLinha(lista1,lista2):
    print('Y')
else:
    print('N')
