# classifying the age group according to their enter ages

age=int(input("Enter your age: \n"))

if(age<13):
    print("you are child")
elif age<20:
    print("you are teenager")
elif age<60:
    print("you are adult")
else:
    print("you are senior")