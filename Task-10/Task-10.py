all_students = []

print("Welcome to Student Data Organizer!")

while True:
    print("\nSelect an Option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subject Offered")
    print("6. Exit")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        print("\nEnter Student Details:")
        all_students.append({
            "roll_no": (int(input("Enter ID: ")),),
            "student_name": input("Name: "),
            "student_age": int(input("Age: ")),
            "student_grade": input("Grade: "),
            "student_dob": (input("Date of Birth (YYYY-MM-DD): "),),
            "student_subjects": set(input("Subjects (comma-separated): ").split(","))
        })
        print("\nStudent added Successfully!")
        
    elif choice == 2:
        for data in all_students:
            print(data)
            
    elif choice == 3:
        pass
        
    elif choice == 4:
        pass
        
    elif choice == 5:
        pass
        
    elif choice == 6:
        break
        
    else:
        print("Please Enter Valid Choice!!")