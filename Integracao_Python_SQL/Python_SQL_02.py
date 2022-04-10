'''
    Integração Python e SQL
    29/03/2022
    
dados_conexao = ("Driver={SQL Server};"
                "Server=SeuServidor;"
                Database=NomeBaseDeDados;")
          
Se estivéssemos usando outro sistema de banco de dados, nosso driver mudaria. Para saber em outros casos, execute:
pyodbc.drivers() -> caso não encontre seu driver ali, basta buscar no google por "driver MeuBancoDeDados for pyodbc" e baixar 
  
caso precisasse de login e senha:
#dados_conexao = ("Driver={SQL Server Native Client 11.0};"
#            "Server=UKXXX00123,45600;"
#            "Database=DB01;"
#            "UID=Login;"
#            "PWD=Senha;")
 
 
 testando purepyodbc 
 Por exemplo, uma conexão pode ser assim:

connect(dsn='myhost:MYDB', user='guido', password='234$', database='ContosoRetailDW')
'''

import pyodbc


dados_conexao = ("Driver={SQL Server};"
                 "Server=W11V1-SQLSERVER;"
                 "Database=ContosoRetailDW;"
                 "UID=markv;"
                 "PWD=2510;"
                 "Trusted_connection=yes;"
                 )
                 

conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida!')
