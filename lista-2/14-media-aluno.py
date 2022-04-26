nota1, nota2, nota3 = [float(x) for x in input('Digite as notas do aluno, separadas por espaço: ').split()]
media = (nota1 + nota2 + nota3)/3

if (media < 5):
    print(f'A média é {media:.1f}. ALUNO REPROVADO')
elif (5 <= media < 7):
    print(f'A média é {media:.1f}. ALUNO EM RECUPERAÇÃO')
elif (media >= 7):
    print(f'A média é {media:.1f}. ALUNO APROVADO')