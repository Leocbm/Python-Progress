# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Informe a quantidade de dias alugado: '))
km = float(input('Informe a quantidade de kilometros rodados: '))
valor = ((dias * 60) + (km * 0.15))
print(f'O valor total pelo aluguel do carro foi de R${valor:.2f}')
