# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]Somar
# [2]Multiplicar
# [3]Maior
# [4]Novos Números
# [5]Sair Do Programa
# Seu programa deverá realizar a operação selecionada em cada caso.

from time import sleep
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
menu = 100
while menu != 5:
    menu = int(input('\nInforme a opção desejada: '
                 '\n[1]Somar'
                 '\n[2]Multiplicas'
                 '\n[3]Maior'
                 '\n[4]Novos Números'
                 '\n[5]Sair Do Programa: '))
    if menu == 1:
        print(f'A soma entre {valor1} e {valor2} é {valor1+valor2}')
    elif menu == 2:
        print(f'A multiplicação entre {valor1} e {valor2} é {valor1*valor2}')
    elif menu == 3:
        if valor1 > valor2:
            print(f'O maior valor é o valor {valor1}')
        elif valor2 > valor1:
            print(f'O maior valor é o valor {valor2}')
        else:
            print('Os valores são iguais!')
    elif menu == 4:
        valor1 = int(input('Informe o primeiro novo valor: '))
        valor2 = int(input('Informe o segundo novo valor: '))
    elif menu == 5:
        print('Encerrando em')
        for c in range(3, -1, -1):
            print(c)
            sleep(1)
    else:
        print('Valor incorreto! Tente novamente!')
print('FIM')
