nome = str(input('Qual é seu nome? '))
if nome == 'LUIS':
    print('Que nome lindo você tem !')
print('Bom dia, {}!'.format(nome))
#
#
# OU COM else
#
#
nome = str(input('Qual é seu nome? '))
if nome == 'LUIS':
    print('Que nome lindo você tem !')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
#
#
#
#
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
#
#
# SIMPLIFICADO
#
#
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABENS' if m >= 6.0 else 'ESTUDE MAIS')

