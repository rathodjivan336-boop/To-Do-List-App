print("🎓 Student Result Management System")

name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))

total = maths + english + science

percentage = total / 3

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n--- Student Result ---")
print("Name:", name)
print("Maths:", maths)
print("English:", english)
print("Science:", science)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)