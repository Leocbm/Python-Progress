# A Confederação Nacional De Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# ate 9 anos: MIRIM
# ate 14 anos: INFANTIL
# ate 19 anos: JUNIOR
# ate 20 anos: SÊNIOR
# acima: MASTER

from datetime import date

ano = int(input('Informe seu ano de nascimento: '))
age = date.today().year - ano
if age <= 9:
    print('MIRIM')
elif 9.1 <= age <= 14:
    print('INFANTIL')
elif 14.1 <= age <= 19:
    print('JUNIOR')
elif 19.1 <= age <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
