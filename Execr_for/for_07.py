'''
Uso for_continue
'''
vendas = [100, 150, 1500, 2000, 120]
vendedores = ['joão', 'Julia', 'Ana', 'José', 'Maria']

meta = 130

for venda in vendas:
    if venda < meta:
        continue
    print(venda)
    


