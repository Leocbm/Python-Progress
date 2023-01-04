# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# ex: apos a sopa
# ex: a sacada da casa

frase = str(input('Informe uma frase qualquer: ')).strip()
semespaco = ''.join(frase.split())
cont = len(semespaco)
inverso = ''
for c in range(len(semespaco)-1, -1, -1):
    inverso += semespaco[c]
if semespaco == inverso:
    print('É um políndromo!')
else:
    print('Não é um políndromo!')
