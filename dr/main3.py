from tkinter import *
from dr.guiClient import GuiClient


class Main3:
    window = Tk()
    window.title("Client")
    window.geometry('800x600')
    window["bg"] = "lightsteelblue"
    def __init__(self):
        pass

    @classmethod
    def method(cls):
        a = GuiClient(cls.window)

print("*")
Main3.method()