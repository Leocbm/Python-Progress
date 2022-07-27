# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente.

from math import radians, tan, cos, sin

angulo = float(input('Informe o valor do ângulo desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Analisando o ângulo {angulo}°, o seno desse valor é {seno:.2f}, o cosseno é {cosseno:.2f} '
      f'e o tangente é {tangente:.2f}')

