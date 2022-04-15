'''
teste de Tuplas e Dicionário
'''

import pyodbc

# Contruir Tela
# Inserir um while para cadastrar
lista_reg = []
lista1 = []
global key_list
opcao_cad = 's'
while opcao_cad == "S" or opcao_cad == "s":
    if opcao_cad == 's' or opcao_cad == 'S':
        print('-=' * 25, '\n')
        incluir = []
        # incluir registros
        id = input("[ID:] ")
        cliente = input("[Cliente]: ")
        produto = input("[Produto]: ")
        qtde = input("[Quantidade]: ")
        incluir.append((id, cliente, produto, qtde))
        lista_reg.append(incluir)
        key_list = ('id', 'cliente', 'produto', 'qtde')
        tupla1 = (id, cliente, produto, qtde)
        
        lista1.append(tupla1)

        # Gravando no Banco de Dados
        print('Aguarde gravando...')
                
        opcao_cad = input('\n>>>>>>>>>> Quer fazer outro cadastro? [S/N] ')
    elif opcao_cad == 'N' or opcao_cad == 'n':
        break
    else:
        print('Opção inválida. Tente novamente!')
        print('=-=' * 15)
print('Fim do programa!')

    

print('---print lista1 - criar_compra ---------')
print(lista1)
print('\n')

print('---print lista_reg  ---------')
print(lista_reg)
print('\n')

print('---print For lista_reg  ---------') # Boaaaa!
for cont in range(0, len(lista_reg)):
    print(lista_reg[cont])


print('\n---Transformar em Tupla lista_reg  ---------\n') # melhor!!!
tupla_reg = tuple(lista_reg)
for cont in range(0, len(tupla_reg)):
    print(f'Registro {cont}: {lista_reg[cont]}')
    
print('---print tupla1  ---------')
for cont in range(0, len(tupla1)):
    print(tupla1[cont])
    
print('\n')
