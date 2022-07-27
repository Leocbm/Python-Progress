# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de
# pagamento:
# à vista dinheiro/cheque: 10% de disconto
# à vista no cartão: 5% de disconto
# 2x no cartão: pagamento normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Informe o valor do produto: '))
pagamento = int(input('Escolha o método de pagamento:'
               '\n1 - a vista no dinheiro/cheque'
               '\n2 - a vista no cartão'
               '\n3 - 2x no cartão'
               '\n4 - 3x ou mais no cartão'))
if pagamento == 1:
    print(f'O valor a pagar era {valor}, com a promoão de 10% é \033[33mR${(valor-(valor*10/100)):.2f}\033[m')
elif pagamento == 2:
    print(f'O valor a pagar era {valor}, com a promoão de 5% é \033[33mR${(valor-(valor*5/100)):.2f}\033[m')
elif pagamento == 3:
    print(f'O valor a pagar é \033[33mR${valor:.2f}\033[m')
else:
    print(f'O valor a pagar é {valor}, mas com 20% de juros é \033[33mR${(valor+(valor*20/100)):.2f}\033[m')
