# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
# ex: ana Maria de Souza
# primeiro = Ana
# Último = Souza

nome = str(input('Digite seu nome completo: ')).strip()
print(f'\nSeu primeiro nome é {nome.split()[0]} e seu último nome é {nome.split()[-1]}')
# ou (nome[len(nome)-1]) para o último nome
