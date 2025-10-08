# leap year checker
year=int(input("Enter year here: \n"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"is Leap Year.")
else:
    print(year,"is NOT Leap Year.")