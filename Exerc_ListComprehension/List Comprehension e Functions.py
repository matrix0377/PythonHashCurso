'''
    List Comprehension e Functions
'''
import os
import sys
# sys.path.insert(1, '/PythonHashCurso/Cores/')
# from Cores import *

# Dicionário de cores
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

os.system('cls')

produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
print(cor['lilas'], '---------- Print Lista Original -------------',cor['limpa'], '\n')
print(produtos)

produtos.sort()
print('\n ----- Utilizando sort -------------\n')
print(produtos)

print(cor['cian'], '\n----------- Utilizando sorted -------------\n',
      cor['limpa'])
# sorted cria uma lista nova, precisa de outra variável para atribuir
lista_nova = sorted(produtos)
print(lista_nova)

print(cor['azul'], '\n----------- Utilizando sort casefold ----------------\n', cor['limpa'])
# ordenando na ordem e deixando os texto da forma que estavam escritas
produtos.sort(key=str.casefold)
print(produtos)

print(cor['amarelo'], '\n\n----->>> Ordenando um dicionário por valor ListCompreehension <<<-------------\n', cor['limpa'])
vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}
print(cor['vermelho'], '\n ---------- Original ----------------\n', cor['limpa'])
print(vendas_produtos)


def segundo_item(tupla):
    return tupla[1]
lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
print(cor['verde'], '\n ---------- dicionario ordenado por vendas ----------------\n', cor['limpa'])
print(dict(lista_vendas))
print('\n')


