'''
Criando a função cor
'''

from turtle import clear


def cores(**kwargs):
    for key, value in kwargs:
        return value
        
    cor = {'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'verde': '\033[32m',
    'lilas': '\033[35m',
    'cinza': '\033[37m',
    'vermelho': '\033[31m',
    'cian': '\033[36m',
    'branco': '\033[30m',
    'pretoevermelho': '\033[7;31;41[m',
    'pretoebranco': '\033[7;30m'}
        
        
        


nome = 'Davi'
idade = 44
# cores('verde')

print("Olá! Muito prazer em conhecer, {} {} {}!!!".format(cores(['verde'])), nome, cores(['limpa']))

# print("Olá! Muito prazer em conhecer, {} {} {}!!!".format(cores(cor['verde'])), nome, cores(cor['limpa']))
#print("Olá! Muito prazer em conhecer, {} {} : {} {}!!!".format(cor['lilas'], nome, idade, cor['limpa']))
#print("Olá! Muito prazer em conhecer, {} {} : {} {}!!!".format(cor['cian'], nome, idade, cor['limpa']))
# as cores fora da função funcionam bem!
# criar a função de cores para
# print(cores(cor['lilas']))
# print(cores(cor['verde']))
# print(kwargs)


