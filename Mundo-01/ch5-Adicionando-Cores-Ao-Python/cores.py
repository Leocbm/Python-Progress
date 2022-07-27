# Exemplo de cores e derivações em negrito e sublinhado.

cores = {    #cores normais

         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'roxo':'\033[35m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;30;m',

                #cores em negrito

         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;30m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',

               #cores sublinhadas

         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;30m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano sublinhado':'\033[4;36m'
         }
print('-='*20)
print('Cores Normais')
print('-='*20)
print(f'{cores["vermelho"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["azul"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["amarelo"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["verde"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["branco"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["roxo"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["ciano"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["preto e branco"]}Olá, Mundo!{cores["limpa"]}')
print('-='*20)
print('-='*20)
print('Cores Em Negrito')
print('-='*20)
print(f'{cores["vermelho em negrito"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["azul em negrito"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["amarelo em negrito"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["branco em negrito"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["roxo em negrito"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["verde em negrito"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["ciano em negrito"]}Olá, Mundo!{cores["limpa"]}')
print('-='*20)
print('-='*20)
print('Cores Sublinhadas')
print('-='*20)
print(f'{cores["vermelho sublinhado"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["azul sublinhado"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["amarelo sublinhado"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["branco sublinhado"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["roxo sublinhado"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["verde sublinhado"]}Olá, Mundo!{cores["limpa"]}')
print(f'{cores["ciano sublinhado"]}Olá, Mundo!{cores["limpa"]}')
print('-='*20)
