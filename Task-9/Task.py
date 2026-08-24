print("Welcome to the Pattern Generator and Number Analyzer!")
print()
print("Select an option:")
print("1. Right-angled Triangle")
print("2. Pyramid")
print("3. Left-angled Triangle")
print("4. Analyze a Range of Numbers")

choice = input("Enter your choice: ")
print()

if choice == "1":
    rows = int(input("Enter number of rows: "))
    for i in range(1, rows + 1):
        print("*" * i)

elif choice == "2":
    rows = int(input("Enter number of rows: "))
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

elif choice == "3":
    rows = int(input("Enter number of rows: "))
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)

elif choice == "4":
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            print("Number",num, "is Even")
        else:
            print("Number ",num, " is Odd")
        total += num

    print("Sum of all numbers from ",start," to", end," is:" ,total)

else:
    print("Invalid choice.")