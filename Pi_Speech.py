#! /usr/bin/python3
import tkinter.font as font
from tkinter import *
import subprocess, time, sys, os

welcome = str('Welcome to Pi Speech. Change this text, adjust the voice and then click Say it')

root = Tk()
root.title('Pi Speech')
font.nametofont('TkDefaultFont').configure(size=10)
root.resizable(0, 0)

selected = IntVar()
selected.set(1)
textStr = StringVar()
textStr.set(welcome)
subprocess.call('espeak -g 2 -v en-gb {} &'.format('"' + welcome + '"'), shell=True)

def speachHandler():
    if selected.get() == 1:
        speakPi('en-gb')
    elif selected.get() == 2:
        speakPi('en-uk-north')
    elif selected.get() == 3:
        speakPi('en-uk-wmids')
    elif selected.get() == 4:
        speakPi('en-sc')
    elif selected.get() == 5:
        speakPi('cy')
    elif selected.get() == 6:
        speakPi('en-us')
    elif selected.get() == 7:
        speakPi('ru')
    elif selected.get() == 8:
        speakPi('de')
    elif selected.get() == 9:
        speakPi('it')
    elif selected.get() == 10:
        speakPi('sv')
    elif selected.get() == 11:
        speakPi('tr')
    elif selected.get() == 12:
        speakPi('es')

def speakPi(thisVoice):
    subprocess.call('espeak -g 2 -v {} {}'.format(thisVoice, '"' + textStr.get() + '"'), shell=True)

Label(root, text='Select voice:').grid(row=0, column=0, padx=5, pady=5)
Radiobutton(root, text='English', width=10, variable=selected, value=1).grid(row=0, column=1, padx=5, pady=5)
Radiobutton(root, text='Geordie', width=10, variable=selected, value=2).grid(row=0, column=2, padx=5, pady=5)
Radiobutton(root, text='West Mids', width=10,  variable=selected, value=3).grid(row=0, column=3, padx=5, pady=5)
Radiobutton(root, text='Scottish', width=10, variable=selected, value=4).grid(row=0, column=4, padx=5, pady=5)
Radiobutton(root, text='Welsh', width=10,  variable=selected, value=5).grid(row=0, column=5, padx=5, pady=5)
Radiobutton(root, text='Polish', width=10,  variable=selected, value=6).grid(row=0, column=6, padx=5, pady=5)
Radiobutton(root, text='Russian', width=10,  variable=selected, value=7).grid(row=1, column=1, padx=5, pady=5)
Radiobutton(root, text='German', width=10,  variable=selected, value=8).grid(row=1, column=2, padx=5, pady=5)
Radiobutton(root, text='Italian', width=10,  variable=selected, value=9).grid(row=1, column=3, padx=5, pady=5)
Radiobutton(root, text='Swedish', width=10,  variable=selected, value=10).grid(row=1, column=4, padx=5, pady=5)
Radiobutton(root, text='Turkish', width=10,  variable=selected, value=11).grid(row=1, column=5, padx=5, pady=5)
Radiobutton(root, text='Spanish', width=10,  variable=selected, value=12).grid(row=1, column=6, padx=5, pady=5)
Entry(root, textvariable=textStr, width=100).grid(row=3, rowspan=3, column=0, columnspan=6, padx=5, pady=5)
Button(root, text='Say it!', width=10, fg='red', command=speachHandler).grid(row=3, rowspan=3, column=6, padx=5, pady=5)

root.mainloop()
