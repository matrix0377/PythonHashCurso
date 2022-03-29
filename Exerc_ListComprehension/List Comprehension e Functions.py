'''
    List Comprehension e Functions
'''
produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos.sort()
print('----- Utilizando sort -------------\n')
print(produtos)

print('\n----- Utilizando sort -------------\n')
# sorted cria uma lista nova, precisa de outra variável para atribuir
lista_nova = sorted(produtos)
print(lista_nova)

print('\n----- Utilizando sort -------------\n')
# ordenando na ordem e deixando os texto da forma que estavam escritas
produtos.sort(key=str.casefold)
print(produtos)

print('\n----- Ordenando um dicionário por valor -------------\n')
vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

def segundo_item(tupla):
    return tupla[1]
lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
print(dict(lista_vendas))

