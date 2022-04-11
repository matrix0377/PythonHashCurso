'''
em "Server=IP, ou Hostname
'''

import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=ANAKIN;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")


cursor = conexao.cursor()


id = 100
cliente = "Katia Fernandes"
produto = "Ipad8"
data = "10/04/2022"
preco = 4000
quantidade = 2

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

# Inserir item a item
# comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
# VALUES
#     (2, 'Alon', 'Iphone', '10/04/2022', 6000, 1)"""


cursor.execute(comando)
cursor.commit()


# itens numericos não precisam de aspas
# status do teste - Funcionou OK
