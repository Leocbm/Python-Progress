# Faça um programa q leia um numero qualquer e mostre seu fatorial.

numero = int(input('Informe um valor qualquer e descubra seu fatorial: '))
mult = numero
for c in range(numero, 1, -1):
    mult *= (c-1)
print(f'O fatorial de {numero} é {mult}')
# ou
# from math import factorial
# print(f'O fatorial de {numero} é {factorial(numero)}')
