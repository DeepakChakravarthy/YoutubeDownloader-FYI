# ------------------ Packages imported ---------------------------------------------
import pytube
from pytube import YouTube
from pytube import Playlist
import sys
import re
import requests as r
import wget
from tkinter import PhotoImage, Label, StringVar, Entry, Button, IntVar, \
     Radiobutton, messagebox, filedialog, Frame, X, Y, LEFT, RIGHT, \
         N, FLAT, CENTER, Canvas, Scrollbar, VERTICAL, BOTH, SUNKEN, SOLID
import tkinter as tk
from tkinter import ttk
import clipboard
import webbrowser
from tkinterhtml import HtmlFrame
from tkinter import Tk,Menu,Toplevel,Text,Spinbox
import pywhatkit
import time
import sys
import os
from youtubepy import Video
from PIL import Image, ImageTk

# ============================ Window Design ================================

top = Tk()
# - Top is Main Screen  Intialization
# - Menu bar Intialization
def Whatsapp_History():
    import whistory
def openweb():      # Software Update response
    webbrowser.open(url1, new=new)

def update_check():     # AutoCheck Software Update and Sub Screen
    response = r.get(res_url)
    response.raise_for_status()
    if messagebox.askyesno("Software Update",
            "New Update is Availabe, Click yes to install.") is True:
        openweb()

def find_update():              # Check Software Update - 2
    try:
        update_check()
        messagebox.showinfo("FYIT", "Thank You.")
    except r.ConnectionError as e:
        messagebox.showinfo("Connection Error",
                            "Check the Internet Connection")
    except r.exceptions.HTTPError as err:
        messagebox.showinfo("FYIT","No Update yet..")

def Cancel_Shutdown():
    try:
        pywhatkit.cancelShutdown()
        messagebox.showinfo("Shutdown Cancelled.", "Shutdown Scheduled time cancelled Successfully.")
    except NameError:
        messagebox.showwarning("No Schedule.", "Shutdown is not been Scheduled.")

# -----------Close Function--------------------------------------------------

def close_btn():
    if messagebox.askyesno("FYIT..", "Are you Sure you want to exit") is True:
        top.withdraw()
        top.destroy()
        top.exit()

# ---------------------------------------------------------------------------

if (1 ==1):
   try:
    import pywhatkit
   except Exception as e:
    messagebox.showwarning("No Internet or Internet is Slow", "Check Internet Connection")
else:
    messagebox.showwarning("No Internet or Internet is Slow", "Check Internet Connection")

menubar = Menu(top)
menubar.add_cascade(label="Whatsapp History", command=Whatsapp_History)
menubar.add_cascade(label="Cancel Shutdown", command=Cancel_Shutdown)
menubar.add_cascade(label="Check Update",command=find_update)
top.config(bg='black', menu=menubar)

# Styles and Designs Functions for Screens
# Color set for youtube for selectcolor, bg & activebackground #0B1D6F
yt_col = "#0B1D6F"  # Youtube bg Color
# Color set for facebook for selectcolor, bg & activebackground #075C90
fb_col = '#075C90' # Facebook bg Color
col_show = 'white'  # pure white fg
col_select = 'gray'  # gray for activeforeground
COLOR_1 = "#90B3DD" # TabControl Config Color
# Font Style and Size
large_font = font = ('Cascadia Mono', 16)  # style='my.head'
DisFont = font = ('', 14)  # style='my.default'
SubFont = font = ('Consolas', 12)  # style='my.sub'
tab_font = font = ('Consolas', 12)  # Tab font style

# Tab Control Style Config
tab_show = "#90B3DD"
tab_select = "#C8D9EE"

g_black = "#262626"
black = "#000000"

style = ttk.Style()
style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": { "tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [15, 5], "foreground": 'gray', "background": black },
            "map":       {"background": [("selected", g_black)],
                          "foreground": [("selected", 'white')],
                          "expand": [("selected", [2, 3, 2, 0])] } } } )
