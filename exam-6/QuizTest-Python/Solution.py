import random


class Question:
    def __init__(self, question_text, options, correct_answer) -> None:
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def get_question_text(self):
        return self.question_text

    def get_options(self):
        return self.options

    def get_correct_answer(self):
        return self.correct_answer

    def set_question_text(self, question):
        self.question_text = question

    def set_options(self, options):
        self.options = options

    def set_correct_answer(self, correct):
        self.correct_answer = correct

    def validate_answer(self, answer):
        return self.correct_answer.lower() == answer.lower()


class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, options, correct_answer):
        super().__init__(question_text, options, correct_answer)

    def validate_answer(self, answer):
        return self.correct_answer.lower() == answer.lower()


class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_answer, options=["True", "False"]):
        super().__init__(question_text, options, correct_answer)

    def validate_answer(self, answer):
        return self.correct_answer.lower() == answer.lower()


class FillInTheBlankQuestion(Question):
    def __init__(self, question_text, correct_answer, options=""):
        super().__init__(question_text, options, correct_answer)

    def validate_answer(self, answer):
        return self.correct_answer.lower() == answer.lower()


class Quiz:
    def __init__(self):
        self._questions = []

    def shuffle_questions(self) -> None:
        random.shuffle(self._questions)

    def add_question(self, question):
        self._questions.append(question)

    def remove_question(self, question):
        for i in self._questions:
            if i.get_question_text() == question.get_question_text():
                self._questions.remove(i)

    def get_questions(self):
        return self._questions

    def get_total_questions(self):
        return len(self._questions)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.score = 0

    def simulate_quiz(self, quiz, answer):
        j = 0
        print()
        print(f"--- {Student.get_name(self)} is taking the quiz ---")
        for i in quiz.get_questions():
            if i.validate_answer(answer[j]):
                print("Correct!")
                self.score += 1
                j += 1
            else:
                print(f"Incorrect! Correct answer: {i.get_correct_answer()}")
                j + 1
        print()
        print(f"{Student.get_name(self)} scored {self.score} out of {len(answer)}.")

    def get_score(self):
        return self.score


class Leaderboard:
    def __init__(self):
        self.leaderboard = []

    def add_student(self, student):
        self.leaderboard.append(student)

    def display_leaderboard(self):
        print()
        print("=== Leaderboard ===")
        for i in self.leaderboard:
            print(f"Student: {i.get_name()} | Score: {i.get_score()}")
