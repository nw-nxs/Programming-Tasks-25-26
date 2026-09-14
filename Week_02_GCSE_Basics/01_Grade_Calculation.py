"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

score = [A,B,C,D]
def get_grade(score):
    student = int(input("Enter score: "))
    if student >= 80 and student <= 100:
        print("Your grade is A")
    elif student >= 60 and student <= 79:
        print("Your grade is B")
    elif student >= 40 and student <= 59:
        print("Your grade is C")
    elif student < 40:
        print("Your grade is D")
