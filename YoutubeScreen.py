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
    resolution = var.get()
    print(var.get())
    try:
        if (var1==None):
            print("error")
        dirname = filedialog.askdirectory(parent=top, initialdir="/",title='Please select a directory')
        if (dirname):
            try:
                yt = pytube.YouTube(var1.get())
                #video = yt.filter(progressive=True).all()
                if(resolution == 1):
                  messagebox.showinfo("Download","Downloading...")
                  video = yt.streams.get_by_itag(136)            
                  video.download(dirname)
                elif(resolution == 2):
                  messagebox.showinfo("Download","Downloading...")
                  video = yt.streams.first()
                  video.download(dirname)
                else:
                  messagebox.showinfo("Download","Downloading...")
                  video = yt.streams.get_by_itag(160)
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
        import YoutubeScreen
downbtn = Button(top, text = "Download",
                  command = get_fetch,
                  activebackground = "lightgreen",
                  activeforeground = "blue").place(x = 630, y = 450,
                                                   width = 200, height = 30 )
name = Label(top, text="Enter the Link to Download",
             font=('Comic Sans MS',14)).place(x =60,y=200)
def back():
  top.withdraw()
  import mainscreen
#----------------back button---------------#
#-----------------radio button for video resolution----------------------#
var = IntVar()
R1 = Radiobutton(top,text = "High",variable = var,value=1,command=get_fetch).place(x = 700,y = 300)
R2 = Radiobutton(top,text = "Good",variable = var,value=2,command=get_fetch).place(x = 700,y = 350)
R3 = Radiobutton(top,text = "low",variable = var,value=3,command=get_fetch).place(x = 700,y = 400)
#------------------------back button--------------------------------------#
back = Button(top,text = "back",command = back).place(x = 30, y =35)
label = Label(top)
#--------------------------------------------------------------------------#
def on_close():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    top.destroy()

top.protocol("WM_DELETE_WINDOW",on_close)
top.mainloop()
#--------------------------------------------------------------------------#
