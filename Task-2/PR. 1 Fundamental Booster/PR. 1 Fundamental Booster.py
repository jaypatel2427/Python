print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name: ")
age = input("Please enter your age: ")
height = input("Please enter your height in meters: ")
favourite_number = input("Please enter your favourite number: ")

print("Thank you! Here is the information we collected:")

print("Name:", name, "Type:", type(name), "Memory Address:" ,id(name))
print("Age:", age, "Type:", type(age), "Memory Address:", id(age))
print("Height:", height, "Type:", type(height), "Memory Address:", id(height))
print("Favourite Number:", favourite_number, "Type:", type(favourite_number), "Memory Address:", id(favourite_number))

current_year = 2026
birth_year = current_year - int(age)

print("Your birth year is approximately: ", birth_year, "(based on your age of", age, ")")

print("Thank you for using the Personal Data Collector. Goodbye!")