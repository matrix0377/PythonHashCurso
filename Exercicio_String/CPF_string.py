'''
Cadastro de CPF
'''
print('\n')
print('-=' * 20)
cpf = input('Insira seu CPF (digite apenas números) : ')

if len(cpf) == 11 and cpf.isnumeric():
    print('-=' * 20)
    print('\n')
    print(' --->>> CPF : ', cpf)
    print('\n')
    print('-=' * 20)
else:
    print('Digite seu CPF corretamente e digite apenas números')
    
