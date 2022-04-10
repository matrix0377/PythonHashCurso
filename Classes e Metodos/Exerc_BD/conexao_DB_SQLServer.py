'''
Conexão de Banco de Dados
'''
import pyodbc
import pandas as pd



dados_conexao = ("Driver={SQL Server Native Client 11.0};"
                 "Server=W11V1-SQLSERVER;"
                 "Database=ContosoRetailDW;"
                 #"UID=markv;"
                 #"PWD=2510;"
                 "Trusted_connection=yes;"
                 )
                 

conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida!')


cursor = conexao.cursor()

produtos_df = pd.read_sql('SELECT * FROM ContosoRetailDW.dbo.DimProduct', conexao)
display(produtos_df)






