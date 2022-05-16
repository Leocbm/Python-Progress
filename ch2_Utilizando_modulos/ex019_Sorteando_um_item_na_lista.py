# um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

n1 = (input('Informe o nome do primeiro aluno: \n'))
n2 = (input('Informe o nome do segundo aluno: \n'))
n3 = (input('Informe o nome do terceiro aluno: \n'))
n4 = (input('Informe o nome do quarto aluno: \n'))

list = [n1, n2, n3, n4]

print(f'O(a) aluno sorteado(a) foi "{choice(list)}"')
