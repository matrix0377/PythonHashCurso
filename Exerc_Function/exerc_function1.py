'''
    def nome_funcao():
        faça alguma coisada
        faça outra coisa
        return valor_final
        
'''

def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar ')
    produto = produto.casefold()
    produto = produto.strip()
    print('==' * 25)
    print('Produto {} cadastrado com sucesso'.format(produto))
    print('==' * 25)


for i in range(3):
    cadastrar_produto()
    
