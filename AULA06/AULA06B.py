n = bool(input('Digite algo: '))  # converte a entrada para booleano e armazena em n
print(type(n))  # mostra o tipo da variável

# OU

n = input('Digite algo: ')  # lê o que foi digitado como texto
print(n.isnumeric())  # verifica se o conteúdo é numérico

# se é possível converter esse valor em um número com o tipo primitivo int
# isnumeric()
# verifica se é numérico

n = input('Digite algo: ')  # lê o que foi digitado como texto
print(n.isalpha())  # verifica se o conteúdo contém apenas letras

# isalpha: verifica se é letra

n = input('Digite algo: ')  # lê o que foi digitado como texto
print(n.isalnum())  # verifica se o conteúdo é alfanumérico

# isalnum = letras e números