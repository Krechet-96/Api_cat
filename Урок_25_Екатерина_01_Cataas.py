from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO


def load_image(url):
    response = requests.get(url)
    print(response)
#    print(response.headers)
#    print(response.content)
    image_data=BytesIO(response.content)
    print(image_data)
    img=Image.open(image_data)
    print(img)
    return ImageTk.PhotoImage(img)


window=Tk()
window.geometry("500x500")


label=Label()
label.pack()

url="https://cataas.com/cat"
img=load_image(url)

if img:
    label.config(image=img)
#    label.image=img

but=Button(text="Загрузка картинки",command=load_image)
but.pack()

window.mainloop()
