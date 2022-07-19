# Criar  um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.

n1 = str(input('Insira seu nome completo: ')).strip()
n2 = 'silva' in n1.lower()
print(f'\nSeu nome completo possui "silva"?: {n2}')
