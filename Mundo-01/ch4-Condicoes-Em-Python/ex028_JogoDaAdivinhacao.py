# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar des-
# cobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

pc = randint(0, 5)
print('\033[36m-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-\033[36m'*20)
numero = int(input('\033[31mDigite o número desejado e teste sua sorte HAHAHA: \033[31m'))
print('\n\033[33mPROCESSANDO.....\033[33m')
sleep(5)
if numero == pc:
    print(f'\n\033[32mPARABÉNS! Você é uma pessoa sortuda!\033[32m')
else:
    print(f'\n\033[31mHAHAHA Você errou! Meu número era {pc}! Tente Novamente!\033[31m')
