'''
    Criando a classe agencia
'''
from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O Valor de Caixa está ok. Caixa Atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


# criando sub-classes
class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        self.site = site
        # chamar a super classe principal(classe mãe) com seus atributos
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0
        
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
        
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
        
        

class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        # chamar a super classe principal(classe mãe) com seus atributos
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        # chamar a super classe principal(classe mãe) com seus atributos
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 100000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            # adicionar cliente
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não tem o patrimônio mínimo necessário para entrar na Agência Premium')


# Para não rodar esse código na importação
# Se o principal for main, digite: if __name__=='__main__':
if __name__=='__main_Banco__':
    # AgenciaVirtual
    # AgenciaComum
    # AgenciaPremium

    #programa
    agencia1 = Agencia(2222-3333, 20000000000, 4568)

    print('------- Agencia Virtual -----------------------------')
    #criando outras agencias
    #Requisitos (agencia_[tipo] = classe_Agencia(telefone, cnpj, num_agencia)
    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 2222-444, 15200000003)
    agencia_virtual.verificar_caixa()
    print(agencia_virtual.site)
    print(agencia_virtual.clientes)

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)



    print('------- Agencia Comum -----------------------------')
    agencia_comum = AgenciaComum(22225555, 25500000000)
    agencia_comum.verificar_caixa()
    agencia_comum.adicionar_cliente('Irmão do Lira', 10200000000, 10)
    print(agencia_comum.clientes)

    print('-------- Agencia Premium ----------------------------')
    agencia_premium = AgenciaPremium(22226666, 15200000001)
    agencia_premium.verificar_caixa()
    agencia_premium.adicionar_cliente('Lira', 15000000000, 50000000)
    print(agencia_premium.clientes)



    agencia1.caixa = 100000000
    agencia1.verificar_caixa()
    agencia1.emprestar_dinheiro(1500, 12345678912, 0.02)
    print(agencia1.emprestimos)
    agencia1.adicionar_cliente('Davi', 12345678914, 10000)
    print(agencia1.clientes)

