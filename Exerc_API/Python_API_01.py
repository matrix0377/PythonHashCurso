'''
API cotação de Moedas
'''

import requests
import os
import json


os.system('cls')

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

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')

cotacoes_dic = cotacoes.json()
#print(cotacoes_dic)

print(cor['verde'], '\nQual  a última cotação do Dólar, Euro e BitCoin?\n', cor['limpa'])

print('\nDólar: {}'.format(cotacoes_dic['USD']['bid']))
print('Euro: {}'.format(cotacoes_dic['EUR']['bid']))
print('Bitcoin: {}'.format(cotacoes_dic['BTC']['bid']))
#print('\n')

print(cor['verde'], '\n Cotação dos últimos 30 dias do Dólar\n', cor['limpa'])

cotacoes_dolar30d = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dolar_dic = cotacoes_dolar30d.json()
#print(cotacoes_dolar_dic[0]) ver o primeiro item
# usar um list comprehensions, se quiser fazer alguma conta pode transformar em float
lista_cotacoes_dolar = [float(item['bid']) for item in cotacoes_dolar_dic]
#lista_cotacoes_dolar = [item['bid'] for item in cotacoes_dolar_dic]
print(lista_cotacoes_dolar)

print(cor['verde'], '\n Pegar as cotações do BitCoin de Jan/20 a Out/20\n', cor['limpa'])


