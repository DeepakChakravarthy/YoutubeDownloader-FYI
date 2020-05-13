# ------------------Import Files-----------------------------------------
import os
import time
import pytube
from pytube import YouTube
from pytube import Playlist
import sys
import re
import requests as r
import wget
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

# Toplevel is used for Supporting the Background Image
top = tk.Tk()
tabControl = ttk.Notebook(top)
DisFont = font = ('Comic Sans MS', 16)
SubFont = font = ('Comic Sans MS', 12)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Youtube')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Facebook',)

tabControl.pack(expand=1, fill="both")
top.iconbitmap('Assets/YoutubeDownloader.ico')     # Icon
top.title("FYI Download Manager :")             # Title
top.geometry("800x500")                         # Resolution

photo = PhotoImage(file="Assets/youtube_bg.png")
w = Label(tab1, image=photo)
w.pack()

photo2 = PhotoImage(file="Assets/facebook_bg.png")
w2 = Label(tab2, image=photo2)
w2.pack()
top.resizable(0, 0)                             # Disable the Maximize

# -----------Close Function--------------------------------------------------
def close_btn():
    if messagebox.askyesno("FYI...", "Are you Sure you want to exit") is True:
        top.withdraw()
        top.destroy()
        top.exit()

# ---------------------------------------------------------------------------
var1 = StringVar()
large_font = ('Verdana', 15)
url = Entry(tab1, textvariable=var1,
                    font=large_font).place(x=60, y=100, width=500, height=30)

cancelbtn = Button(top, text="Quit", font=DisFont, cursor='hand2',
            command=close_btn, activebackground="lightgreen",
            activeforeground="blue").place(x=60, y=430, width=200, height=30)

# --------------Fetching Part from Youtube----------------------------------
def get_fetch():
    resolution = Rvideo.get()
    Select = A_Video.get()
    Selection = A_Audio.get()
    # pb.start()
    try:
        if var1 is None:
            print("error")
        dirname = filedialog.askdirectory(parent=tab1, initialdir="/",
                    title='Please select a directory')
        if dirname:
            try:
                # Video with Resolution
                if resolution <= 3:
                    yt = pytube.YouTube(var1.get())
                    if resolution == 1:
                        progress_bar = ttk.Progressbar(tab1, orient = 'horizontal', length = 500, mode = 'determinate')
                        progress_bar.place(x=60,y=140)
                        progress_bar.start()
                        messagebox.showinfo("Download",
                            "Downloading.. Please Wait for a Minute.")
                        video = yt.streams.get_by_itag(22)
                        video.download(dirname)
                    elif resolution == 2:
                        progress_bar = ttk.Progressbar(tab1, orient = 'horizontal', length = 500, mode = 'determinate')
                        progress_bar.place(x=60,y=140)
                        progress_bar.start()
                        messagebox.showinfo("Download","Downloading...")
                        video = yt.streams.first()
                        video.download(dirname)
                    elif resolution == 3:
                        progress_bar = ttk.Progressbar(tab1, orient = 'horizontal', length = 500, mode = 'determinate')
                        progress_bar.place(x=60,y=140)
                        progress_bar.start()
                        messagebox.showinfo("Download","Downloading...")
                        video = yt.streams.get_by_itag(36)
                        video.download(dirname)
                # Download Playlist
                if Select == 1:
                    playlist = pytube.Playlist(var1.get())
                    progress_bar = ttk.Progressbar(tab1, orient = 'horizontal', length = 500, mode = 'determinate')
                    progress_bar.place(x=60,y=140)
                    progress_bar.start()
                    playlist.populate_video_urls()          # To load bulk list
                    messagebox.showinfo("Download", "Downloading...")
                    playlist.download_all(dirname)

                # Audio files
                if Selection <= 2:
                    link = YouTube(var1.get())
                    format_a = link.streams.filter(only_audio=True).all()
                    if Selection == 1:
                        # mp4
                        progress_bar = ttk.Progressbar(tab1, orient = 'horizontal', length = 500, mode = 'determinate')
                        progress_bar.place(x=60,y=140)
                        progress_bar.start()
                        messagebox.showinfo("Download", "Downloading...")
                        format_a[0].download(dirname)
                    elif Selection == 2:                # webm
                        progress_bar = ttk.Progressbar(tab1, orient = 'horizontal', length = 500, mode = 'determinate')
                        progress_bar.place(x=60,y=140)
                        progress_bar.start()
                        messagebox.showinfo("Download", "Downloading...")
                        format_a[1].download(dirname)
                
                messagebox.showinfo("Downloading.. ", "Thank You.")
            except Exception as a:
                #print(a)
                messagebox.showwarning(" FYI.. ", "Failed")
        else:
            messagebox.showwarning(" FYI. ", "Cancelled")
    except Exception as a:
        messagebox.showwarning(" FYI. ", "Cancelled")
        #print(a)
        sys.exit()

