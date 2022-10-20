# Crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada o pc deve perguntar
# se o usuario quer continuar ou não, no final mostre:
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos

dezoito, homem, vinte = 0, 0, 0
while True:
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Dados incorretos! Informe seu sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade > 20:
        vinte += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados incorretos! Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'No total {dezoito} pessoas possuem mais de dezoito anos!'
      f'\nForam cadastrado(s) {homem} homem(ns)!'
      f'\nExistem {vinte} mulheres com a idade acima de 20 anos!')
