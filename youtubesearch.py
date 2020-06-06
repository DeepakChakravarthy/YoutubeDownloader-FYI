import tkinter
import pywhatkit
from tkinter import Label,StringVar, Entry, Button,Tk
Window = Tk()

Window.geometry("500x400")
Window.title("Fast Youtube Search")
Name_Label = Label(Window,text="Fast Search in Youtube")
Name_Label.place(x=150, y=150)
Search_Key = StringVar()
KeyEntry = Entry(Window, textvariable=Search_Key)

def Key():
    pywhatkit.playonyt(Search_Key.get())
KeyEntry.place(x=150,y=180)
Search_Button = Button(Window,text="        Search      ",command=Key)
Search_Button.place(x=270,y=177)
Window.mainloop()
