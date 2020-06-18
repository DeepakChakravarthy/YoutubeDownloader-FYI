import tkinter as tk
from tkinter import messagebox, StringVar, IntVar, Tk, Entry, \
    Label, PhotoImage, Button, Text, Scrollbar, Y, RIGHT, YES, BOTH, \
    Spinbox
from tkinter import ttk
import pywhatkit
import time
import sys
from PIL import Image, ImageTk

win = Tk()      # Bg_Col #1B1B19
win.geometry("500x400+400+100")
win.resizable(0,0)
win.title("AutoWhatsapp Message")

cust_font = font = ('Consolas', 12)
width = 500
height = 400
img = Image.open("Assets/whatsapp_bg.png")
img = img.resize((width, height), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
wb = Label(win, image=photoImg)
wb.pack()

MobNum = StringVar()
Mob2msg = StringVar()
hour = IntVar()
minutes = IntVar()

Number = Label(win, text="Enter the Mobile No",
                    font=cust_font, bg="#1B1B19", fg="#ffffff")
Number.place(x=55, y=70)

Message = Label(win, text="Enter the Message",
                    font=cust_font, bg="#1B1B19", fg="#ffffff")
Message.place(x=55, y=120)

hourlabel = Label(win, text="Enter Schedule Time",
                    font=cust_font, bg="#1B1B19", fg="#ffffff")
hourlabel.place(x=55, y=220)

Shutdown_label = Label(win, text="Enter Shutdown Timer",
                    font=cust_font, bg="#1B1B19", fg="#ffffff")
Shutdown_label.place(x=55, y=270)

hrs_label = Label(win, text="hrs",
                    font=cust_font, bg="#1B1B19", fg="#ffffff")
hrs_label.place(x=300, y=220)

mins_label = Label(win, text="mins.",
                     font=cust_font, bg="#1B1B19", fg="#ffffff")
mins_label.place(x=390, y=220)

shut_label = Label(win, text="seconds.",
                   font=cust_font, bg="#1B1B19", fg="#ffffff")
shut_label.place(x=340, y=270)

Entrynum = Entry(win, textvariable=MobNum, font=cust_font)
Entrynum.insert(0,"+91")
Entrynum.place(x=250, y=70)

Entrymsg = Text(win, font=cust_font)
Entrymsg.place(x=250, y=120, width=185, height=70)

hours = Spinbox(win, textvariable=hour, font=cust_font, from_=0, to=23)
hours.place(x=250, y=220, width=50)

mins = Spinbox(win, textvariable=minutes, font=cust_font, from_=0, to=59)
mins.place(x=340, y=220, width=50)

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
        shut_timer()
        pywhatkit.sendwhatmsg(num, msg, hr, mini)
    except pywhatkit.CallTimeException:
        messagebox.showerror("AutoWhatsAppMessage",
                             "Set Schedule time More than 1 minute from Current Time")
    except pywhatkit.CountryCodeException:
        messagebox.showerror("AutoWhatsAppMessage",
                             "Please Ensure the mobile number & Coutry code.")

sleep_time = Spinbox(win, textvariable=sleep, font=cust_font, from_=0, to=86399)
sleep_time.place(x=250, y=270, width=80)

GoCheck = Button(win, text="Start Schedule", command=go, font=cust_font)
GoCheck.place(x=160, y=345)

label = Label(win,
        text="Time must be in 24 hours Format & Country Code is Must.",
        font=cust_font, bg="#1B1B19", fg="#ffffff")


infinity = 1
while infinity == 1:
    for i in range(500):
        xpos = i
        label.place(x=xpos, y=20)
        time.sleep(0.01)
        if xpos == 500:
            xpos = 0
        win.update()


def on_close():
    win.destroy()
    #import AddOn
    sys.exit()

win.protocol("WM_DELETE_WINDOW", on_close)

win.mainloop()
