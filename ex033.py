a = int(input('Primeiro valor: '))  # lê o primeiro valor
b = int(input('Segundo valor: '))  # lê o segundo valor
c = int(input('Terceiro valor: '))  # lê o terceiro valor

# Verificando quem é menor
if b < a and b < c:  # verifica se b é o menor
    menor = b  # guarda b como menor
if c < a and c < b:  # verifica se c é o menor
    menor = c  # guarda c como menor

# Verificando quem é o maior
if b > a and b > c:  # verifica se b é o maior
    maior = b  # guarda b como maior
if c > a and c > b:  # verifica se c é o maior
    maior = c  # guarda c como maior

print('O menor valor digitado foi {}'.format(menor))  # mostra o menor valor
print('O maior valor digitado foi {}'.format(maior))  # mostra o maior valor