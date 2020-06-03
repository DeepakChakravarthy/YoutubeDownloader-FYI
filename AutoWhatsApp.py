from tkinter import *
import tkinter
import tkinter 
from tkinter import messagebox,StringVar,IntVar,Tk,Button,Entry
from tkinter import ttk
import pywhatkit
import time

win = Tk()
win.geometry("500x400")
win.title("AutoWhatsapp Message")
#messagebox.showinfo("AutoWhatsappMessage","ENTER THE TIME IN (24 Hours) FORMAT")

MobNum = StringVar()
Mob2msg=StringVar()
hour = IntVar()
minutes=IntVar()

Number =ttk.Label(win,text="Enter the Mobile with CountryCode")
Number.place(x=50,y=25)
Message = ttk.Label(win,text = "Enter the Message")
Message.place(x=50,y =100)
hourlabel = ttk.Label(win,text = "Enter the Hours")
hourlabel.place(x=50, y=200)
minuteslabel =ttk.Label(win,text = "Enter the minutes")
minuteslabel.place(x=50, y=250)
Entrynum = Entry(win,textvariable=MobNum)
Entrynum.place(x =250,y=25)
Entrymsg= Entry(win,textvariable=Mob2msg)
Entrymsg.place(x=250, y=100)
timehour= Entry(win,textvariable=hour)
timehour.place(x=250, y=200)
timeminutes = Entry(win, textvariable=minutes)
timeminutes.place(x=250, y=250)


ypos = 100
label = Label(win, text="Schedule Time must be in 24 hours Format.")

xpos = 0

def go():
	messagebox.showinfo("AutoWhatsappMessage","Will open web.whatsapp.com at before 1 minute of Scheduled time and message will be sent Automatically at Scheduled time exactly Given")
        try:
            num = MobNum.get()
            msg = Mob2msg.get()
            hr = hour.get()
            mini = minutes.get()
            pywhatkit.sendwhatmsg(num,msg,hr,mini)
        except pywhatkit.CallTimeException:
            messagebox.showalert("AutoWhatsAppMessage", "Set Schedule time More than 1 minute from Current Time")
        except pywhatkit.CountryCodeException:
            messagebox.showalert("AutoWhatsAppMessage", "Please Ensure the mobile number & Coutry code.")


GoCheck =ttk.Button(win,text="Start",command=go)
GoCheck.place(x=200, y=350)
infinity= 1
while infinity==1:
    for i in range(260):
    	xpos = i
    	label.place(x=xpos,y=0)
    	time.sleep(0.01)
    	if (xpos==260):
    		xpos = 0
    	win.update()
# Will open web.whatsapp.com at before 1 minute of Scheduled time and message will be sent at exactly Scheduled time.

win.mainloop()
