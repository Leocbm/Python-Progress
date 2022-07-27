# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
# Anos bissextos são anos múltiplos de 4, como  1996, 2000, 2004.. (que divididos por 4 o resto é igual a 0).
# Exceto anos múltiplos de 100 que não são múltiplos de 400.
#
# Uma das duas condições precisa ser verdadeira:
# condição 1: multiplo de 4 e não multiplo de 100
# condição 2: multiplo de 400 (se for multiplo de 400 é automaticamente multiplo de 4)

from datetime import date

ano = int(input('Informe o ano desejado: (0 para o ano atual)'))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto :)')
else:
    print(f'O ano {ano} Não é bissexto :(')
