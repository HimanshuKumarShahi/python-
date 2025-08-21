name=input("name:- ")
roll=int(input("roll_no:-"))
price=float(input("price:-"))
age=int(input("age:-"))
if(age>18):
    print("age you can vote")
elif(age<18 and age>0):
    print("you are not eligible for voteing.")
print(name)
print(roll)
print(price)