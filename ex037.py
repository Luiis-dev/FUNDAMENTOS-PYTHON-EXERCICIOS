# LÊ O NÚMERO DO USUÁRIO
numero = int(input('digite um número inteiro:  '))  # lê um número inteiro

# MOSTRA AS OPÇÕES
print('\nEscolha a base:')  # mostra o menu de opções
print('1 - Binário (Base 2)')  # opção 1
print('2 - Octal (base 8)')  # opção 2
print('3 - Hexadecimal (base 16)')  # opção 3

opcao = int(input('\nDigite sua opção: '))  # lê a opção escolhida

# CONVERTE CONFORME A ESCOLHA
if opcao == 1:  # se escolher binário
    resultado = bin(numero)  # converte para binário
    print('\n{} em binário é: {}'.format(numero, resultado[2:]))  # mostra o resultado sem o prefixo "0b"
elif opcao == 2:  # se escolher octal
    resultado = oct(numero)  # converte para octal
    print('\n{} octal é: {}'.format(numero, resultado[2:]))  # mostra o resultado sem o prefixo "0o"
elif opcao == 3:  # se escolher hexadecimal
    resultado = hex(numero)  # converte para hexadecimal
    print('\n{} em hexadecimal é: {}'.format(numero, resultado[2:].upper()))  # mostra em maiúsculas sem o prefixo "0x"
else:  # caso a opção seja inválida
    print('\nOpção inválida!')  # avisa erro de opção

# EXEMPLO GUSTAVO

num = int(input('digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')