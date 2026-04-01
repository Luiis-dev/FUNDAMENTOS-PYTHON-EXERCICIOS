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

# OU

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO.')

# OU

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')

# OU

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media >= 7:
    print('O aluno está APROVADO.')
else:
    print('O aluno está REPROVADO.')

# OU

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está APROVADO.')
elif media >= 7:
    print('O aluno está REPROVADO.')