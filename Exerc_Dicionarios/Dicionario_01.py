'''
dicionario = {chave:valor, chave:valor,...}
'''
from turtle import clear


cor = {'limpa': '\033[m',
       'azul': '\033[34m',
       'amarelo': '\033[33m',
       'verde': '\033[32m',
       'lilas': '\033[35m',
       'branco': '\033[37m',
       'vermelho': '\033[31m',
       'cian': '\033[36m',
       'pretoevermelho': '\033[7;31;41[m',
       'pretoebranco': '\033[7;30m'}


vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(cor['lilas'], vendas_mes, cor['limpa'])
vendas_mes.clear()
print(cor['amarelo'], vendas_mes, cor['limpa'])
