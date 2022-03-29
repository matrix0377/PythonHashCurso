'''
    Exercícios de map e function
    lista = list(map(função, iterable_original))
'''


def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto


produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', 'BSA151', 'BEB23']

print('\n')
print('---- Função -----------\n')
for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)
print(produtos)

print('\n')
print('---- List Comprehensions -----------\n')
produtos = list(map(padronizar_texto, produtos))
print(produtos)
