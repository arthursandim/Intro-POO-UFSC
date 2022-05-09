valorA, valorB, valorC = [float(x) for x in input().split()]

if (abs(valorB - valorC) < valorA < valorB + valorC and abs(valorA - valorC) < valorB < valorA + valorC and abs(valorA - valorB) < valorC < valorA + valorB):
    perimetro = valorA + valorB + valorC
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((valorA + valorB) * valorC) / 2
    print(f'Area = {area:.1f}')