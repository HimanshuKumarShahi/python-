# /table print using loop
n=int(input("Enter number for Table: \n"))

for i in range(1,11):
    if i==5:
      continue
    print(n,"x",i ,"=", n*i)
