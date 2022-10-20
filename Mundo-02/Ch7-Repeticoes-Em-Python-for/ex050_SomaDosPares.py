# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

contador = 0
for c in range(1, 7):
    numero = int(input('Informe um valor inteiro: '))
    if numero % 2 == 0:
        contador += numero
print(f'A soma dos valores pares informados é igual a {contador}')
