import os

# Person class represents a person with basic info.
class Person:
    def __init__(self, first_name, last_name, nationality, age):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.nationality}, {self.age})"


# Grade class represents a single assignment grade.
class Grade:
    def __init__(self, assignment_name, score):
        self.assignment_name = assignment_name
        self.score = score
        self.weight = self.compute_weight(assignment_name)

    def compute_weight(self, assignment_name):
        aname = assignment_name.upper()
        if aname.startswith("HW"):
            return 0.07
        elif aname.startswith("Q"):
            return 0.015
        elif aname == "MT":
            return 0.14
        elif aname == "F":
            return 0.25
        else:
            return 0.0

    def set_score(self, new_score):
        self.score = new_score

    def __str__(self):
        return f"{self.assignment_name}: {self.score} (weight: {self.weight})"


# Student class extends Person and holds additional course-related info.
class Student(Person):
    def __init__(self, first_name, last_name, nationality, age, major, andrew_id):
        super().__init__(first_name, last_name, nationality, age)
        self.major = major
        self.andrew_id = andrew_id
        self.grades = []  # List to hold Grade objects

    def add_grade(self, grade):
        self.grades.append(grade)

    def change_grade(self, assignment, new_score):
        for grade in self.grades:
            if grade.assignment_name.lower() == assignment.lower():
                grade.set_score(new_score)
                return True
        return False

    def get_grades_str(self):
        result = f"Grades for {self.andrew_id}:\n"
        for grade in self.grades:
            result += f"  {grade}\n"
        return result

    def get_current_score(self):
        total_weighted_score = 0
        total_weight = 0
        for grade in self.grades:
            total_weighted_score += grade.score * grade.weight
            total_weight += grade.weight
        return total_weighted_score / total_weight if total_weight != 0 else 0

    def get_current_letter_grade(self):
        score = self.get_current_score()
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    def what_do_i_need(self, target_grade):
        if target_grade == 'A':
            target = 90
        elif target_grade == 'B':
            target = 80
        elif target_grade == 'C':
            target = 70
        elif target_grade == 'D':
            target = 60
        else:
            target = 0

        total_weight_used = 0
        weighted_score = 0
        for grade in self.grades:
            total_weight_used += grade.weight
            weighted_score += grade.score * grade.weight
        rest = 1.0 - total_weight_used
        current_avg = (weighted_score / total_weight_used) if total_weight_used != 0 else 0
        if rest <= 0:
            return -1
        need = (target - current_avg * total_weight_used) / rest
        return need

    def __str__(self):
        return f"{super().__str__()} | Major: {self.major} | ID: {self.andrew_id}"


# GradeBook class manages a collection of Student objects.
class GradeBook:
    def __init__(self, filename):
        self.students = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    tokens = line.strip().split()
                    if len(tokens) < 6:
                        continue  # Not enough tokens to form a student
                    first_name = tokens[0]
                    last_name = tokens[1]
                    nationality = tokens[2]
                    age = int(tokens[3])
                    major = tokens[4]
                    andrew_id = tokens[5]
                    student = Student(first_name, last_name, nationality, age, major, andrew_id)
                    # Process grade pairs if present
                    i = 6
                    while i < len(tokens) - 1:
                        grade_name = tokens[i]
                        grade_value = int(tokens[i+1])
                        student.add_grade(Grade(grade_name, grade_value))
                        i += 2
                    self.students.append(student)
        except Exception as e:
            print(f"Error reading file: {e}")

    def __str__(self):
        # To-Do
        result = ""
        for student in self.students:
            result += f"{student}\n"
        return result


    def print_individual_grades(self, id):
        # To-Do
        for student in self.students:
            if student.andrew_id == id:
                print(student.get_grades_str())
                return
        print(f"No student found with id: {id}")

    def print_grades_by_major(self, major):
        # To-Do
        for student in self.students:
            if student.major.lower() == major.lower():
                print(student)
                print(student.get_grades_str())
                return
        print(f"No students found in major: {major}")

    def remove_student(self, id):
        # To-Do
        
        for i in range(len(self.students)):
            if self.students[i].andrew_id == id:
                self.students.pop(i)
                print(f"Student with id {id} removed.")
                return
        print(f"Error: No student with id {id} found to remove.")

    def change_grade(self, id, assignment, newgrade):
        # To-Do
        for student in self.students:
            if student.andrew_id == id:
                if student.change_grade(assignment, newgrade):
                    print(f"Grade for {assignment} updated to {newgrade} for student {id}")
                else:
                    print(f"Error: Assignment {assignment} not found for student {id}")
                return
        print(f"Error: No student with id {id} found.")

    def add_grade_to_all(self, assignment_name, score):
        # To-Do
        for student in self.students:
            student.add_grade(Grade(assignment_name, score))
        print(f"Added grade {assignment_name}: {score} to all students.")

    def print_current_grade(self, id):
        # To-Do
        for student in self.students:
            if student.andrew_id == id:
                current_grade = student.get_current_letter_grade()
                print(f"Current letter grade for {id} is: {current_grade}")
                return
        print(f"Error: No student with id {id} found.")

    def what_do_i_need(self, id, grade):
        # To-Do
        for student in self.students:
            if student.andrew_id == id:
                need = student.what_do_i_need(grade)
                if need == -1:
                    print(f"Student {id} has completed all assignments.")
                else:
                    print(f"Student {id} needs an average of {need:.2f} on the remaining work for a(n) {grade}")
                return
        print(f"Error: No student with id {id} found.")

    def update_database(self, filename):
        try:
            with open(filename, 'w') as f:
                for student in self.students:
                    # Write student's basic info
                    line = f"{student.first_name} {student.last_name} {student.nationality} {student.age} {student.major} {student.andrew_id}"
                    for grade in student.grades:
                        line += f" {grade.assignment_name} {grade.score}"
                    f.write(line + "\n")
            print(f"Database updated in file: {filename}")
        except Exception as e:
            print(f"Error writing to file: {e}")


