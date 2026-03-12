n = bool(input('Digite algo: '))
print(type(n))

# OU

n = input('Digite algo: ')
print(n.isnumeric())

# se e possivel converter o esse valor em um numero com o tipo primitivo int
# isnumeric()
# se e numerico

n = input('Digite algo: ')
print(n.isalpha())

# isalpha se ele é letra

n = input('Digite algo: ')
print(n.isalnum())

# isalnum = alfabeto e numero