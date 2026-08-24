print("Welcome to Bill Splitter App")


while True:
    Bill_Amount = float(input("Enter Total Bill: "))
    Number_Of_People = int(input("Enter Number Of People: "))
    Tip_Percentage = int(input("Enter Tip Percentage: "))

    if  Number_Of_People <= 0:
     print("Error: Number of people must be greater than 0. Please try again.")
     print()

    elif Bill_Amount < 0 or Tip_Percentage < 0:
        print("Error: Bill amount and tip percentage cannot be negative.")
    

    else:
     tip_amount = (Tip_Percentage / 100) * Bill_Amount
     total_bill = Bill_Amount + tip_amount
     per_person = total_bill /  Number_Of_People

    print("Tip Amount:", tip_amount)
    print("Total Bill (with Tip):", total_bill)
    print("Each person shoul pay:", per_person)

    again = input("You Want to like calculate another Bill? (y/n): ")
    if again != 'y':
        print("\nThank you for using the Bill Splitter App.")
        break
    
    print("-" * 40)