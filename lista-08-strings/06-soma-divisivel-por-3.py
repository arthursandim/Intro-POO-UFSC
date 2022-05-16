while True:
    n,m = input('Digite a quantidade de algarismos:').split()
    n,m = int(n),int(m)
    soma = 0
    while (n<1 or n>10 or m<1 or m>1000000000 or len(str(m))!=n):
        n,m = input('Valor inválido. Digite a quantidade de algarismos:').split()
        n,m = int(n),int(m)
    m = str(m)
    for i in m:
        soma += int(i)
    if (soma % 3 == 0 ):
        print(f'{soma} sim')
    else:
        print(f'{soma} nao')
    continuar = input('Deseja continuar? [S/N])').upper()
    if(continuar == 'N'):
        break
    
    