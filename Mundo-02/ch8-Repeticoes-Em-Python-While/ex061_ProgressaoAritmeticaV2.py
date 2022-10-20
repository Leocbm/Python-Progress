# Refaça o desafio 51 lendo o primeiro termo e razão de uma PA, mostrando os 10 termos utilizando while.

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
barreira = 10
cont = 0
while cont < barreira:
    print(f'{valor1}', end='')
    print(' -> ' if cont < 10 else '', end='')
    valor1 += valor2
    cont += 1
print('FIM')
