
from Solution import Question, MultipleChoiceQuestion, TrueFalseQuestion, FillInTheBlankQuestion, Quiz, Person, Student, Leaderboard

# =========================
# Main Method: Testing All Classes and Simulated Quiz Participation with Leaderboard
# =========================

def main() -> None:
    # ------------------------------
    # Part 1: Testing Quiz and Question Classes
    # ------------------------------
    print("=== Testing Individual Question Classes ===")

    # Base Question test
    options_base = ["Paris", "London", "Berlin", "Madrid"]
    q_base = Question("What is the capital of France?", options_base, "Paris")
    print("Base Question:", q_base.get_question_text())

    # MultipleChoiceQuestion test
    options_mc = ["Python", "JavaScript", "C++", "Java"]
    q_mc = MultipleChoiceQuestion("Which language is known as the language of the web?", options_mc, "JavaScript")
    print("MultipleChoiceQuestion Options:", q_mc.get_options())

    # TrueFalseQuestion test
    q_tf = TrueFalseQuestion("The Earth is flat.", "False")
    print("TrueFalseQuestion Options:", q_tf.get_options())

    # FillInTheBlankQuestion test
    q_fill = FillInTheBlankQuestion("Complete the sentence: Java is a ____ programming language.", "versatile")
    print("FillInTheBlankQuestion:", q_fill.get_question_text())

    print("\n=== Validating Answers ===")
    if q_base.validate_answer("Paris"):
        print("Base Question: Answer is correct!")
    else:
        print("Base Question: Answer is incorrect!")
    if q_mc.validate_answer("javascript"):
        print("MultipleChoiceQuestion: Answer is correct!")
    else:
        print("MultipleChoiceQuestion: Answer is incorrect!")
    if q_tf.validate_answer("false"):
        print("TrueFalseQuestion: Answer is correct!")
    else:
        print("TrueFalseQuestion: Answer is incorrect!")
    if q_fill.validate_answer("Versatile"):
        print("FillInTheBlankQuestion: Answer is correct!")
    else:
        print("FillInTheBlankQuestion: Answer is incorrect!")

    print("\n=== Testing Setters on Base Question ===")
    q_base.set_question_text("What is the capital city of France?")
    q_base.set_options(["Paris", "Lyon", "Marseille", "Nice"])
    q_base.set_correct_answer("Paris")
    print("Updated Question:", q_base.get_question_text())
    print("Updated Options:", q_base.get_options())

    print("\n=== Building the Quiz ===")
    quiz = Quiz()
    quiz.add_question(q_base)
    quiz.add_question(q_mc)
    quiz.add_question(q_tf)
    quiz.add_question(q_fill)
    print("Total questions in quiz:", quiz.get_total_questions())

    print("\n=== Simulated Quiz Run ===")
    for q in quiz.get_questions():
        print("\nQuestion:", q.get_question_text())
        opts = q.get_options()
        if opts:
            print("Options:")
            for i, opt in enumerate(opts, start=1):
                print(f"  {i}. {opt}")
        else:
            print("No predefined options. Please answer in text.")
        simulated_answer = q.get_correct_answer()
        print("Simulated Answer:", simulated_answer)
        if q.validate_answer(simulated_answer):
            print("Result: Correct!")
        else:
            print("Result: Incorrect!")

    print("\n=== Testing Removal and Shuffling ===")
    quiz.remove_question(q_tf)
    print("After removal, total questions in quiz:", quiz.get_total_questions())
    print("Order after removing:")
    for q in quiz.get_questions():
        print(" -", q.get_question_text())

    # Add the TrueFalseQuestion back
    quiz.add_question(q_tf)
    print("After adding, total questions in quiz:", quiz.get_total_questions())
    print("Order after adding:")
    for q in quiz.get_questions():
        print(" -", q.get_question_text())

    # ------------------------------
    # Part 2: Simulating Student Quiz Participation and Leaderboard
    # ------------------------------
    print("\n=== Simulating Student Quiz Sessions ===")

    # Create a Leaderboard to record student scores
    leaderboard = Leaderboard()

    # Create simulated student data (hardcoded)
    student1 = Student("Alice", 20, "S001")
    # For Alice, simulate answers: assume she gets q_base and q_mc correct, but misses q_tf and q_fill
    answers_alice = ["Paris", "JavaScript", "True", "wrong answer"]

    student2 = Student("Bob", 22, "S002")
    # For Bob, simulate answers: assume he gets all correct
    answers_bob = ["Paris", "JavaScript", "versatile", "False"]

    # Simulate quiz participation for each student
    student1.simulate_quiz(quiz, answers_alice)
    leaderboard.add_student(student1)

    student2.simulate_quiz(quiz, answers_bob)
    leaderboard.add_student(student2)

    # Display the leaderboard (unsorted)
    leaderboard.display_leaderboard()


if __name__ == '__main__':
    main()
