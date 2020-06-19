import tkinter as tk
from tkinter import Label, messagebox

root = tk.Tk()
root.title("WhatsApp History")
root.iconbitmap("Assets/YoutubeDownloader.ico")
root.geometry("200x400+1040+100")
root.resizable(0,0)
try:
    with open("pywhatkit_history.txt", "r") as f:
        Label(root, text=f.read()).pack()
except FileNotFoundError:
	messagebox.showinfo("WhatsApp History.",
                     "No History found.")

root.mainloop()
