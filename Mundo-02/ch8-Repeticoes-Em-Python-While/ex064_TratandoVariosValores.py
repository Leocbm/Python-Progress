# Crie um programa que leia vários números e no final mostre a soma entre eles (desconsiderando o flag)
# o programa para qnd receber o valor 999.

valores = int(input('Informe o valor que deseja somar [999 para parar]: '))
soma = valores
cont = 1
while valores != 999:
    valores = int(input('Informe o próximo valor [999 para parar]: '))
    if valores == 999:
        break
    soma += valores
    cont += 1
if valores == 999 and cont == 1:
    soma = 0
print(f'A soma dos valores informados é igual a {soma}!')
