from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as c
import tkinter.messagebox as tmsg




root=Tk()
root.geometry('1200x800')
root.minsize(1000,800)
root.maxsize(1250,2000)
bg=Image.open('2.jpg')
im=ImageTk.PhotoImage(bg)
Label(root,image=im).place(relwidth=1)

(Label(text='Welcome To Tax Collecting System',
      font=('algerian 33 bold'),fg='gray20',bg='gray43')
 .pack(pady=2))


f1=Frame(root,bg='gray39',relief=SUNKEN,borderwidth=5,
         padx=5,pady=5)
f1.pack(side=TOP,padx=200,pady=90,anchor='nw')

Label(f1,text="USERNAME:",bg='gray52',font=('Baskerville_Old_Face 10 bold')
      ).pack(side='left',padx=9)

f2=Frame(root,bg='gray39',relief=SUNKEN,borderwidth=5,
         padx=5,pady=5)
f2.pack(side="left",anchor='nw',padx=200)
(Label(f2,text="PASSWORD:",bg='gray52',font=('Baskerville_Old_Face 10 bold')
       ).pack(side='left',padx=9))
#

# for input value from user
uv=StringVar()
pv=StringVar()

ue=Entry(f1,textvariable=uv,borderwidth=2,name='userid')
pe=Entry(f2,textvariable=pv,borderwidth=2,name='passwd')

ue.pack(padx=9)
pe.pack(padx=7)


def submit():
    try:
        print('username=',ue.get(),'\npassword=',pe.get())
        # giving info s to database
        i = c.connect(host='localhost', username='root', passwd='mohar466',database='info')
        if i.is_connected():
            print('succesful')
            cur = i.cursor()
            h ="insert into information values('{}','{}')".format(str(ue.get()), str(pe.get()))
            print(h)
            cur.execute(h)
            i.commit()
    except:
        print('Try other password!')


def gg():
    submit()
    root=Tk()
    root.title(f"{ue.get()}page")
    root.geometry('500x500')
    main = Menu(root)
    m1 = Menu(main)
    def h():
        print('happy')
        a=tmsg.showinfo('HELP',
                        "government is not for helping people")

    m1.add_command(label='proj', command=h)
    m1.add_separator()
    m1.add_command(label='save', command=h)
    m1.add_command(label='help', command=h)
    main.add_cascade(label='file', menu=m1)

    root.config(menu=main)

    root.mainloop()

b=Button(text='Enter',borderwidth=4,relief=SUNKEN,bg='LightCyan2',font='arial_black 10 bold'
         ,command=gg)
b.pack(side='top',pady=100,anchor='sw')






#for giiving name to the gui
root.title('First Page')


root.mainloop()