''' Requests officially supports Python 2.7 & 3.6'''

import requests
import os

os.system('cls')


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro:  {cotacao_euro}
    BTC:   {cotacao_btc}'''

    print(texto, '\n')

pegar_cotacoes()


