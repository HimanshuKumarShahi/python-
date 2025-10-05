# grade calculator
name=str(input("Please Enter Student Name: \n"))
score=int(input("Print Enter Student Score: \n"))
grade=str(input("assign GRADE in captial letter b/w A to E "))

if(grade=="A"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is nice and b/w 90-100")
elif(grade=="B"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is good and b/w 80-89")
elif(grade=="C"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is average and b/w 70-79")
elif(grade=="D"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is below average and b/w 60-69")
elif(grade=="E"):
    print("Student Name:",name)
    print("Student Score:",score)
    print("your score is poor and below 60")
else:
    print("please enter valid input !!")