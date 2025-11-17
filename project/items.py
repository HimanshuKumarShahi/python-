from tkinter import *

window = Tk()
window.title("Food Court")
window.geometry("1500x800")
window.configure(bg="#ff7700")
window.resizable(width=False,height=False)



navbar = Frame(window, bg="#1a1a1a", height=80)
navbar.pack(fill="both", pady=10)

content_frame = Frame(window, bg="#d7d7d7",height=790)
content_frame.pack(fill="both", padx=5, pady=10)


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




# def show_home():
#     # Clear previous content
#     for widget in content_frame.winfo_children():
#         widget.destroy()
    
#     # Home page content
#     home_title = Label(
#         content_frame,
#         text="Welcome to FoodCourtX",
#         font=("Arial", 24, "bold"),
#         bg="#f5f5f5",
#         fg="#333"
#     )
#     home_title.pack(pady=20)
    
#     welcome_text = Label(
#         content_frame,
#         text="Browse our menu and place your order for quick delivery!",
#         font=("Arial", 14),
#         bg="#f5f5f5",
#         fg="#666",
#         wraplength=600
#     )
#     welcome_text.pack(pady=10)

# def show_menu():
#     for widget in content_frame.winfo_children():
#         widget.destroy()
    
#     menu_title = Label(
#         content_frame,
#         text="Our Menu",
#         font=("Arial", 24, "bold"),
#         bg="#f5f5f5",
#         fg="#333"
#     )
#     menu_title.pack(pady=20)
    
#     # Sample menu items
#     items = ["Pizza - ₹199", "Burger - ₹99", "Pasta - ₹149"]
#     for item in items:
#         Label(content_frame, text=item, font=("Arial", 12), bg="#f5f5f5").pack(anchor="w")

# def show_order():
#     for widget in content_frame.winfo_children():
#         widget.destroy()
    
#     order_title = Label(
#         content_frame,
#         text="Place Your Order",
#         font=("Arial", 24, "bold"),
#         bg="#f5f5f5",
#         fg="#333"
#     )
#     order_title.pack(pady=20)
    
#     # Simple order form
#     name_label = Label(content_frame, text="Name:", font=("Arial", 12), bg="#f5f5f5")
#     name_entry = Entry(content_frame, font=("Arial", 12), width=30)
#     name_label.pack(pady=5)
#     name_entry.pack(pady=5)

# # Show home page by default
# show_home()

window.mainloop()
