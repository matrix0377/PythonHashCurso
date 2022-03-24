'''
Exercicio de classe e metodos
'''
from datetime import datetime
import pytz


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

    def consultar__saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.__saldo))
        pass

    def depositar_dinheiro(self, valor):
        self.__saldo += valor
        self.transacoes.append((valor, self.__saldo, ContaCorrente._data_hora()))
        pass

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.__saldo - valor < self._limite_conta():
            print('Você não tem saldo sufuciente para sacar esse valor')
            self.consultar__saldo()
        else:
            self.__saldo -= valor
            self.transacoes.append((valor, self.__saldo, ContaCorrente._data_hora()))
        pass

    def consultar_historico_transacoes(self, transacoes):
        print('Histórico de Transações:')
        for transacao in transacoes:
            print(transacao)
        pass    

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        self.transacoes.append((-valor, self.__saldo, ContaCorrente._data_hora()))
        conta_destino.__saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.__saldo, ContaCorrente._data_hora()))


# programa
conta_davi = ContaCorrente("Davi", "111.222.333-45", "3025", "505257")
conta_davi.consultar__saldo()

conta_maeDavi = ContaCorrente("Nilva", "222.333.444-55", "5555", "656565")

# depositar um dinheirinho na conta:
conta_davi.depositar_dinheiro(10000)
conta_davi.consultar__saldo()

# Sacando um dinheirinho na conta:
conta_davi.sacar_dinheiro(100000)
conta_davi.consultar__saldo()
print('-----------------')
conta_davi.consultar_historico_transacoes()

# Transferir dinheiro pra mae
conta_davi.transferir(1000, conta_maeDavi)
conta_davi.consultar__saldo()

# agora 02:32
# Parei na página 485 da apostila...continuar em 23/03/2022
