# chai="massala chai"
# first_char=chai[4]
# slice_char=chai[0:6]
# slice_char=chai[7:12]
# print(first_char)
# print(slice_char)
# print(chai.lower())
# print(chai.upper())
# print(chai.replace("chai","powder"))


# newchar="   hello   Dear   "
# print(newchar.strip())


# words="lemon,ginger,mint,coffee,juice"
# print(words)
# print(words.split())
# print(words.find("mint"))
# print(words.count("mint"))

# chai_type="Mint tea"
# Quantity=4
# order="i ordered {} cups & {}"
# print(order)
# print(order.format(Quantity,chai_type))

# for i in chai:
#     print(i)

# chai="we are \"indian\""
# print(chai)

# tea_varity=["lemon","ginger","massala","black"]
# for i in tea_varity:
#     print(i,end="__")
# if("oolong"in tea_varity):
#     print("not available") 

# tea_varity.append("Oolong")
# print(tea_varity)
# tea_varity.pop()
# print(tea_varity)
# tea_varity.remove("ginger")
# print(tea_varity)
# tea_varity.insert(0,"ginger")
# print(tea_varity)

# tea_varity_copy=tea_varity.copy()
# in memory both are different not give refrence of tea_varity 

# squared_num=[x**2 for x in range(11)]
# print(squared_num)

# cubed_num=[x**3 for x in range(5)]
# print(cubed_num)


chai_types={"masala":"spicy","ginger":"zesty","green":"mild"}
# print(chai_types)
# print(chai_types["green"])
# print(chai_types.get("ginger"))

# chai_types["green"]="fresh"
# print(chai_types)

# for i in chai_types:
    # print(i)
#     print(i, chai_types[i])

# for key, value in chai_types.items():
    # print(key,value)


# if"masala" in chai_types:
#     print("yes !! present here ")
#     print(len(chai_types))

# chai_types["earl grey"]="citrus"
# print(chai_types)

# chai_types.pop("ginger")
# print(chai_types)

# print(chai_types.popitem())

# del chai_types["green"]
# print(chai_types)

# tea_shop={
#     "chai":{"masala":"spicy","green":"zesty"},
#     "tea":{"black":"strong","green":"mild"}
# }
# print(tea_shop)
# print(tea_shop["chai"])
# print(tea_shop["chai"]["green"])
# print(tea_shop["tea"])

# squared_num={x:x**2 for x in range(6)}
# print(squared_num) 
# squared_num.clear()
# print(squared_num) 