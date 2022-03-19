'''
Exercício com Tuplas
Qual foi o faturamento de IPhone no dia 20/08/2020?
Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?
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
       'pretoebranco': '\033[7;30m'
       }


vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

faturamento = 0
for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valor_unitario


# Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?

produto_mais_vendido = ''
qtde_produto_mais_vendido = 0
for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if data == '21/08/2020':
        if unidades > qtde_produto_mais_vendido:
            produto_mais_vendido = produto
            qtde_produto_mais_vendido = unidades


#data, produto, cor, capacidade, unidades, valor_unitario = vendas[0]
#faturamento = unidades * valor_unitario
print('\n')

print(
    f'O faturamento de\033[35m IPhone\033[m no dia 20/08/2020 foi de\033[35m {faturamento}\033[m')

print('\n')
print(f'Meu produto mais vendido no dia 21/08/2020 foi o\033[36m {produto_mais_vendido}\033[m com \033[36m{qtde_produto_mais_vendido} unidades\033[m')
print('\n')

