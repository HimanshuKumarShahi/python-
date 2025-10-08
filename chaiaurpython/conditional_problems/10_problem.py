species=str(input("Pet Food Recommendation for (DOG / CAT) \n"))
year=int(input("Also give Age:  \n"))

if(species=="dog" or species=="DOG"):
    if(year<=2):
        print("AI SUGGEST Puppy Food")
    else:
        print("AI SUGGEST General Dog Food")
elif(species=="cat" or species=="CAT"):
    if(year<5):
        print("AI SUGGEST Kitten Food")
    else:
        print("AI SUGGEST Senior Cat Food")
else:
    print("!! Invalid !!")