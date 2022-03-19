'''
Criação de hospedes
'''

qtde_pessoas = int(input('Quantas pessoas terão no quarto? >>> '))
quarto = []

for i in range(qtde_pessoas):
    nome = input('Qual o nome? ')
    cpf = input('Qual o cpf? ')
    hospede = [nome, 'cpf: {}'.format(cpf)]
    quarto.append(hospede)

print(quarto)


for item in quarto:
    print('Hospede {}  CPF: {}'.format(item[0], item[1]))
    

