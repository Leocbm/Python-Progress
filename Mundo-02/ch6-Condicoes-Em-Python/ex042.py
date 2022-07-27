# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iquais
# Escaleno: todos os lados diferentes

n1 = int(input('Informe a primeira medida: '))
n2 = int(input('Informe a segunda medida: '))
n3 = int(input('Informe a terceira medida: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('Este triângulo é equilátero!')
    if n1 == n2 != n3 or n2 == n3 != n1 or n3 == n1 != n2:
        print('Este triângulo é isósceles!')
    if n1 != n2 != n3:
        print('Este triângulo é escaleno!')
else:
    print('As medidas informadas não formam um triângulo!')
