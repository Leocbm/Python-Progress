# crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# considerar US$1 = RS$3,27

carteira = float(input('Informe o valor atual da sua carteira: '))
print(f'Atualmente você pode comprar {carteira/3.27:.2f} dólares')
