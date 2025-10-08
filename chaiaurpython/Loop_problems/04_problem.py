# Reverse string using loop
string=str(input("Enter String To Reverse:\n"))
rev_string=""
for char in string:
    rev_string=char + rev_string
print(rev_string)
