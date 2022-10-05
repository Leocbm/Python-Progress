# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Informe o valor do produto: R$'))
desconto = preco * 5 / 100
print(f'O novo valor do produto com desconto é igual a R${preco-desconto:.2f}!')
