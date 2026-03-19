preco = float(input('Digite o valor do produto: '))
print('\nEscolha a forma de pagamento:')
print('1 - Dinheiro/Cheque')
print('2 - Cartão à Vista')
print('3 - Até 2x no Cartão')
print('4 - 3x ou mais no Cartão')
escolha= int(input('Digite a condição de pagamento: '))
if escolha == 1:
    total = preco * 0.9
    print('10% de desconto! Valor a pagar: R${:.2f}'.format(total))
elif escolha == 2:
    total = preco * 0.95
    print('5% de desconto! Valor a pagar: R${:.2f}'.format(total))
elif escolha == 3:
    total = preco
    print('Sem desconto ou juros! Valor a pagar: R${:.2f}'.format(total))
else:
    total = preco * 1.2
    print('20% de desconto! Valor a pagar: R${:.2f}'.format(total))
