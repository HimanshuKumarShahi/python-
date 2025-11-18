from tkinter import *
window=Tk()
window.geometry('1200x700')
window.resizable(width=False, height=False)
window.configure(background='#c3f7d1')
window.title("ABC Food Court")

def res():
    dosa_Entry.delete(0,END)
    burger_Entry.delete(0,END)
    gJamun_Entry.delete(0,END)

def cal():
    Label(f4,text='|| Product ||',font=('arial',18,'bold'),bg='white',fg='black').place(x=700,y=150)
    Label(f4,text=' \n Quantity  \n Rate \n Total ',font=('arial',14) ,fg='black').place(x=700,y=200)
    try:v1=int(dosa.get())
    except:v1=0
    try:v2=int(burger.get())
    except:v2=0
    try:v3=int(gJamun.get())
    except:v3=0

    c1=120*v1
    c2=50*v2
    c3=20*v3

    total=c1+c2+c3
    entry_total=Entry(f4,textvariable=tbil).place(x=650,y=250)
    tbil.set(total)



f1=Frame(window,width=1200, height=80,bg='lightgreen').pack()
f2=Frame(window,width=350,height=600,bg='lightpink').place(x=10,y=90)
f3=Frame(window,width=350,height=600,bg='lightpink').place(x=320,y=90)
f4=Frame(window,width=350,height=600,bg='lightpink').place(x=630,y=90)

Label(f1,text='ABC Food Court',font=('arial',25,'bold'),bg='lightgreen').place(x=450,y=25)
Label(f2,text='Menu Card',font=('arial',16,'bold'),bg='#79f7f7').place(x=100,y=70)
Label(f2,text='Dosa--------------@120 Rs.',font=('arial',12),bg='lightpink').place(x=30,y=130)
Label(f2,text='Burger------------@ 50 Rs.',font=('arial',12),bg='lightpink').place(x=30,y=160)
Label(f2,text='Gulab Jamun-------@ 20 Rs.',font=('arial',12),bg='lightpink').place(x=30,y=190)


Label(f3,text='Dosa',font=('arial',12),bg='lightpink').place(x=330,y=130)
Label(f3,text='Burger',font=('arial',12),bg='lightpink').place(x=330,y=160)
Label(f3,text='Gulab Jamun',font=('arial',12),bg='lightpink').place(x=330,y=190)

dosa=StringVar()
burger=StringVar()
gJamun=StringVar()
tbil=StringVar()

dosa_Entry=Entry(f3,font=('arial',12),width=15,textvariable=dosa)
dosa_Entry.place(x=460,y=130)
burger_Entry=Entry(f3,font=('arial',12),width=15,textvariable=burger)
burger_Entry.place(x=460,y=160)
gJamun_Entry=Entry(f3,font=('arial',12),width=15,textvariable=gJamun)
gJamun_Entry.place(x=460,y=190)

Button(f3,text='Reset',width=12,command=res).place(x=350,y=250)
Button(f3,text='Calculate',width=12,command=cal).place(x=490,y=250)

Label(f4,text='Bill Areaa',font=('arial',16,'bold'),bg='#79f7f7').place(x=715,y=70)

window.mainloop()