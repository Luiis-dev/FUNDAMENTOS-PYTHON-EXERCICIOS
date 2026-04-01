from datetime import date  # importa a data atual

nasc = int(input('Qual o ano de nascimento? '))  # lê o ano de nascimento
ano = date.today().year  # pega o ano atual
idade = ano - nasc  # calcula a idade da pessoa

if idade <= 9:  # verifica se a idade é até 9 anos
    print('MIRIM')  # categoria mirim
elif idade <= 14:  # verifica se a idade é até 14 anos
    print('INFANTIL')  # categoria infantil
elif idade <= 19:  # verifica se a idade é até 19 anos
    print('JÚNIOR')  # categoria júnior
elif idade <= 20:  # verifica se a idade é até 20 anos
    print('SÊNIOR')  # categoria sênior
else:  # caso seja maior que 20 anos
    print('MASTER')  # categoria master

# EXEMPLO GUSTAVO

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classficação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')