style.theme_use("yummy")

# ------------------------ Screen and Tab -----------------------------------

style = ttk.Style(top)
style.configure('lefttab.TNotebook', tabposition='sw')
tabControl = ttk.Notebook(top, style='lefttab.TNotebook')

lb = 20
bd = 20

tabimg1 = Image.open("assets/wa.png")
tabimg1 = tabimg1.resize((lb,bd), Image.ANTIALIAS)
timg1 = ImageTk.PhotoImage(tabimg1)

tabimg2 = Image.open("assets/fs.png")
tabimg2 = tabimg2.resize((lb,bd), Image.ANTIALIAS)
timg2 = ImageTk.PhotoImage(tabimg2)

tabimg3 = Image.open("assets/yt.png")
tabimg3 = tabimg3.resize((lb,bd), Image.ANTIALIAS)
timg3 = ImageTk.PhotoImage(tabimg3)

tabimg4 = Image.open("assets/fb.png")
tabimg4 = tabimg4.resize((lb,bd), Image.ANTIALIAS)
timg4 = ImageTk.PhotoImage(tabimg4)

tabimg5 = Image.open("assets/i.png")
tabimg5 = tabimg5.resize((lb,bd), Image.ANTIALIAS)
timg5 = ImageTk.PhotoImage(tabimg5)

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='WhatsApp-MessageSender', image=timg1, compound='left')

tab5 = ttk.Frame(tabControl)
tabControl.add(tab5,text='Fast-YoutubeSearch', image=timg2, compound='left')

tab1 = ttk.Frame(tabControl)        # Tab1 - Youtube
tabControl.add(tab1, text='Youtube-Downloader', image=timg3, compound='left')

tab2 = ttk.Frame(tabControl)        # Tab2 - Facebook
tabControl.add(tab2, text='Facebook-Downloader', image=timg4, compound='left')

tab3 = ttk.Frame(tabControl)        # Tab3 - About
tabControl.add(tab3, text='About', image=timg5, compound='left')

tabControl.pack()

top.iconbitmap('assets/youtubedownloader.ico')  # Window Title Icon
top.title("FYIT Download Manager :")  # Title Label
top.geometry("800x520+100+100")  # Screen Size

photo = PhotoImage(file="assets/youtubebg.png")  # Tab1 Background
w = Label(tab1, image=photo)
w.pack()

photo2 = PhotoImage(file="assets/facebookbg.png")  # Tab2 Background
w2 = Label(tab2, image=photo2)
w2.pack()

top.resizable(0,  0)     # Disable the Maximize & Minimize option

var1 = StringVar()
# Entry Widget for Youtube Downloader Tab
url = Entry(tab1, textvariable=var1, font=large_font, fg='darkblue')
url.place(x=70, y=117, width=500, height=30)

# Entry Widget for Facebook Downloader Tab
url_fb = Entry(tab2, textvariable=var1, font=large_font, fg='darkblue')
url_fb.place(x=70, y=117, width=500, height=30)

# Quit_button placed in tab1
quit_button = Button(tab1,
                         text="Quit",
                         relief=SOLID,
                         font=SubFont,
                         cursor='hand2',
                         command=close_btn)
quit_button.place(x=60, y=400, width=200, height=30)

# ----------------------- Auto URL Paste Functions --------------------------

temp = clipboard.paste()
url.insert('end', temp)
url_fb.insert('end', temp)
var1.set(temp)


def paste():  # Paste text from Clipboard - Function
    variable = clipboard.paste()
    url.insert('end', variable)
    url_fb.insert('end', variable)
    var1.set(variable)

def e1_delete():  # Clear text from Entry - Function
    url.delete(0, 'end')
    url_fb.delete(0, 'end')

def toggle(tog=[0]):  # Toggle Button for clear and paste
    tog[0] = not tog[0]
    if tog[0]:
        t_btn.config(text='Paste')
        t_btn1.config(text='Paste')
        e1_delete()
    else:
        t_btn.config(text='Clear')
        t_btn1.config(text='Clear')
        paste()

