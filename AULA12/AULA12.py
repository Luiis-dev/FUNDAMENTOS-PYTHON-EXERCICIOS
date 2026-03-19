nome = str(input('Qual é seu nome?  '))
if nome == 'LUIS':                             # condicional Simples
    print('Que nome bonito!')
elif nome == ('Pedro' or nome == 'Maria' or nome == 'Paulo'):
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:                                          # Condicional Composta
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

# SEM O: else

nome = str(input('Qual é seu nome?  '))
if nome == 'LUIS':
    print('Que nome bonito!')
elif nome == ('Pedro' or nome == 'Maria' or nome == 'Paulo'):
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
print('Tenha um bom dia, {}!'.format(nome))

