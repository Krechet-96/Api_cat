from cProfile import label
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

from bottle import response


def load_image(url):
    pass


window=Tk()
window.geometry("500x500")


label=Label()
label.pack()

url="https://cataas.com/cat"
img=load_image(url)

if img:
    label.config(image=img)
#    label.image=img

window.mainloop()
