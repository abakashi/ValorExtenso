"""
Módulo de funções do programa.
"""


HUNDREDS = ('', 'Cento', 'Duzentos', 'Trezentos', 'Quatrocentos', 'Quinhentos', 'Seiscentos', 'Setecentos', 'Oitocentos',
           'Novecentos')

DOZENS = ('', ('Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove'),
          'Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa')

UNITS = ('', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove')

JUNC = ' e '


def lenght_counter(num):
    """
    Retorna quantos algarismos tem um número
    :param num: Numero inteiro
    :return: Quantidade de algarismos.
    """
    return len(str(num))


def num_inputer():
    """
    Função para receber do usuário o número a ser escrito.
    :return: Número a ser analisado.
    """
    try:
        number = int(input('Insira um número de 0 à 999: \n'))

        while 0 >= number >= 999:
            print('Número fora da área de comparação.')
            number = int(input('Insira um número de 0 à 999: \n'))
    except ValueError:
        print('Tipo não aceito. \nUse somente números inteiros.')
        number = int(input('Insira um número de 0 à 999: \n'))
    return number


def three_algarisms_namer(num):
    """
    Nomeia por extenso números de três algarismos diferentes de zero.
    :param num: Número inteiro para entrada
    :return: Número por extenso como String
    """
    str_num = str(num)
    if str_num == '100':
        extense = 'Cem'
    elif str_num[1:3] == '00':
        extense = HUNDREDS[int(str_num[0])]
    elif str_num[1] == '1':
        extense = HUNDREDS[int(str_num[0])] + JUNC + DOZENS[1][int(str_num[2])]
    elif str_num[1] == '0':
        extense = HUNDREDS[int(str_num[0])] + JUNC + UNITS[int(str_num[2])]
    else:
        extense = HUNDREDS[int(str_num[0])] + JUNC + DOZENS[int(str_num[1])] + JUNC + UNITS[int(str_num[2])]
    return extense


def two_algarisms_namer(num):
    """
    Nomeia por extenso números de dois algarismos diferentes de zero.
    :param num: Número inteiro para entrada
    :return: Número por extenso como String
    """
    str_num = str(num)
    if str_num == '10':
        extense = DOZENS[1][0]
    elif str_num[1] == '0':
        extense = DOZENS[int(str_num[0])]
    elif str_num[0] == '1':
        extense = DOZENS[1][int(str_num[1])]
    else:
        extense = DOZENS[int(str_num[0])] + JUNC + UNITS[int(str_num[1])]
    return extense


def one_algarism_namer(num):
    """
    Nomeia por extenso números de um algarismo diferentes de zero.
    :param num: Número inteiro para entrada
    :return: Número por extenso como String
    """
    return UNITS[num]
