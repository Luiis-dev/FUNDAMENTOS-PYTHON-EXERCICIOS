valor_casa = float(input('Valor da casa: R$ '))  # lê o valor da casa
salario = float(input('Seu Salário: '))  # lê o salário do comprador
anos = int(input('Quantos anos vai pagar: '))  # lê em quantos anos será pago

prestacao = valor_casa / (anos * 12)  # calcula o valor da prestação mensal
limite = salario * 0.30  # calcula 30% do salário

if salario > 0:  # verifica se o salário é válido
    if anos > 0:  # verifica se a quantidade de anos é válida
        if prestacao <= limite:  # verifica se a prestação cabe no orçamento
            print('APROVADO!')  # informa que o financiamento foi aprovado
            print('Sua prestação será de R${:.2f}'.format(prestacao))  # mostra o valor da prestação
            print('Isso representa menos de 30% do seu Salário R${:.2f} '.format(limite))  # mostra o limite de 30%
        else:  # caso a prestação ultrapasse o limite
            print('NEGADO!')  # informa que foi negado
            print('Sua prestação seria R${}'.format(prestacao))  # mostra o valor da prestação
            print('Mas o limite máximo é R${:.2f}, 30% do salário'.format(limite))  # mostra o limite permitido
            print('Você está pagando R${:.2f} acima do permitido'.format(prestacao - limite))  # mostra o excedente
    else:  # caso os anos sejam inválidos
        print('INVÁLIDO!, O número de anos não pode ser zero ou negativo.')  # avisa que o valor é inválido
        print('você digitou: {}'.format(anos))  # mostra o valor digitado
else:  # caso o salário seja inválido
    print('INVÁLIDO! O salário não pode ser zero ou negativo.')  # avisa que o salário é inválido
    print('Você digitou: R${:.2f}'.format(salario))  # mostra o salário digitado

# EXEMPLO GUSTAVO

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')