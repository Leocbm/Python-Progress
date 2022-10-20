# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Informe um valor para saber sua tabuada: '))
quantidade = int(input('Informe até que numéro quer multiplicar: '))
for c in range(1, quantidade+1):
    print(f'{numero}x{c}={numero*c}')
