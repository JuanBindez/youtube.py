import os
try:
  from pytube import YouTube
  from pytube.cli import on_progress
except ModuleNotFoundError:
  os.system("clear")
  print(color.VERMELHO + "você não tem o pytube instalado ,instale com o pip" + color.RESET)
import urllib3
import time

class color():
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    VERDE_CLARO = '\033[1;92m'
    NEGRITO = '\033[;1m'
    RESET = '\033[0m'

link = input(color.VERDE + "insira o link: " + color.RESET)

yt = YouTube(link, on_progress_callback = on_progress)

print(color.AMARELO + "Titulo = " + color.RESET, yt.title)
print(color.AZUL + "Baixando..." + color.RESET)

ys = yt.streams.get_highest_resolution()

ys.download()

os.system("clear")
time.sleep(2)
print(color.VERDE + "download concluido")
