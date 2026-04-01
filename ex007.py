# ERRADO
n1 = float(input('Primeira nota do aluno:  '))  # lê a primeira nota
n2 = float(input('Segunda nota do aluno:  '))  # lê a segunda nota
média = n1 + n2 / 2  # calcula a média de forma incorreta, sem parênteses
print('A média entre {} e {} é igual a {}'.format(n1, n2, média))  # mostra o resultado

# CORRETO

n1 = float(input('Primeira nota do aluno:  '))  # lê a primeira nota
n2 = float(input('Segunda nota do aluno:  '))  # lê a segunda nota
média = (n1 + n2) / 2  # calcula a média corretamente
print('A média entre {} e {} é igual a {}'.format(n1, n2, média))  # mostra o resultado

# COM DOIS DÍGITOS

n1 = float(input('Primeira nota do aluno:  '))  # lê a primeira nota
n2 = float(input('Segunda nota do aluno:  '))  # lê a segunda nota
média = (n1 + n2) / 2  # calcula a média corretamente
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))  # mostra as notas e a média com 1 casa decimal