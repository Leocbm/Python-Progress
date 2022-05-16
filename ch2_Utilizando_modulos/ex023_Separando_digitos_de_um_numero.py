# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex: O número: 8765
# 5 unidades 6 dezenas 7 centenas 8 milhares

n1 = int(input('Insira o número desejado entre 0 e 9999: '))
unidade = n1 // 1 % 10
dezena = n1 // 10 % 10
centena = n1 // 100 % 10
milhas = n1 // 1000 % 10
print(f'\nSeu número possui {unidade} unidade(s), {dezena} dezena(s), {centena} centena(s) e {milhas} milhar(es)')
