'''
Exercício com "for"

Imagine que você está construindo uma automação para enviar
todo dia por e-mail um resumo de produção de uam fábrica.

Contrua um código que exiba a quantidade produzida de cada
produto nesse 'e-mail'

'''
import time

produtos = ['coca', 'pepsi', 'guaraná', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

tamanho = len(produtos)
print('')
for i in range(tamanho):
    print(' {} unidades produzidas de {}\n'.format(producao[i], produtos[i]))
    

    


