'''
Lambda Expression para gerar funções

Uma das aplicações de lambda expression, além da vista na aula passada, é criar
um "gerador de funções". Nesse caso, usaremos a lambda expressions dentro da 
definição de uma outra função

Exemplo:
1. Vamos criar uma função que me permita calcular o valor acrescido do imposto de
diferentes categorias (produtos, serviços, royalties, etc.)
'''
def calcular_imposto(imposto):
    return lambda preco: preco * (1 + imposto)

# produto 0.1
# produto 0.15
# produto 0.25

# Definir as funções que calculam o imposto das
# 3 categorias (produto, serviço, royalties)

calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(0.25)

# Agora vamos aplicar com um valor de nota fiscal de 100 para ver o resultado

print((calcular_preco_produto(100)))
print((calcular_preco_servico(100)))
print((calcular_preco_royalties(100)))

