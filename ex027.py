n = str(input('Digite seu nome completo: ')).strip()  # lê o nome completo e remove espaços extras
nome = n.split()  # separa o nome em partes
print('Muito prazer em te conhecer!')  # exibe uma saudação
print('Seu primeiro nome é {}'.format(nome[0]))  # mostra o primeiro nome
print('Seu último nome é {}'.format(nome[len(nome)-1]))  # mostra o último nome