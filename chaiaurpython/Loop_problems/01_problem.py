# Find out positive numbers
numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
positive_count=0
for num in numbers:
    if(num>0):
        positive_count +=1
        print("Positive Numbers:",num)
    else:
        print("Negative Numbers: ",num)
print("The Positive Count :",positive_count)