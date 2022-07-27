# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior número é {n3}')
elif n1 == n2 > n3:
    print(f'O número {n1} se repetiu 2 vezes, sendo os maiores')
elif n1 == n3 > n2:
    print(f'O número {n1} se repetiu 2 vezes, sendo os maiores')
elif n2 == n3 > n1:
    print(f'O número {n2} se repetiu 2 vezes, sendo os maiores')
else:
    print('Os três valores informados são iguais')
