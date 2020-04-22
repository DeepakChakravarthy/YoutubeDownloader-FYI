#------------------Import Files---------------------#
import os
import pytube
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#---------------------------------------------------#
# Toplevel is used for Supporting the Background Image
top = Toplevel()
def windows():
    window = Toplevel()
    window.mainloop()
    window.withdraw()
top.iconbitmap('YoutubeDownloader.ico')#Icon
top.title("FYI Download Manager :")#Title
top.geometry("900x600")#Resolution
#------Background------------------#
photo = PhotoImage(file = "ytvideo.png")
w = Label(top, image=photo)
w.pack()
#-----------------------------------#
top.resizable(0, 0)#Disable the Maximize
#-----------Close Function--------------#
def close_btn():
    if messagebox.askyesno("FYI...", "Are you Sure you want to exit") == True:
            top.withdraw()
            top.destroy()
            sys.exit()
#----------------------------------------#
var1 = StringVar()
large_font = ('Verdana',15)
url = Entry(top,textvariable= var1,font=large_font).place(x=60, y=300,width=500,height=30)
cancelbtn = Button(top,text="Quit",
                  command=close_btn,
                  activebackground="lightgreen",
                  activeforeground="blue").place(x = 60, y = 450,
                                                   width=200, height=30 )
#--------------Fetching Part from Youtube----------------------#
def get_fetch():
    try:
        if (var1==None):
            print("error")
        dirname = filedialog.askdirectory(parent=top, initialdir="/",title='Please select a directory')
        if (dirname):
            try:
                youtube = pytube.YouTube(var1.get())
                messagebox.showinfo("Download","Downloading...")
                video = youtube.streams.first()
                video.download(dirname)
                messagebox.showinfo(" Downloading.. ", "Thank You.")
            except:
                messagebox.showwarning(" FYI.. ", "Failed")
        else:
            messagebox.showwarning(" FYI. ", "Cancelled")
    except:
        messagebox.showwarning(" FYI. ", "Cancelled")
        top.destroy
        sys.exit()
        import YouTubeScreen
downbtn = Button(top, text = "Download",
                  command = get_fetch,
                  activebackground = "lightgreen",
                  activeforeground = "blue").place(x = 630, y = 450,
                                                   width = 200, height = 30 )
name = Label(top, text="Enter the Link to Download",
             font=('Comic Sans MS',14)).place(x =60,y=200)
label = Label(top)
top.mainloop()
#--------------------------------------------------------------------------#