from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.geometry('400x500')
#c=Image.open("butterfly.jpg")
img = ImageTk.PhotoImage(file="butterfly.jpg")
Label(root,image=img).place(x=0,y=0,relheight=1,relwidth=1)

root.mainloop()


