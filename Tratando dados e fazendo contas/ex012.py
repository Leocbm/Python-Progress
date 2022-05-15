# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n = float(input('Informe o valor do produto: R$'))

desc = n * 10 / 100
valor = n - desc

print(f'O novo valor do produto com desconto é igual a R${valor:.2f}')
