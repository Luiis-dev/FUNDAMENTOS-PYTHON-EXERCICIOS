nome = str(input('Qual é seu nome? '))  # lê o nome do usuário
if nome == 'LUIS':  # verifica se o nome é LUIS
    print('Que nome lindo você tem !')  # mensagem especial se for LUIS
print('Bom dia, {}!'.format(nome))  # mostra uma saudação para o usuário

# OU COM else

nome = str(input('Qual é seu nome? '))  # lê o nome do usuário
if nome == 'LUIS':  # verifica se o nome é LUIS
    print('Que nome lindo você tem !')  # mensagem especial se for LUIS
else:  # caso o nome seja diferente
    print('Seu nome é tão normal!')  # mensagem para outros nomes
print('Bom dia, {}!'.format(nome))  # mostra uma saudação para o usuário

n1 = float(input('digite a primeira nota: '))  # lê a primeira nota
n2 = float(input('digite a segunda nota: '))  # lê a segunda nota
m = (n1 + n2)/2  # calcula a média
print('A sua média foi {:.1f}'.format(m))  # mostra a média com 1 casa decimal
if m >= 6.0:  # verifica se a média é suficiente
    print('Sua média foi boa! PARABENS!')  # mensagem para média boa
else:  # caso a média seja menor que 6
    print('Sua média foi ruim! ESTUDE MAIS!')  # mensagem de incentivo

# SIMPLIFICADO

n1 = float(input('digite a primeira nota: '))  # lê a primeira nota
n2 = float(input('digite a segunda nota: '))  # lê a segunda nota
m = (n1 + n2)/2  # calcula a média
print('A sua média foi {:.1f}'.format(m))  # mostra a média com 1 casa decimal
print('PARABENS' if m >= 6.0 else 'ESTUDE MAIS')  # expressão condicional curta