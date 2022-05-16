for i in range (1,16):
    M,N = [int(x) for x in input(f'Digite os placar do jogo {i}: ').split()]
    if (M<0 or N<0 or M>20 or N>20 or N == M):
        M,N = [int(x) for x in input(f'Valores errados. Digite o placar do jogo {i} novamente: ').split()]
    if (i == 1):
        venc1 = ''
        if (M > N):
            venc1 = 'A'
        else:
            venc1 = 'B'
    if (i == 2):
        venc2 = ''
        if (M > N):
            venc2 = 'C'
        else:
            venc2 = 'D'
    if (i == 3):
        venc3 = ''
        if (M > N):
            venc3 = 'E'
        else:
            venc3 = 'F'
    if (i == 4):
        venc4 = ''
        if (M > N):
            venc4 = 'G'
        else:
            venc4 = 'H'
    if (i == 5):
        venc5 = ''
        if (M > N):
            venc5 = 'I'
        else:
            venc5 = 'J'
    if (i == 6):
        venc6 = ''
        if (M > N):
            venc6 = 'K'
        else:
            venc6 = 'L'
    if (i == 7):
        venc7 = ''
        if (M > N):
            venc7 = 'M'
        else:
            venc7 = 'N'
    if (i == 8):
        venc8 = ''
        if (M > N):
            venc8 = 'O'
        else:
            venc8 = 'P'
        if (i == 9):
            venc9 = ''
        if (M > N):
            venc9 = venc1
        else:
            venc9 = venc2
    if (i == 10):
        venc10 = ''
        if (M > N):
            venc10 = venc3
        else:
            venc10 = venc4
    if (i == 11):
        venc11 = ''
        if (M > N):
            venc11 = venc5
        else:
            venc11 = venc6
    if (i == 12):
        venc12 = ''
        if (M > N):
            venc12 = venc7
        else:
            venc12 = venc8
    if (i == 13):
        venc13 = ''
        if (M > N):
            venc13 = venc9
        else:
            venc13 = venc10
    if (i == 14):
        venc14 = ''
        if (M > N):
            venc14 = venc11
        else:
            venc14 = venc12
    if (i == 15):
        venc15 = ''
        if (M > N):
            venc15 = venc13
        else:
            venc15 = venc14
print(f'O campeão foi o time: {venc15}')