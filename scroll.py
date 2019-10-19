from tkinter import *
from tkinter import ttk

root = Tk()

mytext = StringVar()
myframe = Frame(root)
myentry = Entry(myframe, font = "bold 30", state = "readonly", textvariable = mytext, fg = "blue", readonlybackground = "yellow")
mytext.set("Hellojdhdjrjdjjsjsjdjdjdjeiieisjejdjsjjejeueidisoskskieiskskdkkeks")
myscroll = Scrollbar(myframe, orient='horizontal', command=myentry.xview)
myentry.config(xscrollcommand=myscroll.set)

myframe.grid()
myentry.grid(row=1, sticky='ew')
myscroll.grid(row=2, sticky='ew')

root.mainloop()