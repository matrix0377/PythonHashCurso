'''
Cadastro de CPF - tratamentos
'''
print('\n')
print('-=' * 20)
cpf = input('Insira seu CPF : ')

# tratar o cpf

# tirar espaços no inínio e no finalizar
cpf = cpf.strip()
# tirar os "." (pontos)
cpf = cpf.replace('.', '')
# tirar os traços (" - ")
cpf = cpf.replace('-', '')


if len(cpf) == 11 and cpf.isnumeric():
    print('-=' * 20)
    print('\n')
    print(' --->>> CPF : ', cpf)
    print('\n')
    print('-=' * 20)
else:
    print('Digite seu CPF corretamente e digite apenas números')
