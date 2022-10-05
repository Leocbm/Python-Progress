# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
# calcule o mostre o comprimento da hipotenusa.

from math import hypot

catetoOposto = float(input('Informe o tamanho do cateto oposto em cm: '))
catetoAdj = float(input('Informe o tamanho do cateto adjacente em cm: '))
print(f'O valor da hipotenusa é {hypot(catetoOposto, catetoAdj)}')
# teste convencional
# hipotenusa2 = (((catetoOposto**2)+(catetoAdj**2))**(1/2))
# print(f'O valor da hipoteusa é {hipotenusa2}')
