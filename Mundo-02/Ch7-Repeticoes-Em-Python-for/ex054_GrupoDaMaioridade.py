# Criar um programa que leia o ano de nascimento de sete pessoas e mostre o número de adultos e de pessoas abaixo de 18
# anos.

from datetime import date
adulto = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Informe o seu ano de nascimento: '))
    if (date.today().year - ano) >= 18:
        adulto += 1
    else:
        menor += 1
print(f'Seu grupo possui {adulto} adultos e {menor} pessoas menores de idade')
