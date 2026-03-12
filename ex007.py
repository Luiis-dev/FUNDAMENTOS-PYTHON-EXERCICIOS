# ERRADO
n1 = float(input('Primeira nota do aluno:  '))
n2 = float(input('Segunda nota do aluno:  '))
média = n1 + n2 / 2
print('A m´dia entre {} e {} é igual a {}'.format(n1, n2, média))

# CORRETO

n1 = float(input('Primeira nota do aluno:  '))
n2 = float(input('Segunda nota do aluno:  '))
média = (n1 + n2) / 2
print('A m´dia entre {} e {} é igual a {}'.format(n1, n2, média))

# COM DOIS DIGITOS

n1 = float(input('Primeira nota do aluno:  '))
n2 = float(input('Segunda nota do aluno:  '))
média = (n1 + n2) / 2
print('A m´dia entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))
