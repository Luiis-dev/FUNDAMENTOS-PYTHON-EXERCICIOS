frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase)  # mostra a frase completa

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase[3])  # mostra o caractere da posição 3

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase[3:13])  # mostra do índice 3 até 12

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase[:13])  # mostra do início até o índice 12

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase[1:15])  # mostra do índice 1 até 14

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase[1:15:2])  # mostra do índice 1 ao 14 pulando de 2 em 2

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase[::2])  # mostra a frase inteira pulando de 2 em 2

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase[::2])  # mostra a frase inteira pulando de 2 em 2

print('Oí')  # imprime uma saudação
print('Welcome! Are you completely new to programming?')  # imprime uma frase em inglês
print('f not then we presume you will be looking for information')  # imprime outra frase

# MAIS PRÁTICO

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase[::2])  # mostra a frase inteira pulando de 2 em 2

print("""Welcome! Are you completely new to programming? If not then we presume you will be
looking for information about why and how to get started with Python. Fortunately an
experienced programmer in any programming language (whatever it may be) can pick up
Python very quickly. Its also easy for beginners to use and learn, so jump in!""")  # imprime texto em várias linhas

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase.count('O'))  # conta quantas vezes o caractere O aparece

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase.upper().count('O'))  # converte para maiúsculas e conta O

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(len(frase))  # mostra o tamanho da frase

# OU

frase = '   Curso em Vídeo Python   '  # define uma frase com espaços extras
print(len(frase.strip()))  # remove espaços extras e mostra o tamanho

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase.replace('Python', 'Android'))  # substitui uma palavra por outra

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print[0] = 'J'  # NÃO DÁ: tentativa incorreta de alterar string diretamente

# CORRETO

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
frase = frase.replace('Python', 'Android')  # substitui a palavra Python por Android
print(frase)  # mostra a frase alterada

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase.lower().find('vídeo'))  # procura a posição da palavra vídeo em minúsculas

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
print(frase.split())  # separa a frase em palavras

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
dividido = frase.split()  # separa a frase em uma lista de palavras
print(dividido)  # mostra a lista criada

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
dividido = frase.split()  # separa a frase em uma lista de palavras
print(dividido[0])  # mostra a primeira palavra

# OU

frase = 'Curso em Vídeo Python'  # define uma frase de exemplo
dividido = frase.split()  # separa a frase em uma lista de palavras
print(dividido[2][3])  # mostra o quarto caractere da terceira palavra