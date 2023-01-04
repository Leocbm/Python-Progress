# Crie um programa que leia o nome e preço de vários produtos, pergunta se quer continuar e mostre:
# qual é o total gasto na compra
# quantos produtos custam mais de 1000 rs
# qual é o nome do produto mais barato

total, mil, barato, nomebarato, cont = 0, 0, 0, 0, 0
while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: '))
    if cont == 0:
        barato = preco
        nomebarato = nome
    if cont > 0:
        if preco < barato:
            barato = preco
            nomebarato = nome
    if preco > 1000:
        mil += 1
    total += preco
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O preço total da compra foi de R${total:.2f}!'
      f'\nA quantidade de produtos que custaram mais de R$1000 é igual a {mil}!'
      f'\nO produto mais barato se chama "{nomebarato}" custando R${barato:.2f}!')
