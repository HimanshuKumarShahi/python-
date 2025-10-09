# Keep Asking input from user b/w 1 and 10
while True:
    number=int(input("Enter number b/w 1 to 10 : "))
    if 1<=number<=10:
        print("\"Wel-Done\" you chose:", number)
        break
    else:
        print("Invalid Input")