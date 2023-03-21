from tkinter import *
from  tkinter import messagebox
import json
import sys
import re

class Window2:
    def __init__(self,window2):
        self.window2 = window2
        self.window2.title("json")
        self.window2.geometry('800x600')
        self.window2["bg"] = "lightsteelblue"
        self.lbl = Label(window2, text="Введите id пользователя")
        self.lbl.grid(column=0, row=0)
        self.txt = Entry(window2, width=10)
        self.txt.grid(column=1, row=0)
        self.lbl1 = Label(window2, text="Введите  логин пользователя")
        self.lbl1.grid(column=0, row=1)
        self.txt1 = Entry(window2, width=10)
        self.txt1.grid(column=1, row=1)
        self.lbl2 = Label(window2, text="Введите пароль буквы верхнего и нижнего регистра, цифры и символы:!£$%&")
        self.lbl2.grid(column=0, row=2)
        self.txt2 = Entry(window2, width=10)
        self.txt2.grid(column=1, row=2)
        self.lbl3 = Label(window2, text="Введите логин у которого хотите поменять пароль")
        self.lbl3.grid(column=0, row=3)
        self.txt3 = Entry(window2, width=10)
        self.txt3.grid(column=1, row=3)
        self.lbl4 = Label(window2, text="Введите новый пароль")
        self.lbl4.grid(column=0, row=4)
        self.txt4 = Entry(window2, width=10)
        self.txt4.grid(column=1, row=4)
        self.lbl4 = Label(window2, text="показать всех пользователей")
        self.lbl4.grid(column=0, row=5)
        self.btn = Button(window2, bg="silver", fg="blue", text="Клац!", command=self.clicked)
        self.btn.grid(column=2, row=0)
        self.btn1 = Button(window2, bg="silver", fg="blue", text="Клац!", command=self.clicked2)
        self.btn1.grid(column=2, row=1)
        self.btn2 = Button(window2, bg="silver", fg="blue", text="Клац!", command=self.clicked3)
        self.btn2.grid(column=2, row=2)
        self.btn3 = Button(window2, bg="silver", fg="blue", text="Клац!", command=self.clicked4)
        self.btn3.grid(column=2, row=3)
        self.btn4 = Button(window2, bg="silver", fg="blue", text="Клац!", command=self.clicked4)
        self.btn4.grid(column=2, row=4)
        self.btn4 = Button(window2, bg="silver", fg="blue", text="ShowUsers!", command=self.clicked5)
        self.btn4.grid(column=2, row=5)
        self.btn5 = Button(window2, bg="silver", fg="blue", text="Clear!", command=self.clear)
        self.btn5.grid(column=0, row=6)
        self.btn6 = Button(window2, bg="silver", fg="blue", text="записать данные в файл!", command=self.result)
        self.btn6.grid(column=0, row=7)
        window2.mainloop()

    @classmethod
    def checkPassword(cls, res):
        sch = 0
        t = True
        print(type(res))
        if len(res) < 8:
            messagebox.showinfo('error', 'пароль менее 8 цифр')
            sys.exit()
        rool = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        if re.fullmatch(rool, res):
            t = True
            sch = 5
            messagebox.showinfo(f'good', f'пароль {sch} баллов')
        rool1 = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        if re.fullmatch(rool1, res):
            t = False
            sch = 4
            messagebox.showwarning(f'no good', f'пароль {sch} баллов надо улучшить')
            a = Window2(Tk())
            sys.exit()
        rool2 = '^(?=.*[a-z])(?=.*[A-Z])[A-Za-z]{8,}$'
        if re.fullmatch(rool2, res):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            t = False
            sch = 3
            messagebox.showwarning(f'no good', f'пароль {sch} баллов надо улучшить')
            b = Window2(Tk())
            sys.exit()
        rool3 = '[A-Z]+'
        if re.fullmatch(rool3, res):
            t = False
            sch = 2
            messagebox.showwarning(f'no good', f'введите другой пароль, баллов {sch}')
            sys.exit()
        rool4 = '[a-z]+'
        if re.fullmatch(rool4, res):
            t = False
            sch = 1
            messagebox.showwarning(f'no good', f'введите другой пароль, баллов {sch}')
            sys.exit()
        rool5 = '[0-9]+'
        if re.fullmatch(rool5, res):
            t = False
            sch = 0
            messagebox.showwarning(f'no good', f'введите другой пароль, баллов {sch}')
            sys.exit()
        if sch == 5:
            t = True
            return res


    def clicked(self):
        try:
            res = "{}".format(self.txt.get())
            if res.isdigit():
                pass
            else:
                messagebox.showinfo('error', 'это не цифра')
            print(type(res))
            with open("/home/sergo/usvers3.json", encoding='utf8') as read_file:
                n = json.load(read_file)
                j = 0
                for i in n['user']:
                    if n['user'][j]['id'] == res:
                        messagebox.showinfo('error','такой айди уже существует')
                        return None
                    j += 1
            return res
        except ValueError:
            messagebox.showinfo('error', 'введите правильно цифры')


    def clicked2(self):
        try:
            res = "{}".format(self.txt1.get())
            print(res)
            with open("/home/sergo/usvers3.json", encoding='utf8') as read_file:
                n = json.load(read_file)
                j = 0
                for i in n['user']:
                    if n['user'][j]['login'] == res:
                        messagebox.showinfo('error','такой логин уже существует')
                        return None
                    j += 1
            return res
        except ValueError:
            messagebox.showinfo('error', 'введите правильно цифры')


    def clicked3(self):
        try:
            res = "{}".format(self.txt2.get())
            print(type(res))
            messagebox.showinfo('!!!', 'нажмите кнопку записать!')
            return Window2.checkPassword(res)
        except ValueError:
            messagebox.showinfo('error', 'введите правильно цифры')

    def clicked4(self):
        try:
            res = "{}".format(self.txt3.get())
            res2 = "{}".format(self.txt4.get())
            res3 = Window2.checkPassword(res2)
            print(res)
            with open("/home/sergo/usvers3.json", encoding='utf8') as read_file:
                n = json.load(read_file)
                j = 0
                o = False
                for i in n['user']:
                    if n['user'][j]['login'] == res:
                        n['user'][j]['password'] = res3
                        o = True
                    j+=1
                if o == False:
                    messagebox.showinfo('no good', f'логин с именем {res} не существует')
                    sys.exit()
                with open("/home/sergo/usvers3.json", 'w', encoding='utf8') as write_file:
                    json.dump(n, write_file, ensure_ascii=False)
                messagebox.showinfo('оки', 'пароль изменен')
        except ValueError:
            messagebox.showinfo('error', 'введите правильно цифры')

    def clicked5(self):
        with open("/home/sergo/usvers3.json", encoding='utf8') as read_file:
            n = json.load(read_file)
            j=0
            mas = []
            for i in n['user']:
                mas.append(n['user'][j]['login'])
                j+=1
            messagebox.showinfo('список пользователей',f'{mas}')

    def clear(self):
        self.txt.delete(0, END)
        self.txt1.delete(0, END)
        self.txt2.delete(0, END)
        self.txt3.delete(0, END)
        self.txt4.delete(0, END)

    def result(self):
       b = self.clicked()
       c = self.clicked2()
       d = self.clicked3()
       new = {"id": b, "login": c, "password": d}

       with open("/home/sergo/usvers3.json", encoding='utf8') as read_file:
           n = json.load(read_file)
           n["user"].append(new)
           with open("/home/sergo/usvers3.json", 'w', encoding='utf8') as write_file:
               json.dump(n, write_file, ensure_ascii=False, )