# tab1 clear & paste
t_btn1 = ttk.Button(tab1, text="Clear", cursor='hand2', style='my.TButton', command=toggle)
t_btn1.place(x=571, y=118, width=45, height=29)

# tab2 clear & paste
t_btn = ttk.Button(tab2, text="Clear", cursor='hand2', style='my.TButton', command=toggle)
t_btn.place(x=571, y=118, width=45, height=29)

# ------------------ Fetching Part from Youtube ----------------------------

new = 1
url1 = "https://bit.ly/site-fyit"
res_url = "https://github.com/DeepakChakravarthy/YoutubeDownloader-FYI/releases/download/V3.0/FYI.DOWNLOAD.EXE"

# -------------------Youtube Function Call-----------------------------------

def get_fetch():
    resolution = Rvideo.get()
    Select = A_Video.get()
    Selection = A_Audio.get()

    try:
        update_check()
    except r.exceptions.HTTPError as err:
        # - No Updates
	    messagebox.showinfo("FYIT", "Select Location to Save the File.")

    except r.ConnectionError as e:
        messagebox.showinfo("Connection Error", "Check the Internet Connection")

    try:
        if var1 is None:
            print("error")
        dirname = filedialog.askdirectory(parent=tab1,
                                          initialdir="/",
                                          title='Please select a directory:')

        if dirname:
            try:
                # Youtube Video with Resolution
                if resolution <= 3:
                    yt = pytube.YouTube(var1.get())

                    if resolution == 1:
                        progress_bar = ttk.Progressbar(tab1,
                                                       orient='horizontal',
                                                       length=500,
                                                       mode='determinate')
                        progress_bar.place(x=70, y=160)
                        progress_bar.start()
                        messagebox.showinfo(
                            "Download",
                            "Downloading.. Please Wait for a Minute.")
                        video = yt.streams.get_by_itag(22)
                        video.download(dirname)
                        messagebox.showinfo("Downloaded. ", "Thank You..")

                    elif resolution == 2:
                        progress_bar = ttk.Progressbar(tab1,
                                                       orient='horizontal',
                                                       length=500,
                                                       mode='determinate')
                        progress_bar.place(x=70, y=160)
                        progress_bar.start()
                        messagebox.showinfo("Download", "Downloading...")
                        video = yt.streams.first()
                        video.download(dirname)
                        messagebox.showinfo("Downloaded. ", "Thank You..")

                    elif resolution == 3:
                        progress_bar = ttk.Progressbar(tab1,
                                                       orient='horizontal',
                                                       length=500,
                                                       mode='determinate')
                        progress_bar.place(x=70, y=160)
                        progress_bar.start()
                        messagebox.showinfo("Download", "Downloading...")
                        video = yt.streams.get_by_itag(36)
                        video.download(dirname)
                        messagebox.showinfo("Downloaded. ", "Thank You..")

                # Download Playlist
                if Select == 1:
                    playlist = pytube.Playlist(var1.get())
                    progress_bar = ttk.Progressbar(tab1,
                                                   orient='horizontal',
                                                   length=500,
                                                   mode='determinate')
                    progress_bar.place(x=70, y=160)
                    progress_bar.start()
                    playlist.populate_video_urls()  # To load bulk list
                    messagebox.showinfo("Download", "Downloading...")
                    playlist.download_all(dirname)
                    messagebox.showinfo("Downloaded. ", "Thank You..")

                # Audio files
                if Selection <= 2:
                    link = YouTube(var1.get())
                    format_a = link.streams.filter(only_audio=True).all()

                    if Selection == 1:  # mp4
                        progress_bar = ttk.Progressbar(tab1,
                                                       orient='horizontal',
                                                       length=500,
                                                       mode='determinate')
                        progress_bar.place(x=70, y=160)
                        progress_bar.start()
                        messagebox.showinfo("Download", "Downloading...")
                        format_a[0].download(dirname)
                        messagebox.showinfo("Downloaded. ", "Thank You..")

                    elif Selection == 2:  # webm
                        progress_bar = ttk.Progressbar(tab1,
                                                       orient='horizontal',
                                                       length=500,
                                                       mode='determinate')
                        progress_bar.place(x=70, y=160)
                        progress_bar.start()
                        messagebox.showinfo("Download", "Downloading...")
                        format_a[1].download(dirname)
                        messagebox.showinfo("Downloaded. ", "Thank You..")
                messagebox.showinfo("FYIT", "Please Select Valid option")
            except Exception as a:
                messagebox.showwarning(" FYIT.. ", "Failed")
        else:
            messagebox.showwarning(" FYIT. ", "Cancelled")
    except Exception as a:
        messagebox.showwarning(" FYIT. ", "Cancelled")
        sys.exit()

