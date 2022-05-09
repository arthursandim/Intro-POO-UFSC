valorProduto = float(input('Valor do produto: R$ '))
condPagamento = int(input('Parcelamento (digite 0 para "à vista"): '))
if (condPagamento == 0):
    desconto = valorProduto * 10/100
    valorProduto = valorProduto - desconto
    print(f'Valor final do produto, à vista: R${valorProduto:.2f}')
elif (condPagamento == 1):
    desconto = valorProduto * 5/100
    valorProduto = valorProduto - desconto
    print(f'Valor final do produto, de 1x: R${valorProduto:.2f}')
elif (condPagamento == 2):
    print(f'Valor final do produto, de 2x: R${valorProduto:.2f}')
elif (condPagamento >= 3):
    acrescimo = valorProduto * 20/100
    valorProduto = valorProduto + acrescimo
    print(f'Valor final do produto, de {condPagamento}x: R${valorProduto:.2f}')


                        