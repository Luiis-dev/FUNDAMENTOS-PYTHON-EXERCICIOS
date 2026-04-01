from datetime import date  # importa a data atual

ano = int(input("Digite o ano de nascimento: "))  # lê o ano de nascimento
idade = date.today().year - ano  # calcula a idade atual
falta = 18 - idade  # calcula quanto falta para o alistamento
passou = idade - 18  # calcula quanto tempo passou do alistamento

if idade < 18:  # verifica se ainda não chegou a hora
    print('Ainda vai se Alistar')  # informa que ainda vai se alistar
    print('Faltam {} anos para o Alistamento'.format(falta))  # mostra quantos anos faltam
elif idade == 18:  # verifica se está na idade exata
    print('É hora de se Alistar')  # informa que é hora de se alistar
else:  # caso já tenha passado da idade
    print('Já passou do tempo de alistamento')  # informa que passou do prazo
    print('Já passaram {} anos do prazo'.format(passou))  # mostra há quantos anos passou