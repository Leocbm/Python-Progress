# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversao.
# 1- binario 2- octal 3- hexadecimal

numero = int(input('Informe o número desejado: '))
conversao = int(input('Escolha a sua preferência de conversão: '
               '[1] Binario'
               '[2] Octal'
               '[3] Hexadecimal '))
if conversao == 1:
    print(f'The number {numero} converted to binario is {bin(numero)[2:]}')
elif conversao == 2:
    print(f'The number {numero} converted to octal is {oct(numero)[2:]}')
elif conversao == 3:
    print(f'The number {numero} converted to hexadecimal is {hex(numero)[2:]}')
else:
    print('Invalid option!')
