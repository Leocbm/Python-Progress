# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele.

tipo = input('Digite a palavra, frase ou número que deseja descobrir o seu tipo: ')
print(f'A palavra/número ({tipo}) é do tipo titulado(tem a primeira letra maiúscula em cada palavra)? ', tipo.istitle())
print(f'A palavra/número ({tipo}) é do tipo alfabeto(apenas caracteres do alfabeto)? ', tipo.isalpha())
print(f'A palavra/número ({tipo}) é do tipo alfanumérico(um caractere que é uma letra ou um número)? ', tipo.isalnum())
print(f'A palavra/número ({tipo}) é do tipo com apenas letras maiúsculas? ', tipo.isupper())
print(f'A palavra/número ({tipo}) é do tipo com apenas letras minúscula? ', tipo.islower())
print(f'A palavra/número ({tipo}) é do tipo decimal(se todos os caracteres forem decimais)? ', tipo.isdecimal())
print(f'A palavra/número ({tipo}) é do tipo dígito(se todos os caracteres na string forem dígitos)? ', tipo.isdigit())
print(f'A palavra/número ({tipo}) é do tipo numérico? ', tipo.isnumeric())
print(f'A palavra/número ({tipo}) é do tipo espace? ', tipo.isspace())
print(f'A palavra/número ({tipo}) é do tipo impresso? ', tipo.isprintable())
