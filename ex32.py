ano = int(input('Que ano quer analizar? '))  # lê o ano informado pelo usuário
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # verifica se o ano é bissexto
    print('O ano {} é BISSEXTO'.format(ano))  # mostra que o ano é bissexto
else:  # caso não seja bissexto
    print('O ano {} NÃO é BISSEXTO'.format(ano))  # mostra que o ano não é bissexto

# import datetime O date, ANO ATUAL

from datetime import date  # importa a classe date para pegar o ano atual
ano = int(input('Que ano quer analizar? coloque 0 para o ano atual '))  # lê o ano ou zero
if ano == 0:  # verifica se o usuário escolheu o ano atual
    ano = date.today().year  # substitui 0 pelo ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # verifica se o ano é bissexto
    print('O ano {} é BISSEXTO'.format(ano))  # mostra que o ano é bissexto
else:  # caso não seja bissexto
    print('O ano {} NÃO é BISSEXTO'.format(ano))  # mostra que o ano não é bissexto