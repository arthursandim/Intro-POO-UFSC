totalEleitores = int(input("Digite o total de eleitores: "))
brancos = int(input("Digite o total de votos em branco: "))
nulos = int(input("Digite o total de votos nulos: "))
validos = int(input("Digite o total de votos válidos: "))

brancosPorCento = brancos/totalEleitores*100
nulosPorCento = nulos/totalEleitores*100
validosPorCento = validos/totalEleitores*100

print("O total percentual de votos válidos é de ", int(validosPorCento), "%")
print("O total percentual de votos nulos é de ", int(nulosPorCento), "%")
print("O total percentual de votos em branco é de ", int(brancosPorCento), "%")
