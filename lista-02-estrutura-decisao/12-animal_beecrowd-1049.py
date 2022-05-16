filo = str(input())
classe = str(input())
ordem = str(input())

if (filo == 'vertebrado'):
    if (classe == 'mamifero'):
        if (ordem == 'onivoro'):
            print('homem')
        else:
            print ('vaca') 
    if (classe == 'ave'):
        if (ordem == 'onivoro'):
            print('pomba')
        else:
            print ('aguia')
else:
    if (classe == 'inseto'):
        if (ordem == 'hematofago'):
            print('pulga')
        else:
            print ('lagarta') 
    if (classe == 'anelideo'):
        if (ordem == 'hematofago'):
            print('sanguessuga')
        else:
            print ('minhoca')
