# Criar um programa que leia o peso de 5 pessoas e mostre o maior e menor peso.

maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input('Informe o seu peso em Kg: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        elif peso > maior:
            maior = peso
print(f'O maior peso foi {maior}Kg e o menor peso foi {menor}Kg!')
