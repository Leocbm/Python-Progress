# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# Média abaixo de 5: REPROVADO
# Média entre 5 e 6.9: RECUPERAÇÂO
# Média 7 ou superior: APROVADO

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
med = (nota1 + nota2) / 2
if med >= 7:
    print('APROVADO!!')
elif 5 <= med <= 6.9:
    print('RECUPERAÇÃO!!')
else:
    print('REPROVADO!!')
