# Melhore o desafio 61 perguntando para o usuário se le quer mostrar mais alguns termos. O programa encerrá quando
# ele disser q quer mostrar 0 termos.

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
barreira = 11
cont = 0
while cont < barreira:
    if cont < barreira - 1:
        print(f'{valor1}', end='')
        print(' -> ' if cont < barreira-1 else '', end='')
        valor1 += valor2
        cont += 1
    else:
        novos = int(input('Deseja ver mais quantos termos? [0 para parar]: '))
        barreira += novos
        if novos == 0:
            break
print('FIM')
