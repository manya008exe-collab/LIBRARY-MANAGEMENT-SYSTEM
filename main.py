print("===== SMART STUDENT PERFORMANCE ANALYZER =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

maths = float(input("Enter Maths marks: "))
python_marks = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

attendance = float(input("Enter attendance percentage: "))
assignments = int(input("Enter completed assignments: "))

total = maths + python_marks + english
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 75 and attendance >= 75:
    category = "Excellent"
elif percentage >= 60 and attendance >= 60:
    category = "Good"
else:
    category = "Needs Improvement"

if maths <= python_marks and maths <= english:
    recommendation = "Focus more on Maths."
elif python_marks <= maths and python_marks <= english:
    recommendation = "Focus more on Python."
else:
    recommendation = "Focus more on English."

print("\n===== STUDENT PERFORMANCE REPORT =====")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Attendance:", attendance, "%")
print("Assignments Completed:", assignments)
print("Performance Category:", category)
print("Recommendation:", recommendation)

if attendance < 75:
    print("Warning: Your attendance is below 75%.")

if assignments < 5:
    print("Suggestion: Complete more assignments.")
