# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
# ex: número 6.127  o número 6.127 tem a parte inteira 6.

from math import trunc

n = float(input('Informe o valor que deseja: '))
print(f'O número {n} tem a parte inteira {trunc(n)}')
# print(f'O número {n} tem a parte inteira {int(n)}')
