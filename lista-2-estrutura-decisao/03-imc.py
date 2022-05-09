peso = float(input('digite o peso(kg): '))
altura = float(input('Digite a altura (metros): '))
imc = peso / (altura**2)

if (imc < 18.5):
    print(f'O imc é {imc:.1f} e indica que está abaixo do peso')
elif (18.5 < imc < 25):
    print(f'O imc é {imc:.1f} e indica que está no peso ideal')
elif (25 < imc < 30):
    print(f'O imc é {imc:.1f} e indica que está com sobrepeso')
elif (30 < imc < 40):
    print(f'O imc é {imc:.1f} e indica que está na faixa de obesidade')
elif (imc > 40 ):
    print(f'O imc é {imc:.1f} e indica que está na faixa da obesidade mórbida')
    