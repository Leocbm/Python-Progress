# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".

n1 = str(input('Digite o nome da cidade desejada: ')).strip()
n2 = n1.lower().split()[0] == 'santo'
print(f'\nSua cidade começa com santo? {n2}')
