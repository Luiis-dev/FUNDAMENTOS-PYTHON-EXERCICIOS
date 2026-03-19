# LÊ O NÚMERO DO USUÁRIO
numero = int(input('digite um número inteiro:  '))

# MOSTRA AS OPÇÕES
print('\nEscolha a base:')
print('1 - Binário (Base 2)')
print('2 - Octal (base 8)')
print('3 - Hexadecimal (base 16)')

opcao = int(input('\nDigite sua opção: '))

# CONVERTE CONFORME A ESCOLHA
if opcao == 1:
    resultado = bin(numero)             # bin() CONVERTE PARA BINÁRIO
    print('\n{} em binário é: {}'.format(numero, resultado[2:]))                # [2:] REMOVE O "Ob"
elif opcao == 2:
    resultado = oct(numero)             # oct() CONVERTE PARA OCTAL
    print('\n em octal é: {}'.format(numero, resultado[2:]))                    # [2:] REMOVE O "Oo"
elif opcao == 3:
    resultado = hex(numero)             # hex() CONVERTE PARA HEXADECIMAL
    print('\n{} em hexadecimal é: {}'.format(numero, resultado[2:].upper()))                # [2:] REMOVE O "Ox"
else:
    print('\nOpção inválida!')