downbtn = Button(tab1,
                 text="Download",
                 relief=SOLID,
                 font=SubFont,
                 command=get_fetch,
                 cursor='hand2' )
downbtn.place(x=500, y=400, width=200, height=30)   # Download button Tab1
yt_label = Label(tab1,
                 text="Enter the Link to Download",
                 font=large_font,
                 bg="#0B1D6F",
                 fg="White")
yt_label.place(x=65, y=65)                          # Label placed in Tab1

# -----------------Radio button for video resolution-------------------------

Rvideo = IntVar()       # Variable Daclaraton for Youtube Video (options)
resolution_label = Label(tab1,
                         text="Video Resolution:",
                         font=DisFont,
                         bg="#0B1D6F",
                         fg="white")
resolution_label.place(x=75, y=200)
R1 = Radiobutton(tab1,
                 text="Mp4 720",
                 cursor='hand2',
                 font=SubFont,
                 variable=Rvideo,
                 value=1,
                 fg=col_show,
                 bg=yt_col,
                 activebackground=yt_col,
                 activeforeground=col_select,
                 selectcolor=yt_col)
R1.place(x=80, y=240)
R2 = Radiobutton(tab1,
                 text="Mp4 360px",
                 cursor='hand2',
                 font=SubFont,
                 variable=Rvideo,
                 value=2,
                 fg=col_show,
                 bg=yt_col,
                 activebackground=yt_col,
                 activeforeground=col_select,
                 selectcolor=yt_col)
R2.place(x=80, y=280)
R3 = Radiobutton(tab1,
                 text="3gp 144px",
                 cursor='hand2',
                 font=SubFont,
                 variable=Rvideo,
                 value=3,
                 fg=col_show,
                 bg=yt_col,
                 activebackground=yt_col,
                 activeforeground=col_select,
                 selectcolor=yt_col)
R3.place(x=80, y=320)

# -----------------Radio button for video to Audio----------------------------

A_Audio = IntVar()      # Variable Daclaraton for Youtube Audio (options)
format_label = Label(tab1,
                     text="Only Audio:",
                     font=DisFont,
                     bg="#0B1D6F",
                     fg="white")
format_label.place(x=260, y=200)
R4 = Radiobutton(tab1,
                 text="Mp4 Audio",
                 cursor='hand2',
                 font=SubFont,
                 variable=A_Audio,
                 value=1,
                 fg=col_show,
                 bg=yt_col,
                 activebackground=yt_col,
                 activeforeground=col_select,
                 selectcolor=yt_col)
R4.place(x=265, y=240)
R5 = Radiobutton(tab1,
                 text="webm",
                 cursor='hand2',
                 font=SubFont,
                 variable=A_Audio,
                 value=2,
                 fg=col_show,
                 bg=yt_col,
                 activebackground=yt_col,
                 activeforeground=col_select,
                 selectcolor=yt_col)
R5.place(x=265, y=280)

