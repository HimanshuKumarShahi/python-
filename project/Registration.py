from tkinter import *
window=Tk()
window.title("Registration Form")
window.geometry('450x500')
window.resizable(width=False,height=False)


def res():
    name_Entry.delete(0,END)
    gender_Entry.delete(0,END)
    contact_Entry.delete(0,END)
    mail_Entry.delete(0,END)
def submit():
    nameData=name.get()
    genderData=gender.get()
    contactData=contact.get()
    mailData=mail.get()

    File = open(nameData+'.txt','w')
    File.write(nameData +'\n')
    File.write(genderData +'\n')
    File.write(contactData +'\n')
    File.write(mailData +'\n')
    Label(window,text="Submitted Successfully",bg='green',font=('arial',20,'bold')).place(x=0,y=430)

# Heading
Label(window,text="Registration Form",bg='lightgreen',font=('arial',20)).pack(fill='both')

#Label
Label(window,text='Name',font=('arial',12)).place(x=30,y=90)
Label(window,text='Gender',font=('arial',12)).place(x=30,y=150)
Label(window,text='Contact',font=('arial',12)).place(x=30,y=210)
Label(window,text='Email',font=('arial',12)).place(x=30,y=270)

# Entry Box
name=StringVar()
gender=StringVar()
contact=StringVar()
mail=StringVar()

name_Entry=Entry(window,width=25,font=('arial',12),textvariable=name)
name_Entry.place(x=150,y=90)
gender_Entry=Entry(window,width=25,font=('arial',12),textvariable=gender)
gender_Entry.place(x=150,y=150)
contact_Entry=Entry(window,width=25,font=('arial',12),textvariable=contact)
contact_Entry.place(x=150,y=210)
mail_Entry=Entry(window,width=25,font=('arial',12),textvariable=mail)
mail_Entry.place(x=150,y=270)

# Button
Button(window,text='Reset',font=('arial',12,'bold'),command=res).place(x=150,y=350)
Button(window,text='Submit',font=('arial',12,'bold'),command=submit).place(x=250,y=350)
window.mainloop()