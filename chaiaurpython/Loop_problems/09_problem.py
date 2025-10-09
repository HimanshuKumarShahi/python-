# list duplicate found

# set does not contains similar items always contain unique value so use set 

items=["apple","banana","orange","apple","mango","mango"]
# for i in items:
#    if items.count(i)>=2:
#       print(i,"present multiple time in list")
      
   
# ------------------------------------------
unique_item=set()
for item in items:
    if item in unique_item:
      print("Duplicate Item : ",item)
      
    unique_item.add(item)
    