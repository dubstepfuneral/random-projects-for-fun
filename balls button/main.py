from tkinter import *
from tkinter import ttk
from pygame import mixer
import os
from random import randrange
from time import sleep

path = os.path.dirname(os.path.abspath(__file__))
path = path + "\\resources"
audioFile = os.listdir(path)[randrange(0, len(os.listdir(path)))]
mixer.init()

def play():
    global path, audioFile
    mixer.music.load(path + "\\" + audioFile)
    mixer.music.set_volume(0.3)
    mixer.music.play()
    os.system('cls')
    sleep(0.6)
    print('CAN I')
    sleep(0.4)
    print('PUT MY BALLS')
    sleep(1.2)
    print('IN YOUR JAW')
    sleep(1.2)
    print('(YOUR JAAW!)')
    sleep(1)
    print('BALLS IN YO JAW?')
    sleep(2)
    print('CAN I')
    sleep(1.7)
    print('CAN I?')
    sleep(1.6)
    print('(CAN I)')
    sleep(1.4)
    print('CAN I?')

    sleep(1.6)
    print('CAN I')
    sleep(0.4)
    print('PUT MY BALLS')
    sleep(1.1)
    print('IN YOUR JAW')
    sleep(1.2)
    print('(YOUR JAAW!)')
    sleep(1)
    print('BALLS IN YO JAW?')
    sleep(2)
    print('CAN I')
    sleep(1.6)
    print('CAN I?')
    sleep(1.6)
    print('(CAN I)')
    sleep(1.4)
    print('CAN I?')

root = Tk()
root.title("balls")
ttk.Button(root, text="Balls!", command=play, width=20).grid(row=1, column=0)
root.mainloop()