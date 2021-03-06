'''
em "Server=IP, ou Hostname

Criar um cadastro de produtos e salvar no Banco de Dados
Database: PythonSQL
Tabela: Vendas (exemplo do vídeo)
->>>>> Como Integrar Python e SQL - Passo a Passo com Exemplo Prático
https://www.youtube.com/watch?v=Mdg1D-Kdmrw

'''
from datetime import datetime
import pytz
import time
import pyodbc
import datetime
import time

# Cores
cor = {'limpa': '\033[m',
       'azul': '\033[34m',
       'amarelo': '\033[33m',
       'verde': '\033[32m',
       'lilas': '\033[35m',
       'branco': '\033[37m',
       'vermelho': '\033[31m',
       'cian': '\033[36m',
       'pretoevermelho': '\033[7;31;41[m',
       'pretoebranco': '\033[7;30m'
       }

arq = str(
    "Cadastra_log_" + (datetime.datetime.now().strftime('%d-%m-%Y_%Hh%Mmin')) + ".txt")
print(cor['vermelho'], arq, cor['limpa'])


# desenvolver o código de

class Compra:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, id, cliente, produto, data, preco, qtde):
        self.id = id
        self.cliente = cliente
        self.produto = produto
        self.data = data
        self.preco = preco
        self.qtde = qtde
        self.historico = []
        self.incluir = []

    def gravar_sql_Server(self, id, cliente, produto, data, preco, qtde):

        import pyodbc
        # gravando no SQL_Server - Local
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=ANAKIN;"
            "Database=PythonSQL;"
        )

        conexao = pyodbc.connect(dados_conexao)
        print("Conexão Bem Sucedida")

        cursor = conexao.cursor()

        # id = 4
        # cliente = "Tania Ferraz"
        # produto = "Ipad"
        # data = "10/04/2022"
        # preco = 7000
        # qtde = 1

        comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
        VALUES
            ({self.id}, '{self.cliente}', '{self.produto}', '{self.data}', {self.preco}, {self.qtde})"""

        # ====>>>> Inserir item a item
        # comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
        # VALUES
        #     (2, 'Alon', 'Iphone', '10/04/2022', 6000, 1)"""

        cursor.execute(comando)
        cursor.commit()

    # def cadastrar_compra(self, id=100, cliente='a', produto='P', data='', preco=1, qtde=1):
    #     # 3 -Fazer um 'for' e gravar no BD
    #     incluir = []

    #     # Contruir Tela
    #     print('-=' * 25, '\n')
    #     compra = Compra(id, cliente, produto, data, preco, qtde)

    #     self.id = input(int("[ID]: "))
    #     self.cliente = input("[Cliente]: ")
    #     self.produto = input("[Produto]: ")
    #     self.data = input("[Data: ]")
    #     self.preco = input(float("[Preço: ]"))
    #     self.qtde = input(int("[Quantidade: ]"))
    #     compra = Compra(id, cliente, produto, data, preco, qtde)
    #     incluir.append(self, id, cliente, produto, data, preco, qtde)
    #     print('-=' * 25, '\n')
    #     print(incluir)
    #     print("Cadastro ok")

    def atualizar_compra():

        pass

    def deletar_compra():

        pass

    def historico_compra(self):
        print('====== Histórico_Compras Classe  ==========\n')
        # for k, v in enumerate(self.historico):
        #     print(f"{k}: {v} \n")
        # listar uma linha por vez...<<<<-----
        # print("\n-----print historico_compra ------------\n")
        
        # for k, v in range(len(key_list)):
        #     print('*****************************')
        #     print("{k} : {v}")
        # print('\n')
        print('\n')
        mytuple = tuple(self.historico)
        for i in self.historico:
            print(i)
            
            
        print("\nNúmero de elementos: ", len(mytuple))
        
        


