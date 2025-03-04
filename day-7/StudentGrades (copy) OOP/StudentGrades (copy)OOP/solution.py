class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        else:
            return 'D'


class StudentGradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number, marks):
        marks = int(marks)
        student = Student(name, roll_number, marks)
        self.students[name] = student

    def calculate_average_marks(self):
        total_marks = 0
        student_count = 0
        for student in self.students.values():
            total_marks += student.marks
            student_count += 1
        avg = total_marks / student_count
        print(f"Average Marks: {avg:.2f}")

    def display_content(self):
        for student in self.students.values():
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Marks: {student.marks}, Grade: {student.grade}")


def main():
    tracker = StudentGradeTracker()

    while True:
        try:
            s = input()
            action = s.split()
            if action[0] == "Add":
                tracker.add_student(action[2].strip(","), action[3].strip(","), action[4].strip(","))
            elif action[0] == "DisplayStudents":
                tracker.display_content()
            elif action[0] == "CalculateAverageMarks":
                tracker.calculate_average_marks()
        except:
            break


if __name__ == "__main__":
    main()
