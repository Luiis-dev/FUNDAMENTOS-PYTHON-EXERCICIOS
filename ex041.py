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