def criar_compra():

    import pyodbc

    # Contruir Tela
    # Inserir um while para cadastrar
    lista_reg=[]
    lista1 = []
    global key_list
    opcao_cad='s'
    while opcao_cad == "S" or opcao_cad == "s":
        if opcao_cad == 's' or opcao_cad == 'S':
            print('-=' * 25, '\n')
            incluir=[]
            # incluir registros
            id=input("[ID:] ")
            cliente=input("[Cliente]: ")
            produto=input("[Produto]: ")
            data=(datetime.datetime.now().strftime('%d-%m-%Y'))
            preco=input("[Preço]: ")
            qtde=input("[Quantidade]: ")
            compra=Compra(id, cliente, produto, data, preco, qtde)
            incluir.append(
                [{id}, {cliente}, {produto}, {data}, {preco}, {qtde}])
            lista_reg.append(incluir)
            key_list = ['id', 'cliente', 'produto', 'data', 'preco', 'qtde']
            tupla1 = (id, cliente, produto, data, preco, qtde)
            lista1.append(tupla1)
                       
            # Gravando no Banco de Dados
            print('Aguarde gravando...')
            compra.gravar_sql_Server(compra.id, compra.cliente,
                                     compra.produto, compra.data, compra.preco, compra.qtde)
            # incluir compra no historico da classe
            compra.historico.append(lista_reg)
            
            # acrescentar no log
            arquivo.write("ID:      ")
            arquivo.write(compra.id)
            arquivo.write('  ' + "\n")
            arquivo.write("Cliente: ")
            arquivo.write(compra.cliente)
            arquivo.write('  ' + "\n")
            arquivo.write("Produto: ")
            arquivo.write(compra.produto)
            arquivo.write('  ' + "\n")
            arquivo.write("Data :   ")
            arquivo.write(compra.data)
            arquivo.write('  ' + "\n")
            arquivo.write("Qtde :   ")
            arquivo.write(compra.qtde)
            arquivo.write('\n')
            arquivo.write("==" * 25)
            arquivo.write('\n')

            opcao_cad=input('\n>>>>>>>>>> Quer fazer outro cadastro? [S/N] ')
        elif opcao_cad == 'N' or opcao_cad == 'n':
            break
        else:
            print('Opção inválida. Tente novamente!')
            print('=-=' * 15)
    print('Fim do programa!')
    print('---print lista1 - criar_compra ---------')
    print(lista1)

    # Gravando....
    # gravando no SQL_Server - Local
    # dados_conexao = (
    #     "Driver={SQL Server};"
    #     "Server=ANAKIN;"
    #     "Database=PythonSQL;"
    # )
    # conexao = pyodbc.connect(dados_conexao)
    # print("Conexão Bem Sucedida")
    # cursor = conexao.cursor()

    # comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
    #     VALUES
    #         ({id}, '{cliente}', '{produto}', '{data}', {preco}, {qtde})"""
    # cursor.execute(comando)
    # cursor.commit()
    # historico.append(incluir)
    print('-=' * 25, '\n')
    print("\n----- print lista_reg total -------------\n")
    print(lista_reg)

    print("-=" * 15)
    print('====== Histórico Compras Classe  ==========\n')
    compra.historico_compra()
    print("\nCadastro ok")
    print("\n")


    print("\n-----print Classe compra ------------\n")
    print("ID:      ", compra.id)
    print("Cliente: ", compra.cliente)
    print("Produto: ", compra.produto)
    print("Data :   ", compra.data)
    print("Qtde :   ", compra.qtde)
    print("-=" * 15)
    print("\n")
    # print for list comprehension
    #  print('---print dict_from_lista - criar_compra ---------')
    


# Menu
# programa principal
arquivo=open(arq, "a", encoding="utf8")
opcao=0
while opcao != 5:
    print('''
          [ 1 ] Cadastrar Compra
          [ 2 ] Atualizar Compra
          [ 3 ] Deletar Compra
          [ 4 ] Listar Compra do Dia
          [ 5 ] Sair do programa
          ''')
    arquivo.write('  ' + "\n")
    opcao=int(input('>>>>>>>>>> Qual é a sua opção?  '))
    if opcao == 1:
        print('\nopção 1 - Cadastrar Compra\n')
        arquivo.write('>>>>>>>>>> opção 1 - Cadastrar Compra' + '\n')
        arquivo.write('  ' + "\n")
        criar_compra()

    elif opcao == 2:
        print('\nopção 2 - Atualizar Compra\n')
        arquivo.write('>>>>>>>>>> opção 2 - Atualizar Compra' + '\n')
        arquivo.write('  ' + "\n")
        atualizar_compra()
    elif opcao == 3:
        print('\nopção 3 - Deletar Compra\n')
        arquivo.write('>>>>>>>>>> opção 5 - Deletar Compra' + '\n')
        arquivo.write('  ' + "\n")
        deletar_compra()
    elif opcao == 4:
        print('\nopção 4 - Listar Compras do Dia\n')
        arquivo.write('>>>>>>>>>> opção 4 - Sair do Programa' + '\n')
        arquivo.write('  ' + "\n")
    elif opcao == 5:
        print('\nopção 5 - Sair do Programa\n')
        arquivo.write('>>>>>>>>>> opção 5 - Sair do Programa' + '\n')
        arquivo.write('  ' + "\n")
        break
    else:
        print('\nOpção inválida. Tente novamente!\n')
        arquivo.write('Opção inválida. Tente novamente!' + "\n")
        arquivo.write('  ' + "\n")
        print('=-=' * 15)
        arquivo.write('=-=' * 15)
        arquivo.write('  ' + "\n")
else:
    print('Fim do programa!\n')
    arquivo.write('Fim do programa!' + "\n")
    arquivo.write('  ' + "\n")


arquivo.close()

# criando as opções
# insert_bd = {}
# update_bd = {}
# delete_bd = {}


# status do teste - Funcionou OK

