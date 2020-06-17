from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.geometry("200x400+1040+100")
root.resizable(0,0)

with open("pywhatkit_history.txt", "r") as f:
    lb = Label(root, text=f.read()).pack()

root.mainloop()
