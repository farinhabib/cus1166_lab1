from mymodules.models import Student
from mymodules.math_utils import average_grade
import random

def main():

    roster = []
    names = ["Farin", "Arna", "Sumaia", "Aisha", "Alia", "John", "Ahmad", "Jolie", "Mikek", "Rob"]

    for i in range(10):
        name = str(names[i])
        grade = random.randint(60, 100)
        student = Student(name, grade)
        roster.append(student)

    for student in roster:
        student.print_student_info();

    print("Average grade: " + str(average_grade(roster)))
main()
