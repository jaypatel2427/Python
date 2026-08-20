price = float(input("Enter the product price : "))

if price < 0:
    print("Invalid input. Price cannot be negative.") 

if price >= 10000:
    print("At price, the product is Expensive.")

else:
    print("At price, the product is Affordable.")
