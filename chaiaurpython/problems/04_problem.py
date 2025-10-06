# fruit Ripeness checker
fruit=str(input("Enter your fruit name please:"))

if fruit=="banana":
    color=str(input("write your fruit color to Determint (Green,Yellow,Brown) !!!  \n"))
    if(color=="green" or color=="GREEN"):
        print("your fruit is Unripe")
    elif(color=="yellow" or color=="YELLOW"):
        print("your fruit is Ripe")
    elif(color=="brown" or color=="BROWN"):
        print("your fruit is OverRipe")
else:
    print("only banana sample available ")