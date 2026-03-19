from datetime import date
nasc = int(input('Qual o ano de nascimento? '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
