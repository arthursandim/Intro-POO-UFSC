media = 0
maiorMedia = 0
melhorAluno = ''
conceito = ''

for i in range(1,6):
    nome = str(input('Nome: '))
    nota1, nota2, nota3 = [float(x) for x in input('Digite as 3 médias do aluno, separado por espaço: ').split()]
    media = (nota1 + nota2 + nota3)/3
    if (maiorMedia < media):
        maiorMedia = media
        melhorAluno = nome
        if (maiorMedia >= 5.75):
            conceito = 'Aprovado'
        elif ( 2.75<= maiorMedia < 5.75):
            conceito = 'Recuperação'
        else:
            conceito = 'Reprovado'
           
       
print ('Melhor Aluno:', melhorAluno)
print ('Média:', maiorMedia)
print ('O conceito do aluno foi:', conceito)