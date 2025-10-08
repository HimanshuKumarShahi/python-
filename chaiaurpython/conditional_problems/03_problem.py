# grade calculator
name=str(input("Please Enter Student Name: \n"))
score=int(input("Print Enter Student Score: \n"))
if(score>=101):
    print("Please enter score b/w 1 to 100")
    exit()

grade=str(input("assign GRADE in captial letter b/w A to E "))
if(grade=="A"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is nice and b/w 90-100 grade=",grade)
elif(grade=="B"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is good and b/w 80-89 grade=",grade)
elif(grade=="C"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is average and b/w 70-79 grade=",grade)
elif(grade=="D"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is below average and b/w 60-69 grade=",grade)
elif(grade=="E"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is poor and below 60 grade=",grade)
else:
    print("please enter valid input !!")