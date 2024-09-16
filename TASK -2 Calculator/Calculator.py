# Addition Program
def add():
    while True:
        try:
            count = int(input("Enter the number of inputs you want to enter: "))
            break
        except ValueError:
            print("Invalid Input")
            continue

    total = 0
    for _ in range(count):
        while True:
            try:
                num = float(input("Enter a number: "))
                total += num
                break
            except ValueError:
                print("Invalid Input")
                continue
    print("Sum of Numbers is:", total)

# Subtraction Program
def sub():
    while True:
        try:
            count = int(input("Enter the number of inputs you want to enter: "))
            break
        except ValueError:
            print("Invalid Input")
            continue

    total = 0
    for _ in range(count):
        while True:
            try:
                num = float(input("Enter a number: "))
                total -= num  # Corrected subtraction logic
                break
            except ValueError:
                print("Invalid Input")
                continue
    print("Difference of Numbers is:", total)

# Multiplication Program
def mul():
    while True:
        try:
            count = int(input("Enter the number of inputs you want to enter: "))
            break
        except ValueError:
            print("Invalid Input")
            continue

    total = 1
    for _ in range(count):
        while True:
            try:
                num = float(input("Enter a number: "))
                total *= num
                break
            except ValueError:
                print("Invalid Input")
                continue
    print("Product of Numbers is:", total)

# Division Program
def dev():
    while True:
        try:
            count = int(input("Enter the number of inputs you want to enter: "))
            break
        except ValueError:
            print("Invalid Input")
            continue

    while True:
        try:
            total = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid Input")
            continue

    for _ in range(1, count):
        while True:
            try:
                num = float(input("Enter a number: "))
                if num == 0:
                    print("Cannot divide by zero. Enter a non-zero number.")
                    continue
                total /= num
                break
            except ValueError:
                print("Invalid Input")
                continue
            except ZeroDivisionError:
                print("Cannot divide by zero. Enter a non-zero number.")
                continue
    print("Quotient of Numbers is:", total)

# Main program
def main():
    print("Welcome to SY. Bsc AI, ML, & VR")
    while True:
        print("What Would you like to do? ")
        print("1 for Addition")
        print("2 for Subtraction")
        print("3 for Multiplication")
        print("4 for Division")

        while True:
            try:
                a = int(input("Enter Your option: "))
                if a not in [1, 2, 3, 4]:
                    print("Invalid Choice. Please enter a number between 1 and 4.")
                    continue # Convert input to integer
                if a == 1:
                    print("You have entered the Addition program")
                    add()
                elif a == 2:
                    print("You have entered the Subtraction program")
                    sub()
                elif a == 3:
                    print("You have entered the Multiplication program")
                    mul()
                elif a == 4:
                    print("You have entered the Division program")
                    dev()
                break
            except ValueError:
                print("Invalid Choice. Please enter a number.")
                continue

        while True:
            try:
                again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
                if again == 'yes':
                    break
                elif again == 'no':
                    print("Thank you for using the program!")
                    return
                else:
                    raise ValueError("Invalid Input")
            except ValueError as e:
                print(e)
                continue
if __name__ == "__main__":
    main()

