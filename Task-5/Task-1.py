age = int(input("Enter your age: "))
        
        # Check eligibility based on age
if age >= 18:
            print("You are eligible for a driving license.")
elif age > 0:
            years_left = 18 - age
            print("You are not eligible")
else:
            print("Invalid age. Please enter a valid positive number.")
