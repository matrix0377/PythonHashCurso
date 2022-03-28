from ContasBanco import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual


# programa
conta_davi = ContaCorrente("Davi", "111.222.333-45", "3025", "505257")
conta_davi.consultar__saldo()

conta_nilva = ContaCorrente("Nilva", "222.333.444-55", "5555", "656565")
conta_drica = ContaCorrente("Adriana", "555.666.777-89", "5030", "757575")

# depositar um dinheirinho na conta:
deposito = 25000
print('\n --- >>> Depositando R$ {:,.2f}\n'.format(deposito))
conta_davi.depositar_dinheiro(deposito)
conta_drica.depositar_dinheiro(deposito)
conta_nilva.depositar_dinheiro(deposito)
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


print('consultar Historico de {}'.format(conta_nilva._nome))
conta_nilva.consultar_historico_transacoes()
print('==' * 28)


print('\n')
print('consultar Historico de {}'.format(conta_drica._nome))
conta_drica.consultar_historico_transacoes()
print('==' * 28)
print('\n')

# Documentação da Classe
# help(ContaCorrente)

cartao_davi = CartaoCredito('Davi', conta_davi)

print('==' * 11 + ' Cartão de Crédito  ========')
print('==' * 25)
print('Titular: {}'.format(cartao_davi.titular))
print('Cartao: {}'.format(cartao_davi.numero))
print('Validade: {}  PIN: {}'.format(
    cartao_davi.validade, cartao_davi.cod_seguranca))
print('Limite do cartão: R$ {:,.2f}'.format(cartao_davi.limite))
print('==' * 25)
print('\n')

cartao_drica = CartaoCredito('Adriana', conta_drica)

print('==' * 11 + ' Cartão de Crédito  ========')
print('==' * 25)
print('Titular: {}'.format(cartao_drica.titular))
print('Cartao: {}'.format(cartao_drica.numero))
print('Validade: {}  PIN: {}'.format(
    cartao_drica.validade, cartao_drica.cod_seguranca))
print('Limite do cartão: R$ {:,.2f}'.format(cartao_drica.limite))
print('==' * 25)

# getter e setter
print('=======----------->>> Getter e Setter')
print('==' * 25)
cartao_davi.senha = '12'
print(cartao_davi.senha)

conta_davi.nome = "Davi Augusto"
print(conta_davi.nome)
print('Nova Senha:')
cartao_davi.senha = '2345'
print(cartao_davi.senha)
print('---------------\n')

print('--------- Todos Atributos ---------------')
print(conta_davi.__dict__)
print(cartao_davi.__dict__)

print('--------- Agencia Premium Especial ---------------')
agencia_premium_especial = AgenciaPremium(22221111, 15888888888)
print(agencia_premium_especial.telefone)
print(agencia_premium_especial.caixa)
