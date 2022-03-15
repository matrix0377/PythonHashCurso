'''
digamos que a gente esteja analisando a meta de vendas de vários
funcionários de uma empresa. A meta de venda é de 1000 reias em
1 dia. Temos uma lista com as vendas de todos os funcionários e
quero calcular qual o % de pessoas que bateram a meta.

'''
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000

qtde_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        qtde_bateu_meta += 1
        
qtde_funcionarios = len(vendas)

print('\n O percentual de pessoas que bateram a meta foi de {:.1%}'.format(qtde_bateu_meta / qtde_funcionarios))
