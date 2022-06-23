def validaLista(mensagem,n):
        lista=[int(x) for x in input(mensagem).split()]
        while True:
            cont=0
            for element in lista:
                if not(len(lista)==n) or not#(0<=element<=10**12): PRECISA ALTERAR A CONDIÇÃO DO ELEMENTO DE ACORDO COM O PROBLEMA.

def validaLista(mensagem,n):
                    cont+=1
            if cont==0:
                return lista
            if cont!=0:
                print('Inválido')
                lista=[int(x) for x in input(mensagem).split()]
            else:
                break