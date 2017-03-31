#!/usr/bin/env python3

# dik-son-ry : Dictionary on the go


import subprocess
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("dik-son-ry")
root.resizable(width=False, height=False)

def quit(event):
    root.destroy()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# word = root.clipboard_get()
word = subprocess.run("xsel", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
cmd = "dict "+ word.stdout
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)

display_text = Text(root)
display_text.pack(side = LEFT,fill = Y)
display_text.insert(END, word.stdout + "\n" + result.stdout)
display_text.config(yscrollcommand=scrollbar.set, state = DISABLED, wrap = WORD)

display_text.tag_add("word", "1.0", "1.end")
display_text.tag_config("word", justify = 'center', font='helvetica 16 bold')

scrollbar.config( command = display_text.yview )

root.bind('<Escape>', quit)
root.mainloop()
