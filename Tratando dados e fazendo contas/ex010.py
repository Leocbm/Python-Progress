# crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# considerar US$1 = RS$3,27

n = float(input('Informe o valor atual da sua carteira: '))

dol = n/3.27

print(f'Atualmente você pode comprar {dol:.2f} dólares')
