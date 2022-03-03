import time

vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453,
          386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca',
              'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

i = 0
indice = 0
n = 0
opcao = 0
while opcao < 3:
    print('''
          [ 1 ] Listar as Vendas
          [ 2 ] Verificar quem bateu as metas
          [ 3 ] Sair do programa
          ''')
    print('\n')
    opcao = int(input(" --->>> Escolha a opção: "))
    if opcao == 1:
        indice = 0
        print('\nopção 1 - Listar as Vendas\n')
        print('  ' + "\n")
        print('  ' + "\n")
        print('Vendedor     |      Venda')
        print('-------------------------')
        while vendas[indice] > meta:
            print('{:<12} | {:>10}'.format(
                vendedores[indice], vendas[indice]))
            indice = indice + 1
    elif opcao == 2:
        print('\nopção 2 - Verificar quem bateu as metas\n')
        while vendas[i] > meta:
            print('{} bateu a meta. Vendas: {}'.format(
                vendedores[i], vendas[i]))
            i += 1
            n += 1
            time.sleep(2)
        print(" --->> {} vendedores bateram a Meta".format(n))
    elif opcao == 0:
        print('\nTente novamente....escolha as opções de 1 a 3!!!\n')
    elif opcao == 3:
        print('\nopção 3 - Sair do Programa\n')
        print('Saindo!...\n')
        break
else:
    print('Fim do programa!\n')
