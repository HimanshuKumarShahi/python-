# Coffee customization
order=str(input("Select the size :(Small,Medium,Large) \n"))
extra_shot=str(input("Do You want Extra shot: (y/n) \n"))
if extra_shot=="y":
    item=order + "_coffee with extra shot"
else:
    item= order + "_coffee_"

print("your order is:",{item})