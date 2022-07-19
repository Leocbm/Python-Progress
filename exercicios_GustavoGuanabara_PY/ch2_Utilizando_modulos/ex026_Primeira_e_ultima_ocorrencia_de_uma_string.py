# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

n1 = str(input('Digite a frase desejada: ')).strip()
n2 = n1.count('a')
print(f'\nO número de vezes que a vogal "a" apare é {n1.count("a")} vez(es)')
print(f'\nA vogal "A" aparece pela primeira vez na {n1.find("a")+1}° posição')
print(f'\nA vogal "A" aparece pela última vez na {n1.rfind("a")+1}° posição')
