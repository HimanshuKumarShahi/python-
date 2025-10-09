# Find out non repeting string
input_str=str(input("Write Your Word Here ......  "))

for i in input_str:
    if input_str.count(i)==1:
        print(i)
        print("Your non repeting string is :",i)
        # break
        # if break use then exit from condition loop not search another non repeting string

