# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".

cidade = str(input('Digite o nome da cidade desejada: ')).strip()
santo = cidade.lower().split()[0] == 'santo'
print(f'\nSua cidade começa com santo? {santo}')
