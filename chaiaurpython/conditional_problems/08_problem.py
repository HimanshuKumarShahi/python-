# password checker

password_length=str(input("Enter your password to check strength. \n"))
password=len(password_length)

if (password)<6:
    result="!! Weak password !!"
elif (password)<=10:
    result="!! Medium Password !!"
else:
    result="!! Strong Password !!"

print("You have ", result)
