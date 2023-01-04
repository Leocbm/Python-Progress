# faça um programa que mostre a tabuada de vários números, um de cada vez para cada número digitado pelo usuário
# o programa deverá ser interrompido se o numero digitado for negativo.

while True:
    numero = int(input('Informe um valor para saber sua tabuada [Número negativo para parar]: '))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {numero} = {c*numero}')
print('FIM')