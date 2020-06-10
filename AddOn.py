import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()

window.overrideredirect(True)


window.geometry("130x400+1000+80")

title_bar = Frame(window, bg='#4682b4', relief='ridge', bd=1, highlightcolor='#4682b4',highlightthickness=0)

title_name = Label(title_bar, text="FYIT ADDON", bg='#4682b4', fg="white")
#window.iconbitmap('YoutubeDownloader.ico')
def WhatsApp():
        from Main import minimize
        import AutoWhatsApp
def Ysearch():
	import youtubesearch
def closer():
        window.destroy()
        window.protocol("WM_DELETE_WINDOW")

AppButton =Button(window,text="WhatsApp",command = WhatsApp)
AppButton1 =Button(window,text="FastYoutubeSearch",command = Ysearch)
closeButton = Button(window,text ="Close",command = closer)
title_bar.pack(fill=X)
title_name.pack(side=LEFT)
AppButton.place(x=25,y=100)
AppButton1.place(x=10,y=200)
closeButton.place(x=65,y=300)
window.config(bg="green")
window.mainloop()
