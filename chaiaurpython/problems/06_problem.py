# Transportation maode selection
distance=int(input("Entey your distance for suggetion !!! \n"))

if(distance>0):
    if(distance<=3):
        transport="Walk"
    elif(distance<=16):
        transport="Bike"
    elif(distance>16):
        transport="Car"
else:
    print("Enter distance above zero(0)")

print("AI Recommends you the transport of:",transport)