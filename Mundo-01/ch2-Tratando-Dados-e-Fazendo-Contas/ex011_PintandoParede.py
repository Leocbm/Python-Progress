# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informa a altura da parede em metros: '))
area = largura * altura
print(f'A área da parede equivale a {area}m² e para pintá-la é necessário {area/2} litros de tinta')
