# Escreva um programa que leia um número n inteiro qualquer e mostre na tela  os n primeiros elementos de uma
# sequencia de fibonacci.

termos = int(input('Informe a quantidade de termos desejadas: '))
primario, cont = 0, 0
secundario = 1
for c in range(1, termos+1):
    if cont < termos:
        print(primario, end=' -> ')
        cont += 1
        if cont < termos:
            print(secundario, end=' -> ')
            cont += 1
    primario += secundario
    secundario += primario
print('FIM')
