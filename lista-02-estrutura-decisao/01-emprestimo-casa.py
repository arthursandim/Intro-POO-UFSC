valorCasa = float(input('Digite o valor da casa: R$ '))
salarioComprador = float(input('Digite o salário do comprador: R$'))
tempoDePagamento = int(input('Digite o tempo para pagamento, em anos: '))

tempoDePagamento = tempoDePagamento * 12

valorParcela = valorCasa / tempoDePagamento

porcentagemMinima = salarioComprador * 30/100

if (valorParcela > porcentagemMinima):
    print ('Empréstimo negado')
else:
    print(f'O empréstimo foi aprovado')
    print(f'{tempoDePagamento} vezes de R$ {valorParcela:.2f}')
    