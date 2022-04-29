maiorMedia = 0
melhorAluno = ''
melhorMensalidade = 0

for i in range(1,6):
    nome = str(input('Nome: '))
    media = float(input('Média Geral: '))
    mensalidade = float(input('Mensalidade: '))
    if (maiorMedia < media):
        maiorMedia = media
        melhorAluno = nome
        melhorMensalidade = mensalidade
       
print ('Melhor Aluno:', melhorAluno)
print ('Média:', maiorMedia)
print ('Mensalidade sem desconto:', melhorMensalidade)
print ('Mensalidade com desconto:', melhorMensalidade * 0.7)
        

