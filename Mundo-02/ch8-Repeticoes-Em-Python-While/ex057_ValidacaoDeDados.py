# Crie um programa que leia o gênero de uma pessoa, só aceita M ou F
# caso seja diferente peça a repetição ate a informação correta

genero = str(input('Informe o seu gênero[M/F]: ')).strip().upper()[0]
while genero not in 'MF':
    print('Dado incorreto! Tente novamente!')
    genero = str(input('Informe o seu gênero[M/F]: ')).strip().upper()[0]
print('Dados Registrados!')

