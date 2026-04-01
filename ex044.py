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

# EXEMPLO GUSTAVO

print('{:^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO 
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('OPOÇÃO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
