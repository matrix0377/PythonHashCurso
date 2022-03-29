'''
Lambda Expression
Usar lambda como argumento de alguma outra função, como 
map e filter
map()


filter()

Estrutura:
filter(funcao, iterable) -> retorna como resposta todos os itens do iterable
onde a função é True

'''
# queremos saber o preço de cada produto adicionando o valor
# do imposto de 30% sobre o valor do produto

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}


# Fazendo por function
print('-----        Fazendo por function               ---------------')
print('----- Calculando 30% de imposto sobre o valor  ---------------\n')
def calcular_preco(preco):
    return preco * 1.3

preco_com_imposto = list(map(calcular_preco, preco_tecnologia.values()))
print(preco_com_imposto)


print('\n----- Fazendo por Lambda ---------------\n')
preco_com_imposto2 = list(map(lambda preco: preco * 1.3, preco_tecnologia.values())) 
print(preco_com_imposto2)

# Filter() - Queremos apenas os produtos que custam acima de 2000
print('\n----- Filter - fazendo por function ---------------\n')
# print(preco_tecnologia.items())
def ehmaior2000(item):
    return item[1] > 2000

produtos_acima2000 = dict(list(filter(ehmaior2000, preco_tecnologia.items())))
print(produtos_acima2000)

print('\n----- Filter - fazendo por Lambda  ---------------\n')
produtos2_acima2000 = dict(list(filter(lambda item: item[1] > 2000 , preco_tecnologia.items())))
print(produtos2_acima2000)

