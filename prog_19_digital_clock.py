from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Digital Clock")

def time():
    #lbl.config(text="Digital Clock\n")
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Digital-font", 30), background="black", foreground="aqua")
label.pack(anchor='center')
time()

mainloop()