downbtn = Button(tab1, text="Download", font=DisFont,
        command=get_fetch, cursor='hand2', activebackground="lightgreen",
        activeforeground="blue").place(x=500, y=405, width=200, height=30)
name = Label(tab1, text="Enter the Link to Download",
        font=('Comic Sans MS', 16), bg="#520B00", fg="White").place(x=60, y=60)

# -----------------Radio button for video resolution-------------------------
Rvideo = IntVar()
resolution_label = Label(tab1, text="Video Resolution:",
            font=DisFont, bg="#520B00", fg="white").place(x=75, y=160)
R1 = Radiobutton(tab1, text="Mp4 720", cursor='hand2', font=SubFont,
            variable=Rvideo, value=1, command=get_fetch, bg="#520B00",
            fg="white").place(x=80, y=200)
R2 = Radiobutton(tab1, text="Mp4 360px", cursor='hand2', font=SubFont,
            variable=Rvideo, value=2, command=get_fetch, bg="#520B00",
            fg="white").place(x=80, y=240)
R3 = Radiobutton(tab1, text="3gp 144px", cursor='hand2', font=SubFont,
            variable=Rvideo, value=3, command=get_fetch, bg="#520B00",
            fg="white").place(x=80, y=280)

# -----------------Radio button for video to Audio----------------------------
A_Audio = IntVar()
format_label = Label(tab1, text="Only Audio:",
                font=DisFont, bg="#520B00", fg="white").place(x=260, y=160)
R4 = Radiobutton(tab1, text="Mp4 Audio", cursor='hand2',
                font=SubFont, variable=A_Audio, value=1, command=get_fetch,
                bg="#520B00", fg="white").place(x=265, y=200)
R5 = Radiobutton(tab1, text="webm", cursor='hand2', font=SubFont,
                variable=A_Audio, value=2, command=get_fetch,
                bg="#520B00", fg="white").place(x=265, y=240)

# -----------------Radio button for Playlist video --------------------------
A_Video = IntVar()
list_label = Label(tab1, text="Download Playlist:", font=DisFont,
                bg="#520B00", fg="white").place(x=415, y=160)
R7 = Radiobutton(tab1, text="High (Default)", cursor='hand2', font=SubFont,
                variable=A_Video, value=1, command=get_fetch, bg="#520B00",
                fg="white").place(x=420, y=200)

# ======================= Facebook Control ==================================

fb_line = StringVar()
fb_url = Entry(tab2, textvariable=fb_line,
                    font=large_font).place(x=60, y=100, width=500, height=30)

fb_downbtn = Button(tab2, text="Download", font=DisFont,
         cursor='hand2', activebackground="lightgreen",
        activeforeground="blue").place(x=500, y=405, width=200, height=30)
fb_name = Label(tab2, text="Enter the Link to Download",
        font=('Comic Sans MS', 16), bg="#075C90", fg="White").place(x=60, y=60)

# -----------------Radio button for video to Quality--------------------------
fb_link = IntVar()
format_label = Label(tab2, text="Select Video Quality:",
                font=DisFont, bg="#075C90", fg="black").place(x=75, y=160)
F1 = Radiobutton(tab2, text="High", cursor='hand2', font=SubFont,
                variable=fb_link, value=1, bg="#075C90",
                fg="black").place(x=80, y=200)
F2 = Radiobutton(tab2, text="Low", cursor='hand2', font=SubFont,
                variable=fb_link, value=2, bg="#075C90",
                fg="black").place(x=200, y=200)
top.mainloop()
# -----------------------------Close Function--------------------------------
def on_close():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    top.destroy()
top.protocol("WM_DELETE_WINDOW", on_close)
# ---------------------------------------------------------------------------
