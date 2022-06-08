#Aluno: Arthur Vinicius Gouvea Sandim
#Matricula: 21204602

def inserirCliente(bc1,bc2):
    if bc1.intersection(bc2):
        return bc1.intersection(bc2)
        
def diferencaConj(bc1,bc2):
    if bc1.symmetric_difference(bc2):
        return bc1.symmetric_difference(bc2)

banco1=set(input('Clientes do Banco UM: ').split())
banco2=set(input('Clientes do Banco DOIS: ').split())


print()
print(f'Clientes do Banco UM: {banco1}')
print(f'Clientes do Banco DOIS: {banco2}')
print()

print('Deseja cadastrar novo cliente? [S/N]')
addNovo=input()

while addNovo.upper()=='S':
    novoModal=int(input('Em qual Banco [1/2]: '))
    if novoModal!=0:
        print('Digite somente um cliente por vez.')
    if novoModal==1:
        banco1.add(input('Banco UM: '))
    elif novoModal==2:
        banco2.add(input('Banco DOIS: '))
    print('Deseja cadastrar novo cliente? [S/N]')
    addNovo=input()



print()
print(f'Clientes do Banco UM: {banco1}')
print(f'Clientes do Banco DOIS: {banco2}')
print()

clienteDup=set(inserirCliente(banco1,banco2))
clienteUni=set(diferencaConj(banco1,banco2))


print(f'Clientes Banco UM: {len(banco1)}')
print(f'Clientes Banco DOIS: {len(banco2)}')
print(f'Clientes simultâneos em banco UM e DOIS: {len(clienteDup)}')
print(f'Clientes somente de um dos bancos: {len(clienteUni)}')
print(f'Total de clientes: {len(banco1.union(banco2))}')