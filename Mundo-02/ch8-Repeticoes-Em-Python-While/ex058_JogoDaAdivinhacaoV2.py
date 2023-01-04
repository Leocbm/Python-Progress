# Melhore o desafio 28, só q dessa vez o jogador tenta até acertar e no final mostra o numero de tentativas feitas
# entra 0 e 10.

from random import randint
cont = 0
pc = randint(1, 10)
tentativa = int(input('Teste a sua sorte HAHA! Escolha um número entre 1 e 10: '))
cont += 1
while tentativa != pc:
    if tentativa < pc:
        print('mais..')
    else:
        print('menos..')
    cont += 1
    tentativa = int(input('Tente novamente: '))
print(f'Parabéns!! Vc acertou com {cont} tentativa(s)!')
