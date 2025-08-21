import math


def calculator():
    while True:
        print("\n===== PYTHON CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Remainder")
        print("6. Percentage")
        print("7. Square")
        print("8. Cube")
        print("9. Logarithm")
        print("10. Circle Area")
        print("11. Circle Circumference")
        print("12. Rectangle Area & Perimeter")
        print("13. Square Area & Perimeter")
        print("14. Triangle Area (base & height)")
        print("0. Exit")

        choice = input("Enter choice: ")

        # Exit condition
        if choice == "0":
            print("Exiting Calculator. Goodbye!")
            break

        # Basic Arithmetic
        if choice in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result =", a + b)
            elif choice == "2":
                print("Result =", a - b)
            elif choice == "3":
                print("Result =", a * b)
            elif choice == "4":
                if b != 0:
                    print("Result =", a / b)
                else:
                    print("Error: Division by zero!")
            elif choice == "5":
                print("Result =", a % b)
            elif choice == "6":
                print(f"{a}% of {b} =", (a / 100) * b)

        # Square
        elif choice == "7":
            n = float(input("Enter number: "))
            print("Square =", n ** 2)

        # Cube
        elif choice == "8":
            n = float(input("Enter number: "))
            print("Cube =", n ** 3)

        # Logarithm
        elif choice == "9":
            n = float(input("Enter number: "))
            if n > 0:
                print("Log (base e) =", math.log(n))
            else:
                print("Error: Logarithm not defined for <= 0")

        # Circle Area
        elif choice == "10":
            r = float(input("Enter radius: "))
            print("Circle Area =", math.pi * r * r)

        # Circle Circumference
        elif choice == "11":
            r = float(input("Enter radius: "))
            print("Circle Circumference =", 2 * math.pi * r)

        # Rectangle
        elif choice == "12":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            print("Rectangle Area =", l * w)
            print("Rectangle Perimeter =", 2 * (l + w))

        # Square
        elif choice == "13":
            s = float(input("Enter side length: "))
            print("Square Area =", s * s)
            print("Square Perimeter =", 4 * s)

        # Triangle
        elif choice == "14":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print("Triangle Area =", 0.5 * b * h)

        else:
            print("Invalid choice! Try again.")


# Run Calculator
calculator()
