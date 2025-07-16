def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Division by zero"

def calculator():
    while True:
        print("\n--- Command-Line Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Select operation (1-5): ")

        if choice == '5':
            print("Exiting calculator.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Try again.")
            continue

        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif choice == '2':
            print(f"{n1} - {n2} = {sub(n1, n2)}")
        elif choice == '3':
            print(f"{n1} * {n2} = {mul(n1, n2)}")
        elif choice == '4':
            print(f"{n1} / {n2} = {div(n1, n2)}")


calculator()
