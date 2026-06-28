import math

while True:
    print("\n1. Basic Arithmetic")
    print("2. Scientific Calculator")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        print("Addition =", a + b)
        print("Subtraction =", a - b)
        print("Multiplication =", a * b)

        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot Divide by Zero")

    elif choice == "2":
        num = float(input("Enter Number: "))

        print("Square Root =", math.sqrt(num))
        print("Square =", math.pow(num, 2))
        print("Factorial =", math.factorial(int(num)))

    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
