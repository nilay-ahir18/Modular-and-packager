import math
import random
import string
import uuid
from datetime import datetime

# ===================== DATETIME MODULE =====================
def datetime_menu():
    while True:
        print("\n--- Datetime Operations ---")
        print("1. Current Date & Time")
        print("2. Date Difference")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Current Date & Time:", datetime.now())

        elif choice == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            d1 = datetime.strptime(d1, "%Y-%m-%d")
            d2 = datetime.strptime(d2, "%Y-%m-%d")

            print("Difference:", abs((d2 - d1).days), "days")

        elif choice == "3":
            break


# ===================== MATH MODULE =====================
def math_menu():
    while True:
        print("\n--- Mathematical Operations ---")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            num = int(input("Enter number: "))
            print("Factorial:", math.factorial(num))

        elif choice == "2":
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))

            ci = p * (1 + r/100) ** t
            print("Compound Interest:", round(ci, 2))

        elif choice == "3":
            break


# ===================== RANDOM MODULE =====================
def random_menu():
    while True:
        print("\n--- Random Data Generation ---")
        print("1. Random Number")
        print("2. Random Password")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits
            password = ''.join(random.choice(chars) for _ in range(length))
            print("Generated Password:", password)

        elif choice == "3":
            break


# ===================== UUID MODULE =====================
def generate_uuid():
    print("\nGenerated UUID:", uuid.uuid4())


# ===================== FILE MODULE =====================
def file_menu():
    while True:
        print("\n--- File Operations ---")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice in ["1", "2", "3", "4"]:
            filename = input("Enter file name: ")

        if choice == "1":
            open(filename, "w").close()
            print("File created successfully!")

        elif choice == "2":
            data = input("Enter data: ")
            with open(filename, "w") as f:
                f.write(data)
            print("Data written successfully!")

        elif choice == "3":
            try:
                with open(filename, "r") as f:
                    print("File Content:\n", f.read())
            except:
                print("File not found!")

        elif choice == "4":
            data = input("Enter data to append: ")
            with open(filename, "a") as f:
                f.write("\n" + data)
            print("Data appended successfully!")

        elif choice == "5":
            break


# ===================== EXPLORE MODULE =====================
def explore_module():
    module_name = input("Enter module name: ")
    try:
        module = __import__(module_name)
        print("Attributes:\n", dir(module))
    except:
        print("Module not found!")


# ===================== MAIN MENU =====================
def main():
    while True:
        print("\n========== Multi-Utility Toolkit ==========")
        print("1. Datetime Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            generate_uuid()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("Thank you for using the toolkit!")
            break
        else:
            print("Invalid choice!")


# ===================== RUN =====================
if __name__ == "__main__":
    main()