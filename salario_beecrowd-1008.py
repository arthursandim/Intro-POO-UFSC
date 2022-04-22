numFuncionario = int(input())
horasTrabalhadas = int(input())
valorPorHora = float(input())

salario = horasTrabalhadas * valorPorHora

print(f'Número = {numFuncionario}')
print (f'Salário = R$ {salario:.2f}')