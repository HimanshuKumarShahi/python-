from tkinter import *
import  mysql.connector as mycon
window = Tk()
window.title("Registration Form")
window.geometry('450x500')
window.resizable(width=False, height=False)

# Heading
Label(window, text="Registration Form", bg='orange', font=('arial', 20)).pack(fill='both')

# Labels for entries
Label(window, text="Name", font=('arial', 12)).place(x=50, y=90)
Label(window, text="Gender", font=('arial', 12)).place(x=50, y=150)
Label(window, text="Contact", font=('arial', 12)).place(x=50, y=210)
Label(window, text="Email", font=('arial', 12)).place(x=50, y=270)

# Entry fields
name=StringVar()
gender=StringVar()
contact=StringVar()
mail=StringVar()

name_Entry = Entry(window, width=25, font=('arial', 12),textvariable=name)
name_Entry.place(x=150, y=90)
gender_Entry = Entry(window, width=25, font=('arial', 12),textvariable=gender)
gender_Entry.place(x=150, y=150)
contact_Entry = Entry(window, width=25, font=('arial', 12),textvariable=contact)
contact_Entry.place(x=150, y=210)
mail_Entry = Entry(window, width=25, font=('arial', 12),textvariable=mail)
mail_Entry.place(x=150, y=270)


# Reset Button
def reset():
    name_Entry.delete(0, END)
    gender_Entry.delete(0, END)
    contact_Entry.delete(0, END)
    mail_Entry.delete(0, END)

# Submit Button
def submit():
    nameData=name.get()
    genderData=gender.get()
    contactData=contact.get()
    mailData=mail.get()
    # Insert into MySQL
    mydb = mycon.connect(
        host="localhost",
        user="root",
        password="Password😠",
        database="registration"
    )
    cursor = mydb.cursor()

    # Change table/columns as per your DB
    sql = "INSERT INTO registration_data (name, gender, contact, email) VALUES (%s, %s, %s, %s)"
    vals = (nameData, genderData, contactData, mailData)
    cursor.execute(sql, vals)
    mydb.commit()

    cursor.close()
    mydb.close()

    Label(window, text="Submitted Successfully", bg='green',
          font=('arial', 20, 'bold')).place(x=120, y=400)

    Label(window,text="Submitted Successfully",bg='green', font=('arial',20,'bold')).place(x=200,y=400)
    
Button(window,text='Reset',font=('arial',12,'bold'),command=reset).place(x=150,y=350)
Button(window,text='Submit',font=('arial',12,'bold'),command=submit).place(x=250,y=350)

window.mainloop()