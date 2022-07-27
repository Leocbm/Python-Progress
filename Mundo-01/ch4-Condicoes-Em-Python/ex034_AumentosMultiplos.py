# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumente é de 15%.

salario = float(input('Informe seu salário: '))
if salario <= 1250:
    print(f'\nSeu novo salário com aumento de 15% é R${salario+(salario*15/100)}')
else:
    print(f'\nSeu novo salário com aumento de 10% é R${salario+(salario*10/100)}')