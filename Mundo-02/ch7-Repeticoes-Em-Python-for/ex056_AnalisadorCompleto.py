# Criar um programa que leia o nome, idade e gênero de 4 pessoas e mostre:
# A média das idades
# O nome do homem mais velho
# O número de mulheres com menos de 20 anos

media = 0
homemvelho = 0
idadehomem = 0
mulher = 0
for c in range(1, 5):
    nome = str(input('Informe o seu nome: '))
    idade = int(input('Informe a sua idade: '))
    genero = str(input('Informe o seu gênero[M/F]: ')).strip().upper()[0]
    media += idade
    if genero == 'M' and idade > idadehomem:
        homemvelho = nome
        idadehomem = idade
    if genero == 'F' and idade < 20:
        mulher += 1
    print(' ')
print(f'A maior idade do grupo é {media/4}, o homem mais velho se chama {homemvelho} e existem {mulher} mulher(es) '
      f'com menos de 18 anos! ')
