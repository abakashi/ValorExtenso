"""
Módulo de funções do programa.
"""


CENTENA = ('', 'Cento', 'Duzentos', 'Trezentos', 'Quatrocentos', 'Quinhentos', 'Seiscentos', 'Setecentos', 'Oitocentos',
           'Novecentos')

DEZENA = ('', ('Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove'),
          'Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa')

UNIDADE = ('', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove')

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
        extense = CENTENA[int(str_num[0])]
    elif str_num[1] == '1':
        extense = CENTENA[int(str_num[0])] + JUNC + DEZENA[1][int(str_num[2])]
    elif str_num[1] == '0':
        extense = CENTENA[int(str_num[0])] + JUNC + UNIDADE[int(str_num[2])]
    else:
        extense = CENTENA[int(str_num[0])] + JUNC + DEZENA[int(str_num[1])] + JUNC + UNIDADE[int(str_num[2])]
    return extense


def two_algarisms_namer(num):
    """
    Nomeia por extenso números de dois algarismos diferentes de zero.
    :param num: Número inteiro para entrada
    :return: Número por extenso como String
    """
    str_num = str(num)
    if str_num == '10':
        extense = DEZENA[1][0]
    elif str_num[1] == '0':
        extense = DEZENA[int(str_num[0])]
    elif str_num[0] == '1':
        extense = DEZENA[1][int(str_num[1])]
    else:
        extense = DEZENA[int(str_num[0])] + JUNC + UNIDADE[int(str_num[1])]
    return extense


def one_algarism_namer(num):
    """
    Nomeia por extenso números de um algarismo diferentes de zero.
    :param num: Número inteiro para entrada
    :return: Número por extenso como String
    """
    return UNIDADE[num]


if __name__ == '__main__':
