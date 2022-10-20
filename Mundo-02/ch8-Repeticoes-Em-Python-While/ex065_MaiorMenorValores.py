# Faça um programa que leia vários números inteiros pelo teclado e no final mostre a média entre todos ele e qual foi
# o maior e o menor. o programa deve perguntar se o usuario quer ou nao continuar a digitar os valores.

continuar = 'x'
maior, menor, cont, soma = 0, 0, 0, 0
while continuar not in 'N':
    valor = int(input('\nInforme o valor desejado: '))
    soma += valor
    cont += 1
    if cont == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    continuar = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Informação incorreta! Deseja continuar?[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'A média dos valores informados é igual a {soma/cont:.2f}!')
print(f'O maior valor foi {maior} e o menor foi {menor}!')
