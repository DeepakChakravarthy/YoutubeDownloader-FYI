import os
import pytube
from tkinter import *
from tkinter import messagebox
def GetLink():
    from tkinter import messagebox
    messagebox.showinfo("Youtube Downloader", "Thank You")
top = Tk()
top.title("FYI Download Manager :")
top.geometry("900x600")
top.resizable(0, 0)
radio = IntVar()
def close_btn():
    if messagebox.askyesno("FYI...", "Are you Sure you want to exit") == True:
            top.withdraw()
            sys.exit()
    else:
        pass
name = Label(top, text="Enter the Link to Download",
             font=('Comic Sans MS',14))
name.pack()
var1 = StringVar()
large_font = ('Verdana',15)
url = Entry(top,textvariable= var1,font=large_font).place(x=250, y=218,width=500,height=30)
cancelbtn = Button(top,text="Quit",
                  command=close_btn,
                  activebackground="lightgreen",
                  activeforeground="blue").place(x = 60, y = 450,
                                                   width=200, height=30 )
def get_fetch():
    #Open Directory & save path
    from tkinter import filedialog
    dirname=filedialog.askdirectory(parent=top, initialdir="/",title='Please select a directory')
    #print(dirname)//Check the Location
    youtube = pytube.YouTube(var1.get())
    messagebox.showinfo("Download","Downloading...")
    video = youtube.streams.first()
    messagebox.showinfo
    video.download(dirname)
    messagebox.showinfo(" Downloading.. ", "Thank You.")
downbtn = Button(top, text = "Download",
                  command = get_fetch,
                  activebackground = "lightgreen",
                  activeforeground = "blue").place(x = 630, y = 450,
                                                   width = 200, height = 30 )
top.config(bg='black')
label = Label(top)
top.mainloop()