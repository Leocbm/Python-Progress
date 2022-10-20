# Crie um programa que simule um caixa eletronico. no inicio pergunte ao usuario qual o valor a ser sacado (int)
# e o programa deve calcular qnts cédulas de cada valor serão entregues
# obs: caixa possui cédulas de 50, 20, 10, 1

total = int(input('Informe o valor a ser sacado: '))
nota, quant = 50, 0
while True:
    if total >= nota:
        total -= nota
        quant += 1
    else:
        if quant > 0:
            print(f'{quant} notas de {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        quant = 0
        if total == 0:
            break
