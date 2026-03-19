from datetime import date
ano = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano
if idade < 18:
    print('ainda vai se alistar')
    print('')