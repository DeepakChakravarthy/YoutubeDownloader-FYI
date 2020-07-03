import tkinter as tk
from tkinter import Frame, Label, Button, X, LEFT
from tkinter import messagebox
import os
import pywhatkit
from PIL import Image, ImageTk
import Main

#Main.top.withdraw()
window = tk.Tk()
window.overrideredirect(True)
window.geometry("150x400+908+130")

title_bar = Frame(window, bg='#4682b4', relief='ridge', bd=1, highlightcolor='#4682b4',highlightthickness=0)
title_name = Label(title_bar, text="FYIT ADDON", bg='#4682b4', fg="white")

width = 150
height = 400
imgs = Image.open("Assets/addon_bg.png")
imgs = imgs.resize((width, height), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(imgs)
ws = Label(window, image=photoImg)
ws.pack()

def WhatsApp():
	try:
		Main.top.destroy()
		import AutoWhatsApp

	except pywhatkit.InternetException:
		messagebox.showerror("No Internet", "Please Check the Internet Connection.")

def YSearchcall():
	import youtubesearch
	Main.top.destroy()
	'''
	try:
		import youtubesearch
	except pywhatkit.InternetException:
		messagebox.showerror("No Internet","Please Check the Internet Connection.")'''

def closer():
	window.destroy()
	#window.protocol("WM_DELETE_WINDOW")

def call_main():
	import Main
	window.destroy()

def cancel_shutdown():
	try:
		pywhatkit.cancelShutdown()
		messagebox.showinfo("Shutdown Cancelled.", "Shutdown Scheduled time cancelled Successfully.")
	except NameError:
		messagebox.showwarning("No Schedule.", "Shutdown is not been Scheduled.")

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
#MainScreen_call.place(x=10,y=200)
wb_hist.place(x=10, y=250)
clr_shutdown.place(x=10, y=300)
closeButton.place(x=10,y=350)

window.config(bg="green")
window.update()
Main.top.mainloop()
window.mainloop()

def on_close():
    window.destroy()
    #sys.exit()

window.protocol("WM_DELETE_WINDOW", on_close)
