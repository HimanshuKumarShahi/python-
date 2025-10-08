# sum of Even Number
number=int(input("Enter Your Number: \n"))
sum_even=0
count=0
if(number<=0):
    print("Please Enter Valid Number upto zero(0)")
else:
    print("The Number calculate from first even number to ",number)
    for num in range(1,number+1):
        if(num%2==0):
            count+=1
            sum_even+=num

print("The count of even sum is: ", count)
print("even sum is: ", sum_even)
        
