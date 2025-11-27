from tkinter import *


window = Tk()
window.title("ABC Food Court")
window.geometry('1200x700')
window.configure(background='#c3f7d1')
window.resizable(width=False, height=False)


def res():
    dosa_Entry.delete(0, END)
    burger_Entry.delete(0, END)
    gJamun_Entry.delete(0, END)
    tbil.set("")
    bill_text.delete("1.0", END)


def cal():
    try:
        v1 = int(dosa.get())
    except:
        v1 = 0
    try:
        v2 = int(burger.get())
    except:
        v2 = 0
    try:
        v3 = int(gJamun.get())
    except:
        v3 = 0

    c1 = 120 * v1
    c2 = 50 * v2
    c3 = 20 * v3

    total = c1 + c2 + c3
    tbil.set(f"₹ {total}")

    # Format bill text with tabs for alignment
    bill_text.delete("1.0", END)
    bill_text.insert(END, "Item\t\tQty\tPrice\n")
    bill_text.insert(END, "-" * 30 + "\n")
    if v1 > 0:
        bill_text.insert(END, f"Dosa\t\t{v1}\t₹{c1}\n")
    if v2 > 0:
        bill_text.insert(END, f"Burger\t\t{v2}\t₹{c2}\n")
    if v3 > 0:
        bill_text.insert(END, f"Gulab Jamun\t{v3}\t₹{c3}\n")
    bill_text.insert(END, "\n")
    bill_text.insert(END, f"Total Amount:\t\t₹{total}")


def print_bill():
    # Remove previous message label if any
    for widget in window.place_slaves():
        if isinstance(widget, Label) and str(widget.cget("text")).startswith("!!"):
            widget.destroy()
    Label(window, text="!! Printing Successfully !!",
          bg='green', font=('arial', 15, 'bold')).place(x=780, y=570)


# Frame 1 - Header
f1 = Frame(window, width=1200, height=80, bg="#2284c5")
f1.pack(fill=X)
Label(f1, text='ABC Food Court', font=('arial', 25, 'bold'),
      bg='#2284c5', fg="white").place(x=450, y=24)


# Frame 2 - Menu Card
f2 = Frame(window, width=350, height=600, bg='lightpink', bd=2, relief='ridge')
f2.place(x=20, y=90)

Label(f2, text='Menu Card', font=('arial', 16, 'bold'),
      bg='lightpink').place(x=120, y=20)

menu_items = [
    ("Dosa", 120, 80),
    ("Burger", 50, 120),
    ("Gulab Jamun", 20, 160),
    ("Idli Sambar", 60, 200),
    ("Vada Pav", 40, 240),
    ("Pav Bhaji", 80, 280),
    ("Samosa", 25, 320),
    ("Chole Bhature", 90, 360),
    ("Fried Rice", 100, 400),
    ("Noodles", 90, 440),
    ("Paneer Sandwich", 70, 480),
    ("Veg Puff", 30, 520),
    ("Masala Maggi", 50, 560),
    ("Cold Coffee", 60, 600),
    ("Lemon Soda", 30, 640),
    ("Masala Tea", 20, 680),
    ("Ice Cream Cup", 40, 720),
    ("French Fries", 60, 760),
]

for item, price, y_pos in menu_items:
    label_text = f'{item}{"." * (30 - len(item))}@ ₹{price}'
    Label(f2, text=label_text, font=('arial', 12), bg='lightpink').place(x=30, y=y_pos)


# Frame 3 - Order Input
f3 = Frame(window, width=350, height=600, bg='lightpink', bd=2, relief='ridge')
f3.place(x=400, y=90)
Label(f3, text='Order Here', font=('arial', 16, 'bold'),
      bg='lightpink').place(x=120, y=20)

dosa = StringVar()
burger = StringVar()
gJamun = StringVar()
tbil = StringVar()

Label(f3, text='Dosa', font=('arial', 12), bg='lightpink').place(x=50, y=80)
dosa_Entry = Entry(f3, font=('arial', 12), width=15, textvariable=dosa)
dosa_Entry.place(x=150, y=80)

Label(f3, text='Burger', font=('arial', 12), bg='lightpink').place(x=50, y=120)
burger_Entry = Entry(f3, font=('arial', 12), width=15, textvariable=burger)
burger_Entry.place(x=150, y=120)

Label(f3, text='Gulab Jamun', font=('arial', 12), bg='lightpink').place(x=50, y=160)
gJamun_Entry = Entry(f3, font=('arial', 12), width=15, textvariable=gJamun)
gJamun_Entry.place(x=150, y=160)

Button(f3, text='Calculate', width=12, command=cal).place(x=50, y=220)
Button(f3, text='Reset', width=12, command=res).place(x=170, y=220)


# Frame 4 - Bill Area
f4 = Frame(window, width=350, height=600, bg='lightpink', bd=2, relief='ridge')
f4.place(x=780, y=90)

Label(f4, text='Bill Area', font=('arial', 16, 'bold'),
      bg='lightpink').place(x=125, y=20)

Label(f4, text='Total Bill:', font=('arial', 14), bg='lightpink').place(x=30, y=80)
entry_total = Entry(f4, font=('arial', 14), textvariable=tbil,
                    width=15, state='readonly')
entry_total.place(x=130, y=80)

bill_text = Text(f4, width=30, height=15, font=('arial', 12))
bill_text.place(x=20, y=130)

Button(f4, text='Print Bill', font=("arial", 10, "bold"),
       width=10, command=print_bill, padx=20, pady=10).place(x=100, y=530)

window.mainloop()
