#-------------------Files Required-----------------------#
import os
import pytube
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
#-------------------------------------------#
Display = Toplevel()
def windows():#Support For Background Image
    window = Toplevel()
    window.mainloop()
    window.withdraw()
#--------------------------------------------#
#-------------------Screen-------------------#
Display.title("FYI Download Manager :")
Display.geometry("900x600")
Display.iconbitmap('YoutubeDownloader.ico')
photo = PhotoImage(file = "mp3.png")
w = Label(Display, image=photo)
w.pack()
Display.resizable(0, 0)
#-------------------Close Functions----------------------#
def close_btn():
    if messagebox.askyesno("FYI...", "Are you Sure you want to exit") == True:
            Display.withdraw()
            Display.destroy()
            sys.exit()
#----------------------------------------Widgets---------------------#
var1 = StringVar()
large_font = ('Verdana',15)
url = Entry(Display,textvariable= var1,font=large_font).place(x=60, y=300,width=500,height=30)
cancelbtn = Button(Display,text="Quit",
                  command=close_btn,
                  activebackground="lightgreen",
                  activeforeground="blue").place(x = 60, y = 450,
                                                   width=200, height=30 )
#---------------------------Fetch From YouTube--------------------------#
def get_fetch():
    try:
        if (var1==None):
            print("error")
        dirname = filedialog.askdirectory(parent=Display, initialdir="/",title='Please select a directory')
        if (dirname):
            try:
                link=YouTube(var1.get())
                format_a=link.streams.filter(only_audio=True)
                messagebox.showinfo("Download","Downloading...")
                format_a[0].download(dirname)
                messagebox.showinfo(" Downloading.. ", "Thank You.")
            except:
                messagebox.showwarning(" FYI.. ", "Failed")
        else:
            messagebox.showwarning(" FYI. ", "Cancelled")
    except:
        messagebox.showwarning(" FYI. ", "Cancelled")
        Display.destroy
        sys.exit()
        import YouTubeScreen
downbtn = Button(Display, text = "Download",
                  command = get_fetch,
                  activebackground = "lightgreen",
                  activeforeground = "blue").place(x = 630, y = 450,
                                                   width = 200, height = 30 )
name = Label(Display, text="Enter the Link to Download",
             font=('Comic Sans MS',14)).place(x =60,y=200)
label = Label(Display)
Display.mainloop()
#-------------------------------------------------------------------------------#