#-----------------------Files To be Imported-------------------------#
import tkinter
from tkinter import *
from tkinter import messagebox
window = Tk()
def background():#For Images
    top =Toplevel()
    top.mainloop()
    top.withdraw()
#------------Selection Button---------------------#
def button1():
    window.withdraw()
    import YoutubeScreen
def button2():
    window.withdraw()
    import Playlist
def button3():
    window.withdraw()
    import Audio
#-----------Close Function--------------#
def close_btn():
    if messagebox.askyesno("FYI...", "Are you Sure you want to exit") == True:
            window.withdraw()
            window.destroy()
            sys.exit()
#--------------------Buttons And Screen --------------------------#
window.iconbitmap('YoutubeDownloader.ico')
photo = PhotoImage(file = "mainbg.png")
w = Label(window, image=photo)
w.pack()
window.geometry("900x600")
window.resizable(0,0)
window.title("Youtube Downloader")
button1 = Button(window,font= ('Comic Sans MS',14,'bold'),text = "Youtube",command =button1,fg= "white",  bg="#4f0505",
activebackground = "pink",activeforeground = "Blue").place(x = 200, y = 80,height = 50, width = 300)
button2 = Button(window,font= ('Comic Sans MS',14,'bold'),text = "Download Playlist",command =button2,fg= "white",  bg="#4f0505",activebackground = "pink",
activeforeground = "blue").place(x = 300, y = 280,height = 50, width = 300)
button3 = Button(window,font= ('Comic Sans MS',14,'bold'),text = "Download Only Audio",command =button3,fg= "white",  bg="#4f0505",activebackground = "pink",
activeforeground = "blue").place(x = 400, y = 480,height = 50, width = 300)
window.protocol("WM_DELETE_WINDOW",close_btn)
window.mainloop()
#-------------------------------------------------------------------#