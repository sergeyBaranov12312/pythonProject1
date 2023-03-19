import json

usvers = """{
    "user": [
            {
                 "id":1,
                 "login":"admin",
                 "password":12 
            }
        ]
    }
"""


b=""
c=""
d=""

while True:
    a = input("Добавьте пользователя введите 1 или e")
    if a == 'e':
        break
    if a == "1":
       b = input("Введите id пользователя")
       c = input("Введите логин ")
       if c == "admin":
           print("логин admin зарезервирован")
           continue
       d = input("Введите пароль, длина пароля не менее 8 символов, пароль должен включать буквы верхнего регистра; \n"
                 "пароль должен включать буквы верхнего и нижнего регистра, цифры \n"
                 "включать хотя бы один специальный символ: !, £, $, %, &")
       if len(d)<8:
           print("пароль менее 8 символов")
           continue

       break
print(b,c,d)
# преобразуем строку в словарь
info = json.loads(usvers)
new = {"id":b,"login":c,"password":d}
j=0
k=True
with open("/home/sergo/usvers.json", "r") as read_file:
    x = json.load(read_file)
    for i in a:
        print(x,"()()()()")
        print(x['user'][j]['login'])
        if x['user'][j]["login"] == c:
            print("логин занят")
            k=False
        j+=1
        if k:
            x['user'].append(new)
 # j=0
 # for i in info:
 #     info["user"][j]["id"]=b
 #     info["user"][j]["login"] = c
 #     info["user"][j]["password"] = d
 #     j+=1
# print(info)
# print(info['user'][0])
print("***************")
with open("/home/sergo/usvers.json", "w") as write_file:
    json.dump(a, write_file, ensure_ascii=False)

with open("/home/sergo/usvers.json", "r") as read_file:
    a = json.load(read_file)
print(a)
