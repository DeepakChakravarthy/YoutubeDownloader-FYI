import tkinter
import pywhatkit
from tkinter import Label, StringVar, Entry, Button, Tk
from PIL import Image, ImageTk

Window = Tk()   # bg & fg color : #610536 , #232621
Window.geometry("500x400+400+100")
Window.title("Fast Youtube Search")
Window.resizable(0,0)

cust_font = font = ('Consolas', 14)
width = 500
height = 400
img = Image.open("Assets/ytsearch_bg.png")
img = img.resize((width, height), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
wb = Label(Window, image=photoImg)
wb.pack()

Name_Label = Label(Window, font=cust_font,
                   text="Fast Search in Youtube", bg='#232621', fg='#ffffff')  
Name_Label.place(x=105, y=100,  width=300, height=30)

Search_Key = StringVar()
KeyEntry = Entry(Window, font=cust_font, textvariable=Search_Key)
KeyEntry.place(x=105, y=160, width=320, height=30)

def Key():
    pywhatkit.playonyt(Search_Key.get())

Search_Button = Button(Window, font=cust_font, text="Search", command=Key)
Search_Button.place(x=280, y=280, width=150, height=30)

Window.mainloop()