# -----------------Radio button for Playlist video --------------------------

A_Video = IntVar()      # Variable Daclaraton for Youtube Playlist (options)
list_label = Label(tab1,
                   text="Download Playlist:",
                   font=DisFont,
                   bg="#0B1D6F",
                   fg="white")
list_label.place(x=415, y=200)
R7 = Radiobutton(tab1,
                 text="High (Default)",
                 cursor='hand2',
                 font=SubFont,
                 variable=A_Video,
                 value=1,
                 fg=col_show,
                 bg=yt_col,
                 activebackground=yt_col,
                 activeforeground=col_select,
                 selectcolor=yt_col)
R7.place(x=420, y=240)

# ======================= Facebook Control ==================================

quit_button = Button(tab2,
                         text="Quit",
                         relief=SOLID,
                         font=SubFont,
                         cursor='hand2',
                         command=close_btn)
quit_button.place(x=60, y=400, width=200, height=30)    # Quit_button placed in tab2
fb_label = Label(tab2,
                 text="Enter the Link to Download",
                 font=large_font,
                 bg="#075C90",
                 fg="White")
fb_label.place(x=65, y=65)      # Label placed in Tab2

def FacebookDownload():         # FacebookDownloader Main Fuction
    try:
        update_check()
    except r.exceptions.HTTPError as err:
	    messagebox.showinfo("FYIT", "Select Location to Download.")
    except r.ConnectionError as e:
        messagebox.showinfo("Connection Error",
                            "Check the Internet Connection")

    try:
        html = r.get(var1.get())
        dirname = filedialog.askdirectory(parent=tab2,
                                          initialdir="/",
                                          title='Please select a directory:')

        if dirname:
            hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
        try:
            hd_url = hdvideo_url.replace('hd_src:"', '')
            messagebox.showinfo("FYIT", "[+] Video Started Downloading")
            progress_bar = ttk.Progressbar(tab2,
                                           orient='horizontal',
                                           length=500,
                                           mode='determinate')
            progress_bar.place(x=60, y=180)
            progress_bar.start()
            wget.download(hd_url, dirname)
            ERASE_LINE = '\x1b[2K'
            sys.stdout.write(ERASE_LINE)
            messagebox.showinfo("FYIT", "Video downloaded")
            progress_bar.stop()
        except r.ConnectionError as e:
            messagebox.showerror("FYIT", "ConnectionError")
        except r.Timeout as e:
            messagebox.showinfo("FYIT", "Tomeout")
        except r.RequestException as e:
            messagebox.showerror("FYIT", "General Error or Invalid URL")
        except (KeyboardInterrupt, SystemExit):
            messagebox.showinfo("FYIT", "SystemExit")
            sys.exit()
        except TypeError:
            messagebox.showerror("FYIT", "Video May Private or InvalidURL")
    except Exception as e:
        messagebox.showwarning("FYIT", "Cancelled")

downbtnfb = Button(tab2,
                   text="Download",
                   relief=SOLID,
                   font=SubFont,
                   command=FacebookDownload,
                   cursor='hand2')
downbtnfb.place(x=500, y=400, width=200, height=30)    # Download placed in Tab2

# ======================= About Tab Control ===================================

def check_it(hyper_link):
    # About tab Redirect Link (Frame1)
    webbrowser.open_new(hyper_link)

tab3_style = ttk.Style()

frame1 = tk.Frame(master=tab3, width=260)           # Tab3_Frame1
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

imge = PhotoImage(file='assets/sidebar.png')
pht = Label(frame1, image=imge)
pht.pack()

link_1 = Label(frame1,
                text="How to use..?",
                font=tab_font,
                fg="blue",
                bg="#90B3DD",
                activeforeground="red",
                activebackground="green",
                cursor="hand2",
                underline=0)
link_1.place(x=20, y=260)
link_1.bind("<Button-1>",
            lambda e: check_it())

