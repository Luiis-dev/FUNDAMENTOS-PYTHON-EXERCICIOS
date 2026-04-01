print('\033[1;31;43mOlá, Mundo!')  # imprime texto com estilo ANSI, mas sem limpar ao final

# OU

print('\033[1;31;43mOlá, Mundo!\033[m')  # imprime texto colorido e limpa a formatação no final

# OU

print('\033[4;30;45mOlá, Mundo!\033[m')  # imprime texto sublinhado, preto, com fundo roxo

#

print('\033[37mOlá, Mundo!\033[m')  # imprime texto branco com limpeza ao final

#

print('\033[37mOlá, Mundo!\033[m')  # repete a impressão em branco

#

print('\033[30mOlá, Mundo!\033[m')  # imprime texto preto com limpeza ao final

#

print('\033[7;30mOlá, Mundo!\033[m')  # aplica o efeito invertido com texto preto

a = 3  # define o valor de a
b = 5  # define o valor de b
print('Os valores são \033[32;44m{}\033[m e \033[32;44m{}\033[m!'.format(a, b))  # mostra os valores com destaque

#

nome = 'LUIS'  # define o nome
print('Olá! muito prazer em te conhecer, {}{}!!'.format('\033[4;34m', nome, '\033[m'))  # exibe o nome com cor e sublinhado

#

nome = 'LUIS'  # define o nome
cores = {'limpa':'\033[m',  # código para limpar a cor
         'azul':'\033[34m',  # código azul
         'amarelo':'\033[33m',  # código amarelo
         'pretoebranco':'\033[7;30m',}  # código com fundo invertido e texto preto
print('Olá! muito prazer em te conhecer, {}{}!!'.format(cores['pretoebranco'], nome, cores ['\033[m']))  # exibe a frase com as cores definidas