n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
media = (n1 + n2) / 2
if media >= 6:
    print('VOCÊ ESTÁ APROVADO!!')
    print('MUITO BEM!!')
elif media < 5:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO!!')
    print('ESTUDE PRA PASSAR!')
else:
    print('REPROVADO!!')
