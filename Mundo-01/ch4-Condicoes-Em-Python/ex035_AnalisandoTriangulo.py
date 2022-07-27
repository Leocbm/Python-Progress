# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo

r1 = int(input('Informe a medida da primeira reta: '))
r2 = int(input('Informe a medida da segunda reta: '))
r3 = int(input('Informe a medida da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas informadas podem formar um triangulo! :)')
else:
    print(f'As retas informadas não podem formar um triangulo! :(')
