from socket import *
import time
import calendar
import datetime
from tkinter import *
from  tkinter import messagebox
class Server:
    def start_server(self):
        # AF_INET - указываем, что сокет является сетевым
        # SOCK_STREAM - определет сокет как потоковый
        s = socket(AF_INET, SOCK_STREAM)  # создали сокет TCP
        s.bind(("", 8005))  # настроили сокет, чтобы он принимал запросы от клиента по локальному IP и порту
        s.listen(5)  # Переходим в режим ожидания запросов и допускаем не более 5 запросов одновременно

        while True:
            client, addr = s.accept()  # принимаем запрос на соединение
            data = client.recv(1000000)  # получаем данные от клиента
            d = data.decode('utf-8')
            if d == 'какой сегодня день':
                b = datetime.date.today()
                b = calendar.day_name[b.weekday()]
                print("Сообщение от клиента", data.decode('utf-8'), ' ответ ', b)
                client.send(str(b).encode('utf-8'))
            if d == 'сколько сейчас времени':
                t = time.localtime()
                b = time.strftime("%H:%M:%S", t)
                print("Сообщение от клиента", data.decode('utf-8'), ' ответ ', b)
                client.send(str(b).encode('utf-8'))
            if d == 'назовите столицу Алжир':
                b = 'Алжир'
                print("Сообщение от клиента ", data.decode('utf-8'), ' ответ ', b)
                client.send(str(b).encode('utf-8'))
            if d == 'кто написал Война и мир':
                b = 'Толстой'
                print("Сообщение от клиента", data.decode('utf-8'), ' ответ ', b)
                client.send(str(b).encode('utf-8'))
            if d == 'кто написал таблицу Менделеева':
                b = 'Менделеев'
                print("Сообщение от клиента", data.decode('utf-8'), ' ответ ', b)
                client.send(str(b).encode('utf-8'))
            st = ''
            st1 = ''
            st2 = ''
            for i in range(len(d)):
                if d[i].isdigit():
                    st += d[i]
                if d[i] == "+":
                    st2 = "+"
                if d[i] == "-":
                    st2 = "-"
                if d[i] == "*":
                    st2 = "*"
                if d[i] == "/":
                    st2 = "/"
                if d[i] == '+' or d[i] == '-' or d[i] == '*' or d[i] == '/':
                    for i in range(i, len(d) - 1):
                        st1 += d[i + 1]
                        if i == len(d) - 1:
                            break
                    break

            if st2 == "+":
                b = float(st) + float(st1)
                print("Сообщение от клиента чему равно", data.decode('utf-8'), ' ответ', b)
                client.send(str(b).encode('utf-8'))
            if st2 == "-":
                b = float(st) - float(st1)
                print("Сообщение от клиента чему равно", data.decode('utf-8'), ' ответ', b)
                client.send(str(b).encode('utf-8'))
            if st2 == "*":
                b = float(st) * float(st1)
                print("Сообщение от клиента чему равно", data.decode('utf-8'), ' ответ', b)
                client.send(str(b).encode('utf-8'))
            if st2 == "/":
                b = float(st) / float(st1)
                print("Сообщение от клиента чему равно", data.decode('utf-8'), ' ответ', b)
                client.send(str(b).encode('utf-8'))
            client.close()
            print('*')
a = Server()
a.start_server()


