#cliente.py
#exemplo de agregação

class Cliente:
    def __init__(self,nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf   
    
    def get_nome(self):
        return self.nome
    
    def get_sobrenome(self):
        return self.sobrenome
    
    def get_cpf(self):
        return self.cpf
    
    def set_nome(self,novo_nome):
        self.nome = novo_nome
        
    def set_sobrenome(self,novo_sobrenome):
        self.sobrenome = novo_sobrenome
    

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        
    def get_titular(self):
        return self.titular
     
    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self,valor):
        self.saldo = valor
