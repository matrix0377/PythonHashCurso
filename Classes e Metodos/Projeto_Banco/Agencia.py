'''
    Criando a classe agencia
'''


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 10000000:
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


# programa
agencia1 = Agencia(2222-3333, 20000000000, 4568)

agencia1.caixa = 100000000

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(1500, 12345678912, 0.02)
print(agencia1.emprestimos)

agencia1.adicionar_cliente('Davi', 12345678914, 10000)
print(agencia1.clientes)

