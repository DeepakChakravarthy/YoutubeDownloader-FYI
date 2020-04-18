import tkinter
from tkinter import *
window = Tk()
def button1():
    window.withdraw()
    import YoutubeScreen
def button2():
    window.withdraw()
def button3():
    window.withdraw()
photo = PhotoImage(file = "mainbg.png")
w = Label(window, image=photo)
w.pack()
window.geometry("900x600")
window.resizable(0,0)
button1 = Button(window,font= ('Comic Sans MS',14,'bold'),text = "Youtube",command =button1,fg= "white",  bg="grey",activebackground = "pink").place(x = 200, y = 100,height = 50, width = 300)
button2 = Button(window,font= ('Comic Sans MS',14,'bold'),text = "Download Playlist",command =button2,fg= "white",  bg="grey",activebackground = "pink",
activeforeground = "blue").place(x = 300, y = 280,height = 50, width = 300)
button3 = Button(window,font= ('Comic Sans MS',14,'bold'),text = "Download Only Audio",command =button3,fg= "white",  bg="grey",activebackground = "pink",
activeforeground = "blue").place(x = 400, y = 480,height = 50, width = 300)
window.config(bg="black")
window.mainloop()