horaInicial, horaFinal = [int(x) for x in input().split()]
horasDeJogo = 0

if (horaInicial < 24 and horaFinal < 24):
    if (horaFinal > horaInicial):
        horasDeJogo = horaFinal - horaInicial
    elif (horaFinal < horaInicial):
        horasDeJogo = horaInicial - horaFinal
        horasDeJogo = 24 - horasDeJogo
    elif (horasDeJogo == 0):
        horasDeJogo = 24
    if (horasDeJogo < 0):
        horasDeJogo *= -1
print(f'O JOGO DUROU {horasDeJogo} HORA(S)')