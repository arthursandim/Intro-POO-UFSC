def escadaLigada():
    N = int(input('Número de pessoas: '))
    t1 = 0
    t2 = 0
    while(N<1 or N>1000):
        print('Entrada inválida, digite novamente.')
        N = int(input('Número de pessoas: '))
        
    for i in range(0,N):
        segundos = int(input('Segundos: '))
        t3 = 10
        t2 = segundos
        while (segundos<0 or segundos>10000):
            print('Entrada inválida, digite novamente.')
            segundos = int(input('Segundos: '))
        if(t2 - t1 == 10 or i==0):
            t3 += t2 + t1
            t1 = t2
    print(t3)   
        
escadaLigada()