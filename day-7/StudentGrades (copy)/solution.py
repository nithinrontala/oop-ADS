def Student_grade_tracker(d):
    total_marks = 0
    # print(d.values())
    for student_marks in d.values():

        total_marks+=student_marks[1]
        
    avg = total_marks / len(d)
    print(f"Average Marks: {avg:.2f}")

def addStudent(d, Name, Rollnumber, Marks):
    Marks = int(Marks)
    Grade = calculateGrade(Marks)
    d[Name] = [Rollnumber, Marks, Grade]
    # print(d)

def calculateGrade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    else:
        return 'D'

def displayContent(d):
    for name, info in d.items():
        print(f"Name: {name}, Roll Number: {info[0]}, Marks: {info[1]}, Grade: {info[2]}")

d = {}
while True:
    try:
        s = input()
        action = s.split()
        # print(action)
        if action[0] == "Add":
            addStudent(d, action[2].rstrip(","), action[3].rstrip(","), action[4].rstrip(","))
        elif action[0] == "DisplayStudents":
            displayContent(d)
        elif action[0] == "CalculateAverageMarks":
            Student_grade_tracker(d)
    except :
        break
