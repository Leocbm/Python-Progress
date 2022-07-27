# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = int(input('Informe a distância da viagem em km: '))
if distancia <= 200:
    print(f'\nO custo dessa viagem será R${(distancia*0.50):.2f}')
else:
    print(f'\nO custo dessa viagem será R${(distancia*0.45):.2f}')
