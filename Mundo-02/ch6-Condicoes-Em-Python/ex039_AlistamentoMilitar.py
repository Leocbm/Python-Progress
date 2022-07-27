# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora de se alistar ou se ja passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nascimento = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - nascimento
if idade < 18:
    print(f'falta {18 - idade} anos para você se alistar')
elif idade == 18:
    print('Você já pode se alistar')
else:
    print(f'Já passou {idade - 18} ano(s) para você se alistar')
