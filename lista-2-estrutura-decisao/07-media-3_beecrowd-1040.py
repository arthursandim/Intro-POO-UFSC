nota1, nota2, nota3, nota4= [float(x) for x in input().split()]
media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + nota4)/10

if (media < 5):
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
elif (5 <= media <= 6.9):
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    notaExame = float(input())
    print(f'Nota do exame: {notaExame:.1f}')
    novaMedia = (media + notaExame)/2
    if (novaMedia < 5):
        print('Aluno reprovado.')
        print(f'Media final: {novaMedia:.1f}')
    else:
        print('Aluno aprovado.')
        print(f'Media final: {novaMedia:.1f}')        
elif (media >= 7):
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')