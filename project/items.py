from tkinter import *

window = Tk()
window.title("Food Court")
window.geometry("1500x900")
window.configure(bg="#ff7700")
window.resizable(width=False,height=False)



navbar = Frame(window, bg="#1a1a1a", height=80)
navbar.pack(fill="both", pady=10)

title_label = Label(
    navbar,
    text="FoodCourt",
    font=("Arial", 20, "bold"),
    bg="#1a1a1a",
    fg="white",
    cursor="hand2",
)
title_label.pack(side="left", padx=20, pady=15)

home_btn = Button(
    navbar,
    text="Home",
    font=("Arial", 12, "bold"),
    bg="#1a1a1a",
    fg="white",
    bd=0,
    cursor="hand2",
)
home_btn.pack(side="right", padx=20, pady=15)
home_btn.place(x=550,y=22)

Items_btn = Button(
    navbar,
    text="Items",
    font=("Arial", 12, "bold"),
    bg="#1a1a1a",
    fg="white",
    bd=0,
    cursor="hand2",
)
Items_btn.pack(side="right", padx=10, pady=15)
Items_btn.place(x=650,y=22)

order_btn = Button(
     navbar,
    text="Orders",
    font=("Arial", 12, "bold"),
    bg="#1a1a1a",
    fg="white",
    bd=0,
    cursor="hand2",
)
order_btn.pack(side="right", padx=20, pady=15)
order_btn.place(x=750,y=22)

contact_btn = Button(
     navbar,
    text="Contact-Us",
    font=("Arial", 12, "bold"),
    bg="#1a1a1a",
    fg="white",
    bd=0,
    cursor="hand2",
)
contact_btn.pack(padx=30, pady=20)
contact_btn.place(x=1200,y=22)


# navbar = Frame(window, bg="#1a1a1a", height=80)
# navbar.pack(fill="both", pady=10)

Content_frame=Frame(window,bg="#212121",height=750)
Content_frame.pack(fill="both",padx=3,pady=2)

Label(Content_frame,text="Your one-stop destination for delicious meals from a variety of stalls.\n"
        "Enjoy fast delivery, great taste, and excellent service.\n"
        "Order now and satisfy your cravings!",
        font=("Arial", 25),
    bg="#ff7700",
    fg="#0A0909",
    pady=100,
    padx=40,
    justify="center"
).pack(fill="both")

Item_frame = Frame(Content_frame, bg="white", padx=20, pady=20, bd=2, relief="ridge")
Item_frame.pack(padx=80, pady=40)

most_liked = Label(
    Item_frame,
    text="Most Liked",
    bg="#02a2ff",
    fg="black",
    font=("Arial", 9, "bold"),
    padx=2,
    pady=5
)
most_liked.pack(anchor="n", pady=(8, 15))

image_placeholder = Label(
    Item_frame,
    text="[Image here]",
    bg="#ddd",
    fg="#666",
    font=("Arial", 14),
    width=25,
    height=8
)
name_label = Label(
    Item_frame,
    text="Delicious Pizza",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="#333",
    pady=10
)
name_label.pack()

price_label = Label(
    Item_frame,
    text="Price: ₹199",
    font=("Arial", 16),
    bg="white",
    fg="#ff6600"
)
price_label.pack()
desc_label = Label(
    Item_frame,
    text="A crispy thin crust topped with fresh mozzarella, basil, and tomatoes.",
    font=("Arial", 12),
    bg="white",
    fg="#555",
    wraplength=300,
    pady=15,
    padx=10,
    justify="center"
)
desc_label.pack()


window.mainloop()
