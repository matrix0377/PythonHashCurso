'''
Lambda Expression
As lambdas expressions são funções anônimas (sem nome mesmo)
que tem 1 linha de código e são atribuidas a uma variável, como
se a variável virasse uma função.add()

Cria uma função só para isso.add()

Estrutura:

minha_funcao = lambda parametro: expressão
'''


print('\n----- Função Normal 1  ---------------\n')
def minha_funcao(num):
    return num * 2
print(minha_funcao(5))


print('\n----- Função Lambda 1 ---------------\n')
minha_funcao2 = lambda num: num * 2 
print(minha_funcao2(5))


print('\n----- Função Normal 2 ---------------\n')
imposto = 0.3
def preco_imposto(preco):
    return preco * (1 + 0.3)
print(preco_imposto(100))

print('\n----- Função Lambda 2 ---------------\n')
preco_imposto2 = lambda preco: preco * (1.0 + imposto)
print(preco_imposto2(100))

