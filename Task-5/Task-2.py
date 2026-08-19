marks = float(input("Enter the student's marks: "))

if marks < 0:
     print("Invalid input. Marks cannot be negative.")
    
            
if marks >= 40:
    print("Result: Pass! Congratulations.")
else:
     marks_needed = 40 - marks
     print("Result: Fail. You needed marks_needed} more mark(s) to pass.")
            