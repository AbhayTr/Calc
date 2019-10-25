from tkinter import *

s = ""
k = ""
root = Tk()
mytext = StringVar()    
f = Frame(root, width = "130", height = "180", bg = "yellow")
l = Entry(root, font = "Helvetica 20 bold", readonlybackground = "pink", textvariable = mytext, width = 8, state = "readonly")
myscroll = Scrollbar(root, orient='horizontal', command=l.xview)
l.config(xscrollcommand=myscroll.set)
l.grid(row=1, sticky='ew')
myscroll.grid(row=2, sticky='ew')
f.grid()
def num1():
                global s; global k
                s += "1"
                k += "1"
                mtext.set(s)
b1 = Button(root, text = "1", command = num1).place(x = 10, y = 70)
def num2():
                global s; global k
                s += "2"
                k += "2"
                mytext.set(s)
b2 = Button(root, text = "2", command = num2).place(x = 40, y = 70)
def num3():
                global s; global k
                s += "3"
                k += "3"
                mytext.set(s)
b3 = Button(root, text = "3", command = num3).place(x = 70, y = 70)
def num4():
                global s; global k
                s += "4"
                k += "4"
                mytext.set(s)
b4 = Button(root, text = "4", command = num4).place(x = 10, y = 100)
def num5():
                global s; global k
                s += "5"
                k += "5"
                mytext.set(s)
b5 = Button(root, text = "5", command = num5).place(x = 40, y = 100)
def num6():
                global s; global k
                s += "6"
                k += "6"
                mytext.set(s)
b6 = Button(root, text = "6", command = num6).place(x = 70, y = 100)
def num7():
                global s; global k
                s += "7"
                k += "7"
                mytext.set(s)
b7 = Button(root, text = "7", command = num7).place(x = 10, y = 130)
def num8():
                global s; global k
                s += "8"
                k += "8"
                mytext.set(s)
b8 = Button(root, text = "8", command = num8).place(x = 40, y = 130)
def num9():
                global s; global k
                s += "9"
                k += "9"
                mytext.set(s)
b9 = Button(root, text = "9", command = num9).place(x = 70, y = 130)
def num0():
                global s; global k
                s += "0"
                k += "0"
                mytext.set(s)
b0 = Button(root, text = "0", command = num0).place(x = 10, y = 160)
def plus():
                global s; global k
                s += " + "
                k += "+"
                mytext.set(s)
bp = Button(root, text = "+", command = plus).place(x = 100, y = 70)
def sub():
                global s; global k
                s += " - "
                k += "-"
                mytext.set(s)
bs = Button(root, text = "-", command = sub).place(x = 100, y = 100)
def mult():
                global s; global k
                s += " x "
                k += "*"
                mytext.set(s)
bm = Button(root, text = "X", command = mult).place(x = 100, y = 130)
def div():
                global s; global k
                s += " / "
                k += "/"
                mytext.set(s)
bd = Button(root, text = "/", command = div).place(x = 100, y = 160)
def exe():
                global s; global k
                try:
                                exec("mytext.set(" + k + ")")
                                k = l.get()
                                s = str(l.get())
                                mytext.set(s)
                except SyntaxError:
                                mytext.set("BAD EXPRESSION")
                except ZeroDivisionError:
                                mytext.set("BAD EXPRESSION")
                except NameError:
                                mytext.set("BAD EXPRESSION")
be = Button(root, text = "=", command = exe).place(x = 70, y = 160)
    
def clear():
                global s; global k
                mytext.set("")
                s = ""
                k = ""
bkd = Button(root, text = "C", command = clear).place(x = 40, y = 160)
def de():
                global s; global k
                k = k[:-1]
                for i in range(len(s) - 1, -1, -1):
                    if s[i] != " ":
                        f = len(s) - i
                        s = s[:(-1 * f)]
                        mytext.set(s)
                        break
bde = Button(root, text = "D", command = de).place(x = 100, y = 190)
def bro():
                global s; global k
                s += "("
                mytext.set(s)
bo = Button(root, text = "(", command = bro).place(x = 10, y = 190)
def brc():
                global s; global k
                s += ")"
                mytext.set(s)
bc = Button(root, text = ")", command = brc).place(x = 40, y = 190)
root.resizable(0, 0)
f.mainloop()
