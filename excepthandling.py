try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("1. Add")
    print("2. Divide")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a / b)

    else:
        print("Invalid choice")

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")