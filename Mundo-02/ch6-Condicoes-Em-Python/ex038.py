# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# -O primeiro valor é maior
# -O segundo valor é maior
# -Não existe valor maior, os dois são iguais

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
if n1 > n2:
    print(f'O valor {n1} é o maior!')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais!')
else:
    print(f'O valor {n2} é o maior!')
