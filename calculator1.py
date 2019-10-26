from tkinter import *

s = ""
k = ""
root = Tk()
mytext = StringVar()    
f = Frame(root, width = "130", height = "180", bg = "yellow")
l = Text(root, font = "Helvetica 20 bold", bg = "pink", width = 8, height = 1, fg = "blue", wrap = NONE)
myscroll = Scrollbar(root, orient='horizontal', command=l.xview)
l.grid(row=1, sticky='ew')
myscroll.grid(column = 0, row=2, sticky='nsew')
f.grid()
l['xscrollcommand'] = myscroll.set
def num1():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "1")
                l.see(END)
b1 = Button(root, text = "1", command = num1, fg = "brown", bg = "aqua").place(x = 10, y = 70)
def num2():
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "2")
                l.see(END)
b2 = Button(root, text = "2", command = num2, fg = "brown", bg = "aqua").place(x = 40, y = 70)
def num3():
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "3")
                l.see(END)
b3 = Button(root, text = "3", command = num3, fg = "brown", bg = "aqua").place(x = 70, y = 70)
def num4():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "4")
                l.see(END)
b4 = Button(root, text = "4", command = num4, fg = "brown", bg = "aqua").place(x = 10, y = 100)
def num5():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "5")
                l.see(END)
b5 = Button(root, text = "5", command = num5, fg = "brown", bg = "aqua").place(x = 40, y = 100)
def num6():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "6")
                l.see(END)
b6 = Button(root, text = "6", command = num6, fg = "brown", bg = "aqua").place(x = 70, y = 100)
def num7():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "7")
                l.see(END)
b7 = Button(root, text = "7", command = num7, fg = "brown", bg = "aqua").place(x = 10, y = 130)
def num8():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "8")
                l.see(END)
b8 = Button(root, text = "8", command = num8, fg = "brown", bg = "aqua").place(x = 40, y = 130)
def num9():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "9")
                l.see(END)
b9 = Button(root, text = "9", command = num9, fg = "brown", bg = "aqua").place(x = 70, y = 130)
def num0():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "0")
                l.see(END)
b0 = Button(root, text = "0", command = num0, fg = "brown", bg = "aqua").place(x = 10, y = 160)
def plus():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, " + ")
                l.see(END)
bp = Button(root, text = "+", command = plus, fg = "brown", bg = "aqua").place(x = 100, y = 70)
def sub():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, " - ")
                l.see(END)
bs = Button(root, text = "-", command = sub, fg = "brown", bg = "aqua").place(x = 100, y = 100)
def mult():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, " x ")
                l.see(END)
bm = Button(root, text = "X", command = mult, fg = "brown", bg = "aqua").place(x = 100, y = 130)
def div():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, " / ")
                l.see(END)
bd = Button(root, text = "/", command = div, fg = "brown", bg = "aqua").place(x = 100, y = 160)
def exp():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, ".")
                l.see(END)
ep = Button(root, text = ".", command = exp, fg = "brown", bg = "aqua").place(x = 70, y = 190)
def exe():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                try:
                                q = l.get("1.0", END)
                                q = q.replace(" ", "")
                                q = q.replace("x", "*")
                                l.delete('1.0', END)
                                l.insert(END, eval(q));
                except SyntaxError:
                                l.config(font = "Helvetica 10 bold")
                                l.config(fg = "red")
                                l.delete("1.0", END)
                                l.insert(END, "BAD EXPRESSION")
                except ZeroDivisionError:
                                l.config(font = "Helvetica 10 bold")
                                l.config(fg = "red")
                                l.delete("1.0", END)
                                l.insert(END, "NOT DEFINED")
                except NameError:
                                l.config(font = "Helvetica 10 bold")
                                l.config(fg = "red")
                                l.delete("1.0", END)
                                l.insert(END, "BAD EXPRESSION")
                except TypeError:
                                l.config(font = "Helvetica 10 bold")
                                l.config(fg = "red")
                                l.delete("1.0", END)
                                l.insert(END, "BAD EXPRESSION")
be = Button(root, text = "=", command = exe, fg = "brown", bg = "aqua").place(x = 70, y = 160)
    
def clear():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.delete("1.0", END)
                s = ""
                k = ""
bkd = Button(root, text = "C", command = clear, fg = "brown", bg = "aqua").place(x = 40, y = 160)
def de():
                
                if l.get("1.0", "end - 1c") != "BAD EXPRESSION" and l.get("1.0", "end - 1c") != "NOT DEFINED":
                    h = l.get("1.0", "end - 1c")
                    for i in range(len(h) - 1, -1, -1):
                        if h[i] != " ":
                            f = len(h) - i
                            z = h[:(-1 * f)]
                            l.delete("1.0", END)
                            l.insert(END, z)
                            l.update()
                            break
                else:
                    l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                    l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                    l.delete("1.0", END)
                    l.see(END)
bde = Button(root, text = "D", command = de, fg = "brown", bg = "aqua").place(x = 100, y = 190)
def bro():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, "(")
                l.see(END)
bo = Button(root, text = "(", command = bro, fg = "brown", bg = "aqua").place(x = 10, y = 190)
def brc():
                
                l.config(font = "Helvetica 20 bold"); l.config(fg = "blue")
                l.insert(END, ")")
                l.see(END)
bc = Button(root, text = ")", command = brc, fg = "brown", bg = "aqua").place(x = 40, y = 190)
root.resizable(0, 0)
f.mainloop()
