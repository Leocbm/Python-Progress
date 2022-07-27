# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite a frase desejada: ')).strip()
contador = frase.count('a')
print(f'\nO número de vezes que a vogal "a" apare é {frase.count("a")} vez(es)')
print(f'\nA vogal "A" aparece pela primeira vez na {frase.find("a")+1}° posição')
print(f'\nA vogal "A" aparece pela última vez na {frase.rfind("a")+1}° posição')
