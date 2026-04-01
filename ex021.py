import pyglet  # importa a biblioteca pyglet para tocar áudio

music = pyglet.media.load("ex021.mp3")  # carrega o arquivo de música
music.play()  # inicia a reprodução do áudio
pyglet.app.run()  # mantém o programa em execução para tocar a música