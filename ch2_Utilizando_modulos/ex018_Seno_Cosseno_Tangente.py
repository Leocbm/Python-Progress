# faça um programa que leia um angulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente
from math import radians, tan, cos, sin

ang = float(input('Informe o valor do ângulo desejado: '))

se = sin(radians(ang))
co = cos(radians(ang))
tan = tan(radians(ang))

print(f'Analisando o ângulo {ang}°, o seno desse valor é {se:.2f}, o cosseno é {co:.2f} e o tangente é {tan:.2f}')

