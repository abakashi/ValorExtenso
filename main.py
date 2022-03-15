"""
Arquivo principal

Programa que retorna, por extenso, números de 0 a 999.

O intuito do programa é somente para praticar Python e usar programação funcional básica.

Me senti enferrujado.... =S

"""

import funcs as f  # Importe das funções do módulo "funcs".

control = True  # Variável de controle de execução do programa (loop while da linha seguinte).

while control:
    num = f.num_inputer()  # Variável que recebe o número a ser analisado.
    alg_len = f.lenght_counter(num)  # Variável que contém o número de algarismos que o número contém para as decisões.

    if num == 0:  # Caso o número seja literalmente zero...
        print('Zero\n')
    else:
        if alg_len == 3:  # Caso o número tenha três algarismos.
            print(f.three_algarisms_namer(num) + '\n')
        elif alg_len == 2:  # Caso o número tenha dois algarismos.
            print(f.two_algarisms_namer(num) + '\n')
        elif alg_len == 1:  # Caso o número tenha um algarismo.
            print(f.one_algarism_namer(num) + '\n')

    print('Deseja continuar?')  # Ponto de verificação da continuidade do programa.
    extng = input('Digite "s" para sim ou "n" para não:\n')
    if extng.lower() == 'n':
        control = False
