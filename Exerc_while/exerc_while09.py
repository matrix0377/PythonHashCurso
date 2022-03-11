vendas = []

while True:
    produto = input('Qual o produto? ')
    if not produto:
        break
    qtde = int(input('Qual a quantidade? '))
    vendas.append([produto, qtde])
print(vendas)

