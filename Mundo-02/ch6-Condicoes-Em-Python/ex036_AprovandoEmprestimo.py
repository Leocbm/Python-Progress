# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

nome = str(input('Informe o seu nome: '))
print(f'Bem Vindo, {nome} !!')
valorDaCasa = float(input('Informe o valor da casa desejada: '))
salario = float(input('Informe seu salário: '))
tempo = int(input('Informe a quantidade de anos em que deseja pagar: '))
parcelas = valorDaCasa / (tempo * 12)
if parcelas < salario * 30 / 100:
    print('Parabéns! O banco aprovou seu empréstimo!')
else:
    print('Desculpa! O banco não aprovou o seu empréstimo!')
