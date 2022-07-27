# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

list = ['pedra', 'papel', 'tesoura']
npc = choice(list)
print('\033[31m-=\033[m'*20)
print('\033[31mEu desafio você para uma batalha de JOKENPÔ\033[m')
print('\033[31m-=\033[m'*20)
print('\033[36mFaça sua escolha e teste sua sorte!!\033[m')
user = str(input('\033[36mPedra, Papel ou Tesoura?: \033[m')).strip().lower()
if user != 'pedra' and user != 'papel' and user != 'tesoura':
    print('Informação incorreta!')
if npc == 'pedra':
    if user == 'pedra':
        print('\033[36mAcabamos em um empate\033[m')
    elif user == 'papel':
        print('\033[32mVocê Ganhou, desta vez..\033[m')
    elif user == 'tesoura':
        print('\033[31mHAHAHA Eu Ganhei!Tente Novamente!\033[m')
elif npc == 'papel':
    if user == 'pedra':
        print('\033[31mHAHAHA Eu Ganhei!Tente Novamente!\033[m')
    elif user == 'papel':
        print('\033[36mAcabamos em um empate\033[m')
    elif user == 'tesoura':
        print('\033[32mVocê Ganhou, desta vez..\033[m')
elif npc == 'tesoura':
    if user == 'pedra':
        print('\033[32mVocê Ganhou, desta vez..\033[m')
    elif user == 'papel':
        print('\033[31mHAHAHA Eu Ganhei!Tente Novamente!\033[m')
    elif user == 'tesoura':
        print('\033[36mAcabamos em um empate\033[m')
