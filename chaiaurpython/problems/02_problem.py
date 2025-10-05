# price checker for movies 
age=int(input("please enter your age for movie ticket: \n"))
day=str(input("please enter day to redeem discount: \n"))

# price=12 if age>=18 else 8

if(age<19):
    if(day=="wednesday"):
        print("you are under 18 so Ticket price is: $8")
        print("your discount price to pay: $6")
    else:
         print("you are under 18 so Ticket price is: $8") 
elif(age>19):
    if(day=="wednesday"):
        print("you are above 18 so you have to pay: $ 12")
        print("your discount price to pay: $10")
    else:
        print("you are above 18 so you have to pay: $ 12")
else:
    print("please Enter Valid Input...")
