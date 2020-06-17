import tkinter
from tkinter import *
from tkinter import messagebox
import os
import pywhatkit

window = Tk()
window.overrideredirect(True)
window.geometry("150x400+908+130")

title_bar = Frame(window, bg='#4682b4', relief='ridge', bd=1, highlightcolor='#4682b4',highlightthickness=0)
title_name = Label(title_bar, text="FYIT ADDON", bg='#4682b4', fg="white")
#window.iconbitmap('Assets/YoutubeDownloader.ico')

def WhatsApp():
	try:
		window.destroy()
		import AutoWhatsApp
	except pywhatkit.InternetException:
		messagebox.showerror("No Internet", "Please Check the Internet Connection.")

def YSearchcall():
	try:
		window.destroy()
		import youtubesearch
	except pywhatkit.InternetException:
		messagebox.showerror("No Internet","Please Check the Internet Connection.")

def Ysearch():
	window.destroy()
	import youtubesearch
		
def closer():
	window.destroy()
	window.protocol("WM_DELETE_WINDOW")

def call_main():
	import Main
	window.update()
	
def cancel_shutdown():
	try:
		pywhatkit.cancelShutdown()
		messagebox.showinfo("Shutdown Cancelled.", "Shutdown Scheduled time cancelled Successfully.")
	except NameError:
		messagebox.showerror("No Schedule.", "Shutdown time is not defined.")

def show_hist():
	import WA_history

MainScreen_call = Button(window, text="Video Downloader",
                         cursor='hand2', command=call_main)
AppButton = Button(window, text="WhatsApp", cursor='hand2', command=WhatsApp)
AppButton1 = Button(window, text="FastYoutubeSearch",
                    cursor='hand2', command=YSearchcall)
closeButton = Button(window, text="Close", cursor='hand2', command=closer)
clr_shutdown = Button(window, text="Cancel Shutdown",
                      cursor='hand2', command=cancel_shutdown)
wb_hist = Button(window, text="View WhatsApp History",
                      cursor='hand2', command=show_hist)

title_bar.pack(fill=X)
title_name.pack(side=LEFT)

AppButton.place(x=10,y=100)
AppButton1.place(x=10,y=150)
MainScreen_call.place(x=10,y=200)
wb_hist.place(x=10, y=250)
clr_shutdown.place(x=10, y=300)
closeButton.place(x=10,y=350)

window.config(bg="green")
window.update()
window.mainloop()
