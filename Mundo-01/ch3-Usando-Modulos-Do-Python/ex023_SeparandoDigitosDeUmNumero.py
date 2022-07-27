# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex: O número: 8765
# 5 unidades 6 dezenas 7 centenas 8 milhares

numero = int(input('Insira o número desejado entre 0 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhas = numero // 1000 % 10
print(f'\nSeu número possui {unidade} unidade(s), {dezena} dezena(s), {centena} centena(s) e {milhas} milhar(es)')
