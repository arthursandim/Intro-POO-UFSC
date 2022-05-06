def calculoFuso (saida, tempo, fuso):
    
    chegada = saida + tempo + fuso
    
    if (chegada == 24):
        print ('0')
    elif (chegada > 24):
        print (chegada - 24)
    elif (chegada < 0):
        print (24 + chegada)
    else:
        print (chegada)
        
saida, tempo, fuso = [int(x) for x in input().split()]

calculoFuso (saida, tempo, fuso)
