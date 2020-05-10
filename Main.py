#------------------Import Files-------------------------------------------------
import os
import time
import pytube
from pytube import YouTube
from pytube import Playlist
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk


# Toplevel is used for Supporting the Background Image
top = tk.Tk()
tabControl=ttk.Notebook(top)

DisFont = font=('Comic Sans MS',14)
SubFont = font=('Comic Sans MS',12)
#self.progressBar()
tab1=ttk.Frame(tabControl)
tabControl.add(tab1, text='Youtube')

tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text='Facebook',)

tabControl.pack(expand=1, fill="both")
top.iconbitmap('YoutubeDownloader.ico')         # Icon
top.title("FYI Download Manager :")             # Title
top.geometry("800x500")                         # Resolution
#photo = PhotoImage(file = "mainbg.png")
#w = Label(tab1, image=photo)
#w.pack()
top.resizable(0, 0)                             # Disable the Maximize
#-----------Close Function-----------------------------------------------------
def close_btn():
    if messagebox.askyesno("FYI...", "Are you Sure you want to exit") == True:
            top.withdraw()
            top.destroy()
            top.exit()

#------------------------------------------------------------------------------
var1 = StringVar()
large_font = ('Verdana',15)
url = Entry(tab1,textvariable= var1,font=large_font).place(x=60, y=100,width=500,height=30)

cancelbtn = Button(top,text="Quit",font = DisFont, cursor = 'hand2',command=close_btn,
                activebackground="lightgreen",activeforeground="blue").place(x = 60, y = 430,
                width=200, height=30 )

#----------------------Progress Loader----------------------------------------
#--------------Fetching Part from Youtube--------------------------------------
def get_fetch():
    resolution = Rvideo.get()
    Select = A_Video.get()
    Selection = A_Audio.get()
    #pb.start()
    try:
        if var1 is None:
            print("error")
        dirname = filedialog.askdirectory(parent=tab1, initialdir="/", title='Please select a directory')
        if (dirname):
            try:
                #   Video with Resolution
                if (resolution <= 3):
                    yt = pytube.YouTube(var1.get())
                    if(resolution == 1):
                        progress_bar = ttk.Progressbar(tab1, orient = 'horizontal', length = 286, mode = 'determinate')
                        progress_bar.place(x=60,y=140)
                        progress_bar.start()
                        messagebox.showinfo("Download","Please Wait for a Minute and Give Ok")
                        video = yt.streams.get_by_itag(136)
                        video.download(dirname)

                        #messagebox.showinfo(" Downloading.. ", "Thank You.")
                    elif(resolution == 2):
                        #messagebox.showinfo("Download","Downloading...")
                        video = yt.streams.first()
                        video.download(dirname)
                        #messagebox.showinfo(" Downloading.. ", "Thank You.")
                    elif(resolution ==3):
                        #messagebox.showinfo("Download","Downloading...")
                        video = yt.streams.get_by_itag(160)
                        video.download(dirname)
                        #messagebox.showinfo(" Downloading.. ", "Thank You.")

                #----Download Playlist----#
                if (Select == 1):
                    playlist = pytube.Playlist(var1.get())
                    playlist.populate_video_urls()                      # To load bulk list
                    messagebox.showinfo("Download","Downloading...")
                    playlist.download_all(dirname)

                #------Audio------#
                if(Selection <= 2):
                    link=YouTube(var1.get())
                    format_a=link.streams.filter(only_audio=True).all()
                    if(Selection==1):           #mp4
                        messagebox.showinfo("Download","Downloading...")
                        format_a[0].download(dirname)
                    elif(Selection==2):         #webm
                        messagebox.showinfo("Download","Downloading...")
                        format_a[1].download(dirname)
                progress_bar.stop()
                messagebox.showinfo(" Downloading.. ", "Thank You.")
            except:
                messagebox.showwarning(" FYI.. ", "Failed")
        else:
            messagebox.showwarning(" FYI. ", "Cancelled")
    except:
        messagebox.showwarning(" FYI. ", "Cancelled")
        sys.exit()

downbtn = Button(tab1, text = "Download", font = DisFont,
                  command = get_fetch,cursor = 'hand2',
                  activebackground = "lightgreen",
                  activeforeground = "blue").place(x = 500, y = 405,
                                                   width = 200, height = 30 )
name = Label(tab1, text="Enter the Link to Download",
             font=('Comic Sans MS',14),bg="black",fg="White").place(x=60,y=60)

#-----------------Radio button for video resolution----------------------------
Rvideo = IntVar()
resolution_label = Label(tab1, text="Video Resolution:",
             font=DisFont,fg="black").place(x=75,y=160)
R1 = Radiobutton(tab1,text = "Mp4 720",cursor = 'hand2',font=SubFont,variable =Rvideo,value=1,
                        command=get_fetch).place(x = 80,y = 200)
R2 = Radiobutton(tab1,text = "Mp4 360px",cursor = 'hand2',font=SubFont,variable=Rvideo,value=2,
                        command=get_fetch).place(x = 80,y = 240)
R3 = Radiobutton(tab1,text = "3gp 144px",cursor = 'hand2',font=SubFont,variable =Rvideo,value=3,
                        command=get_fetch).place(x = 80,y = 280)

#-----------------Radio button for video to Audio------------------------------
A_Audio = IntVar()
format_label = Label(tab1, text="Only Audio:",
             font=DisFont, fg="black").place(x=260,y=160)
R4 = Radiobutton(tab1,text = "Mp4 Audio",cursor = 'hand2',font=SubFont,variable =A_Audio,value=1,
                        command=get_fetch).place(x = 265,y = 200)
R5 = Radiobutton(tab1,text = "webm",cursor = 'hand2',font=SubFont,variable =A_Audio,value=2,
                        command=get_fetch).place(x = 265,y = 240)
#-----------------Radio button for Playlist video -----------------------------
A_Video = IntVar()
list_label = Label(tab1, text="Download Playlist:",
             font=DisFont,fg="black").place(x=430,y=160)
R7 = Radiobutton(tab1, text = "High (Default)", cursor='hand2', font=SubFont, variable=A_Video, value=1,
                        command=get_fetch).place(x = 430,y = 200)

#-----------------------------Close Function-----------------------------------
def on_close():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    top.destroy()

top.protocol("WM_DELETE_WINDOW", on_close)
top.mainloop()
#------------------------------------------------------------------------------
