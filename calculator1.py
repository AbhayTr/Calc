from tkinter import *

root = Tk()
f = Frame(root, width = "130", height = "150", bg = "yellow")
l = Label(root,  font = "Helvetica 20 bold", bg = "pink")
def num1():
                s = l["text"]
                s += "1"
                l.config(text = s)
b1 = Button(root, text = "1", command = num1).place(x = 10, y = 40)
def num2():
                s = l["text"]
                s += "2"
                l.config(text = s)
b2 = Button(root, text = "2", command = num2).place(x = 40, y = 40)
def num3():
                s = l["text"]
                s += "3"
                l.config(text = s)
b3 = Button(root, text = "3", command = num3).place(x = 70, y = 40)
def num4():
                s = l["text"]
                s += "4"
                l.config(text = s)
b4 = Button(root, text = "4", command = num4).place(x = 10, y = 70)
def num5():
                s = l["text"]
                s += "5"
                l.config(text = s)
b5 = Button(root, text = "5", command = num5).place(x = 40, y = 70)
def num6():
                s = l["text"]
                s += "6"
                l.config(text = s)
b6 = Button(root, text = "6", command = num6).place(x = 70, y = 70)
def num7():
                s = l["text"]
                s += "7"
                l.config(text = s)
b7 = Button(root, text = "7", command = num7).place(x = 10, y = 100)
def num8():
                s = l["text"]
                s += "8"
                l.config(text = s)
b8 = Button(root, text = "8", command = num8).place(x = 40, y = 100)
def num9():
                s = l["text"]
                s += "9"
                l.config(text = s)
b9 = Button(root, text = "9", command = num9).place(x = 70, y = 100)
def num0():
                s = l["text"]
                s += "0"
                l.config(text = s)
b0 = Button(root, text = "0", command = num0).place(x = 10, y = 130)
def plus():
                s = l["text"]
                s += " + "
                l.config(text = s)
bp = Button(root, text = "+", command = plus).place(x = 100, y = 40)
def sub():
                s = l["text"]
                s += " - "
                l.config(text = s)
bs = Button(root, text = "-", command = sub).place(x = 100, y = 70)
def mult():
                s = l["text"]
                s += " * "
                l.config(text = s)
bm = Button(root, text = "X", command = mult).place(x = 100, y = 100)
def div():
                s = l["text"]
                s += " / "
                l.config(text = s)
bd = Button(root, text = "/", command = div).place(x = 100, y = 130)
def exe():
                try:
                                s = l["text"]
                                exec("l.config(text = " + s + ")")
                                z = str(l["text"])
                                l.config(text = z)
                except SyntaxError:
                                l.config(text = "BAD EXPRESSION")
be = Button(root, text = "=", command = exe).place(x = 70, y = 130)

def clear():
                l.config(text = "")
bkd = Button(root, text = "C", command = clear).place(x = 40, y = 130)

l.pack()
f.pack()
f.mainloop()
