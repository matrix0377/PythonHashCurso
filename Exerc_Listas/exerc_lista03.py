'''
Exercício com listas - consulta produtos na lista
i = lista.index('item')
'''
produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

'''
i = produtos.index('geladeira')
qtde_estoque = estoque[i]
print('quantidade de estoque da geladeira é de : {}'.format(qtde_estoque))
'''
print('\n')
print('-=' * 20)
produto = input('Insira o nome do produto em letra minúscula: ')
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque'.format(qtde_estoque, produto))
else:
    print('{} não existe no estoque'.format(produto))
    print('-=' * 20)

