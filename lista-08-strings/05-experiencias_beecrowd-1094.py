N=int(input('Digite o número de casos testes: '))
cont,rato,sapo,coelho=0,0,0,0
print('-------------------------------------')
for i in range(1,N+1):
    print(f'Teste {i}')
    quantia,tipo=input('Digite a quantidade e o tipo da cobaia: ').split()
    quantia = int(quantia)
    while(quantia<1 or quantia>15):
        quantia,tipo=input('Quantidade inválida. Digite novamente: ').split()
        quantia = int(quantia)
    cont += quantia
    if tipo.upper() == 'C':
        coelho += quantia
    elif tipo.upper() =='R':
        rato += quantia
    elif tipo.upper() =='S':
        sapo += quantia
    print('-------------------------------------')
print(f'Total: {cont} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {float(((100*coelho)/cont)):.2f} %')
print(f'Percentual de ratos: {float(((100*rato)/cont)):.2f} %')
print(f'Percentual de sapos: {float(((100*sapo)/cont)):.2f} %')