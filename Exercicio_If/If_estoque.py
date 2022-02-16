estoque_alimentos = 50
estoque_bebidas = 75
estoque_limpeza = 30
pte = ('Produto tem Estoque!')

produto = input('Qual é o produto? ')
categoria = input('Qual a categoria do produto? ')
qtde = int(input('Qual a quantidade atual do produto? '))

if produto and categoria and qtde:
    qtde = int(qtde)
    if categoria == 'bebidas':
        if qtde < 75:
            print('solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
        else:
            print(pte)
    elif not categoria == 'limpeza':
        if qtde < 30:
            print('solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(produto, qtde))
        else:
            print(pte)
    else:
        if qtde <50:
            print('solicitar {} à equipe de compras, temos apenas {} unidades em estoque'.format(
                produto, qtde))
        else:
            print(' ------->>>  ' + pte)
else:
    print('Preencha todas as informações')



