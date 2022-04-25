nome = str(input())
salario = float(input())
vendas = float(input())

porcentagemComissao = (15/100)

total = salario + (vendas * porcentagemComissao)

print (f'TOTAL = R$ {total:.2f}')



