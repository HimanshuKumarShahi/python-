# Factorial Calculator using while loop
number=int(input("Enter Your Number Here .....  "))
fact=1

# using for loop
# for i in range(1,number+1):
#     fact=fact*i
# print(fact)

# using while loop
while number>0:
    # fact=fact*number
    # number=number-1

    fact*=number
    number-=1

print("factorial is : ",fact)