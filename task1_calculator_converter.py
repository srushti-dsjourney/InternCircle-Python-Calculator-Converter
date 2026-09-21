def calculator():
    print("\n--- Basic Calculator ---")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numbers.")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    choice = input("Choose an option: ")

    try:
        value = float(input("Enter value: "))

        if choice == "1":
            print("Miles:", value * 0.621371)
        elif choice == "2":
            print("Kilometers:", value * 1.60934)
        elif choice == "3":
            print("Fahrenheit:", (value * 9 / 5) + 32)
        elif choice == "4":
            print("Celsius:", (value - 32) * 5 / 9)
        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("1. INR to USD")
    print("2. USD to INR")

    choice = input("Choose an option: ")

    try:
        amount = float(input("Enter amount: "))

        # Example fixed conversion rate for this task
        if choice == "1":
            print("USD:", amount / 83)
        elif choice == "2":
            print("INR:", amount * 83)
        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    while True:
        print("\n===== Python Calculator & Converter =====")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Currency Converter")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            currency_converter()
        elif choice == "4":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()