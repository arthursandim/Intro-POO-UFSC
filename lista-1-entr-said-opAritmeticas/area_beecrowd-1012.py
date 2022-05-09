valorA, valorB, valorC = [float(x) for x in input().split()]

areaTriangulo = valorA * valorC / 2
areaCirculo = (valorC ** 2) * 3.14159
areaTrapezio = ((valorA + valorB)*valorC) / 2
areaQuadrado = valorB ** 2
areaRetangulo = valorA * valorB

print (f'TRIANGULO: {areaTriangulo:.3f}')
print (f'CIRCULO: {areaCirculo:.3f}')
print (f'TRAPEZIO: {areaTrapezio:.3f}')
print (f'QUADRADO: {areaQuadrado:.3f}')
print (f'RETANGULO: {areaRetangulo:.3f}')