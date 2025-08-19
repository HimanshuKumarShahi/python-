import tkinter as tk
from tkinter import ttk

# Main App
root = tk.Tk()
root.title("YouTube Clone UI")
root.geometry("1000x600")
root.configure(bg="white")

# ---------------- Header (Top Bar) ----------------
header = tk.Frame(root, bg="white", height=60, relief="raised", bd=1)
header.pack(side="top", fill="x")

# YouTube Logo (text placeholder)
logo = tk.Label(header, text="YouTube", fg="red", bg="white", font=("Arial", 20, "bold"))
logo.pack(side="left", padx=20)

# Search Bar
search_var = tk.StringVar()
search_entry = tk.Entry(header, textvariable=search_var, font=("Arial", 14), width=50, relief="solid", bd=1)
search_entry.pack(side="left", padx=10, pady=10)

search_btn = tk.Button(header, text="🔍", font=("Arial", 14), relief="solid", bd=1)
search_btn.pack(side="left", padx=5)

# ---------------- Sidebar ----------------
sidebar = tk.Frame(root, bg="white", width=200, relief="ridge", bd=1)
sidebar.pack(side="left", fill="y")

menu_items = ["Home", "Trending", "Subscriptions", "Library", "History"]
for item in menu_items:
    btn = tk.Button(sidebar, text=item, anchor="w", padx=20, pady=10, bg="white", relief="flat")
    btn.pack(fill="x")

# ---------------- Content Area ----------------
content_frame = tk.Frame(root, bg="white")
content_frame.pack(side="left", fill="both", expand=True)

# Scrollable Canvas for Videos
canvas = tk.Canvas(content_frame, bg="white")
scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="white")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ---------------- Fake Video Thumbnails ----------------
for i in range(20):
    video_frame = tk.Frame(scrollable_frame, bg="white", bd=1, relief="solid")
    video_frame.grid(row=i//3, column=i%3, padx=10, pady=10, ipadx=5, ipady=5)

    thumbnail = tk.Label(video_frame, text="🎬", bg="lightgray", width=30, height=10)
    thumbnail.pack()

    title = tk.Label(video_frame, text=f"Video Title {i+1}", font=("Arial", 12, "bold"), bg="white")
    title.pack(anchor="w")

    channel = tk.Label(video_frame, text="Channel Name", font=("Arial", 10), fg="gray", bg="white")
    channel.pack(anchor="w")

# Run App
root.mainloop()
