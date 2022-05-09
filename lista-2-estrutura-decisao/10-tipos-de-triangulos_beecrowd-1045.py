A,B,C = sorted([float(x) for x in input().split()])[::-1]
verificador = True

if (A >= B + C):
    print('NAO FORMA TRIANGULO')
    verificador = False
if (A**2 == B**2 + C**2 and verificador):
    print('TRIANGULO RETANGULO')
if (A**2 > B**2 + C**2 and verificador):
    print('TRIANGULO OBTUSANGULO')
if (A**2 < B**2 + C**2 and verificador):
    print('TRIANGULO ACUTANGULO')
if (A == B == C and verificador):
    print('TRIANGULO EQUILATERO')
if (A == B != C or A == C != B or B == C != A and verificador):
    print('TRIANGULO ISOSCELES')
