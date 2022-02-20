'''
Function para Cálculo de Carga Tributária
'''

preco = 1500
custo = 400
lucro = 800

# funcao
def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco



# Aplique sua function nos valores fornecidos para ver se
# ela está funcionando corretamente para
print('A carga tributária foi de {:.1%}'.format(carga_tributaria(preco, custo, lucro)))


