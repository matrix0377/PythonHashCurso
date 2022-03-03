'''
Criando a função cor
'''

def cores(*args):
    cor = {'limpa':'\033[m',
            'azul':'\033[34m',
            'amarelo':'\033[33m',
            'verde':'\033[32m',
            'lilas':'\033[35m',
            'cinza':'\033[37m',
            'vermelho':'\033[31m',
            'cian': '\033[36m',
            'branco': '\033[30m',
            'pretoevermelho':'\033[7;31;41[m',
            'pretoebranco': '\033[7;30m'}
    return cor[value]
    
                                  

                          
nome = 'Davi'

print("Olá! Muito prazer em conhecer, {}{}{}!!!".format(cores(['amarelo']), nome, cores(['limpa'])))

