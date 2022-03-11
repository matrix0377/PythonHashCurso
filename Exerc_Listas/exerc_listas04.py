'''
Adicionar e Remover itens de uma Lista

Adicionar:
    lista.append(item)
  
  Remover:
    lista.remove(item)
    item_removido = lista.pop(indice)
'''
produtos = ['apple tv', 'mac', 'iphone x', 'Ipad', 'apple watch', 'airpods']

# adicionar o iphone 11,
produtos.append('iphone 11')
print(produtos)

# remover iphone x
produtos.remove('iphone x')
# ou 
# item_removido = produtos.pop(2)
print(produtos)

tamanho = len(produtos)
print('Temos {} produtos'.format(tamanho))



