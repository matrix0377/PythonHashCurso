'''
    def nome_funcao():
        return valor_final
        
'''
def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar ')
    produto = produto.casefold()
    produto = produto.strip()
    return produto    
    

produto = cadastrar_produto()
print('==' * 25)
print('Produto {} cadastrado com sucesso'.format(produto))
print('==' * 25)

