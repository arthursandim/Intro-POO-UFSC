def reajuste (salario):
    if (salario <= 400.00):
        novoSalario = salario + (salario * 0.15)
        reajuste = novoSalario - salario
        print (f'Novo salario: {novoSalario:.2f}')
        print (f'Reajuste ganho: {reajuste:.2f}')
        print (f'Em percentual: 15 %')
    elif (salario <= 800.00):
        novoSalario = salario + (salario * 0.12)
        reajuste = novoSalario - salario
        print (f'Novo salario: {novoSalario:.2f}')
        print (f'Reajuste ganho: {reajuste:.2f}')
        print (f'Em percentual: 12 %')
    elif (salario <= 1200.00):
        novoSalario = salario + (salario * 0.10)
        reajuste = novoSalario - salario
        print (f'Novo salario: {novoSalario:.2f}')
        print (f'Reajuste ganho: {reajuste:.2f}')
        print (f'Em percentual: 10 %')
    elif (salario <= 2000.00):
        novoSalario = salario + (salario * 0.07)
        reajuste = novoSalario - salario
        print (f'Novo salario: {novoSalario:.2f}')
        print (f'Reajuste ganho: {reajuste:.2f}')
        print (f'Em percentual: 7 %')
    else:
        novoSalario = salario + (salario * 0.04)
        reajuste = novoSalario - salario
        print (f'Novo salario: {novoSalario:.2f}')
        print (f'Reajuste ganho: {reajuste:.2f}')
        print (f'Em percentual: 4 %')
        
    
salario = float(input())
reajuste(salario)