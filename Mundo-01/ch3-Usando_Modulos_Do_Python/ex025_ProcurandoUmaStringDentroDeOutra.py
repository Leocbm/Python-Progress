# Criar um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.

nome = str(input('Insira seu nome completo: ')).strip()
silva = 'silva' in nome.lower()
print(f'\nSeu nome completo possui "silva"?: {silva}')
