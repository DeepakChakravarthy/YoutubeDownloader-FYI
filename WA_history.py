import tkinter as tk
from tkinter import Label

root = tk.Tk()
root.title("WhatsApp History")
root.iconbitmap("Assest/YoutubeDownloader.ico")
root.geometry("200x400+1040+100")
root.resizable(0,0)

with open("pywhatkit_history.txt", "r") as f:
    lb = Label(root, text=f.read()).pack()

root.mainloop()
