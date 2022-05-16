# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# ex: ana Maria de Souza
# primeiro = Ana
# Último = Souza


n1 = str(input('Digite seu nome completo: ')).strip()
print(f'\nSeu primeiro nome é {n1.split()[0]} e seu último nome é {n1.split()[-1]}')

# ou
# n2 = n1.split()
# print(n2[len(n2)-1]) para o último nome
