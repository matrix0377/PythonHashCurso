'''
    Criar um conector ao MySQL
    
- Instalação do conector mysql-connector-python via pip
- Criar string de conexão
- Efetuar e testar a conexão ao servidor MySQL
- Executar um comando SQL via Python em um banco de dados
- Como criar e usar um objeto cursor
- Fechar cursor e conexão abertas
'''
import mysql.conector

con = mysql.connector.connect(
    host='localhost', database='db_MeusLivros', user='root', password='')

if con.is_connected():
    dbinfo = con.get_server_info()
    print("Conectado ao servidor MySQL versão", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()  # busca 1 linha
    print("Conectado ao Banco de Dados ", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")
