'''
Exercício de Dicionário Colorido
'''
niveis_co2 = {
    'AC': [325, 405, 429, 486, 402],
    'AL': [492, 495, 310, 407, 388],
    'AP': [507, 503, 368, 338, 400],
    'AM': [429, 456, 352, 377, 363],
    'BA': [321, 508, 372, 490, 412],
    'CE': [424, 328, 425, 516, 480],
    'ES': [449, 506, 461, 337, 336],
    'GO': [425, 460, 385, 485, 460],
    'MA': [361, 310, 344, 425, 490],
    'MT': [358, 402, 425, 386, 379],
    'MS': [324, 357, 441, 405, 427],
    'MG': [345, 367, 391, 427, 516],
    'PA': [479, 514, 392, 493, 329],
    'PB': [418, 499, 317, 302, 476],
    'PR': [420, 508, 419, 396, 327],
    'PE': [404, 444, 495, 320, 343],
    'PI': [513, 513, 304, 377, 475],
    'RJ': [502, 481, 492, 502, 506],
    'RN': [446, 437, 519, 356, 317],
    'RS': [427, 518, 459, 317, 321],
    'RO': [517, 466, 512, 326, 458],
    'RR': [466, 495, 469, 495, 310],
    'SC': [495, 436, 382, 483, 479],
    'SP': [495, 407, 362, 389, 317],
    'SE': [508, 351, 334, 389, 418],
    'TO': [339, 490, 304, 488, 419],
    'DF': [376, 516, 320, 310, 518],
}


# for estado in niveis_co2:
#     qtde_sensores = len(niveis_co2[estado])
#     total_co2 = sum(niveis_co2[estado])
#     media_co2 = total_co2 / qtde_sensores


Verm = '\x1b[0;30;41m'
Amar = '\x1b[0;30;43m'
Verd = '\x1b[0;30;42m'
Norm = '\33[0m' + '\33[1m'   # 'x1b[1;30;47m'

print(Norm)
print(Norm + '-----------------------------------------')
print('         Monitoramento de CO²                    ')
print('-----------------------------------------')

Grupo3 = []
for chave in niveis_co2:
    Media = sum(niveis_co2[chave]) / 5
    if Media >= 450:
        aviso = 'Crítico'
        IText = Verm
    elif Media > 400:
        aviso = 'Atenção'
        IText = Amar
    else:
        aviso = 'Normal'
        IText = Verd

    Grupo3.append((chave, Media, aviso, IText))
    if len(Grupo3) == 3:
        Est_0 = Grupo3[0]
        Est_1 = Grupo3[1]
        Est_2 = Grupo3[2]

        Q11 = Est_0[3] + '{:^4}:{:^8.2f}'.format(Est_0[0], Est_0[1]) + Norm
        Q12 = Est_0[3] + '{:^13}'.format(Est_0[2]) + Norm
        Q21 = Est_1[3] + '{:^4}:{:^8.2f}'.format(Est_1[0], Est_1[1]) + Norm
        Q22 = Est_1[3] + '{:^13}'.format(Est_1[2]) + Norm
        Q31 = Est_2[3] + '{:^4}:{:^8.2f}'.format(Est_2[0], Est_2[1]) + Norm
        Q32 = Est_2[3] + '{:^13}'.format(Est_2[2]) + Norm

        print(Q11 + '|' + Q21 + '|' + Q31)
        print(Q12 + '|' + Q22 + '|' + Q32)
        print('-----------------------------------------')
        Grupo3 = []
print(Norm)
