nome = str(input('Digite seu nome completo: '))  # lê o nome completo
print('Analisando seu nome...')  # informa que a análise vai começar
print('Seu nome em maiusculas é {}'.format(nome.upper()))  # mostra o nome em maiúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))  # mostra o nome em minúsculas
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  # conta as letras sem espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))  # mostra a quantidade de letras até o primeiro espaço

# OU

nome = str(input('Digite seu nome completo: '))  # lê o nome completo
print('Analisando seu nome...')  # informa que a análise vai começar
print('Seu nome em maiusculas é {}'.format(nome.upper()))  # mostra o nome em maiúsculas
print('Seu nome em minúsculas é {}'.format(nome.lower()))  # mostra o nome em minúsculas
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  # conta as letras sem espaços
separa = nome.split()  # separa o nome em partes
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))  # mostra o primeiro nome e seu tamanho