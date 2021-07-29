from tkinter import *
from tkinter import ttk
from pygame import mixer
import os
from random import randrange

path = os.path.dirname(os.path.abspath(__file__))
path = path + "\\resources"
audioFile = os.listdir(path)[randrange(0, len(os.listdir(path)))]
mixer.init()

def play():
    global path, audioFile
    mixer.music.load(path + "\\" + audioFile)
    mixer.music.set_volume(0.3)
    mixer.music.play()

root = Tk()
root.title("balls")
ttk.Button(root, text="Balls!", command=play, width=20).grid(row=1, column=0)
root.mainloop()