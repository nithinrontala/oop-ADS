class Student:
    def __init__(self, sid, name, ec):
        self.studentID = sid
        self.name = name
        self.enrolledCourses = ec

    def enroll(self, course):
        self.enrolledCourses.append(course)

    def getCourses(self):
        courses = []
        for course in self.enrolledCourses:
            courses.append(course.courseCode)
        return courses

class Course:
    def __init__(self, cc, cn, me, ce):
        self.courseCode = cc
        self.courseName = cn
        self.maxEnrollment = me
        self.currentEnrollment = ce

    def canEnroll(self):
        return self.currentEnrollment < self.maxEnrollment

class EnrollmentManager:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses

    def enrollStudent(self, student_id, course_code):
        for s in self.students:
            if s.studentID == student_id:
                student = s
                for c in self.courses:
                    if c.courseCode == course_code:
                        course = c

        if student and course and course.canEnroll():
            student.enroll(course)
            course.currentEnrollment += 1
            return True
        return False

    def listStudentsInCourse(self, course_code):
        students_in_course = []
        for s in self.students:
            for c in s.enrolledCourses:
                if c.courseCode == course_code:
                    students_in_course.append(s)
        return students_in_course

def main():
# Create students
    student1 = Student(1, "Alice", [])
    student2 = Student(2, "Bob", [])
    # Create a course with maximum enrollment 1 to test capacity limits
    course = Course("CS101", "Intro to CS", 1, 0)
    # Create EnrollmentManager with students and the course
    em = EnrollmentManager([student1, student2], [course])
    # Test enrolling first student (should succeed)
    enroll1 = em.enrollStudent(1, "CS101")
    print("Alice enrolled in CS101:", enroll1)
    # Test enrolling second student (should fail due to capacity)
    enroll2 = em.enrollStudent(2, "CS101")
    print("Bob enrolled in CS101 (should fail):", enroll2)

    # List students in CS101
    print("Students in CS101:")
    for s in em.listStudentsInCourse("CS101"):
        print(s.name)
    # Additional: Check student's enrolled courses
    print("Alice's courses:", student1.getCourses())
    print("Bob's courses:", student2.getCourses())
if __name__ == '__main__':
    main()
