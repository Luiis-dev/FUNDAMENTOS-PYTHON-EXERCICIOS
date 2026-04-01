nome = str(input('Qual é seu nome?  '))  # lê o nome do usuário como string
if nome == 'LUIS':  # verifica se o nome é exatamente LUIS
    print('Que nome bonito!')  # mensagem se a condição for verdadeira
elif nome == ('Pedro' or nome == 'Maria' or nome == 'Paulo'):  # tentativa de verificar outros nomes
    print('Seu nome é bem popular no Brasil.')  # mensagem para nomes populares
elif nome in 'Ana Cláudia Jéssica Juliana':  # verifica se o nome aparece na lista de nomes
    print('Belo nome feminino!')  # mensagem para nomes femininos
else:  # caso nenhuma condição anterior seja atendida
    print('Seu nome é bem normal.')  # mensagem padrão
print('Tenha um bom dia, {}!'.format(nome))  # saudação final com o nome informado

# SEM O: else

nome = str(input('Qual é seu nome?  '))  # lê o nome do usuário como string
if nome == 'LUIS':  # verifica se o nome é exatamente LUIS
    print('Que nome bonito!')  # mensagem se a condição for verdadeira
elif nome == ('Pedro' or nome == 'Maria' or nome == 'Paulo'):  # tentativa de verificar outros nomes
    print('Seu nome é bem popular no Brasil.')  # mensagem para nomes populares
elif nome in 'Ana Cláudia Jéssica Juliana':  # verifica se o nome aparece na lista de nomes
    print('Belo nome feminino!')  # mensagem para nomes femininos
print('Tenha um bom dia, {}!'.format(nome))  # saudação final com o nome informado