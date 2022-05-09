maiorMedia = 0
mediaTurma = 0
conceito = ''

def calculoMedias(mM,mT):
    for i in range(1,6):
        n1,n2,n3 = [float(x) for x in input().split()]
        mediaAluno = (n1 + n2 + n3)/3
        mT += mediaAluno
        if (mM < mediaAluno):
            mM = mediaAluno
        if (i == 5):
            mT = mT/i
    return mM, mT

def conceitoUfsc(conc, mM):
    if (mM >= 5.75):
        conc = 'Aprovado'
    elif ( 2.75 <= mM < 5.75):
        conc = 'Recuperação'
    else:
        conc = 'Reprovado'
    return conc
        
maiorMedia, mediaTurma = calculoMedias(maiorMedia,mediaTurma)

print(f'Nota do melhor aluno: {maiorMedia:.1f}')
print(f'O aluno foi {conceitoUfsc(conceito, maiorMedia)}')

