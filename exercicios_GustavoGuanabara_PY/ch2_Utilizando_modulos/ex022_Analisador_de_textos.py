# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras no total (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Insira seu nome completo: ')).strip()
nome2 = ''.join(nome.split())
n = len(nome2) - nome2.count(' ')
print(f'\nSeu nome em maiúsculo é {nome.upper()}')
print(f'\nSeu nome em minúsculo é {nome.lower()}')
print(f'\nSeu nome completo possui {len(nome2)} letras')
# ou
# print(f'\nSeu nome completo possui {n} letras')
print(f'\nSeu primeiro nome possui {len(nome.split()[0])} letras')
