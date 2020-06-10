from tkinter import *
from AutoWhatsApp import vari

master = Tk()

end_hr = Spinbox(master, from_=0, to=23)
end_hr.pack()

end_min = Spinbox(master, from_=0, to=59)
end_min.pack()

def pr():
    ehr = end_hr.get()
    emin = end_min.get()
    print(ehr)
    print(emin)
    #print(shr)

print(vari.smin)

bt = Button(master, text="clic", command=vari)
bt.pack() 

mainloop()
