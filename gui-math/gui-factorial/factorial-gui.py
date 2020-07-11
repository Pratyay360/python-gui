import tkinter as tk
from tkinter import *
#file which is going to create is answer.txt
def save(e):
    open("answer.txt", "w+").close()
    text = str(fact(int(e.get())))
    with open("answer.txt", "a") as f:
        f.write(text)


def loadme(l):
    f = open('answer.txt', 'r')
    line = f.readline()
    la1 = line.split()
    l.config(text=la1)
    f.close()

def fact(n):
    a = 1
    for i in range(1, n+1):
            a = a * i
    return a



mywindow = tk.Tk()

c = tk.Canvas(mywindow, width=300)
c.pack(side='left', expand=1,)
c2 = tk.Canvas(c, width=300)
c2.pack(side='left', expand=1,)
c3 = tk.Canvas(c, width=300)
c3.pack(side='left', expand=1,)
w1 = tk.Label(c2, text="Enter Number : ")
w1.pack()
e = tk.Entry(c2)#e = entry no 1
e.pack()

toolbar = tk.Frame(c2)
b = tk.Button(toolbar, text="SUBMIT", width=9, command=lambda: save(e))
b.pack(side='left', padx=2, pady=2)
toolbar.pack(side='top',)
l = tk.Label(c3, text='')
l.pack(side='left', expand=1)
b2 = tk.Button(c3, text='VIEW ANSWER', command=lambda: loadme(l))
b2.pack(fill='x')#press view answer to view saved answer
#window size
mywindow.minsize(300,100)#fixing minimum size
# Fixing the window size
mywindow.resizable(width=FALSE, height=FALSE)
# Title bar Title
mywindow.title('Factorial Gui')#title name = Factorial Gui
# Title Bar Icon
mywindow.iconbitmap('icon.ico')#icon file name = icon.ico

mywindow.mainloop()

