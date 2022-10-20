# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

contador = 0
for c in range(1, 500+1):
    if c % 2 == 1 and c % 3 == 0:
        contador += c
        print(c)
print(f'A soma entre todos os valores é igual a {contador}')
