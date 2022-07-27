# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

speed = int(input('Informe a sua velocidade atual: '))
multa = (speed-80)*7
if speed > 80:
    print(f'Você foi multado em R${multa:.2f} devido a sua velocidade elevada!')
else:
    print(f'Tenha um bom dia! Dirija Seguro!')
