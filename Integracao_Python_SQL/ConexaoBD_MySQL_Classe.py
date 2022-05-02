'''
Banco de Dados MySQL usando classe
'''

import mysql.connector

class ConexaoBD():
    def __init__(self, host = "localhost", user = "root", pwd = "", db = "dbestoque"):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
    
    def conecta(self):
        self.con = mysql.connector.connect(host = self.host,
                                           user = self.user, 
                                           password = self.pwd,
                                           database = self.db)
        self.cursor = self.con.cursor()
    
    def desconecta(self):
        self.con.close()
    
    def executa_DQL(self, sql): # executa comandos SQL
        self.conecta()
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.desconecta()
        return res
    
    def executa_DML(self, sql): # Salva as alterações no BD
        self.conecta()
        self.cursor.execute(sql)
        self.con.commit()
        self.desconecta()
 
 
 
 # c = ConexaoBD()
 # c.conecta()  -- faz a conexão ao Banco de Dados
 # c.executa_DQL("SELECT * FROM tbSetor")       
    
    
    
