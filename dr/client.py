from  tkinter import messagebox
from socket import *

class Client:
    def __init__(self,a):
        self.a = a

    def method(self):
        s = socket(AF_INET,SOCK_STREAM)
        s.connect(('localhost',8005))
        msg = f"{self.a}"
        print(msg)
        s.send(msg.encode('UTF-8'))
        answer = s.recv(1000000)
        print("Сообщение от сервера",answer.decode('utf-8'),'длиной',len(answer),'байт')
        messagebox.showinfo('Сообщение от сервера',answer.decode('utf-8'))
        print("*")
        s.close()