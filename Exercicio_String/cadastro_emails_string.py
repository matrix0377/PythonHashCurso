'''
Cadastro de e-mails - tratamentos
'''
print('\n')
print('-=' * 20)

nome = input('Digite seu nome: ')
email = input('Digite o seu e-mail: ')

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluído!')
    else:
        print('E-mail inválido!')
else:
    print('Digite seu nome e e-mail corretamente')
