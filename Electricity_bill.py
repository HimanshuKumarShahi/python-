def calculate_bill(prev_reading, pres_reading, area_type):
    # Define rates
    rates = {
        "urban": 3.50,
        "city": 5.50,
        "village": 2.50
    }

    # Units consumed
    units = pres_reading - prev_reading
    if units < 0:
        raise ValueError("Present reading must be greater than previous reading.")

    # Free units
    free_units = 125
    chargeable_units = max(0, units - free_units)

    # Get rate based on area type
    if area_type.lower() not in rates:
        raise ValueError("Invalid area type. Choose 'urban', 'city', or 'village'.")

    rate = rates[area_type.lower()]
    amount = chargeable_units * rate

    # Bill details dictionary
    bill_details = {
        "Previous Reading": prev_reading,
        "Present Reading": pres_reading,
        "Units Consumed": units,
        "Free Units": free_units,
        "Chargeable Units": chargeable_units,
        "Rate per Unit": rate,
        "Total Bill": amount
    }
    return bill_details


# Example usage
if __name__ == "__main__":
    print("Electricity Bill Calculator")
    prev = int(input("Enter Previous Reading: "))
    pres = int(input("Enter Present Reading: "))
    area = input("Enter Area Type (urban/city/village): ")

    try:
        bill = calculate_bill(prev, pres, area)
        print("\n------ Bill Details ------")
        for key, value in bill.items():
            print(f"{key:20}: {value}")
    except ValueError as e:
        print("Error:", e)
