print("Digite quantos anos, meses e dias a pessoa tem.")

idadeAnos = int(input("Anos: "))
idadeMeses = int(input("Meses:"))
idadeDias = int(input("Dias: "))

anosEmDias = idadeAnos*365
mesesEmDias = idadeMeses*30

idadeCompletaEmDias = int(anosEmDias + mesesEmDias + idadeDias)

print("A pessoas tem ", int(idadeCompletaEmDias),"dias de vida")