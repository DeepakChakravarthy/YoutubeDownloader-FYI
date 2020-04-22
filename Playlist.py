#-------------------------Files Required-------------------------------------#
import os
import pytube
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import Playlist
#------------------------------------------------------------------------#
Screen = Toplevel()
#--------------------Support for Background Image------------------------#
def windows():
    window = Toplevel()
    window.mainloop()
    window.withdraw()
#------------------------------------------------------------------------#
Screen.title("FYI Download Manager")
Screen.geometry("900x600")
Screen.iconbitmap('YoutubeDownloader.ico')
photo = PhotoImage(file = "playlist.png")
w = Label(Screen, image=photo)
w.pack()
#-----------------------------------------------------------------------#
Screen.resizable(0, 0)
#---------Close Function----------------------------#
def close_btn():
    if messagebox.askyesno("FYI...", "Are you Sure you want to exit") == True:
            Screen.withdraw()
            Screen.destroy()
            sys.exit()
#-----------------------------------------------------#
var1 = StringVar()
large_font = ('Verdana',15)
url = Entry(Screen,textvariable= var1,font=large_font).place(x=60, y=300,width=500,height=30)
cancelbtn = Button(Screen,text="Quit",
                  command=close_btn,
                  activebackground="lightgreen",
                  activeforeground="blue").place(x = 60, y = 450,
                                                   width=200, height=30 )
#--------------------------------------Fetching from Youtube------------------------#
def get_fetch():
    try:
        if (var1==None):
            print("error")
        dirname = filedialog.askdirectory(parent=Screen, initialdir="/",title='Please select a directory')
        if (dirname):
            try:
                playlist = Playlist(var1.get())
                messagebox.showinfo("Download","Downloading...")
                playlist.download_all(dirname)
                messagebox.showinfo(" Downloading.. ", "Thank You.")
            except:
                messagebox.showwarning(" FYI.. ", "Failed")
        else:
            messagebox.showwarning(" FYI. ", "Cancelled")
    except:
        messagebox.showwarning(" FYI. ", "Cancelled")
        Screen.destroy
        sys.exit()
        import YouTubeScreen
downbtn = Button(Screen, text = "Download",
                  command = get_fetch,
                  activebackground = "lightgreen",
                  activeforeground = "blue").place(x = 630, y = 450,
                                                   width = 200, height = 30 )
name = Label(Screen, text="Enter the Link to Download",
             font=('Comic Sans MS',14)).place(x =60,y=200)
label = Label(Screen)
Screen.mainloop()
#---------------------------------------------------------------------------------#