total_marks = float(input("Enter total marks secured by the student: "))

if total_marks >= 90:
    grade = 'S'
elif total_marks >= 80:
    grade = 'A'
elif total_marks >= 70:
    grade = 'B'
elif total_marks >= 60:
    grade = 'C'
elif total_marks >= 50:
    grade = 'D'
else:
    grade = 'F'

print(f"The grade for {total_marks} marks is: {grade}")