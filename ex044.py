preco = float(input('Digite o valor do produto: '))  # lê o preço do produto

print('\nEscolha a forma de pagamento:')  # mostra o menu de pagamento
print('1 - Dinheiro/Cheque')  # opção 1
print('2 - Cartão à Vista')  # opção 2
print('3 - Até 2x no Cartão')  # opção 3
print('4 - 3x ou mais no Cartão')  # opção 4

escolha = int(input('Digite a condição de pagamento: '))  # lê a forma de pagamento escolhida

if escolha == 1:  # pagamento em dinheiro ou cheque
    total = preco * 0.9  # aplica 10% de desconto
    print('10% de desconto! Valor a pagar: R${:.2f}'.format(total))  # mostra o valor final
elif escolha == 2:  # pagamento no cartão à vista
    total = preco * 0.95  # aplica 5% de desconto
    print('5% de desconto! Valor a pagar: R${:.2f}'.format(total))  # mostra o valor final
elif escolha == 3:  # pagamento em até 2x
    total = preco  # não aplica desconto nem juros
    print('Sem desconto ou juros! Valor a pagar: R${:.2f}'.format(total))  # mostra o valor final
else:  # pagamento em 3x ou mais
    total = preco * 1.2  # aplica 20% de acréscimo
    print('20% de desconto! Valor a pagar: R${:.2f}'.format(total))  # mostra o valor final