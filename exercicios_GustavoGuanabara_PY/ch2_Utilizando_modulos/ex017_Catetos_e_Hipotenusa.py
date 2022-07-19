# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
# calcule o mostre o comprimento da hipotenusa

import math

co = float(input('Informe o tamanho do cateto oposto em cm: '))
ca = float(input('Informe o tamanho do cateto adjacente em cm: '))

h = math.hypot(co, ca)

print(f'O valor da hipotenusa é {h}')

hi = ((co**2)+(ca**2))
hip = (hi**(1/2))

print(f'Teste de método convencional é igual a {hip}')
