from tkinter import *
from dr.client import Client


class GuiClient:
    def __init__(self,window):
        self.btn = Button(window, text="какой сегодня день", bg="silver", fg="red", command=self.clicked)
        self.btn.grid(column=0, row=0)
        self.btn1 = Button(window, text="сколько сейчас времени", bg="silver", fg="red", command=self.clicked2)
        self.btn1.grid(column=0, row=1)
        self.btn2 = Button(window, text="назовите столицу Алжир", bg="silver", fg="red", command=self.clicked3)
        self.btn2.grid(column=0, row=2)
        self.btn3 = Button(window, text="кто написал Война и мир", bg="silver", fg="red", command=self.clicked4)
        self.btn3.grid(column=0, row=3)
        self.btn4 = Button(window, text="кто написал таблицу Менделеева", bg="silver", fg="red", command=self.clicked5)
        self.btn4.grid(column=0, row=4)
        self.lbl = Label(window, text="введите цифру затем знак + - * / потом опять цифру,", bg="silver", fg="red",)
        self.lbl.grid(column=0, row=5)
        self.txt = Entry(window, width=20)
        self.txt.grid(column=0, row=6)
        self.btn3 = Button(window, text="Clear!", command=self.clear, bg="silver", fg="red",)
        self.btn3.grid(column=0, row=8)
        self.btn4 = Button(window, text="Результат", command=self.result, bg="silver", fg="red",)
        self.btn4.grid(column=0, row=7)
        window.mainloop()


    def clicked(self):
        a = "какой сегодня день"
        rs = Client(a)
        rss = rs.method()
        return a

    def clicked2(self):
        a = "сколько сейчас времени"
        rs = Client(a)
        rss = rs.method()
        return a

    def clicked3(self):
        a = "назовите столицу Алжир"
        rs = Client(a)
        rss = rs.method()
        return a

    def clicked4(self):
        a = "кто написал Война и мир"
        rs = Client(a)
        rss = rs.method()
        return a

    def clicked5(self):
        a = "кто написал таблицу Менделеева"
        rs = Client(a)
        rss = rs.method()
        return a

    def clear(self):
        self.txt.delete(0, END)


    def result(self):
        print("*")
        res = self.txt.get()
        rs = Client(res)
        rss = rs.method()



