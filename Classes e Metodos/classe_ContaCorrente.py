'''
Exercicio de classe e metodos
'''
from datetime import datetime
import pytz
import time


class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self.cpf = cpf
        self.__saldo = 0
        self.limite = None
        self.agencia = agencia
        self.conta = num_conta
        self.transacoes = []
        self.tipo = None

    def consultar__saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.__saldo))

    def depositar_dinheiro(self, valor, tipo='Deposito'):
        self.__saldo += valor
        self.transacoes.append(
            (tipo, valor, self.__saldo, ContaCorrente._data_hora()))
        self.consultar__saldo()

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def consultar_limite_chequeespecial(self):
        print('Seu limite de Cheque Especial é de R$ {:,.2f}'.format(
            self._limite_conta()))

    def sacar_dinheiro(self, valor, tipo='Saque'):
        if self.__saldo - valor < self._limite_conta():
            print('Você não tem saldo sufuciente para sacar esse valor')
            self.consultar__saldo()
        else:
            self.__saldo -= valor
            self.transacoes.append(
                (tipo, -valor, self.__saldo, ContaCorrente._data_hora()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('==' * 28)
        print('Tipo_Transação, Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino, tipo='Transferencia'):
        self.__saldo -= valor
        self.transacoes.append(
            (tipo, -valor, self.__saldo, ContaCorrente._data_hora()))
        conta_destino.__saldo += valor
        conta_destino.transacoes.append(
            (tipo, valor, conta_destino.__saldo, ContaCorrente._data_hora()))


# programa
conta_davi = ContaCorrente("Davi", "111.222.333-45", "3025", "505257")
conta_davi.consultar__saldo()

conta_maeDavi = ContaCorrente("Nilva", "222.333.444-55", "5555", "656565")

# depositar um dinheirinho na conta:
deposito = 10000
print('\n --- >>> Depositando R$ {:,.2f}\n'.format(deposito))
conta_davi.depositar_dinheiro(deposito)
# conta_davi.consultar__saldo()
print('-----------------')

# Sacando um dinheirinho na conta:
saque = 100000
print('\n --- >>>  Sacando R$ {:,.2f}\n'.format(saque))
conta_davi.sacar_dinheiro(saque)
# conta_davi.consultar__saldo()
print('-----------------')


# Transferir dinheiro pra mae
transferencia = 1500
print('\n --- >>>  Transferindo R$ {:,.2f}\n'.format(transferencia))
conta_davi.transferir(transferencia, conta_maeDavi)
conta_davi.consultar__saldo()
print('-----------------')

# Mostrando Saldo e Limite de Conta
print(' --- >>> Mostrando saldo Final: ')
conta_davi.consultar__saldo()
conta_davi.consultar_limite_chequeespecial()

print('==' * 28)
# print(conta_davi.transacoes)
conta_davi.consultar_historico_transacoes()
print('==' * 28)
print('\n')


print('consultar Historico maeDavi\n')
conta_maeDavi.consultar_historico_transacoes()
print('==' * 28)
print('\n')
