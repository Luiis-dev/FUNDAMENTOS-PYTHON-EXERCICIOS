valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Seu Salário: '))
anos = int(input('Quantos anos vai pagar: '))
prestacao = valor_casa / (anos * 12)
limite = salario * 0.30
if salario > 0:         # 1º: salário é válido?
   if anos > 0:         # 2º: anos é válido?
        if prestacao <= limite:         # 3º: cabe no orçamento?
            print('APROVADO!')
            print('Sua prestação será de R${:.2f}'.format(prestacao))
            print('Isso representa menos de 30% do seu Salário R${:.2f} '.format(limite))
        else:
            print('NEGADO!')
            print('Sua prestação seria R${}'.format(prestacao))
            print('Mas o limite máximo é R${:.2f}, 30% do salário'.format(limite))
            print('Você está pagando R${:.2f} acima do permitido'.format(prestacao - limite))
   else:
       print('INVÁLIDO!, O número de anos não pode ser zero ou negativo.')
       print('você digitou: {}'.format(anos))
else:
    print('INVÁLIDO! O salário não pode ser zero ou negativo.')
    print('Você digitou: R${:.2f}'.format(salario))

