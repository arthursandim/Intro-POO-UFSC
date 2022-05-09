def compraColchao(a,b,c,h,l, passa):
    if(a <= h and b <= l):
        passa = 'S'
    elif(a <= h and c <= l):
        passa = 'S'
    elif(b <= h and a <= l):
        passa = 'S'
    elif(b <= h and c <= l):
        passa = 'S'
    elif(c <= h and a <= l):
        passa = 'S'
    elif(c <= h and b <= l):
        passa = 'S'
    else:
        passa = 'N'
    return passa

a, b, c = [int(x) for x in input().split()]
h, l = [int(x) for x in input().split()]
passa = ''

compraColchao (a,b,c,h,l,passa)

if (passa == 'S'):
    print ('Tudo certo. Parabéns pela Compra.')
else:
    print ('Escolha outro colchão')
