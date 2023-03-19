import json
import os
import re

usvers = {
    "user": [
        {
            "id": "0",
            "login": "admin",
            "password": "admin"
        }
    ]
}

if os.path.getsize("/home/sergo/usvers.json") == 0:
    with open("/home/sergo/usvers.json", 'w', encoding='utf8') as write_file1:
        json.dump(usvers, write_file1, ensure_ascii=False)

def method(b,c,d):
    new = {"id": b, "login": c, "password": d}

    if t:
        with open("/home/sergo/usvers.json", encoding='utf8') as read_file:
            n = json.load(read_file)
            # print(n)
            n["user"].append(new)
            with open("/home/sergo/usvers.json", 'w', encoding='utf8') as write_file:
                json.dump(n, write_file, ensure_ascii=False, )


o = False
b = ""
c = ""
d = ""
sch = 0
t = True
while True:
    a = input("Добавьте пользователя введите 1 2 3 4")
    if a == '4':
        break
    if a == "1":
        b = input("Введите id пользователя")
        with open("/home/sergo/usvers.json", encoding='utf8') as read_file:
            n = json.load(read_file)
            j = 0
            for i in n['user']:
                if n['user'][j]['id'] == b:
                    print("такой айди уже существует!!!")
                    t = False
                    break
                j += 1
            if t == False:
                break
        c = input("Введите логин ")
        with open("/home/sergo/usvers.json", encoding='utf8') as read_file:
            n = json.load(read_file)
            j = 0
            for i in n['user']:
                if n['user'][j]['login'] == c:
                    print("такой логин уже существует!!!")
                    t = False
                    break
                j += 1
            if t == False:
                break
        d = input("Введите пароль, длина пароля не менее 8 символов, пароль должен включать буквы верхнего регистра; \n"
                  "пароль должен включать буквы верхнего и нижнего регистра, цифры \n"
                  "включать хотя бы один специальный символ: !, £, $, %, &")
        if len(d) < 8:
            print("пароль менее 8 символов")
            t = False
            break
        rool = '[A-Za-z0-9!@#$%&]{8,}'
        if re.fullmatch(rool, d):
            t = True
            sch =5
            print(sch)
        rool1 = '[a-zA-Z0-9]+'
        if re.fullmatch(rool1, d):
            t = True
            sch =4
            print(sch)
        rool2 = '[a-zA-Z]+'
        if re.fullmatch(rool2, d):
            t = True
            sch =3
            print(sch)
        rool3 = '[A-Z]+'
        if re.fullmatch(rool3, d):
            t = False
            sch =2
            print(sch)
        rool4 = '[a-z]+'
        if re.fullmatch(rool4, d):
            t = False
            sch = 1
            print(sch)
        rool5 = '[0-9]+'
        if re.fullmatch(rool5, d):
            t = False
            sch = 0
            print(sch)
        if sch <= 2:
            t = False
            print("введите новый пароль")
            break
        if 4 >= sch > 2:
            e = input("надо улучшить пароль введите да или нет")
            if e == "нет":
                t = False
                break
            if e == "да":
                t = True
            continue
        if sch == 5:
            t = True
        method(b,c,d)
        break
    if a == '2':
        r = input("введите логин пользователя у которого хотите поменять пароль")
        with open("/home/sergo/usvers.json", encoding='utf8') as read_file:
            n = json.load(read_file)
            j = 0
            q = False
            for i in n['user']:
                if n['user'][j]['login'] == r:
                   o = True
                   p = input("введите новый пароль! ")
                   rool = '[A-Za-z0-9!@$%&]{8,}'
                   if re.fullmatch(rool, p):
                       print("yes")
                       q = True
                   else:
                       print("no")
                   if q:
                       n['user'][j]['password'] = p
                   else:
                       print("Плохой пароль")
                       break
                j +=1
            if o == False:
                print("такого логина нет в файле! ")
            with open("/home/sergo/usvers.json", 'w', encoding='utf8') as write_file:
                json.dump(n, write_file, ensure_ascii=False)
        break
    if a == '3':
        with open("/home/sergo/usvers.json", encoding='utf8') as read_file:
            n = json.load(read_file)
            j=0
            for i in n['user']:
                print("логины пользователей ", n['user'][j]['login'])
                j+=1
        break

