marks = [ 45, 67, 89, 21, 98, 55, 40, 78, 62, 33, 90, 71, 58, 100, 49, 66, 83, 39, 60, 75, ]

print("Total Students:", len(marks))


highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", round(average, 2))

passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

print("Passed:", passed)
print("Failed:", failed)

full_marks_count = marks.count(100)
print("Students with 100 marks:", full_marks_count)

pass_percentage = (passed / len(marks)) * 100
print("Pass Percentage:", round(pass_percentage, 2), "%")

ascending_marks = sorted(marks)
descending_marks = sorted(marks, reverse=True)

print("Sorted Marks (Ascending):", ascending_marks)
print("Sorted Marks (Descending):", descending_marks)

second_highest = ascending_marks[-2]
second_lowest = ascending_marks[1]

print("Second Highest Marks:", second_highest)
print("Second Lowest Marks:", second_lowest)

all_passed = all(mark >= 40 for mark in marks)
any_failed = any(mark < 40 for mark in marks)

print("Did all students pass?:", all_passed)
print("Did any student fail?:", any_failed)

user_mark = int(input("Enter a mark to check if it exists in the list: "))

if user_mark in marks:
    print(user_mark, "exists in the marks list.")
else:
    print(user_mark, "does not exist in the marks list.")

grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_e = 0
grade_f = 0

for mark in marks:
    if mark >= 90:
        grade_a = grade_a + 1
    elif mark >= 80:
        grade_b = grade_b + 1
    elif mark >= 70:
        grade_c = grade_c + 1
    elif mark >= 60:
        grade_d = grade_d + 1
    elif mark >= 40:
        grade_e = grade_e + 1
    else:
        grade_f = grade_f + 1

print("Grade A (>=90):", grade_a, "Students")
print("Grade B (80-89):", grade_b, "Students")
print("Grade C (70-79):", grade_c, "Students")
print("Grade D (60-69):", grade_d, "Students")
print("Grade E (40-59):", grade_e, "Students")
print("Grade F (<40):", grade_f, "Students")
