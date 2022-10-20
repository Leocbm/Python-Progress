# Faça um programa em que o usuário joga par ou impar com o computador e so para qnd o jogador perder
# mostrando no final o tanto de vitórias consecutivas

from random import randint
cont = 0
while True:
    pc = randint(0, 10)
    parouimpar = str(input('Escolha, impar ou par: ')).strip().upper()
    while parouimpar != 'PAR' and parouimpar != 'IMPAR':
        parouimpar = str(input('Tente novamente, impar ou par: ')).strip().upper()
    numero = int(input('Escolha um numero entre 0 e 10: '))
    if parouimpar == 'PAR':
        if ((pc + numero) % 2) == 0:
            print('Parabéns, vc venceu!!')
            print(f'O número do pc foi {pc}, e {pc}+{numero} é par!')
            print('Tente a sorte novamente!')
            cont += 1
        else:
            print(f'Você perdeu! O pc escolheu {pc} e {pc}+{numero} é ímpar!')
            break
    else:
        if ((pc + numero) % 2) != 0:
            print('Parabéns, vc venceu!!')
            print(f'O número do pc foi {pc}, e {pc}+{numero} é ímpar!')
            print('Tente a sorte novamente!')
            cont += 1
        else:
            print(f'Você perdeu! O pc escolheu {pc} e {pc}+{numero} é par!')
            break
    if pc == 0 and numero == 0:
        print('Empate! Tente novamente!')
print(f'O número total de vitórias consecutivas foi {cont}')
