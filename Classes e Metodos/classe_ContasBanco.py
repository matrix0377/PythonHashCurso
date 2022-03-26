'''
Exercicio de classe e metodos
'''
from datetime import datetime
import pytz
import time
from random import randint

class ContaCorrente():
    '''
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome (str): Nome do Cliente
        cpf (str): CPF do Cliente
        agencia (int): Agência Responsável pela conta do Cliente
        num_conta (int): Número da Conta Corrente do Cliente
        saldo (float): Saldo disponível na conta do Cliente
        limite (float): Limite de Cheque Especial daquele cliente
        transacoes (str): Histórico de Transações do Cliente
        tipo (str:list): tipo de transação [Saque, Deposito, Transferencia]
    '''

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self.__saldo = 0
        self._limite = None
        self._agencia = agencia
        self._conta = num_conta
        self._transacoes = []
        self.tipo = ['Saque', 'Depósito', 'Transferência']
        self.cartoes = []

    def consultar__saldo(self):
        '''
            Exibe o saldo atual da conta do cliente
            Não há parâmetros necessários.
        '''
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.__saldo))

    def depositar_dinheiro(self, valor):
        self.__saldo += valor
        self._transacoes.append(
            (self.tipo[1], valor, self.__saldo, ContaCorrente._data_hora()))
        self.consultar__saldo()

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def consultar_limite_chequeespecial(self):
        print('Seu limite de Cheque Especial é de R$ {:,.2f}'.format(
            self._limite_conta()))

    def sacar_dinheiro(self, valor):
        if self.__saldo - valor < self._limite_conta():
            print('Você não tem saldo sufuciente para sacar esse valor')
            self.consultar__saldo()
        else:
            self.__saldo -= valor
            self._transacoes.append(
                (self.tipo[0], -valor, self.__saldo, ContaCorrente._data_hora()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('==' * 28)
        print('Tipo_Transação, Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        if self.__saldo - valor < self._limite_conta():
            print('Você não tem saldo sufuciente para sacar esse valor')
            self.consultar__saldo()
        else:
            self.__saldo -= valor
            self._transacoes.append(
                (self.tipo[2], -valor, self.__saldo, ContaCorrente._data_hora()))
            conta_destino.__saldo += valor
            conta_destino._transacoes.append(
                (self.tipo[2], valor, conta_destino.__saldo, ContaCorrente._data_hora()))


class CartaoCredito:
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)



# programa
conta_davi = ContaCorrente("Davi", "111.222.333-45", "3025", "505257")
conta_davi.consultar__saldo()

conta_maeDavi = ContaCorrente("Nilva", "222.333.444-55", "5555", "656565")

#depositar um dinheirinho na conta:
deposito = 10000
print('\n --- >>> Depositando R$ {:,.2f}\n'.format(deposito))
conta_davi.depositar_dinheiro(deposito)
print('-----------------')

# # Sacando um dinheirinho na conta:
# saque = 100000
# print('\n --- >>>  Sacando R$ {:,.2f}\n'.format(saque))
# conta_davi.sacar_dinheiro(saque)
# # conta_davi.consultar__saldo()
# print('-----------------')


# Transferir dinheiro pra mae
# transferencia = 1500
# print('\n --- >>>  Transferindo R$ {:,.2f}\n'.format(transferencia))
# conta_davi.transferir(transferencia, conta_maeDavi)
# conta_davi.consultar__saldo()
# print('-----------------')

# Mostrando Saldo e Limite de Conta
# print(' --- >>> Mostrando saldo Final: ')
# conta_davi.consultar__saldo()
# conta_davi.consultar_limite_chequeespecial()

# print('==' * 28)
# print(conta_davi.transacoes)
# conta_davi.consultar_historico_transacoes()
# print('==' * 28)
# print('\n')


# print('consultar Historico maeDavi\n')
# conta_maeDavi.consultar_historico_transacoes()
# print('==' * 28)
# print('\n')

# Documentação da Classe
# help(ContaCorrente)

cartao_davi = CartaoCredito('Davi', conta_davi)

print('==' * 25)
print('Cartao: {}'.format(cartao_davi.numero))
print('Validade: {}  PIN: {}'.format(cartao_davi.validade, cartao_davi.cod_seguranca))
print('Limite do cartão: ', cartao_davi.limite)
print('==' * 25)
