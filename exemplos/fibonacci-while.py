num = int(input("Digite um numero: "))
t1 = 0
t2 = 1
t3 = 0
contador = 0

while contador < num:
    print (t1, end=' ')
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    contador += 1

