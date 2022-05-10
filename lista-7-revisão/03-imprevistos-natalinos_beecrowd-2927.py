alunos,comput,caio,scomp = [int(x) for x in input().split()]

if (comput - caio - scomp > alunos):
    print ('Igor feliz!')
if (comput - caio - scomp <= alunos):
    if (caio > scomp/2):
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')
