# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Informe o valor desejado: '))
dob = n1 * 2
trip = n1 * 3
raiz = n1 ** (1/2)

print(f'O dobro do número informado é {dob} \nO triplo do número informado é {trip} '
      f'\nA raiz quadrada do número informado é {raiz:.3f}')
