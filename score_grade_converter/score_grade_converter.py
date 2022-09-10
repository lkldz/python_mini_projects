#Score into grade converter
#Score 91 - 100 = Outstanding
#Score 81 - 90 = Exceeds Expectations
#Score 71 - 80 = Acceptable
#Score 70 or lower = Fail

student_scores = {
    "Mark" : 74,
    "Emily" : 80,
    "Judy" : 91,
    "Hugo" : 93,
    "Patty" : 79,
    "Monica" : 89,
    "Rick" : 65,
    "Amy" : 90,
    "Zack" : 70,
}

student_grade = {}

for name, score in student_scores.items():
    if score >= 91:
        student_grade[name] = "Outstanding"
        print(f"{name} has Outstanding result: {score}.")
    elif score >= 81 and score <= 90:
        student_grade[name] = "Exceeds Expectations"
        print(f"{name} Exceeds Expectations: {score}.")
    elif score >= 71 and score <= 80:
        student_grade[name] = "Acceptable"
        print(f"{name} has Acceptable: {score}.")
    else:
        student_grade[name] = "Fail"
        print(f"{name} Fails: {score}.")

print(student_grade)