link_2 = Label(frame1,
                text="Help..!",
                font=tab_font,
                fg="blue",
                bg="#90B3DD",
                activeforeground="red",
                activebackground="green",
                cursor="hand2",
                underline=0)
link_2.place(x=20, y=300)
link_2.bind("<Button-1>",
            lambda e: check_it("http://bit.ly/site-fyit"))

link_3 = Label(frame1,
               text="Contact us..",
               font=tab_font,
               fg="blue",
               bg="#90B3DD",
               activeforeground="red",
               activebackground="green",
               cursor="hand2",
               underline=0)
link_3.place(x=20, y=340)
link_3.bind("<Button-1>",
            lambda e: check_it("https://gitter.im/FYIT-DOWNLOADER/DEV-FYI?utm_source=share-link&utm_medium=link&utm_campaign=share-link"))

link_4 = Label(frame1,
                text="Visit us..",
                font=tab_font,
                fg="blue",
                bg="#90B3DD",
                activeforeground="red",
                activebackground="green",
                cursor="hand2",
                underline=0)
link_4.place(x=20, y=380)
link_4.bind("<Button-1>",
            lambda e: check_it("http://bit.ly/site-fyit"))

link_5 = Button(frame1,
                text="Check Update..",
                font=tab_font,
                command=find_update,
                fg="blue",
                bg="#90B3DD",
                activeforeground="red",
                activebackground="#90B3DD",
                cursor="hand2",
                relief=FLAT,
                underline=0)
link_5.place(x=20, y=420)
link_5.config(highlightthickness=0)

frame2 = HtmlFrame(master=tab3, width=640, horizontal_scrollbar="auto")     # Tab3_Frame2
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2.set_content(open("assets/help.html", "r").read())

# ----------------------------Fast Youtube Search ----------------

cust_font = font = ('Consolas', 16)
width = 800
height = 500
img1 = Image.open("assets/ytsearchbg.png")
img1 = img1.resize((width, height), Image.ANTIALIAS)
photoImg1 = ImageTk.PhotoImage(img1)
wb1 = Label(tab5, image=photoImg1)
wb1.pack()

Name_Label = Label(tab5, font=cust_font,
                   text="Fast Search in Youtube", bg='#232621', fg='#ffffff')
Name_Label.place(x=130, y=140,  width=280, height=30)

Search_Key = StringVar()

KeyEntry = Entry(tab5, font=cust_font, textvariable=Search_Key)
KeyEntry.place(x=130, y=200, width=550, height=30)

def Key():
    #pywhatkit.playonyt(Search_Key.get())
    #Search_Key Variable to check the Keyword

    Fs_Search = Video(Search_Key.get())
    Out = Fs_Search.search()
    webbrowser.open_new(Out)


Search_Button = Button(tab5, font=cust_font, text="Search", command=Key)
Search_Button.place(x=530, y=320, width=150, height=30)
tab5.update()

# ----------------------- Whatsapp Screen-----------------------------------

