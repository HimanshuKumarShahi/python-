# Prime Number Checker
number=int(input("Enter your Number ...  "))
is_prime=True

if number>1:
    for i in range(2,number):
        if (number % i )== 0:
            is_prime=False
            break


# print(is_prime)
if(is_prime==True):
    print(number,"is prime number")
else:
    print(number,"is NOT prime number")