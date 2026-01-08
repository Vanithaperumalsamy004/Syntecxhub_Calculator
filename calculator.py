# Simple Calculator - Intern Task 1

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def calculate(num1, num2, operator):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        return "Invalid operator"


def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Clear")
    print("6. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '6':
            print("Exiting calculator. Goodbye!")
            break

        if choice == '5':
            print("Calculator cleared!")
            continue

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operators = {
            '1': '+',
            '2': '-',
            '3': '*',
            '4': '/'
        }

        operator = operators[choice]
        result = calculate(num1, num2, operator)

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
