'''
For nos dicionarios

Estrutura:

for chave in dicionario:
    faça alguma coisa

'''
vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

#demonstrando o for
for chave in vendas_tecnologia:
    print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))

print('-=' * 20, '\n')
print('Qual o total de notebooks vendidos?')
print('\n')
total_notebooks = 0 
for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_notebooks += vendas_tecnologia[chave]
print('O total de notebooks vendidos é {}'.format(total_notebooks))
print('-=' * 20)
    
