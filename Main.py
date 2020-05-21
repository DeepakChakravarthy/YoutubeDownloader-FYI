# ------------------Import Files-----------------------------------------
import pytube
from pytube import YouTube
from pytube import Playlist
import sys
import re
import requests as r
import wget
from tkinter import PhotoImage,Label,StringVar,Entry,Button,IntVar,\
Radiobutton,messagebox,filedialog
import tkinter as tk
from tkinter import ttk
import clipboard
# -------------------------------------------------------------------------#
# Toplevel is used for Supporting the Background Image
top = tk.Tk()
tabControl = ttk.Notebook(top)
DisFont = font = ('Comic Sans MS', 16)
SubFont = font = ('Comic Sans MS', 12)

# ------------TAB PROCESS----------------------------------
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

top.resizable(0, 0)

# -----------Close Function--------------------------------------------------
def close_btn():
    if messagebox.askyesno("FYI...", "Are you Sure you want to exit") is True:
        top.withdraw()
        top.destroy()
        top.exit()

# ---------------------------------------------------------------------------
var1 = StringVar()
large_font = ('Verdana', 15)
url = Entry(top, textvariable=var1,
                    font=large_font)
url.place(x=20, y=100, width=500, height=30)

cancelbtn = Button(top, text="Quit", font=DisFont, cursor='hand2',
            command=close_btn, activebackground="lightgreen",
            activeforeground="blue")
cancelbtn.place(x=60, y=430, width=200, height=30)
#---Auto Paste Without Using the Function----#
temp = clipboard.paste()
url.insert('end', temp)
#fburl.insert('end',temp)
var1.set(temp)
#-- Auto paste Function-----#
def paste():
    variable = clipboard.paste()
    url.insert('end', variable)
    #fburl.insert('end',variable)
    var1.set(variable)                         # Disable the Maximize
#---Clear Function-----#
def e1_delete():
    url.delete(0,'end')
#--------------Button for Paste and Clear----#
def toggle(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        t_btn.config(text='paste')
        e1_delete()
    else:
        t_btn.config(text='clear')
        paste()
t_btn = tk.Button(top,text="Clear", width=8, command=toggle)
t_btn.place(x=530,y=100)
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
                messagebox.showwarning(" FYI.. ", "Failed")
        else:
            messagebox.showwarning(" FYI. ", "Cancelled")
    except Exception as a:

        messagebox.showwarning(" FYI. ", "Cancelled")
        #print(a)
        sys.exit()

downbtn = Button(tab1, text="Download", font=DisFont,
        command=get_fetch, cursor='hand2', activebackground="lightgreen",
        activeforeground="blue")
downbtn.place(x=500, y=405, width=200, height=30)
name = Label(top, text="Enter the Link to Download",
        font=('Comic Sans MS', 16), bg="#520B00", fg="White")
name.place(x=60, y=60)

# -----------------Radio button for video resolution-------------------------
Rvideo = IntVar()
resolution_label = Label(tab1, text="Video Resolution:",
            font=DisFont, bg="#520B00", fg="white")
resolution_label.place(x=75, y=160)
R1 = Radiobutton(tab1, text="Mp4 720", cursor='hand2', font=SubFont,
            variable=Rvideo, value=1, command=get_fetch, bg="#520B00",
            fg="white")
R1.place(x=80, y=200)
R2 = Radiobutton(tab1, text="Mp4 360px", cursor='hand2', font=SubFont,
            variable=Rvideo, value=2, command=get_fetch, bg="#520B00",
            fg="white")
R2.place(x=80, y=240)
R3 = Radiobutton(tab1, text="3gp 144px", cursor='hand2', font=SubFont,
            variable=Rvideo, value=3, command=get_fetch, bg="#520B00",
            fg="white")
R3.place(x=80, y=280)

# -----------------Radio button for video to Audio----------------------------
A_Audio = IntVar()
format_label = Label(tab1, text="Only Audio:",
                font=DisFont, bg="#520B00", fg="white")
format_label.place(x=260, y=160)
R4 = Radiobutton(tab1, text="Mp4 Audio", cursor='hand2',
                font=SubFont, variable=A_Audio, value=1, command=get_fetch,
                bg="#520B00", fg="white")
R4.place(x=265, y=200)
R5 = Radiobutton(tab1, text="webm", cursor='hand2', font=SubFont,
                variable=A_Audio, value=2, command=get_fetch,
                bg="#520B00", fg="white")
R5.place(x=265, y=240)

# -----------------Radio button for Playlist video --------------------------
A_Video = IntVar()
list_label = Label(tab1, text="Download Playlist:", font=DisFont,
                bg="#520B00", fg="white")
list_label.place(x=415, y=160)
R7 = Radiobutton(tab1, text="High (Default)", cursor='hand2', font=SubFont,
                variable=A_Video, value=1, command=get_fetch, bg="#520B00",
                fg="white")
R7.place(x=420, y=200)

# ======================= Facebook Control ==================================

#burl = Entry(tab2, textvariable=Var1,
#                    font=large_font)
#fburl.place(x=60, y=100, width=500, height=30)



def FacebookDownload():
    try:
        html = r.get(var1.get())
        dirname = filedialog.askdirectory(parent=tab2, initialdir="/",
                    title='Please select a directory')
        if dirname:
            hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
        try:
            hd_url = hdvideo_url.replace('hd_src:"', '')
            messagebox.showinfo("FYIT","[+] Video Started Downloading")
            progress_bar = ttk.Progressbar(tab2, orient = 'horizontal', length = 500, mode = 'determinate')
            progress_bar.place(x=60,y=140)
            progress_bar.start()
            wget.download(hd_url, dirname)
            ERASE_LINE = '\x1b[2K'
            sys.stdout.write(ERASE_LINE)
            messagebox.showinfo("FYIT","Video downloaded")
            progress_bar.stop()
        except r.ConnectionError as e:
            messagebox.showerror("FYIT","ConnectionError")
        except r.Timeout as e:
            messagebox.showinfo("FYIT","TIMEOUT")
        except r.RequestException as e:
            messagebox.showerror("FYIT","GENRAL ERROR OR INVALID URL")
        except(KeyboardInterrupt,SystemExit):
            messagebox.showinfo("FYIT","SystemExit")
            sys.exit()
        except TypeError:
            messagebox.showerror("FYIT","Video May Private or InvalidURL")
    except Exception as e:
        messagebox.showwarning("FYIT","CANCELED") 
downbtnfb = Button(tab2, text="Download", font=DisFont,
                 command=FacebookDownload, cursor='hand2', activebackground="lightgreen",
                 activeforeground="blue")
downbtnfb.place(x=500, y=405, width=200, height=30)
top.mainloop()
# -----------------------------Close Function--------------------------------
def on_close():
    top.destroy()
    sys.exit()
top.protocol("WM_DELETE_WINDOW", on_close)
# ---------------------------------------------------------------------------
