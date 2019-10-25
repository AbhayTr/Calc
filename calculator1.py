from tkinter import *

s = ""
root = Tk()
mytext = StringVar()    
f = Frame(root, width = "130", height = "150", bg = "yellow")
l = Entry(root, font = "Helvetica 20 bold", readonlybackground = "pink", textvariable = mytext, width = 8, state = "readonly")
myscroll = Scrollbar(root, orient='horizontal', command=l.xview)
l.config(xscrollcommand=myscroll.set)
l.grid(row=1, sticky='ew')
myscroll.grid(row=2, sticky='ew')
f.grid()
def num1():
                global s
                s += "1"
                mtext.set(s)
b1 = Button(root, text = "1", command = num1).place(x = 10, y = 70)
def num2():
                global s
                s += "2"
                mytext.set(s)
b2 = Button(root, text = "2", command = num2).place(x = 40, y = 70)
def num3():
                global s
                s += "3"
                mytext.set(s)
b3 = Button(root, text = "3", command = num3).place(x = 70, y = 70)
def num4():
                global s
                s += "4"
                mytext.set(s)
b4 = Button(root, text = "4", command = num4).place(x = 10, y = 100)
def num5():
                global s
                s += "5"
                mytext.set(s)
b5 = Button(root, text = "5", command = num5).place(x = 40, y = 100)
def num6():
                global s
                s += "6"
                mytext.set(s)
b6 = Button(root, text = "6", command = num6).place(x = 70, y = 100)
def num7():
                global s
                s += "7"
                mytext.set(s)
b7 = Button(root, text = "7", command = num7).place(x = 10, y = 130)
def num8():
                global s
                s += "8"
                mytext.set(s)
b8 = Button(root, text = "8", command = num8).place(x = 40, y = 130)
def num9():
                global s
                s += "9"
                mytext.set(s)
b9 = Button(root, text = "9", command = num9).place(x = 70, y = 130)
def num0():
                global s
                s += "0"
                mytext.set(s)
b0 = Button(root, text = "0", command = num0).place(x = 10, y = 160)
def plus():
                global s
                s += " + "
                mytext.set(s)
bp = Button(root, text = "+", command = plus).place(x = 100, y = 70)
def sub():
                global s
                s += " - "
                mytext.set(s)
bs = Button(root, text = "-", command = sub).place(x = 100, y = 100)
def mult():
                global s
                s += " * "
                mytext.set(s)
bm = Button(root, text = "X", command = mult).place(x = 100, y = 130)
def div():
                global s
                s += " / "
                mytext.set(s)
bd = Button(root, text = "/", command = div).place(x = 100, y = 160)
def exe():
                global s
                try:
                                exec("mytext.set(str(" + l.get() + "))")
                                s = l.get()
                                mytext.set(s)
                except SyntaxError:
                                mytext.set("BAD EXPRESSION")
                except ZeroDivisionError:
                                mytext.set("BAD EXPRESSION")
                except NameError:
                                mytext.set("BAD EXPRESSION")
be = Button(root, text = "=", command = exe).place(x = 70, y = 160)
    
def clear():
                global s
                mytext.set("")
                s = ""
bkd = Button(root, text = "C", command = clear).place(x = 40, y = 160)
f.mainloop()
