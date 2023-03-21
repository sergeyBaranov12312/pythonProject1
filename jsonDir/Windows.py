from tkinter import *
from  tkinter import messagebox
from jsonDir.Windows2 import Window2

class Window:
    def __init__(self,window):
        self.lbl = Label(window, text="Введите параметр 1")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(window, width=10)
        self.txt.grid(column=1, row=0)
        self.lbl1 = Label(window, text="Введите параметр 2")
        self.lbl1.grid(column=0, row=1)
        self.txt1 = Entry(window, width=10)
        self.txt1.grid(column=1, row=1)
        self.lbl2 = Label(window, text="Введите параметр 3")
        self.lbl2.grid(column=0, row=2)
        self.txt2 = Entry(window, width=10)
        self.txt2.grid(column=1, row=2)
        self.lbl3 = Label(window, text="Введите параметр 4")
        self.lbl3.grid(column=0, row=3)
        self.txt3 = Entry(window, width=10)
        self.txt3.grid(column=1, row=3)
        self.btn = Button(window, bg="silver", fg="blue", text="Клац!", command=self.clicked)
        self.btn.grid(column=2, row=0)
        self.btn1 = Button(window, bg="silver", fg="blue", text="Клац!", command=self.clicked2)
        self.btn1.grid(column=2, row=1)
        self.btn2 = Button(window, bg="silver", fg="blue", text="Клац!", command=self.clicked3)
        self.btn2.grid(column=2, row=2)
        self.btn3 = Button(window, bg="silver", fg="blue", text="Клац!", command=self.clicked4)
        self.btn3.grid(column=2, row=3)
        window.mainloop()


    def clicked(self):
        w = Tk()
        wn2 = Window2(w)


    def clicked2(self):
        w = Tk()
        wn2 = Window2(w)

    def clicked3(self):
        w = Tk()
        wn2 = Window2(w)

    def clicked4(self):
        w = Tk()
        wn2 = Window2(w)

