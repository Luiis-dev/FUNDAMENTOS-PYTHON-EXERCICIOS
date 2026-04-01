n1 = float(input('Digite sua nota: '))  # lê a primeira nota
n2 = float(input('Digite sua nota: '))  # lê a segunda nota
media = (n1 + n2) / 2  # calcula a média

if media >= 6:  # verifica se a média é boa
    print('VOCÊ ESTÁ APROVADO!!')  # informa aprovação
    print('MUITO BEM!!')  # reforça a mensagem positiva
elif media < 5:  # verifica se a média é baixa
    print('VOCÊ ESTÁ DE RECUPERAÇÃO!!')  # informa recuperação
    print('ESTUDE PRA PASSAR!')  # incentivo para estudar
else:  # caso a média esteja entre 5 e 5.9
    print('REPROVADO!!')  # informa reprovação