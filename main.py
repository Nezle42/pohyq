import tkinter
from tkinter import Label

root = tkinter.Tk()

root.title("Hello world")
root.geometry("300x250")
root.iconbitmap("icon.ico")

label_1_Hello_world = Label(text = "Hello world!!!")
label_1_Hello_world.pack()

root.mainloop()