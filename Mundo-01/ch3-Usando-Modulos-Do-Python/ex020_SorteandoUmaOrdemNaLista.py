# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e diga a ordem sorteada.

from random import shuffle
n1 = str(input('Informe o nome do primeiro aluno: \n'))
n2 = str(input('Informe o nome do segundo aluno: \n'))
n3 = str(input('Informe o nome do terceiro aluno: \n'))
n4 = str(input('Informe o nome do quarto aluno: \n'))
list = [n1, n2, n3, n4]
shuffle(list)
print(f'A ordem de apresentação dos trabalhos será: {list}')
