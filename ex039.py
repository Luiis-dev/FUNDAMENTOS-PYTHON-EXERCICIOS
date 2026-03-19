from datetime import date
ano = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano
falta = 18 - idade
passou = idade - 18
if idade < 18:
    print('Ainda vai se Alistar')
    print('Faltam {} anos para o Alistamento'.format(falta))
elif idade == 18:
    print('É hora de se Alistar')
else:
    print('Já passou do tempo de alistamento')
    print('Já passaram {} anos do prazo'.format(passou))