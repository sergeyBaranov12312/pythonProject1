from tkinter import *
import json
import os
from jsonDir.Windows import Window


class Main:
    window = Tk()
    window.title("JSON")
    window.geometry('800x600')
    window["bg"] = "lightsteelblue"
    def __init__(self):
        pass

    @classmethod
    def method(cls):
        a = Window(cls.window)

    @classmethod
    def method_addAdmin(cls):
        usvers = {
            "user": [
                {
                    "id": "0",
                    "login": "admin",
                    "password": "admin"
                }
            ]
        }
        if os.path.exists("/home/sergo/usvers3.json"):
            print("hello")
        else:
            with open("/home/sergo/usvers3.json", 'w', encoding='utf8') as write_file1:
                json.dump(usvers, write_file1, ensure_ascii=False)


Main.method_addAdmin()
Main.method()