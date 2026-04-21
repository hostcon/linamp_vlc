# ==========================================================
# PLAYER COM VLC (ROBUSTO)
# Prof. Wagner R. da Silva 21/04/2026 02:26 AM
# ==========================================================

import tkinter as tk
from tkinter import filedialog
import vlc
import os

instancia = vlc.Instance()
player = instancia.media_player_new()

playlist = []
index = 0

def carregar():
    arquivos = filedialog.askopenfilenames(filetypes=[("MP3", "*.mp3")])
    for a in arquivos:
        playlist.append(a)
        lista.insert(tk.END, os.path.basename(a))

def tocar():
    global index

    if not playlist:
        return

    media = instancia.media_new(playlist[index])
    player.set_media(media)
    player.play()

    label.config(text=os.path.basename(playlist[index]))

def pausar():
    player.pause()

def parar():
    player.stop()

def proxima():
    global index
    index += 1
    if index >= len(playlist):
        index = 0
    tocar()

def selecionar(event):
    global index
    index = lista.curselection()[0]
    tocar()

# Interface
janela = tk.Tk()
janela.title("Player VLC")
janela.geometry("400x400")

label = tk.Label(janela, text="Nenhuma música")
label.pack()

lista = tk.Listbox(janela)
lista.pack(fill=tk.BOTH, expand=True)
lista.bind("<<ListboxSelect>>", selecionar)

tk.Button(janela, text="Carregar", command=carregar).pack()
tk.Button(janela, text="Play", command=tocar).pack()
tk.Button(janela, text="Pause", command=pausar).pack()
tk.Button(janela, text="Stop", command=parar).pack()
tk.Button(janela, text="Next", command=proxima).pack()

janela.mainloop()