cust_font1 = font = ('Consolas', 14)
width1 = 800
height1 = 500
img = Image.open("assets/whatsappbg.png")
img = img.resize((width1, height1), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
wb = Label(tab4, image=photoImg)
wb.pack()

MobNum = StringVar()
Mob2msg = StringVar()
hour = IntVar()
minutes = IntVar()

Number = Label(tab4, text="Enter the Mobile No",
                    font=cust_font1, bg="#1B1B19", fg="#ffffff")
Number.place(x=100, y=70, width=200, height=30)

Message = Label(tab4, text="Enter the Message",
                    font=cust_font1, bg="#1B1B19", fg="#ffffff")
Message.place(x=100, y=120, width=185, height=30)

hourlabel = Label(tab4, text="Enter Schedule Time",
                    font=cust_font1, bg="#1B1B19", fg="#ffffff")
hourlabel.place(x=100, y=260, width=210, height=30)

Shutdown_label = Label(tab4, text="Enter Shutdown Timer",
                    font=cust_font1, bg="#1B1B19", fg="#ffffff")
Shutdown_label.place(x=100, y=310, width=220, height=30)

hrs_label = Label(tab4, text="hrs",
                    font=cust_font1, bg="#1B1B19", fg="#ffffff")
hrs_label.place(x=400, y=260, width=100, height=30)

mins_label = Label(tab4, text="mins.",
                     font=cust_font1, bg="#1B1B19", fg="#ffffff")
mins_label.place(x=560, y=260, width=100, height=30)

shut_label = Label(tab4, text="seconds.",
                   font=cust_font1, bg="#1B1B19", fg="#ffffff")
shut_label.place(x=430, y=310, width=100, height=30)

Entrynum = Entry(tab4, textvariable=MobNum, font=cust_font)
Entrynum.insert(0,"+91")
Entrynum.place(x=350, y=70, width=300, height=30)

Entrymsg = Text(tab4, font=cust_font)
Entrymsg.place(x=350, y=120, width=300, height=120)

hours = Spinbox(tab4, textvariable=hour, font=cust_font, from_=0, to=23)
hours.place(x=350, y=260, width=70, height=30)

mins = Spinbox(tab4, textvariable=minutes, font=cust_font, from_=0, to=59)
mins.place(x=500, y=260, width=70, height=30)

sleep = IntVar()

def shut_timer():
    sh_time = sleep.get()

    if sh_time == 0:
        try:
            pywhatkit.cancelShutdown()
            messagebox.showinfo("Shutdown Timer", "Shutdown timer is not fixed")
        except NameError:
            messagebox.showinfo("Shutdown Timer", "Shutdown timer is not fixed")

    elif sh_time <= 86400:
        messagebox.showinfo("Shutdown Timer", "When we sent WhatsApp message PC will shutdown after fixed timer")
        pywhatkit.shutdown(time=sh_time)
    else:
        messagebox.showinfo("Shutdown Timer", "Shutdown timer is Greater than 24hrs.")

def go():
    messagebox.showinfo("AutoWhatsappMessage",
    "Will open web.whatsapp.com at before 1 minute of Scheduled time and message \
    will be send Automatically at Scheduled time exactly Given")

    try:
        num = MobNum.get()
        msg = Entrymsg.get("1.0", "end-1c")
        hr = hour.get()
        mini = minutes.get()

        if (1 ==1):
            try:
                import pywhatkit
            except Exception as e:
                messagebox.showwarning("No Internet or Internet is Slow", "Check Internet Connection")
        else:
            messagebox.showwarning("No Internet or Internet is Slow", "Check Internet Connection")
        shut_timer()
        pywhatkit.sendwhatmsg(num, msg, hr, mini)
    except pywhatkit.CallTimeException:
        messagebox.showerror("AutoWhatsAppMessage",
                             "Set Schedule time More than 1 minute from Current Time")
    except pywhatkit.CountryCodeException:
        messagebox.showerror("AutoWhatsAppMessage",
                             "Please Ensure the mobile number & Coutry code.")

sleep_time = Spinbox(tab4, textvariable=sleep, font=cust_font, from_=0, to=86399)
sleep_time.place(x=350, y=310, height=30, width=80)

GoCheck = Button(tab4, text="Start Schedule", command=go, font=cust_font)
GoCheck.place(x=300, y=405)




label = Label(tab4,
        text="Time must be in 24 hours Format & Country Code is Must.",
        font=cust_font1, bg="#1B1B19", fg="#ffffff")

infinity = 1
while infinity == 1:
    for i in range(500):
        xpos = i
        label.place(x=xpos, y=20)
        time.sleep(0.01)
        if xpos == 500:
            xpos = 0
        tab4.update()





# ----------------------------- Close Function -------------------------------

top.config(bg='black')

top.mainloop()

def on_close():
    top.destroy()
    sys.exit()

top.protocol("WM_DELETE_WINDOW", on_close)
