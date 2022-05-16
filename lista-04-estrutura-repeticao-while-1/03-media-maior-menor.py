deNovo = 'S'
maior = 0
soma = 0
media = 0
contador = 0
menor = 0

while deNovo == 'S':
    num = int(input('Digite um número: '))
    deNovo = input('Deseja digitar novamente? [S/N]   ').upper()
    soma += num
    contador += 1
    media = soma / contador
    
    if (num < menor or menor == 0):
        menor = num
    if (num > maior):
        maior = num
        
print (f'A média entre os números digitados foi {media}')
print (f'O menor número digitado foi {menor}')
print (f'O maior número digitado foi {maior}')

    