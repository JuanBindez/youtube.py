import os
try:
  from pytube import YouTube
  from pytube.cli import on_progress
except ModuleNotFoundError:
  os.system("clear")
  print("você não tem o pytube instalado ,instale com o pip")
import urllib3
import time

link = input("insira o link: ")

yt = YouTube(link, on_progress_callback = on_progress)

print("Titulo = ", yt.title)
print("Baixando...")

ys = yt.streams.get_highest_resolution()

ys.download()

os.system("clear")
time.sleep(2)
print("download concluido")
