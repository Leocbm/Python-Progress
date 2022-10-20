# Crie um programa que leia vários números inteiros que só irão parar qnd receber 999
# no final mostre qnts numeros foram digitados e qual foi a soma entre eles

soma, numero, cont = 0, 0, 0
while numero != 999:
    numero = int(input('Informe o valor que deseja somar [999 para parar]: '))
    if numero != 999:
        soma += numero
        cont += 1
    else:
        break
print(f'A quantidade de valores informados foi {cont}!'
      f'\nA soma entre os valores é igual a {soma}!')
