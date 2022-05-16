# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n1 = float(input('Informe uma metragem: '))

cm = n1 * 100
mil = n1 * 1000

print(f'{n1} metro(s) equivale a {cm} centímetros ou {mil} milímetros')
