continua = 'S'
while continua == 'S':
    salario = float(input('Digite o salário do funcionário: '))
    descontoPrev = salario * 0.11
    
    if (descontoPrev > 320.00):
        descontoPrev = 320.00
        porcentagem = 320 / salario * 100
        print (f'O desconto previdenciário foi de R$ {descontoPrev:.2f}')
        print (f'A porcentagem em cima do salário foi {porcentagem:.1f}%')
    else:    
        print (f'O desconto previdenciário foi de R$ {descontoPrev:.2f}')
    
    continua = input ('Deseja inserir outro salário para cálculo? [S/N]:  ').upper()
    if (continua == 'N'):
        break
