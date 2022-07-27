# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ele.

tipo = input('Digite a palavra ou número que deseja descobrir o tipo: ')
print(f'A palavra/número ({tipo}) é do tipo string? ', tipo.isalpha())
print(f'A palavra/número ({tipo}) é do tipo espace? ', tipo.isspace())
print(f'A palavra/número ({tipo}) é do tipo numérico? ', tipo.isnumeric())
print(f'A palavra/número ({tipo}) é do tipo impresso? ', tipo.isprintable())
print(f'A palavra/número ({tipo}) é do tipo alfa numérico? ', tipo.isalnum())
print(f'A palavra/número ({tipo}) é do tipo com apenas letras maiúsculas? ', tipo.isupper())
print(f'A palavra/número ({tipo}) é do tipo com apenas letras minúscula? ', tipo.islower())
print(f'A palavra/número ({tipo}) é do tipo capitalizado? ', tipo.istitle())
