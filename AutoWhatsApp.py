import tkinter as tk
from tkinter import messagebox, StringVar, IntVar, Tk, Entry, \
    Label, PhotoImage, Button, Text, Scrollbar, Y, RIGHT, YES, BOTH
from tkinter import ttk
import pywhatkit
import time
from PIL import Image, ImageTk

win = Tk()      # Bg_Col #1B1B19
win.geometry("500x400+400+100")
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

hourlabel = Label(win, text="Enter the Hours",
                    font=cust_font, bg="#1B1B19", fg="#ffffff")
hourlabel.place(x=55, y=220)

minuteslabel = Label(win, text="Enter the minutes", 
                    font=cust_font, bg="#1B1B19", fg="#ffffff")
minuteslabel.place(x=55, y=270)

Entrynum = Entry(win, textvariable=MobNum, font=cust_font)
Entrynum.place(x=250, y=70)

Entrymsg = Text(win, font=cust_font)
Entrymsg.place(x=250, y=120, width=185, height=70)

timehour = Entry(win, textvariable=hour, font=cust_font)
timehour.place(x=250, y=220)

timeminutes = Entry(win, textvariable=minutes, font=cust_font)
timeminutes.place(x=250, y=270)

def go():
    messagebox.showinfo("AutoWhatsappMessage", 
    "Will open web.whatsapp.com at before 1 minute of Scheduled time and message \
    will be send Automatically at Scheduled time exactly Given")
    try:
        num = MobNum.get()
        msg = Entrymsg.get("1.0", "end-1c")
        hr = hour.get()
        mini = minutes.get()
        pywhatkit.sendwhatmsg(num, msg, hr, mini)
    except pywhatkit.CallTimeException:
        messagebox.showalert("AutoWhatsAppMessage",
                             "Set Schedule time More than 1 minute from Current Time")
    except pywhatkit.CountryCodeException:
        messagebox.showalert("AutoWhatsAppMessage",
                             "Please Ensure the mobile number & Coutry code.")
    except pywhatkit.InternetException:
        messagebox.showalert("No Internet",
                             "Please Check the Internet Connection.")

GoCheck = Button(win, text="Start Schedule", command=go, font=cust_font)
GoCheck.place(x=160, y=345)

label = Label(win, 
        text="Time must be in 24 hours Format & Country Code is Must.", 
        font=cust_font, bg="#1B1B19", fg="#ffffff")
import AddOn
infinity = 1
while infinity == 1:
    for i in range(500):
        xpos = i
        label.place(x=xpos, y=20)
        time.sleep(0.01)
        if (xpos == 500):
            xpos = 0
        win.update()

        
def on_close():
    win.destroy()
    #import AddOn
    sys.exit()

win.protocol("WM_DELETE_WINDOW", on_close)
import AddOn
win.mainloop()
