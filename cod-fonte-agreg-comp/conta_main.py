from cliente import Cliente
from conta_historico import Conta,Historico

listaClientes = []
listaContas = []


while True:
    print("===================================")
    print('1 - Criar conta')
    print('2 - Saque')
    print('3 - Depósito')
    print('4 - Transferência')
    print('5 - Extrato')
    print('6 - Cadastrar cliente')
    print('7 - Sair')
    print("===================================")
    opp = int(input('Digite o número da opção desejada: '))
    
    if not 0<opp<8:
        print("===================================")
        print("Opção inválida")
        print("===================================")
        opp = int(input('Digite o número da opção desejada: '))
    
    elif opp == 7:
        print("===================================")
        print('Fim da execução.')
        print("===================================")
        break
    
    elif opp == 1:
        if listaClientes == []:
            print("===================================")
            print("Abertura de conta")
            print("-----------")
            print('Cadastre um cliente primeiro.')
        else:
            print("===================================")
            print("Abertura de conta")
            print("-----------")
            print('Qual cliente deseja inserir?')
            print("-----------")
            for pos,client in enumerate(listaClientes):
                print(f'ID {pos+1} - {client.nome}')
            print("===================================")
            indice = int(input('Digite o ID do cliente: '))      
            numero = int(input('Nº da conta: '))            
            limite = int(input('Limite da conta: '))
            saldo = int(input('Saldo da conta: '))
            cco = Conta(numero, listaClientes[indice-1].nome, saldo, limite)
            listaContas.append(cco)
    
    elif opp == 2:
        print("===================================")
        print("Saque")
        print("-----------")
        conta = int(input("Nº da Conta: "))
        valor = int(input(("Valor da retirada: R$ ")))
        existe = False
        for element in listaContas:
            if element.numero == conta:
                element.retira(valor)
                existe = True
        if not existe:
            print("===================================")
            print("Não existe conta com esse número.")
            
    elif opp == 3:
        print("===================================")
        print("Depósito")
        print("-----------")
        conta = int(input("Nº da Conta: "))
        valor = int(input(("Valor do depósito: R$ ")))
        existe = False
        for element in listaContas:
            if element.numero == conta:
                element.deposita(valor)
                existe = True
        if not existe:
            print("===================================")
            print("Não existe conta com esse número.")

    elif opp == 4:
        print("===================================")
        print("Transferência: ")
        print("-----------")
        conta = int(input("Nº da Conta transferente: "))
        valor = int(input("Valor da transferência: R$ "))
        destinatario = int(input("Nº da Conta destinatário: "))
        existe = False
        for element in listaContas:
            for element2 in listaContas:
                if element.numero == conta and element2.numero == destinatario:
                    element.transfere(element2, valor)
                    existe = True
        if not existe:
            print("===================================")
            print("Uma das contas inexistente. Verifique os números e tente novamente.")
    
    elif opp == 5:
        print("===================================")
        print("Extrato:")
        print("-----------")
        conta = int(input("Nº da Conta: "))
        existe = False
        for element in listaContas:
            if element.numero == conta:
                element.extrato()
                element.historico.imprime()
                existe = True
        if not existe:
            print("===================================")
            print("Não existe conta com esse número.")

    elif opp == 6:
        print("===================================")
        print("Cadastro de cliente")
        print("-----------")
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        cpf = input('Cpf: ')
        cli = Cliente(nome, sobrenome, cpf)
        listaClientes.append(cli)
        

